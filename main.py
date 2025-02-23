import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import sys
import spacy

#load the local dataset from within directory
df = pd.read_csv("country_descriptions_final.csv")

#main function: recommend countries based on user input, give top 5 results
def recommend_countries(user_input, top_n=5):
    #append the user's input to dataset so it is read in the same column as the description
    descriptions = df["Description"].tolist() + [user_input]  
    
    #need to convert text into numbers to find frequency of words used
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(descriptions)

    #use the cosine similarity to compute the similarity between words in user input and dataset
    cosine_sim = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])  #compare last entry(user input) with all others

    #get the top 5 most similar countries
    #sort similarity score in ascending order using argsort()

    top_indices = cosine_sim[0].argsort()[-top_n:][::-1]  # Sort in descending order of similarity
    recommendations = df.iloc[top_indices]

    print("\n **Top Travel Recommendations for You:**")
    for idx, row in recommendations.iterrows():
        print(f"{row['Country']}: {row['Description']}")

#load the spaCy English NLP model to process the text more thouroughly and give more defined responses
nlp = spacy.load("en_core_web_sm")

#will extract key terms(nouns, proper nons, adjectives) from the input and improve recommendation accuracy by focusing on finding the important words
def extract_keywords(text):
    doc = nlp(text) #process the input text
    return [token.lemma_ for token in doc if token.pos_ in ["NOUN", "PROPN", "ADJ"]] #extract those keywords

#command line takes input arguments
if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_input = " ".join(sys.argv[1:])  #take and store user input argument from command line
        recommend_countries(user_input)
    else:
        print("Usage: python3 main.py \"I want to visit a country with ....\"")