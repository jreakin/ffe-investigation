from typing import Optional
import time
import csv
from pathlib import Path
from icecream import ic

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options

from pydantic import EmailStr
from pydantic.dataclasses import dataclass as pydantic_dataclass


@pydantic_dataclass
class Employee:
    name: str
    email: EmailStr
    titles: Optional[str] = None
    locations: Optional[str] = None

    def __hash__(self):
        return hash(self.email)


EMPLOYEE_FIELDS = list(Employee.__dataclass_fields__.keys())
DIRECTORY_URL = "https://www.fcs.org/directory"


def scrape_emails(url: str = DIRECTORY_URL, max_pages: int = None) -> set[Employee]:
    emails_ = set()
    current_page = 1

    _chrome_options = Options()
    _chrome_options.add_argument("--headless")
    _chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=_chrome_options)
    driver.get(url)

    while current_page <= max_pages if max_pages else True:
        ic(f"Scraping page {current_page}...")

        # Wait for constituent items to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "fsConstituentItem"))
        )
        # Process items on current page
        constituent_items = driver.find_elements(By.CLASS_NAME, "fsConstituentItem")
        for item in constituent_items:
            name = (item
                    .find_element(By.CLASS_NAME, "fsConstituentProfileLink")
                    .text)
            try:
                titles = (item
                          .find_element(By.CLASS_NAME, "fsTitles")
                          .text
                          .replace("Titles:", "").strip())
            except NoSuchElementException:
                titles = None
            try:
                locations = (item
                             .find_element(By.CLASS_NAME, "fsLocations")
                             .text
                             .replace("Locations:", "").strip())
            except NoSuchElementException:
                locations = None

            try:
                email = (item
                         .find_element(By.CLASS_NAME, "fsEmail")
                         .text.replace("Email:", "").strip())
            except NoSuchElementException:
                email = None

            emails_.add(
                Employee(
                    name=name,
                    email=email,
                    titles=titles,
                    locations=locations
                )
            )

        try:
            next_button = (WebDriverWait(driver, 10)
            .until(
                EC.element_to_be_clickable(
                    (By.CLASS_NAME, "fsNextPageLink")
                )
            ))
            driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
            time.sleep(1)
            next_button.click()
            current_page += 1
            time.sleep(2)
        except (TimeoutException, NoSuchElementException):
            ic("No more pages found or reached the end")
            break
    return emails_


emails = scrape_emails()
with open(Path.home() / 'Downloads' / 'fcs_emails2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(EMPLOYEE_FIELDS)
    for employee in emails:
        writer.writerow([getattr(employee, x) for x in EMPLOYEE_FIELDS])
