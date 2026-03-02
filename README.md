# 📦 Swiggy Delivery Time Prediction

🔹 PROJECT OVERVIEW
## ➤ Machine Learning model to predict food delivery time (minutes)
## ➤ Helps improve ETA accuracy
## ➤ Reduces delivery delays
## ➤ Improves customer satisfaction
## ➤ Target Variable → Time_taken

------------------------------------------------------------

🔹 BUSINESS PROBLEM
➤ Swiggy needs accurate delivery time prediction
➤ Wrong ETA leads to cancellations and poor ratings
➤ Delivery time depends on traffic, distance, rider and order conditions
➤ Goal → Predict delivery time at order placement

------------------------------------------------------------

🔹 MACHINE LEARNING TYPE
➤ Supervised Learning
➤ Regression Problem
➤ Continuous Output Prediction

------------------------------------------------------------

🔹 DATASET INFORMATION
➤ 45,000+ records
➤ 26 features

Features include:

➤ Rider Details → Age, Ratings, Vehicle Condition
➤ Order Details → Order Time, Festival, Order Type
➤ Delivery Factors → Traffic, Weather
➤ Location Factors → Distance, City Type
➤ Target → Time_taken (minutes)

------------------------------------------------------------

🔹 DATA CLEANING

Missing values handled carefully:

➤ Age filled using rider-wise mean
➤ Ratings filled using rider-wise mean
➤ Weather filled using mode
➤ Traffic filled using mode
➤ Festival filled using mode
➤ Multiple deliveries filled using median
➤ Pickup time filled using reasonable values
➤ Order hour filled using median by time of day

Rows with missing coordinates removed:

➤ Restaurant latitude & longitude
➤ Delivery latitude & longitude
➤ Distance

After cleaning:

➤ No missing values remain
➤ Dataset ready for modeling

------------------------------------------------------------

🔹 FEATURE ENGINEERING

Irrelevant columns removed using domain knowledge:

➤ Rider_id removed (no prediction value)
➤ Order_date removed
➤ Latitude & Longitude removed

Reason:

➤ Distance already represents location information
➤ Prevents noise in model

------------------------------------------------------------

🔹 ENCODING

Categorical variables converted to numeric values.

Nominal Encoding (OneHotEncoder):

➤ Weather
➤ Type_of_order
➤ Type_of_vehicle
➤ Festival
➤ City_type
➤ City_name
➤ Order_day_of_week
➤ Order_time_of_day

Reason:

➤ These variables have no natural order
➤ OneHotEncoding prevents wrong relationships

Ordinal Encoding:

Traffic encoded as:

➤ Low = 0
➤ Medium = 1
➤ High = 2
➤ Jam = 3

Reason:

➤ Traffic has natural severity order
➤ Ordinal encoding preserves ranking

------------------------------------------------------------

🔹 FEATURE SCALING

StandardScaler applied to numeric variables:

➤ Age
➤ Ratings
➤ Vehicle_condition
➤ Multiple_deliveries
➤ Order_day
➤ Order_month
➤ Pickup_time_minutes
➤ Order_time_hour
➤ Distance
➤ Traffic

Reason:

➤ Normalize feature values
➤ Improves Linear Regression performance
➤ Makes features comparable

------------------------------------------------------------

🔹 FEATURE SELECTION

Techniques Used:

➤ Correlation Analysis
➤ SelectKBest (F-Regression)

Reason:

➤ Identify important variables
➤ Remove unnecessary features
➤ Improve model accuracy
➤ Reduce overfitting

Final Selected Features:

➤ Age
➤ Ratings
➤ Vehicle_condition
➤ Multiple_deliveries
➤ Distance
➤ Traffic
➤ Festival_yes
➤ Order_time_hour
➤ Order_time_of_day_morning
➤ Weather_sunny
➤ City_type_urban

------------------------------------------------------------

🔹 TRAIN TEST SPLIT

Dataset divided into:

➤ Training Data → 80%
➤ Testing Data → 20%

random_state = 23

Reason:

➤ Train model on training data
➤ Evaluate on unseen test data

------------------------------------------------------------

🔹 MODELS USED

Three models trained:

➤ Linear Regression
➤ Random Forest Regressor
➤ XGBoost Regressor

Reason:

➤ Compare multiple algorithms
➤ Select best performing model

------------------------------------------------------------

🔹 MODEL PERFORMANCE

Linear Regression:

➤ Captures linear relationships
➤ Moderate performance

Random Forest:

➤ Handles non-linear relationships
➤ Best performance

R² Score ≈ 0.76

XGBoost:

➤ Boosting based model
➤ High performance

R² Score ≈ 0.72

Best Model:

➤ Random Forest Regressor

------------------------------------------------------------

🔹 CROSS VALIDATION

Method Used:

➤ 5-Fold Cross Validation

Reason:

➤ Check model stability
➤ Verify model generalization
➤ Reduce overfitting risk

Result:

➤ Cross Validation Score ≈ 0.69

Model shows stable performance.

------------------------------------------------------------

🔹 HYPERPARAMETER TUNING

Method Used:

➤ RandomizedSearchCV

Parameters Tuned:

➤ n_estimators
➤ max_depth
➤ min_samples_split
➤ min_samples_leaf
➤ max_features

Reason:

➤ Improve model accuracy
➤ Optimize model parameters

------------------------------------------------------------

🔹 FINAL MODEL

Algorithm:

➤ Random Forest Regressor

Performance:

➤ Test R² Score ≈ 0.76
➤ Cross Validation Score ≈ 0.69

Model generalizes well on unseen data.

------------------------------------------------------------

🔹 MODEL SAVING

Model saved using pickle:

➤ swiggy_delivery_time_rf.pkl
➤ final_features.pkl

Reason:

➤ Reuse model for deployment

------------------------------------------------------------

🔹 DEPLOYMENT

Deployment Tools:

➤ Streamlit
➤ HuggingFace Spaces

User can:

➤ Enter order details
➤ Predict delivery time instantly

------------------------------------------------------------

🔹 TECHNOLOGIES USED

➤ Python
➤ Pandas
➤ NumPy
➤ Scikit-Learn
➤ XGBoost
➤ Streamlit

------------------------------------------------------------

🔹 PROJECT WORKFLOW

Business Understanding  
→ Data Cleaning  
→ Feature Engineering  
→ Encoding  
→ Scaling  
→ Feature Selection  
→ Model Training  
→ Cross Validation  
→ Hyperparameter Tuning  
→ Final Model  
→ Deployment

------------------------------------------------------------
