import pickle
from sklearn.linear_model import LogisticRegression
import os
import argparse

def build_model(input_path, output_dir):
    print(f"Loading training data from {input_path}...")
    with open(input_path, 'rb') as f:
        X_train, y_train = pickle.load(f)
        
    print("Training Logistic Regression model...")
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'sentiment_model.pkl')
    
    print(f"Saving trained model to {output_path}...")
    with open(output_path, 'wb') as f:
        pickle.dump(model, f)
        
    print("Model building completed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', type=str, default='data/processed/train_data.pkl', help='Path to training data')
    parser.add_argument('--output_dir', type=str, default='models', help='Directory to save the trained model')
    args = parser.parse_args()
    
    build_model(args.input_file, args.output_dir)
