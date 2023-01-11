
# Fraudulent Job Postings
*Restricted to only install scikit-learn, gensim, and pandas.*

The full instructions to this project can be found [here.](https://github.com/victorbpeterson/Fraudulent-Job-Postings/blob/main/Instructions.md)

## Project Overview
The [Better Business Bureau](https://www.bbb.org/content/dam/0734-st-louis/job-scams/JOB%20SCAMS%20STUDY%20v5.pdf) estimates that each year, 14 million people are exposed to job scams, with $2 billion in direct losses[^1]. Although job scams have been around for a while, fraudulent job postings can be tricky to spot. 
The [dataset](https://github.com/victorbpeterson/Fraudulent-Job-Postings/tree/main/data) provided, contains around 9k job postings, of which 400 are fake. 

## Goal
This project aims to create a classifier to identify whether a job posting is fake or real.

## Grading Metrics
Due to the data imbalance, submissions were ranked by their F1 score and graded accordingly (higher F1 = higher grade). All submissions needed a total runtime no more than 30 minutes. 

## Data Preprocessing
Cleaned the data with [Regex](https://docs.python.org/3/library/re.html)
1. Combined 'description', 'title', and, 'requirements' columns.
2. Converted the text to lowercase
3. Remove punctuation, digits, underscore, single characters, and multiple spaces.

Sent this data to the [TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
1. Removed Stopwords
2. Transformed text to feature vectors

## Model Training
Implemented [AdaBoostClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html), 
[SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html), [SGDClassifer](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html), 
[RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html), and [PassiveAggressiveClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveClassifier.html)
with both [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html) and [RandomizedSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html).

For the final model, PassiveAggressiveClassifier outperformed the other classifiers and had matching F1 scores from both tuning algorithms.
RandomizedSearchCV was chosen based on its faster runtime.



## Outcome
The [finished product](https://github.com/victorbpeterson/Fraudulent-Job-Postings/blob/main/Project/project.py) outperformed all but one of my peers.

F1: 0.81

Total Runtime: ~ 18 seconds

## Improvements
Due to the restriction in libraries that could be used, the amount of NLP was limited. Installing other packages such as NLTK, could provide some useful methods to help preprocess the data. 
Also, the data used for this project was very imbalanced. Using techniques like SMOTE to generate more fraudulent job postings may provide better results.

[^1]: Baker , C. Steven. 2021, Job Scams, https://www.bbb.org/content/dam/0734-st-louis/job-scams/JOB%20SCAMS%20STUDY%20v5.pdf. Accessed Jan. 2023.