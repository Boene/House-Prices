import os
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, GradientBoostingRegressor, VotingRegressor
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

import preprocessing, training, evaluate, helper

path = os.path.dirname(os.path.abspath(__file__))
os.chdir(path)

### Load Data ###

daten = pd.read_csv("../data/train.csv")

### Load training and test Data ###

X_train, X_test, y_train, y_test = helper.load_data()

### Set Preprocessor & Pipeline ###

preprocessor = preprocessing.create_preprocessor(helper.get_feature_by_type("num"), helper.get_feature_by_type("cat"), helper.get_feature_by_type("ord"))

pipe = preprocessing.create_pipeline(GradientBoostingRegressor(), preprocessor)         # Additional parameters for the Estimator can be entered here.

### Configure and run GridSearch ###

param_grid = {          # Choice of parameters has to be in line with the chosen Estimator 
    "modell__max_depth": [3, 10],
    "modell__n_estimators": [10, 50, 100],
    "modell__learning_rate": [0.05, 0.15, 0.25]    
}

grid_search = training.run_grid_search(X_train, y_train, pipe, param_grid, cv=5, scoring="r2")

### Run analysis of results ###

importance_df, grid_quality = evaluate.analyze_grid(grid_search, X_test, y_test)

evaluate.show_gridsearch_analysis(importance_df.head(20), grid_quality)

results = pd.DataFrame(grid_search.cv_results_)


### Save best Estimator (optional) ###

#optimal_model = grid_search.best_estimator_

#joblib.dump(optimal_model, "../models/best_estimator_RandF.pkl")

#joblib.dump(grid_search, "../models/grid_search_RandF.pkl")