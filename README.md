# Travel Recommendation System  

This project recommends countries based on user descriptions using TF-IDF vectorization and cosine similarity. It processes a dataset of country descriptions and matches them to a user’s input to return the top 5 most relevant travel destinations.

I chose to create a travel recommendation system because travel has been a huge inspiration in my life and has increased my appreciation for the world and the people around me by understanding so many different perspectives. Through this challenge, I felt like I could create a platform to inspire more people to explore some place other than where they've lived and grow from that experience in the way they would like to. 

---

## Dataset  
- **File:** `country_descriptions_final.csv`  
- **Source:** I created the dataset myself using BBC's and World Banks country profiles pages. It is a simple table with one sentence descriptions of over 100 countries. I was unable to find a dataset that provided me with text descriptions of countries as the problem statement required, therefore, I built it myself.  
- **Loading Steps:** The dataset is automatically loaded in `main.py`, so no additional steps are required. Ensure the file is in the same directory as the script. It is uploaded to this repo as 'country_descriptions_final.csv'.

---

## Setup  
### **Python Version**  
- Recommended: **Python 3.8+**  

## Install Dependencies
- to install pandas, scikit-learn, and spacy: 
**pip install pandas scikit-learn spacy**
- to download the language model:
**python -m spacy download en_core_web_sm**

## Run the Recommender
**python3 main.py "what do you look for in a travel destination?"**
- example 1) python3 main.py i want to visit a country with mountains and hiking trails
- example 2) python3 main.py i like to immerse in a country's art, history, and culture

## Expected Results
**example 1** 

**Top Travel Recommendations for You:**
1) Haiti: Haiti has a vibrant Creole culture and adventure in its rugged mountain trails.
2) Czech Republic: The Czech Republic boasts fairy-tale castles, Gothic cathedrals, and forested hiking trails.
3) Belgium: Belgium is famous for its medieval cities, castles, and adventure activities like hiking in the Ardennes.
4) Guatemala: Guatemala features Mayan ruins and volcano hiking adventures.
5) Lebanon: Lebanon is home to Phoenician history and beautiful mountain landscapes for hiking.

### Salary Expectations
$23-25/hour 
