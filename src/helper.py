data_info = {   # class_name : [(num/cat/ord), (mean, med, min, max, const, "unknown")]   
    "MSSubClass": ["cat", "unknown"],
    "MSZoning": ["cat", "unknown"],
    "LotFrontage": ["num", ""],   # ???
    "LotArea": ["num", ""],   # ???
    "Street": ["cat", "unknown"],
    "Alley": ["cat", "unknown"],
    "LotShape": ["cat", "unknown"],   # ???
    "LandContour": ["cat", "unknown"],   # ???
    "Utilities": ["ord", "med"],   # ???
    "LotConfig": ["cat", "unknown"],
    "LandSlope": ["ord", "med"],   # ???
    "Neighborhood": ["cat", "unknown"],
    "Condition1": ["cat", "unknown"],
    "Condition2": ["cat", "unknown"],
    "BldgType": ["cat", "unknown"],   # ???
    "HouseStyle": ["ord", "unknown"],   # 2 neue Kategorien? -> finished/unfinished
    "OverallQual": ["ord", "med"],   # mean/unknown?
    "OverallCond": ["ord", "med"],   # mean/unknown? + Kategorie nötig oder lin. ab. mit OverallQual?
    "YearBuilt": ["num", "unknown"],   # jünger = tendenziell besser? Bestimmte Phasen eher schlecht?
    "YearRemodAdd": ["num", "unknown"],
    "RoofStyle": ["cat", "unknown"],   # teils ord?
    "RoofMatl": ["cat", "unknown"],   # teils ord?
    "Exterior1st": ["cat", "unknown"],   # teils ord?
    "Exterior2nd": ["cat", "unknown"],   # "" ""
    "MasVnrType": ["cat", "unknown"],   # ord?
    "MasVnrArea": ["num", "unknown"],
    "ExterQual": ["ord", "unknown"],
    "ExterCond": ["ord", "unknown"],
    "Foundation": ["cat", "unknown"],   # ord?
    "BsmtQual": ["ord", "unknown"],   # vorsicht, Bezeichnung mies gewählt
    "BsmtCond": ["ord", "unknown"],
    "BsmtExposure": ["ord", "unknown"],   # ord korrekt?
    "BsmtFinType1": ["ord", "unknown"],
    "BsmtFinSF1": ["num", "unknown"],
    "BsmtFinType2": ["ord", "unknown"],
    "BsmtFinSF2": ["num", "unknown"],
    "BsmtUnfSF": ["num", "unknown"],
    "TotalBsmtSF": ["num", "unknown"],   # Basement m² lin. ab.?
    "Heating": ["cat", "unknown"],   # ord?
    "HeatingQC": ["ord", "unknown"],
    "CentralAir": ["cat", "unknown"],
    "Electrical": ["ord", "unknown"],   # alle ord?
    "1stFlrSF": ["num", "unknown"],
    "2ndFlrSF": ["num", "unknown"], 
    "LowQualFinSF": ["num", "unknown"],   # Bedeutung?
    "GrLivArea": ["num", "unknown"],   # Bedeutung
    "BsmtFullBath": ["num", "unknown"],
    "BsmtHalfBath": ["num", "unknown"],
    "BedroomAbvGr": ["num", "unknown"],
    "KitchenAbvGr": ["num", "unknown"],
    "KitchenQual": ["ord", "unknown"],
    "TotRmsAbvGrd": ["num", "unknown"],
    "Functional": ["ord", "unknown"],   # const = Typ?
    "Fireplaces": ["num", "unknown"],
    "FireplaceQu": ["ord", "unknown"],
    "GarageType": ["cat", "unknown"],   # teils ord?
    "GarageYrBlt": ["num", "unknown"],   # const = Jahr in dem Haus gebaut wurde?
    "GarageFinish": ["ord", "unknown"],
    "GarageCars": ["num", "unknown"],   # const/med denkbar
    "GarageArea": ["num", "unknown"],
    "GarageQual": ["ord", "unknown"],
    "GarageCond": ["ord", "unknown"],
    "PavedDrive": ["ord", "unknown"],
    "WoodDeckSF": ["num", "unknown"],
    "OpenPorchSF": ["num", "unknown"],
    "EnclosedPorch": ["num", "unknown"],
    "3SsnPorch": ["num", "unknown"],   # WTF? Vielleicht const = 0?
    "ScreenPorch": ["num", "unknown"],   # same
    "PoolArea": ["num", "unknown"],
    "PoolQC": ["ord", "unknown"],
    "Fence": ["ord", "unknown"],
    "MiscFeature": ["cat", "unknown"],   # const = NA?
    "MiscVal": ["num", "unknown"],   # same
    "MoSold": ["cat", "unknown"],   # völlig unbedeutsam
    "YrSold": ["num", "unknown"],   # vielleicht bedeutsam??
    "SaleType": ["cat", "unknown"],   # ord?
    "SaleCondition": ["cat", "unknown"]
}

def sort_features():
    cat_num = []
    cat_cat = []
    cat_ord = []
    for key in data_info:
        if data_info[key][0] == "num":
            cat_num.append(key)
        elif data_info[key][0] == "cat":
            cat_cat.append(key)
        elif data_info[key][0] == "ord":
            cat_ord.append(key)
    return cat_num, cat_cat, cat_ord

def all_features():
    features = []
    for key in data_info:
        features.append(key)
    return features