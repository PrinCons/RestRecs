## Restaurant Recommnder Project 

### Introduction 

This project is a demonstartion of some of my skills - a portfolio project of sorts, perhaps a Proof of Concept (POC). It is inspired by a real issue I have - I want to grab dinner somwhere, but where? I have an idea of what I want and where I am, but I don't want to spend time reading reviews, examinig menus, and picking a place out of several options. 

This solution is meant to be a work with a simple input: name a cuisine or a dish and a New York area, and the recommender will find a place where the user can eat that food right now. The value proposition here is all about reducing decision fatigue and potential disappointment in dinner after a long day. The engine, ideally, would consider all relevant constraints - is it open? is it clean? is it close enough? is the particular item I'm looking for highly regarded in this establishment? do people like me tend to enjoy this place? has it gotten worse recently? etc. etc.

The aim here is not to find the absolute best place to eat, but rather to find a place where one can fulfill their dining wishes here and now to a satisfactory degree; in simple terms - I don't want to stand in line for an hour to eat a "the best" taco everyone's talking about on social media and ranking highly on Google Maps if there's a delicious nopale taco waiting for me behind the corener. 

### Diagrams

[project structure plan diagrams](https://www.figma.com/board/AQLD5w02zfO4W1SyS9XRGD/Restaurant-Recommender?node-id=0-1&t=GldYO8Z9WjQPcsbr-1)

The figma includes two diagrams: 
- main project 
- rec engine 

### Work in Progress: Notes and Progress

While the data used for this POC is essentially dummy data (it's too old and too sparse to be reliable), the issue this project solves is a real one, at least in my personal experience. 

**Complete files:**
1. [_rest_data_exploration.ipynb_](https://github.com/PrinCons/RestRecs/blob/e0e59f8b1dffd4f2a75f791572838840b7cfa714/models/research/rest_data_exploration.ipynb) - construction of a working dataset** that will be used for enrichment and reccomendations; the notebook includes the full process from four seperate tables to the final product, including all the considerations that went into processing. The notebook concludes with some descritipve statistics about the working dataset.
2.  [_cuisine_exploration.ipynb_](https://github.com/PrinCons/RestRecs/blob/e0e59f8b1dffd4f2a75f791572838840b7cfa714/models/research/cuisine_exploration.ipynb) - preparing for enriching the data for recommender using machine learning methods; using Word2Vec to create a set of tagged menus and cuisines to be used as a training set in the next step.

**Work in Progress:** 
2. _item_prediction.ipynb_ - data enrichemnt using logistic regression for menu classification. 
3. _review_sent_analysis.ipynb_ - extracting recommended items using aspect-based sentiment analysis (ABSA). 
4. _recommener.ipynb_ - the actual recomendation engine, filtering and ranking to output a single recomendation.


** working dataset - the dataset that will used for enrichment and recommendations. 
