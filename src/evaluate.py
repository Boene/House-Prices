import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error


### Analyze Pipeline ###

def analyze_grid(grid_search, test_features, test_target):

    transformed_feature_names = (                    # Features got changed by OneHot.
        grid_search                         
        .best_estimator_                             # This addresses the optimal estimator of our model. 
        .named_steps["preprocessor"]                 # This addresses the preprocessor, which delivers them to the pipeline.
        .get_feature_names_out()            
    )

    feature_importances = (
        grid_search
        .best_estimator_
        .named_steps["modell"]                       # The importances are part of the optimal RF that was fitted.
        .feature_importances_
    )

    importance_df = pd.DataFrame({                   # Combine new features names with their importances.
        "feature": transformed_feature_names,
        "importance": feature_importances
    })

    importance_df = importance_df.sort_values(       # Sort the importances by value, since we re most interested in their hierarchy.
        by="importance",
        ascending=False
    )

    test_quality = grid_search.score(test_features, test_target)

    return importance_df, test_quality

def show_gridsearch_analysis(importance_df, test_quality):      # Prints given test quality and barplots features and their importance. I recommend .head(n) for top n features, since you else cant read anything.  

    print(f"Quality of test data: {test_quality}")

    plt.figure(figsize=(10,6))
    
    sns.barplot(
        x=importance_df["importance"],
        y=importance_df["feature"]
    )

    plt.xlabel("Importance")
    plt.ylabel("Feature")
    plt.title("Feature Importances [RF]")
    plt.tight_layout()

    plt.show()
    return

def show_target_correlations(       # Shows the correlations of numeric Features and a target, which in our case would usually be "SalePrice"
    data: pd.DataFrame,
    features: list,
    target: str
    ):

    correlations = (
        data[features + [target]]       # Adds "SalePrice" as entry in list.
        .corr(numeric_only=True)[target]        
        .drop(target)                   # Removes "SalePrice" because a correlation of to itself is obv.
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(6,10))

    sns.heatmap(
        correlations.to_frame(),
        annot=True,
        cmap="coolwarm",
        center=0
    )

    plt.title(f"Correlation with {target}")
    plt.tight_layout()
    plt.show()

def show_category_price(        # Plots the mean SalePrice for every value of the given Feature. Helpful to see systematic behavior i.e. in Features labeled as categorical. 
    data,
    feature,
    target="SalePrice"
):
    (
        data
        .groupby(feature)[target]
        .mean()
        .sort_values()
        .plot.barh()
    )

    plt.show()
