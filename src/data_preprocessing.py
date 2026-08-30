import pandas as pd
import re
import os
import argparse

def clean_tweet(tweet):
    """
    Basic text cleaning for tweets.
    """
    # Remove URLs
    tweet = re.sub(r'http\S+|www\S+|https\S+', '', tweet, flags=re.MULTILINE)
    # Remove user @ references and '#' from tweet
    tweet = re.sub(r'\@\w+|\#','', tweet)
    # Convert to lowercase
    tweet = tweet.lower().strip()
    return tweet

def preprocess_data(input_path, output_dir):
    print(f"Loading raw data from {input_path}...")
    df = pd.read_csv(input_path)
    
    print("Preprocessing tweets...")
    df['cleaned_tweet'] = df['tweet'].apply(clean_tweet)
    
    # Drop empty strings
    df = df[df['cleaned_tweet'] != '']
    
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'cleaned_tweets.csv')
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', type=str, default='data/raw/tweets.csv', help='Path to raw data')
    parser.add_argument('--output_dir', type=str, default='data/interim', help='Directory to save preprocessed data')
    args = parser.parse_args()
    
    preprocess_data(args.input_file, args.output_dir)
