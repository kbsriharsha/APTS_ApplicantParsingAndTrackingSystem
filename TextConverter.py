# !/Users/kbsriharsha/anaconda3/bin/python
# coding: utf-8
# @author: Bharat Sri Harsha karpurapu

"""
This program helps converting different formats of the
input file (pdf, doc, etc) to text (.txt)

"""

# Importing libraries
import sys
import os
import re
import pyap
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
#from cStringIO import StringIO #use this for python2
'''
additional libraries for other formats

#from pyth.plugins.rtf15.reader import Rtf15Reader
#from pyth.plugins.plaintext.writer import PlaintextWriter
#from docx import Document
'''

def convertPDFToText(path):
    """
    This function converts pdf to text

    path: path of the file to be converted
    """
    fp = open(path, 'rb')
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.

    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        data =  retstr.getvalue()

    return data

'''
def convertRtfToText(path):
    """
    This function converts Rtf to text

    path: path of the file to be converted
    """

	doc = Rtf15Reader.read(open(path))

	return PlaintextWriter.write(doc).getvalue()

def convertDocxToText(path):
    """
    This function converts Rtf to text

    path: path of the file to be converted
    """

	document = Document(path)

	return "\n".join([para.text for para in document.paragraphs])
'''

def extract_email(text):
    '''
    Helper function to extract email id from text
    :param text: plain text extracted from resume file
    '''
    email = re.findall(r"([^@|\s]+@[^@]+\.[^@|\s]+)", text)
    if email:
        try:
            return email[0].split()[0].strip(';')
        except IndexError:
            return None

def extract_mobile_number(text):
    '''
    Helper function to extract mobile number from text
    :param text: plain text extracted from resume file
    :return: string of extracted mobile numbers
    '''
    mob_num_regex = r'''\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}
                    |\(\d{3}\)[-\.\s]*\d{3}[-\.\s]??\d{4}
                    |\d{3}[-\.\s]??\d{4}
                    |\(\d{3}[)-\.\s].\d{3}.\d{4}'''

    phone = re.findall(re.compile(mob_num_regex), text)
    if phone:
        number = ''.join(phone[0])
        return number

def extract_address(text):
    """
    Extracts the address information

    text: input text from where address to be extracted
    """
    return pyap.parse(re.sub(r',', "", f), country='US')[0]

def extract_linkedin(text):
    """
    Extracts linkedin details

    text: input text from where linkedin details have to be extracted
    """
    linkedin_reg = r'''https:\/\/www.linkedin.com\/in\/\w*'''
    linkedin = re.findall(re.compile(linkedin_reg), text)
    return linkedin[0]

def extract_github(text):
    """
    Extracts linkedin details

    text: input text from where linkedin details have to be extracted
    """
    github_req = r'''https:\/\/github.com\/\w*'''
    github = re.findall(re.compile(github_req), text)
    return github[0]



if __name__ == '__main__':
    f = convertPDFToText("Resume_Harsha_Updated.pdf")
    #print(get_total_experience('f'))
    print((f))
