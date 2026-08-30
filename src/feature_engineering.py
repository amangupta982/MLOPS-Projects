import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import os
import argparse

def engineer_features(input_path, output_dir):
    print(f"Loading preprocessed data from {input_path}...")
    df = pd.read_csv(input_path)
    
    # Ensure there are no NaNs in cleaned_tweet
    df.dropna(subset=['cleaned_tweet'], inplace=True)
    
    X = df['cleaned_tweet']
    y = df['sentiment']
    
    print("Splitting data into train and test sets...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    print("Extracting TF-IDF features...")
    vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)
    
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"Saving features and vectorizer to {output_dir}...")
    with open(os.path.join(output_dir, 'train_data.pkl'), 'wb') as f:
        pickle.dump((X_train_tfidf, y_train), f)
        
    with open(os.path.join(output_dir, 'test_data.pkl'), 'wb') as f:
        pickle.dump((X_test_tfidf, y_test), f)
        
    with open(os.path.join(output_dir, 'tfidf_vectorizer.pkl'), 'wb') as f:
        pickle.dump(vectorizer, f)
        
    print("Feature engineering completed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', type=str, default='data/interim/cleaned_tweets.csv', help='Path to preprocessed data')
    parser.add_argument('--output_dir', type=str, default='data/processed', help='Directory to save features')
    args = parser.parse_args()
    
    engineer_features(args.input_file, args.output_dir)
