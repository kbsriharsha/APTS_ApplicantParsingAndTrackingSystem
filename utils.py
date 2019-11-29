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
import spacy
import collections

from TextConverter import convertPDFToText

def preprocess(text):
    """
    Elimates the noise and unwanted characters

    text: text that has to be cleaned
    """
    return re.sub(r'[^\x00-\x7f]',"","\n".join([el.strip() for el in text.split("\n") if len(el.strip()) > 1]))

def sent_pos(text):
    """
    Splits the given text into words and identifies the pos tags
    """
    lines = [el.strip() for el in text.split("\n") if len(el) > 0]
    lines = [nltk.word_tokenize(el) for el in lines]
    tokens = lines
    lines = [nltk.pos_tag(el) for el in lines]

    return lines, tokens

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
    mob_num_regex = mob_num_regex = r'''\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)[-\.\s]*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]\d{3}.\d{4}|\(\d{3}[)-\.\s].\d{3}.\d{4}'''

    phone = re.findall(re.compile(mob_num_regex), text)
    if phone:
        number = ''.join(phone[0])

        return str(number)
    else:

        return None

def address(text):
    """
    Extracts the address information

    text: input text from where address to be extracted
    """
    if pyap.parse(re.sub(r',|#\d+', "", text), country='US'):

        return pyap.parse(re.sub(r',|#\d+', "", text), country='US')[0]
    else:

        return None

def linkedin(text):
    """
    Extracts linkedin details

    text: input text from where linkedin details have to be extracted
    """
    linkedin_reg = r'''https:\/\/www.linkedin.com\/in\/\w*'''
    linkedin = re.findall(re.compile(linkedin_reg), text)
    if linkedin:

        return str(linkedin[0])
    else:

        return None

def github(text):
    """
    Extracts github details

    text: input text from where linkedin details have to be extracted
    """
    github_req = r'''https:\/\/github.com\/\w*'''
    github = re.findall(re.compile(github_req), text)
    if github:

        return str(github[0])
    else:

        return None

def name(text):
    """
    This function gives the names from the given text

    text: Text from which names has to be extracted
    """
    Names = open("data/first_names.txt", "r").read().lower()
    # Lookup in a set is much faster
    Names = set(Names.split("\n"))
    otherNameHits = []
    nameHits = []
    name = None
    lines = [el.strip() for el in text.split("\n") if len(el) > 0]
    lines = [nltk.word_tokenize(el) for el in lines]
    tokens = lines
    lines = [nltk.pos_tag(el) for el in lines]
    grammar = r'NAME: {<NN.*><NN.*><NN.*><NN.*>*}'
    chunkParser = nltk.RegexpParser(grammar)
    all_chunked_tokens = []
    for tagged_tokens in lines:
        if len(tagged_tokens) == 0: continue # Prevent it from printing warnings
        chunked_tokens = chunkParser.parse(tagged_tokens)
        all_chunked_tokens.append(chunked_tokens)
        for subtree in chunked_tokens.subtrees():
            if subtree.label() == 'NAME':
                for ind, leaf in enumerate(subtree.leaves()):
                    if leaf[0].lower() in Names and 'NN' in leaf[1]:
                        hit = " ".join([el[0] for el in subtree.leaves()[ind:ind+3]])
                        if re.compile(r'[\d,:]').search(hit): continue
                        nameHits.append(hit)
    if len(nameHits) > 0:
        nameHits = [re.sub(r'[^a-zA-Z \-]', '', el).strip() for el in nameHits]
        name = " ".join([el[0].upper()+el[1:].lower() for el in nameHits[0].split() if len(el)>0])
        otherNameHits = nameHits[1:]

    return str(name)

def expertise_match(text):
    """
    Matches the given text to the expertise list

    text: text which has to be matched with the expertise
    """
    lines, tokens = sent_pos(text)

    # Selecting only nouns from the text
    lis = []
    for x in lines:
        lines_nns = " ".join([i for (i,j) in x if j in ('NN', 'NNP', 'NNS', 'NNPS')])
        lis.append(lines_nns)
    text = "\n".join([x for x in lis if len(x) > 1])

    #Importing the expertise list and preprocessing it
    exps = open("data/expertise.txt", "r").read().lower()
    exps = set([re.sub(r'"', "", x) for x in exps.split("\n")])

    #Loading word embedding model
    nlp = spacy.load('en_core_web_md')

    # Measuring the simiarity of score of every expertise with the resume
    sim_scores = dict([(x, float(nlp(x).similarity(nlp(text)))) for x in exps])

    # Returning the top 5 expertises which has more expertise scores
    top5_sim = collections.Counter(sim_scores)
    top5_sim = [x for x,y in top5_sim.most_common(5)]

    return ", ".join(top5_sim)

def jobdes_rsm_similarity(text):
    """
    Provides a similarity score between the job description and resume

    text: text to which the similarity score has to be calcualted from the job description
    """
    lines, tokens = sent_pos(text)

    # Selecting only nouns and verbs from the text
    lis = []
    for x in lines:
        lines_nns = " ".join([i for (i,j) in x if j in ('NN', 'NNP', 'NNS', 'NNPS', 'VB', 'VBP', 'VBD')])
        lis.append(lines_nns)
    text_resume = "\n".join([x for x in lis if len(x) > 1])


    # Importing the job descrioption; currently matches to data engineer resume from travelers insurance job board
    jobdes = open("data/jobdescription_dataengineer.txt", "r").read().lower()

    lines, tokens = sent_pos(jobdes)

    # Selecting only nouns from the text
    lis = []
    for x in lines:
        lines_nns = " ".join([i for (i,j) in x if j in ('NN', 'NNP', 'NNS', 'NNPS')])
        lis.append(lines_nns)
    text_jobdes = "\n".join([x for x in lis if len(x) > 1])

    #Loading word embedding model
    nlp = spacy.load('en_core_web_md')

    # Calculating similarity score
    sim_score = float(nlp(jobdes).similarity(nlp(text_resume)))

    return sim_score


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
    print("Importing Utils")
