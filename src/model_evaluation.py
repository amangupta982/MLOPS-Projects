import pickle
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
import json
import os
import argparse

def evaluate_model(test_data_path, model_path, output_dir):
    print(f"Loading test data from {test_data_path}...")
    with open(test_data_path, 'rb') as f:
        X_test, y_test = pickle.load(f)
        
    print(f"Loading model from {model_path}...")
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
        
    print("Evaluating model...")
    y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    metrics = {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1_score': f1
    }
    
    print("Metrics:")
    for k, v in metrics.items():
        print(f"  {k}: {v:.4f}")
        
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'scores.json')
    
    print(f"Saving metrics to {output_path}...")
    with open(output_path, 'w') as f:
        json.dump(metrics, f, indent=4)
        
    print("Model evaluation completed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test_data', type=str, default='data/processed/test_data.pkl', help='Path to test data')
    parser.add_argument('--model_path', type=str, default='models/sentiment_model.pkl', help='Path to trained model')
    parser.add_argument('--output_dir', type=str, default='metrics', help='Directory to save metrics')
    args = parser.parse_args()
    
    evaluate_model(args.test_data, args.model_path, args.output_dir)
