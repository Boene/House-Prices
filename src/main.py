import os
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

import preprocessing, training, evaluate, helper

path = os.path.dirname(os.path.abspath(__file__))
os.chdir(path)

### Load Data ###

daten = pd.read_csv("../data/train.csv")

### Define Features, Target, numerical, categorical ###

all_features = helper.get_feature_by_type("all")

X = daten[all_features]

y = daten["SalePrice"]

numerical_cats = helper.get_feature_by_type("num")
categorical_cats = helper.get_feature_by_type("cat")
ordinal_cats = helper.get_feature_by_type("ord")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25, 
    random_state=42
)

### Set Preprocessor & Pipeline ###

preprocessor = preprocessing.create_preprocessor(numerical_cats, categorical_cats, ordinal_cats)

pipe = preprocessing.create_pipeline(RandomForestRegressor(), preprocessor)

### Configure and run GridSearch ###

param_grid = {
    "modell__max_depth": [5, 15],
    "modell__n_estimators": [30, 100]    
}

grid_search = training.run_grid_search(X_train, y_train, pipe, param_grid, cv=5, scoring="r2")

importance_df, grid_quality = evaluate.analyze_grid(grid_search, X_test, y_test)


evaluate.show_gridsearch_analysis(importance_df.head(10), grid_quality)
