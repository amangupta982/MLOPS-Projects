import nltk
from nltk.corpus import twitter_samples
import pandas as pd
import os
import argparse

def ingest_data(output_dir='data/raw'):
    """
    Downloads twitter samples dataset from NLTK and saves it as a CSV.
    """
    print("Downloading twitter_samples dataset from NLTK...")
    nltk.download('twitter_samples', quiet=True)

    print("Loading tweets...")
    positive_tweets = twitter_samples.strings('positive_tweets.json')
    negative_tweets = twitter_samples.strings('negative_tweets.json')

    print(f"Loaded {len(positive_tweets)} positive and {len(negative_tweets)} negative tweets.")

    # Create a dataframe
    df_pos = pd.DataFrame({'tweet': positive_tweets, 'sentiment': 1})
    df_neg = pd.DataFrame({'tweet': negative_tweets, 'sentiment': 0})
    df = pd.concat([df_pos, df_neg], ignore_index=True)

    # Save to data/raw
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'tweets.csv')
    df.to_csv(output_path, index=False)
    print(f"Data saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_dir', type=str, default='data/raw', help='Directory to save raw data')
    args = parser.parse_args()
    ingest_data(args.output_dir)
