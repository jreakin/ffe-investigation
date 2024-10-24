from __future__ import annotations
from typing import Optional
import time
import csv
from functools import partial
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


def find_replace_element(item: webdriver, cls_name: str, replace: Optional[str] = None):
    try:
        stmt = (item
                .find_element(By.CLASS_NAME, cls_name)
                .text)
        return stmt.replace(replace, "") if replace else stmt
    except NoSuchElementException:
        return None


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
            _find = partial(find_replace_element, item)
            emails_.add(
                Employee(
                    name=_find(cls_name="fsConstituentProfileLink"),
                    email=_find(cls_name="fsEmail", replace="Email:"),
                    titles=_find(cls_name="fsTitles", replace="Titles:"),
                    locations=_find(cls_name="fsLocations", replace="Locations:")
                )
            )

        try:
            next_button = (
                WebDriverWait(driver, 10)
                .until(
                    EC.element_to_be_clickable(
                        (By.CLASS_NAME, "fsNextPageLink")
                    )
                )
            )
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
