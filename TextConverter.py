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

''' # Decomment for using other formats
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

if __name__ == '__main__':
    f = convertPDFToText("Resume_Harsha_Updated.pdf")
    #print(get_total_experience('f'))
    print((f))
