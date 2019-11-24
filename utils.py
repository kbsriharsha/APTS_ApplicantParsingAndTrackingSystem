# !/Users/kbsriharsha/anaconda3/bin/python
# coding: utf-8
# @author: Bharat Sri Harsha karpurapu

"""
This program provides utilities functions
for extracting information from the resume

"""

# Importing libraries
import sys
import os
import re
import pyap
import nltk
import textstat

def email(text):
    """
    function to extract email
    text: plain text extracted from resume file
    """
    email = re.findall(r"([^@|\s]+@[^@]+\.[^@|\s]+)", text)
    if email:
        try:

            return email[0].split()[0].strip(';')
        except IndexError:

            return None

def mobile_number(text):
    """
    function to extract mobile number from text
    text: plain text extracted from resume file
    """
    mob_num_regex = r'''\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}
                    |\(\d{3}\)[-\.\s]*\d{3}[-\.\s]??\d{4}
                    |\d{3}[-\.\s]??\d{4}
                    |\(\d{3}[)-\.\s].\d{3}.\d{4}'''

    phone = re.findall(re.compile(mob_num_regex), text)
    if phone:
        number = ''.join(phone[0])

        return number

def address(text):
    """
    Extracts the address information

    text: input text from where address to be extracted
    """
    return pyap.parse(re.sub(r',', "", f), country='US')[0]

def linkedin(text):
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

def name(text):
    """
    Extracts Name from the
    """

def readability(text):
    """
    Provides the readability grade for the text. Here we are using the
    flesch reading ease score. Higher the score, easier to read

    text: input text on which score has to be calculated
    """
    score = textstat.flesch_reading_ease(text)
    grade = round(textstat.flesch_kincaid_grade(text))

    if score > 90:
        summary = "Very easy to read. Easily understood by an average 11-year-old student; "
    elif score > 80:
        summary = "Easy to read. Conversational English for consumers"
    elif score > 70:
        summary = "Fairly easy to read"
    elif score > 60:
        summary = "Plain English. Easily understood by 13- to 15-year-old students."
    elif score > 50:
        summary = "Fairly difficult to read."
    elif score > 30:
        summary = "Difficult to read"
    else:
        summary = "Very difficult to read. Best understood by university graduates."

    return score, summary, grade



if __name__ == '__main__':
    print("Provides Helper Functions")
    print(readability("Harsha is a nostalgic romio"))
