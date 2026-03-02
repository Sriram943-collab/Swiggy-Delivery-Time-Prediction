# Swiggy Delivery Time Prediction using Machine Learning

PROJECT OVERVIEW
This project predicts food delivery time using Machine Learning based on rider details, order information, traffic conditions and delivery distance.
The model estimates delivery time at the moment of order placement and improves ETA accuracy.
Target Variable : Time_taken (minutes)

---------------------------------------------------------------------

BUSINESS PROBLEM
Food delivery companies require accurate delivery time prediction.
Incorrect delivery time leads to customer dissatisfaction and order cancellations.
Delivery time depends on traffic conditions, distance and rider workload.
The goal is to predict delivery time accurately using historical data.

---------------------------------------------------------------------

PROBLEM TYPE
Supervised Machine Learning
Regression Problem
Continuous value prediction

---------------------------------------------------------------------

DATASET INFORMATION
Dataset contains more than 45,000 delivery records with 26 features.

Main Features:

Rider Information
- Age
- Ratings
- Vehicle Condition

Order Information
- Order Time
- Festival Indicator
- Multiple Deliveries

Delivery Conditions
- Weather
- Traffic

Location Factors
- Distance
- City Type

Target Variable
- Time_taken

---------------------------------------------------------------------

DATA CLEANING

Missing values handled carefully to improve data quality.

- Age filled using rider-wise mean values
- Ratings filled using rider-wise mean values
- Weather filled using most frequent value
- Traffic filled using most frequent value
- Festival filled using most frequent value
- Multiple deliveries filled using median values
- Pickup time filled using reasonable values
- Order hour filled using median values

Rows with missing distance and coordinates were removed.

After cleaning:
Dataset contains no missing values and is ready for modeling.

---------------------------------------------------------------------

FEATURE ENGINEERING

Irrelevant columns removed using domain knowledge.

Removed Columns:

- Rider_id
- Order_date
- Restaurant latitude
- Restaurant longitude
- Delivery latitude
- Delivery longitude

Reason:

ID columns do not help prediction.
Distance already represents location information.
Removing unnecessary columns improves model performance.

---------------------------------------------------------------------

ENCODING

Categorical variables converted into numerical values.

OneHotEncoding applied to nominal variables:

- Weather
- Type_of_order
- Type_of_vehicle
- Festival
- City_type
- City_name
- Order_day_of_week
- Order_time_of_day

Reason:
These variables have no natural order and must be converted into binary features.

OrdinalEncoding applied to Traffic:

Low = 0  
Medium = 1  
High = 2  
Jam = 3  

Reason:
Traffic has a natural order and ordinal encoding preserves ranking.

---------------------------------------------------------------------

FEATURE SCALING

StandardScaler applied to numeric features.

Scaled Features:

- Age
- Ratings
- Vehicle_condition
- Multiple_deliveries
- Order_day
- Order_month
- Pickup_time_minutes
- Order_time_hour
- Distance
- Traffic

Reason:

Scaling normalizes feature values.
Improves performance of linear models.
Ensures all features are in similar range.

---------------------------------------------------------------------

FEATURE SELECTION

Important features selected using statistical methods.

Techniques Used:

- Correlation Analysis
- SelectKBest (F Regression)

Reason:

Remove unnecessary features.
Improve model accuracy.
Reduce overfitting.
Simplify the model.

Final Selected Features:

- Age
- Ratings
- Vehicle_condition
- Multiple_deliveries
- Distance
- Traffic
- Festival_yes
- Order_time_hour
- Order_time_of_day_morning
- Weather_sunny
- City_type_urban

---------------------------------------------------------------------

TRAIN TEST SPLIT

Dataset divided into training and testing data.

Training Data : 80%
Testing Data : 20%

Random State : 23

Training data used for model learning.
Testing data used for model evaluation.

---------------------------------------------------------------------

MODELS USED

Multiple machine learning algorithms were trained and compared.

Models:

- Linear Regression
- Random Forest Regressor
- XGBoost Regressor

Training multiple models helped identify the best algorithm.

---------------------------------------------------------------------

MODEL PERFORMANCE

Linear Regression

Moderate performance.
Captures linear relationships.

Random Forest

Best performing model.
Handles non-linear relationships well.

R² Score ≈ 0.76

XGBoost

High performance boosting algorithm.

R² Score ≈ 0.72

Best Model:
Random Forest Regressor

---------------------------------------------------------------------

CROSS VALIDATION

5-Fold Cross Validation used to verify model stability.

Cross validation divides data into multiple parts and tests the model repeatedly.

Purpose:

- Verify model generalization
- Check model stability
- Reduce overfitting

Cross Validation Score ≈ 0.69

---------------------------------------------------------------------

HYPERPARAMETER TUNING

RandomizedSearchCV used to improve model performance.

Parameters Tuned:

- n_estimators
- max_depth
- min_samples_split
- min_samples_leaf
- max_features

Tuning improved model accuracy and stability.

---------------------------------------------------------------------

FINAL MODEL

Algorithm:
Random Forest Regressor

Performance:

Test R² Score ≈ 0.76
Cross Validation Score ≈ 0.69

Model performs well on unseen data.

---------------------------------------------------------------------

MODEL SAVING

Model saved using pickle.

Files:

swiggy_delivery_time_rf.pkl  
final_features.pkl

Saved model used for deployment.

---------------------------------------------------------------------

DEPLOYMENT

Model deployed using:

Streamlit
HuggingFace Spaces

User can enter delivery details and predict delivery time instantly.

---------------------------------------------------------------------

TECHNOLOGIES USED

Python  
Pandas  
NumPy  
Scikit-learn  
XGBoost  
Streamlit

---------------------------------------------------------------------

AUTHOR

Krishnasagarapu Sri Ram

---------------------------------------------------------------------
