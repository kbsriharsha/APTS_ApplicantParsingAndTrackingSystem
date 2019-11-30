# APTS_ApplicantParsingAndTrackingSystem ![](https://img.shields.io/badge/Harsha-Karpurapu-brightgreen.svg?colorB=ff0000)

### Objectives: 
- Extract the important information from the resume
- Matches the resume to the provided expertise list (This list was provided by *Vinod* to Harsha)
- Matches the resume to the Job description (For Concept purpose, I have downloaded the data engineer resume from the job board of travelers insurance)

### Code Requirements
- Execute the below command from your terminal for installing all the required libraries

```
pip install requirement.txt
```
- Download the spacy word embedding model using the below command

```
python -m spacy download en_core_web_md
```
### Usage

```
python resumeparser [-resume resumeFile]

-resume; input resume file

Example: 
python resumeparser -resume "/data/resumes/resume_trail4.pdf"
```

when someone executes the code, the code pushes the output to the respective columns in the database and prints the contents in the json format

- Download the DB Browser from [here](https://sqlitebrowser.org/dl/) for viewing the sqlite database

### Procedures Used for Achieving the objectives (At highlevel)

#### Obj1: Extract the important information from the resume
- Mobile, Email Address, Github, Linkedin
  - Used Regex

- Address
  - Used the combination of Regex and pyad library (for standardization)

- Name
  - Used the chunking and chinking concepts incombination with a lookup table. Unlike any NER model, this process can prescribe the name rather than predict
    - ``` This process is proven to give better results rather than using any pretrained NER models as its going to be hard for any NER model to understand the variations and the variety of resume.``` 

## Matching the Resume to provided expertise list

- For every word in the expertise list, we have got the gllove word embedding provided by spacy library
- Then we got the similarity score of the each word embedding to the nouns and verbs of the resume
- The top 5 words with more similarity score to the score are given as the top 5 expertises of the resume 

```We have used the pretrained glove embeddeding moodek, in an ideal scenario we need to train our own emebddeding model on our domain corpus. The above appproach was presented as a proof of concept```

## Matching the Resume to the job description

- This process also uses glove word embedding and calculate the similarity score between the job description and the resume

```All the traditional ATS systems uses the keywords to filter out the resumes, however there are many scenarios where keyword approach is proven wrong. This is presented as a POC how can we better construct any ATS system with word embedding as they care both for keywords and the order of the words```


