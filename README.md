# Data Science Midterm Project

## Project
This project aims to predict house sale prices using advanced machine learning techniques. We collected and cleaned extensive real estate data, conducted comprehensive exploratory data analysis (EDA), created valuable new features, and tested several machine learning models to improve predictive accuracy.

## Goals
Data Cleaning & Processing: Handle missing values, remove outliers, and standardize features.
Feature Engineering: Create new features to enhance model predictions.
Model Selection: Train multiple machine learning models and select the best one.
Evaluation: Compare model performance using key regression metrics.


## Process
### Data Loading & Cleaning
- Loaded JSON files.

- Flatten and merge into a single DataFrame.
  
- Dropped irrelevant, highly correlated, or redundant features.

- Clean missing values and drop columns with all-null values.

### Feature Engineering
- One-hot encoding of the most frequent tags (binary columns).

- Extract geographic features (latitude, longitude, county).

### Exploratory Data Analysis (EDA)
- Statistical summaries and visualizations (boxplots, histograms, pairplots).

- Correlation heatmaps to detect multicollinearity.

- Outlier detection and optional removal.

### Scaling & Preprocessing
- Standardization of numeric features (mean=0, std=1).

- Processed datasets saved to data/processed/:
  - property_listings_scaled.csv


## EDA 

### Scatterplot - Correlation Between Features

![image](https://github.com/user-attachments/assets/6245f32c-2ee1-43ec-8a57-069295404d40)

### Boxplot - Outliers and Distribution Trends

![image](https://github.com/user-attachments/assets/20cce184-c08d-4e37-a1d9-a3c6eeb3aa63)



## Results
After testing multiple machine learning models, we identified XGBoost as the most performant model, based on evaluation metrics such as RMSE, MAE, and R². To prepare the model for deployment or future predictions, we created a pipeline that combines preprocessing and the tuned XGBoost regressor into a single, reusable object.

Results indicated that the model explains approximately 96% of the variance in the target variable, with an average absolute error of around $20,250, which is quite good for real estate price predictions.



## Challenges 
 - Handling Missing Values: Some data columns had a lot of missing values, so we filled them in or removed them.

- Too Many Features: We removed features that weren’t useful to make the model simpler and faster.

- Outliers: We removed extreme price values that could confuse the model.

## Future Goals
Explore blending or stacking models (e.g., combining XGBoost with Random Forest or Ridge regression) for potentially better performance.
Build a simple web interface where users can input property details and get a price prediction.
Package the pipeline into an API using Flask or FastAPI for integration with other systems.



👥 Contributors

Ikenna Harold Odikamnoro - Data sourcing, initial setup, and modeling.

Ipek Korfez - Data cleaning, EDA, visualization, and preprocessing.
