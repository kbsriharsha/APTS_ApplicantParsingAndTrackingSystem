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
import dataconnections

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
    conts = {}

    # Preprocessing the document
    text = utils.preprocess(text)

    # Extracting name
    conts['name'] = utils.name(text)

    # Extracting Address
    conts['address'] = utils.address(text)

    # Extracting mobile number
    conts['mobile'] = utils.mobile_number(text)

    # Extracting Email
    conts['email'] = utils.email(text)

    # Extracting github
    conts['github'] = utils.github(text)

    # Extracting linkedin
    conts['linkedin'] = utils.linkedin(text)

    # Provides the expertise list match
    conts['expertise'] = utils.expertise_match(text)

    # Provides the resume to job description simiarity
    conts['similarity_score'] = utils.jobdes_rsm_similarity(text)

    return conts

if __name__ == '__main__':
    # Developing the argparser to take the resume
    # Instantiate the parser
    parser = argparse.ArgumentParser(description='Optional app description')

    # Required positional argument
    parser.add_argument('-resume',
                    help='A required integer positional argument')

    args = parser.parse_args()

    resume = args.resume

    text_resume = pdfToText(resume)

    contents = resume_extracts(text_resume)

    print(contents)

    print("\n Connecting to the database and pushing the contents")
    # Connecting to the database
    c, conn = dataconnections.connect_database("resume_info.db")

    # Creating the table: Execute this only for the first time
    dataconnections.create_table(c, "resume_information")

    # Data Entry to data
    dataconnections.data_entry(c, conn, "resume_information", contents)

    print("Successfully Completed")
