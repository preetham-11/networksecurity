# Network Security - Phishing Detection System

## Overview

A comprehensive machine learning project that detects phishing URLs using network security features. The system implements a complete MLOps pipeline from MongoDB data ingestion to model deployment with experiment tracking and a FastAPI web interface.

## Features

- **End-to-End MLOps Pipeline**: Complete workflow from data ingestion to model deployment with MLflow tracking
- **Multiple Algorithm Comparison**: Tests 5 different classification algorithms with hyperparameter tuning
- **Real-time Predictions**: FastAPI web application for batch phishing detection
- **Automated Model Selection**: Automatically selects the best performing model based on classification metrics
- **Data Quality Assurance**: Schema validation and statistical drift detection using Kolmogorov-Smirnov test
- **MongoDB Integration**: Scalable data storage and retrieval with secure connection handling

## Project Structure

networksecurity/
├── final_model/                 # Stored models and preprocessors
│   ├── model.pkl               # Trained ML model
│   └── preprocessor.pkl        # Data preprocessing pipeline
├── Network_Data/
│   └── phisingData.csv         # Original phishing dataset
├── data_schema/
│   └── schema.yaml             # Data validation schema
├── networksecurity/
│   ├── components/             # Core ML pipeline components
│   │   ├── data_ingestion.py   # MongoDB data loading and splitting
│   │   ├── data_validation.py  # Schema validation and drift detection
│   │   ├── data_transformation.py # Data preprocessing with KNN imputation
│   │   └── model_trainer.py    # Model training and MLflow tracking
│   ├── pipeline/               # Pipeline orchestration
│   │   ├── training_pipeline.py # Complete training workflow
│   │   └── batch_prediction.py # Batch inference pipeline
│   ├── utils/                  # Utility modules
│   └── entity/                 # Configuration classes
├── templates/                  # HTML templates for web app
│   └── table.html             # Prediction results template
├── prediction_output/          # Prediction results storage
├── app.py                      # FastAPI web application
├── main.py                     # Training pipeline execution
└── requirements.txt            # Project dependencies

## Machine Learning Pipeline

### Data Ingestion

- Connects to MongoDB database using secure environment variables
- Splits data into training and testing sets
- Saves processed datasets to feature store for reproducibility

### Data Validation

- Validates data schema compliance against predefined YAML schema
- Performs statistical drift detection using Kolmogorov-Smirnov test
- Ensures data quality before proceeding to transformation

### Data Transformation

- Handles missing values using intelligent KNNImputer algorithm
- Converts target labels for binary classification
- Creates sklearn preprocessing pipeline for consistent transformations

### Model Training

The system evaluates multiple classification algorithms:

- **Random Forest Classifier**
- **Decision Tree Classifier** 
- **Gradient Boosting Classifier**
- **Logistic Regression**
- **AdaBoost Classifier**

Each model undergoes hyperparameter tuning using GridSearchCV with comprehensive parameter grids.

### Model Selection & Tracking

- Automatically selects the best performing model based on F1-score, precision, and recall
- Integrates with MLflow and DagHub for experiment tracking and versioning
- Saves the best model and preprocessing pipeline for production deployment

## Input Features

The system analyzes 30 phishing detection features including URL structure, security indicators, content analysis, and behavioral patterns to classify URLs as legitimate or phishing attempts.

## Output

- **Phishing Classification**: Binary prediction (0 = Legitimate, 1 = Phishing) with batch processing capabilities and CSV output results.

## Technologies Used

- **Python 3.10**
- **Scikit-learn**: Machine learning algorithms and preprocessing
- **MLflow & DagHub**: Experiment tracking and model versioning
- **FastAPI**: High-performance web application framework
- **MongoDB & PyMongo**: Scalable database storage and connectivity
- **Pandas & NumPy**: Data manipulation and numerical computations

## Model Performance

The system automatically selects the best performing model based on comprehensive classification metrics evaluation on test data, with full experiment tracking in MLflow ensuring reliable and reproducible phishing detection capabilities.
