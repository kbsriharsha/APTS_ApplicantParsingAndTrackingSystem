# APTS_ApplicantParsingAndTrackingSystem ![](https://img.shields.io/badge/Harsha-Karpurapu-brightgreen.svg?colorB=ff0000)

## Objectives: 
- Extracts the important information from the resume
- Matches the resume to the provided expertise list (This list was provided by Vinod to Harsha)
- Matches the resume to the Job description (For Concept purpose, I downloaded one of the resumes from the job board of travelers insurance)

## Information Extraction Details

- Name
Based on the concepts of chunking and chinking along with the lookup data

- Mobile, Email Address, Github, Linkedin
Regex

- Address
Regex and pyad library (for standardization)

## Matching the Resume to provided expertise list

- For every word in the expertise list, we have got the gllove word embedding provided by spacy library
- Then we got the similarity score of the each word embedding to the nouns and verbs of the resume
- The top 5 words with more similarity score to the score are given as the top 5 expertises of the resume 

```We have used the pretrained glove embeddeding moodek, in an ideal scenario we need to train our own emebddeding model on our domain corpus. The above appproach was presented as a proof of concept```

## Matching the Resume to the job description

- This process also uses glove word embedding and calculate the similarity score between the job description and the resume

```All the traditional ATS systems uses the keywords to filter out the resumes, however there are many scenarios where keyword approach is proven wrong. This is presented as a POC how can we better construct any ATS system with word embedding as they care both for keywords and the order of the words```

## Usage

```
python resumeparser [-resume resumeFile]

-resume; input resume file

Example: 
python resumeparser -resume "/data/resumes/resume_trail4.pdf"
```
