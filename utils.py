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

if __name__ == '__main__':
    print("Provides Helper Functions")
