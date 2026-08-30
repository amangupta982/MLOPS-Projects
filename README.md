# Tweet Sentiment Analysis (MLOps)

An end-to-end Machine Learning Operations (MLOps) project for performing sentiment analysis on Twitter data. This repository demonstrates professional ML engineering practices including pipeline orchestration, data versioning, model tracking, and reproducible experimentation.

## 🚀 Key Features

*   **Automated ML Pipelines**: Uses Data Version Control (DVC) to manage end-to-end reproducible pipelines.
*   **Data Versioning**: Large datasets and models are tracked efficiently using DVC.
*   **Experiment Tracking**: Integrates with MLflow for logging metrics, parameters, and models (see the `mlflow` directory).
*   **Modular Architecture**: Clean separation of concerns across ingestion, preprocessing, feature engineering, model training, and evaluation.

## 📁 Project Structure

```text
.
├── .dvc/                   # DVC configuration and cache
├── data/
│   ├── raw/                # Original, immutable dataset
│   ├── interim/            # Intermediate data that has been transformed
│   └── processed/          # Final feature sets for modeling
├── metrics/
│   └── scores.json         # Evaluation metrics tracked by DVC
├── mlflow/                 # MLflow tracking scripts and configuration
├── models/                 # Serialized models and vectorizers
├── src/                    # Source code for the ML pipeline
│   ├── data_ingestion.py
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── model_building.py
│   └── model_evaluation.py
├── dvc.yaml                # DVC pipeline definition
└── requirements.txt        # Python dependencies
```

## ⚙️ Getting Started

### Prerequisites
*   Python 3.x
*   Git & DVC

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/amangupta982/MLOPS-Projects.git
   cd MLOPS-Projects
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Pipeline
This project relies on DVC to orchestrate the pipeline stages defined in `dvc.yaml`.

To execute the entire pipeline (Data Ingestion ➔ Preprocessing ➔ Feature Engineering ➔ Training ➔ Evaluation):
```bash
dvc repro
```

To view the generated metrics:
```bash
dvc metrics show
```

### MLflow Tracking
You can explore the tracked experiments locally by starting the MLflow UI:
```bash
mlflow ui
```
Navigate to `http://localhost:5000` in your browser.

## 📝 Pipeline Stages
1. **`data_ingestion`**: Fetches the raw Twitter data and stores it in `data/raw`.
2. **`data_preprocessing`**: Cleans the text (removes noise, handles stop words) and outputs to `data/interim`.
3. **`feature_engineering`**: Converts the cleaned text into numerical features using TF-IDF and outputs to `data/processed`.
4. **`model_building`**: Trains the sentiment analysis model.
5. **`model_evaluation`**: Evaluates the trained model on test data and logs metrics.
