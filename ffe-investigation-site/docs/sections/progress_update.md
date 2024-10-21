# Letter to FCS Board of Education Requesting A Progress Update

Findlay City Schools Board of Education

April 17, 2024

Mr. Chris Aldrich, President  
Dr. Karthy Siebenaler Wilson, Vice President  
Mrs. Susan Russel, Member  
Ms. Laura Eier, Member  
Mr. Matt Cooper, Member  
Mrs. Pam Harrington, Treasurer  

Re: Follow-up to Public Information Request Submitted February 5, 2024

Dear Distinguished Members of the Board,

On January 29, my father, Rick Eakin, and I sent a letter to the School Board members, seeking clarification on important matters. On January 30, we received a reply from the FCS Board President, Chris Aldrich, which was utterly devoid of any clarification. In response, I promptly sent a follow-up email later that day, inquiring about which specific part of our letter his reply was addressing. Disappointingly, there has been no response to this follow-up.

On February 5, I submitted a public information request, expecting a response within 10 business days. FCS Treasurer Pam Harrington acknowledged receipt of the request via email on February 9.

A staggering 42 days passed after my public information request submission before receiving an update on March 19. The school district claimed they had only begun reviewing the records due to the volume produced, engaging an outside company to process the data. However, this company had just set up the review platform the previous week. The email vaguely promised to continue working on the documents and produce them within a couple of weeks.

Yet, 4 weeks after this supposed "progress update" and a total of 71 days since the initial request, I still haven't received any of the requested information. This delay is unacceptable and demonstrates a blatant disregard for the importance of transparency and timely communication.

It is highly suspect that it took 42 days to develop an interface for reviewing and filtering text data. With just 50 lines of code and some 'for' loops, a script utilizing Optical Character Recognition (OCR) can easily convert PDF and image contents into text (I have included an [^1]example for reference). Moreover, email contents from Microsoft Outlook and Google Workspaces can be accessed easily through the APIs provided by both platforms.

The delay in fulfilling my public information request, regarding an investigation completed in a mere 48 days, is nearly twice the time and is deeply concerning. The initial investigation involved in-person interviews with multiple individuals, carefully coordinating their schedules and including parents, legal or union representation, or other relevant parties.

In President Aldrich's email, to which I have not received a response to my reply, he emphasized that the District sought to conduct an unbiased investigation into the culture and behaviors of the program. In the interest of transparency and the credibility of the investigation's findings, the actual materials examined during the investigation should also be made available for scrutiny, agreed?

If the District's dedication to transparency isn't sufficient motivation to fulfill my request promptly, please be aware that the Ohio Revised Code offers various alternatives to ensure proper motivation. Pursuing these avenues would likely be embarrassing for the District and intensify the community's skepticism about the integrity of the investigation, which is an outcome neither of us wants to see.

Due to the District's delay in processing my public information request, which was not initiated until 42 days after submission, I insist on receiving a precise and credible expected time of delivery by Friday, April 19, 2024.

Sincerely, 

John R. Eakin

[^1]: 
    ```py title="Example OCR Function" linenums='1'

    import PyPDF2
    from PIL import Image
    import pytesseract

    def read_pdf(file_path):
        pdf_file = open(file_path, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        num_pages = pdf_reader.numPages
        for page in range(num_pages):
            text = ""
            text += pdf_reader.getPage(page).extractText()
            pdf_file.close()
        return text

    def read_image (file_path):
        img = Image.open(file_path)
        text = pytesseract.image_to_string(img)
        return text

    # Usage
    pdf_text = read_pdf('path_to_your_pdf.pdf')
    image_text = read_image('path_to_your_image.png')

    print("PDF Text: ", pdf_text)
    print("Image Text: ", image_text)
    ```