from sklearn.preprocessing import OneHotEncoder, StandardScaler, OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.base import ClassifierMixin, RegressorMixin, BaseEstimator
from typing import Literal
from helper import get_maplist_for_ord

def create_preprocessor(numerical:list, categorical:list, ordinal: list, /, num_strategy="constant", num_fill_value=0, cat_strategy="constant", cat_fill_value="Missing", ord_strategy="constant", ord_fill_value="Missing", enc_handle_unknown: Literal["error","ignore"] = "ignore"):
    numerical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy=num_strategy, fill_value=num_fill_value)),
    ("scaler", StandardScaler())
    ])

    categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy=cat_strategy,fill_value=cat_fill_value)),
    ("encoder", OneHotEncoder(handle_unknown=enc_handle_unknown)) 
    ])
    
    ordinal_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy=ord_strategy, fill_value=ord_fill_value)),
    ("encoder", OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=-1, categories=get_maplist_for_ord()))
    ])

    prepro = ColumnTransformer([
    ("numerical", numerical_pipeline, numerical),
    ("categorical",categorical_pipeline, categorical),
    ("ordinal", ordinal_pipeline, ordinal)
    ])

    return prepro

### Join the Pipelines ###

def create_pipeline (modell, preprocessor):
    if not isinstance(modell, BaseEstimator):
        raise ValueError("modell must be an sklearn estimator")
    
    pipe = Pipeline([
        ("preprocessor", preprocessor),
        ("modell", modell)
    ])
    return pipe