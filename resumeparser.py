# !/Users/kbsriharsha/anaconda3/bin/python
# coding: utf-8
# author: Bharat Sri Harsha karpurapu

# Importing libraries
import sys
import os
import pandas as pd
import numpy as np
import argparse

import utils
import TextConverter

# Developing the argparser to take the resume
# Instantiate the parser
parser = argparse.ArgumentParser(description='Optional app description')

# Required positional argument
parser.add_argument('-resume',
                    help='A required integer positional argument')

args = parser.parse_args()

resume = args.resume

def pdfToText(resume):
    """
    Takes the pdf format resume and converts it to text

    Resume: Resume to be converted to text
    """

    return TextConverter.convertPDFToText(resume)

def resume_extracts(text):
    """
    Takes the text format of the resume and returns all the values

    text: text format of the resume
    """

    # Preprocessing the document
