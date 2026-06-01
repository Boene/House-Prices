data_info = {   
    "MSSubClass": {
        "type": "cat",
        "imputer": "unknown"
    },
    "MSZoning": {       # mehrere Optionen werden nicht genutzt
        "type": "cat",
        "imputer": "unknown"
    },
    "LotFrontage": {        # 2-3 Ausreißer --- NaN: (259) vermutlich keine Straße
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
    "Alley": {              # NaN: (1369) NA
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
        "imputer": "med"
    },
    "YearRemodAdd": {       # 1950 = unknown???
        "type": "num",
        "imputer": "med"
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
    "MasVnrType": {         # CBlock kommt nicht vor --- NaN: (872) None
        "type": "cat",
        "imputer": "unknown"
    },
    "MasVnrArea": {         # ein paar Ausreißer --- NaN: (8) trotz 861 "0" 
        "type": "num",
        "imputer": "med"
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
    "BsmtQual": {          # "Po" gar nicht genutzt --- NaN: (37) eigentlich "NA"
        "type": "ord",
        "imputer": "const"
    }, 
    "BsmtCond": {          # "Ex" gar nicht genutzt --- NaN: (37) eigentlich "NA"
        "type": "ord",
        "imputer": "const"
    },
    "BsmtExposure": {       # NaN: (38) eigentlich "NA"
        "type": "ord",
        "imputer": "const"
    },
    "BsmtFinType1": {       # NaN: (37) eigentlich "NA"
        "type": "ord",
        "imputer": "const"
    },
    "BsmtFinSF1": {         # Großteil "0" => imputer??? --- ein Ausreißer
        "type": "num",
        "imputer": "mean"
    },
    "BsmtFinType2": {       # NaN: (38) eigentlich "NA"
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
    "Electrical": {         # ord? --- 2 Kategorien < 4 entrys --- NaN: (1) 
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
    "FireplaceQu": {        # NaN: (690) eigentlich "NA"
        "type": "ord",
        "imputer": "const"
    },
    "GarageType": {        # NaN: (81) eigentlich "NA"
        "type": "cat",
        "imputer": "const"
    },  
    "GarageYrBlt": {        # NaN: (81) 
        "type": "num",
        "imputer": "med",
        "enabled": "False"
    },  
    "GarageFinish": {       # NaN: (81)
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
    "GarageQual": {         # "Ex" und "Po" < 5 entrys --- NaN: (81) eigentlich "NA"
        "type": "ord",
        "imputer": "med"
    },
    "GarageCond": {         # "Ex", "Po" und "Gd" < 10 entrys --- NaN: (81) eigentlich "NA"
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
    "PoolQC": {             # "TA" kommt nicht vor --- NaN: (1453) eigentlich "NA"
        "type": "ord",
        "imputer": "const"
    },
    "Fence": {              # NaN: (1179) eigentlich "NA"
        "type": "ord",
        "imputer": "unknown"
    },
    "MiscFeature": {        # "Elev" kommt nicht vor --- NaN: (1406) eigentlich "NA"
        "type": "cat",
        "imputer": "unknown"
    },
    "MiscVal": {            # fast alle 0 
        "type": "num",
        "imputer": "med"
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

def get_feature_by_type(type:str, data_info:dict=data_info):
    cat_list = []
    if type == "all":
        for key in data_info:
            if data_info.get("enabled", True):
                cat_list.append(key)
    else: 
        for key in data_info:
            if (data_info[key]["type"] == type) and (data_info.get("enabled", True)):
                cat_list.append(key)
    return cat_list

def get_imputer_strat(feature:str, data_info:dict=data_info):
    return data_info[feature]["imputer"]

# "type": "num"[\r\n\s,]*"imputer": "unknown"