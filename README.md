# APTS_ApplicantParsingAndTrackingSystem ![](https://img.shields.io/badge/Harsha-Karpurapu-brightgreen.svg?colorB=ff0000)

### Objectives: 
- Extract the important information from the resume
- Match the resume to the provided expertise list (This list was provided by *Vinod* to Harsha)
- Match the resume to the Job description (For Concept purpose, I have downloaded the data engineer resume from the job board of travelers insurance)

---

### Code Requirements
- Execute the below command from your terminal for installing all the required libraries

```
pip install requirement.txt
```
- Download the spacy word embedding model using the below command

```
python -m spacy download en_core_web_md
```

---

### Usage

```
python resumeparser [-resume resumeFile]

-resume; input resume file

Example: 
python resumeparser -resume "data/resumes/resume_trail4.pdf"
```

when you execute the code, the code pushes the output to the respective columns in the database and prints the contents in the json format

- Download the DB Browser from [here](https://sqlitebrowser.org/dl/) for viewing the sqlite database

---

### Procedures Used for Achieving the objectives (At highlevel)

#### Obj1: Extract the important information from the resume
- Mobile, Email Address, Github, Linkedin
  - Used Regex

- Address
  - Used the combination of Regex and pyad library (for standardization)

- Name
  - Used the chunking and chinking concepts in combination with a lookup table. Unlike any NER model, this process can prescribe the name rather than predict
    - ``` This process is proven to give better results rather than using any pretrained NER models as its hard for any NER model to understand the variations and the variety of resume.``` 

#### Obj2: Matching the Resume to provided expertise list

- For every word in the expertise list, get the glove word embedding provided by spacy library
- Then get the similarity score of the each word embedding to all the `nouns` (do the parts of speech tagging and eliminate all other part of speech words  other than nouns) of the resume;
- The top 5 highest similarity score words are the top 5 as the expertise of the resume

```

We have used the pretrained glove embedded model, in an ideal scenario we need to train our 
own word embedded model on a specfic domain corpus. But the results from the above approach 
seem compelling too. 

Examples: 
--------------------------------------------------------------------------------------------
-'resume_trail4'(data/resumes) is the resume of an Orthopaedic Spine Surgery, below are the top5 expertises 
the code matched from the expertise list

'radiology, internal medicine, general dentistry, general surgeon, physical therapy'
--------------------------------------------------------------------------------------------
- 'resume_trail2' is the resume of a Building inspector (related to construction), below are 
the top5 expertises the code matched from the expertise list

'highway design & construction, public health, life care planner, fire cause & analysis, 
hospital administration'
--------------------------------------------------------------------------------------------
```

#### Matching the Resume to the job description

- Get the Glove word embedding to every `noun and verb` of the resume and the job description. 
- The calcuate the similarity score between those documents with only verbs and nouns

```
All the traditional ATS systems uses the keywords to filter out the resumes, however there are 
many scenarios where keyword approach is proven wrong. This approach is presented as a POC how can we 
better construct the ATS system with word embedding as they care both for keywords and the dependency 
between words

Examples:
Currently the job description to be matched is a data engineer position from Travelers Insurance

Similarity score between Resume_Harsha_AIScientist (my resume) and job description is 0.90
Similarity score between resume_trail2 (related to construction) and job description is 0.71

We can clearly see how this process can be efficient in picking the best resumes from a pool of 
resumes. 
```


