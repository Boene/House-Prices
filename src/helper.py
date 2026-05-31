data_info = {   # class_name : [(num/cat/ord), (mean, med, min, max, const, "unknown")]   
    "MSSubClass": {
        "type": "cat",
        "imputer": "unknown"
    },
    "MSZoning": {       # mehrere Optionen werden nicht genutzt
        "type": "cat",
        "imputer": "unknown"
    },
    "LotFrontage": {        # 2-3 Ausreißer
        "type": "num",
        "imputer": "mean"
    },
    "LotArea": {        # mehrere Ausreißer
        "type": "num",
        "imputer": "mean"
    },
    "Street": {
        "type": "cat",
        "imputer": "unknown"
    },
    "Alley": {
        "type": "cat",
        "imputer": "unknown"
    },
    "LotShape": {
        "type": "cat",
        "imputer": "unknown"
    }, 
    "LandContour": {
        "type": "cat",
        "imputer": "unknown"
    },
    "Utilities": {      # nur 2 von 4 Optionen existieren
        "type": "ord",
        "imputer": "const"
    },
    "LotConfig": {
        "type": "cat",
        "imputer": "unknown"
    },
    "LandSlope": {      # -1?
        "type": "ord",
        "imputer": "med"
    },
    "Neighborhood": {       # alle sehr gleichverteilt (bedeutungslos mit 25 Optionen??)
        "type": "cat",
        "imputer": "unknown"
    },
    "Condition1": {
        "type": "cat",
        "imputer": "unknown"
    },
    "Condition2": {        # RRNe nicht genutzt 
        "type": "cat",
        "imputer": "unknown"
    },
    "BldgType": {
        "type": "cat",
        "imputer": "unknown"
    },
    "HouseStyle": {       # 2 neue Kategorien? -> finished/unfinished
        "type": "ord",
        "imputer": "unknown"
    },
    "OverallQual": {        # Option "1" und "2" super selten
        "type": "ord",
        "imputer": "med"
    },
    "OverallCond": {        # med/const? + Kategorie nötig oder lin. ab. mit OverallQual?
        "type": "ord",
        "imputer": "med"
    },
    "YearBuilt": {       # jünger = tendenziell besser? Bestimmte Phasen eher schlecht?
        "type": "num",
        "imputer": "unknown"
    },
    "YearRemodAdd": {       # 1950 = unknown???
        "type": "num",
        "imputer": "unknown"
    },
    "RoofStyle": {      # fast nur "hip" und "gable" --> diverse-Kategorie? 
        "type": "cat",
        "imputer": "unknown"
    },
    "RoofMatl": {       # fast ausschließlich "CompShg" --> diverse-Kategorie?
        "type": "cat",
        "imputer": "unknown"
    },   
    "Exterior1st": {        # "Other" und "PreCast" nicht verwendet --- "CBlock", "ImStucc", "Stone", "AsphShn" und "BrkCoomm" jeweils 1-2 entrys
        "type": "cat",
        "imputer": "unknown"
    },    
    "Exterior2nd": {        # "WdShing" (data_description.txt) heißt "Wd Shng" --- "Precast" nicht genutzt --- mehrere Kategorien sehr selten genutzt
        "type": "cat",
        "imputer": "unknown"
    }, 
    "MasVnrType": {         # sehr viele NaN, anstatt "None"
        "type": "cat",
        "imputer": "unknown"
    },
    "MasVnrArea": {         # Sehr viele "0" und ein paar Ausreißer
        "type": "num",
        "imputer": "unknown"
    },
    "ExterQual": {          # "Po" nicht genutzt
        "type": "ord",
        "imputer": "const"
    },
    "ExterCond": {         # "Po" und "Ex" fast gar nicht genutzt
        "type": "ord",
        "imputer": "const"
    }, 
    "Foundation": {        # ord? --- "Stone" und "Wood" fast gar nicht und "Slab" wenig genutzt
        "type": "cat",
        "imputer": "const"
    },   
    "BsmtQual": {          # "Av" gar nicht genutzt --- No Basement ist NaN, nicht "NA"
        "type": "ord",
        "imputer": "const"
    }, 
    "BsmtCond": {          # "Ex" gar nicht genutzt --- No Basement ist NaN, nicht "NA"
        "type": "ord",
        "imputer": "const"
    },
    "BsmtExposure": {       # No Basement ist NaN, nicht "NA"
        "type": "ord",
        "imputer": "const"
    },
    "BsmtFinType1": {       # No Basement ist NaN, nicht "NA"
        "type": "ord",
        "imputer": "const"
    },
    "BsmtFinSF1": {         # Großteil "0" => imputer??? --- ein Ausreißer
        "type": "num",
        "imputer": "mean"
    },
    "BsmtFinType2": {         # No Basement ist NaN, nicht "NA"
        "type": "ord",
        "imputer": "const"
    },
    "BsmtFinSF2": {         # Großteil "0" => imputer??? --- ein leichter Ausreißer
        "type": "num",
        "imputer": "mean"    
    },
    "BsmtUnfSF": {          # Großteil "0" => imputer??
        "type": "num",
        "imputer": "mean"
    },
    "TotalBsmtSF": {        # no basement vermutlich = "0" ==> impute?? --- ein Ausreißer --- lin. ab. von unfinished + finished??
        "type": "num",
        "imputer": "mean"
    },
    "Heating": {            # ord?
        "type": "cat",
        "imputer": "unknown"
    },
    "HeatingQC": {
        "type": "ord",
        "imputer": "const"
    },
    "CentralAir": {         # Central Air besser als ohne ... ?
        "type": "ord",
        "imputer": "const"
    },
    "Electrical": {         # ord? knifflig
        "type": "cat",
        "imputer": "unknown"
    },
    "1stFlrSF": {          # ein Ausreißer
        "type": "num",
        "imputer": "mean"
    },
    "2ndFlrSF": {          # no 2nd floor = 0 ==> imputer??
        "type": "num",
        "imputer": "mean"
    }, 
    "LowQualFinSF": {       # Großteil 0 ==> imputer??
        "type": "num",
        "imputer": "mean"
    },  
    "GrLivArea": {         # 4 leichte Ausreißer
        "type": "num",
        "imputer": "mean"
    },
    "BsmtFullBath": {      # nur einer mit 3 --- no basement <=> 0 bathrooms?
        "type": "cat",
        "imputer": "const"
    },
    "BsmtHalfBath": {      # nur zwei mit 2 --- " "  " "
        "type": "cat",
        "imputer": "const"
    },
    "BedroomAbvGr": {
        "type": "ord",
        "imputer": "med"
    },
    "KitchenAbvGr": {       # 3 Ausreißer
        "type": "ord",
        "imputer": "med"
    },
    "KitchenQual": {        # "Po" kommt nicht vor
        "type": "ord",
        "imputer": "const"
    },
    "TotRmsAbvGrd": {        # 2 Ausreißer
        "type": "ord",
        "imputer": "const"
    },
    "Functional": {         # "Sal" kommt nicht vor
        "type": "ord",
        "imputer": "const"
    },
    "Fireplaces": {         # 5 kleine Aureißer
        "type": "ord",
        "imputer": "const"
    },
    "FireplaceQu": {        # no Fireplace = Nan
        "type": "ord",
        "imputer": "const"
    },
    "GarageType": {        # "NA" = Nan --- 3 Kategorien sehr selten
        "type": "cat",
        "imputer": "const"
    },  
    "GarageYrBlt": {        # const = Jahr in dem Haus gebaut wurde?
        "type": "num",
        "imputer": "unknown"
    },  
    "GarageFinish": {       # unknown = NaN
        "type": "ord",
        "imputer": "const"
    },
    "GarageCars": {         # med oder const?
        "type": "ord",
        "imputer": "med"
    },
    "GarageArea": {        # no garage = 0
        "type": "num",
        "imputer": "mean"
    },
    "GarageQual": {         # no garage = NaN
        "type": "ord",
        "imputer": "med"
    },
    "GarageCond": {         # no garage = NaN
        "type": "ord",
        "imputer": "med"
    },
    "PavedDrive": {
        "type": "ord",
        "imputer": "med"
    },
    "WoodDeckSF": {         # no wood deck = 0
        "type": "num",
        "imputer": "const"
    },
    "OpenPorchSF": {        # no porch = 0
        "type": "num",
        "imputer": "const"
    },
    "EnclosedPorch": {      # no porch = 0
        "type": "num",
        "imputer": "const"
    },
    "3SsnPorch": {          # no porch = 0
        "type": "num",
        "imputer": "const"
    }, 
    "ScreenPorch": {        # no porch = 0
        "type": "num",
        "imputer": "const"
    },  
    "PoolArea": {           # no pool = 0
        "type": "num",
        "imputer": "const"
    },
    "PoolQC": {             # no pool = NaN --- "TA" kommt nicht vor
        "type": "ord",
        "imputer": "const"
    },
    "Fence": {              # "NA" = NaN
        "type": "ord",
        "imputer": "unknown"
    },
    "MiscFeature": {        # fast alle NaN
        "type": "cat",
        "imputer": "unknown"
    },
    "MiscVal": {            # fast alle 0 
        "type": "num",
        "imputer": "unknown"
    },  
    "MoSold": {             # völlig bedeutungslos
        "type": "cat",
        "imputer": "unknown"
    },   
    "YrSold": {             # nur 2006-2010 --- auch völlig bedeutungslos
        "type": "cat",
        "imputer": "unknown"
    },   
    "SaleType": {           # "VWD" kommt nicht vor --- Großteil "WD" --- impute unknown?
        "type": "cat",
        "imputer": "const"
    },  
    "SaleCondition": {      # Großteil "Normal" --- impute unknown?
        "type": "cat",
        "imputer": "const"
    }
}

def sort_features():
    cat_num = []
    cat_cat = []
    cat_ord = []
    for key in data_info:
        if data_info[key]["type"] == "num":
            cat_num.append(key)
        elif data_info[key]["type"][0] == "cat":
            cat_cat.append(key)
        elif data_info[key]["type"][0] == "ord":
            cat_ord.append(key)
    return cat_num, cat_cat, cat_ord

def all_features():
    return list(data_info.keys())