from sklearn.model_selection import train_test_split
import os
import pandas as pd

path = os.path.dirname(os.path.abspath(__file__))
os.chdir(path)

### Load Data ###

daten = pd.read_csv("../data/train.csv")

### Define new Categories ###

daten["HouseAge"] = daten["YrSold"] - daten["YearBuilt"]
daten["AgeRemod"] = daten["YrSold"] - daten["YearRemodAdd"]
daten["TotHouseSF"] = daten["GrLivArea"] + daten["TotalBsmtSF"] 
daten["TotFinishedSF"] = daten["TotHouseSF"] - daten["BsmtUnfSF"]

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
        "imputer": "const",
        "cats": ["ELO", "NoSeWa", "NoSewr", "AllPub" ]
    },
    "LotConfig": {
        "type": "cat",
        "imputer": "unknown"
    },
    "LandSlope": {      # -1?
        "type": "ord",
        "imputer": "med",
        "cats": ["Sev", "Mod", "Gtl"]
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
        "imputer": "unknown",
        "cats": ["1.5Unf", "SFoyer", "1.5Fin", "2.5Unf", "SLvl", "1Story", "2Story", "2.5Fin"]
    },
    "OverallQual": {        # Option "1" und "2" super selten
        "type": "ord",
        "imputer": "med",
        "cats": ["1", "2", "3", "4", "5", "6", "7", "8", "9" , "10"]
    },
    "OverallCond": {        # med/const? + Kategorie nötig oder lin. ab. mit OverallQual?
        "type": "ord",
        "imputer": "med",
        "cats": ["1", "2", "3", "4", "5", "6", "7", "8", "9" , "10"]
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
        "imputer": "const",
        "cats": ["Po", "Fa", "TA", "Gd", "Ex"]
    },
    "ExterCond": {         # "Po" und "Ex" fast gar nicht genutzt
        "type": "ord",
        "imputer": "const",
        "cats": ["Po", "Fa", "TA", "Gd", "Ex"]
    }, 
    "Foundation": {        # ord? --- "Stone" und "Wood" fast gar nicht und "Slab" wenig genutzt
        "type": "cat",
        "imputer": "const"
    },   
    "BsmtQual": {          # "Po" gar nicht genutzt --- NaN: (37) eigentlich "NA"
        "type": "ord",
        "imputer": "const",
        "cats": ["Missing", "Po", "Fa", "TA", "Gd", "Ex"]
    }, 
    "BsmtCond": {          # "Ex" gar nicht genutzt --- NaN: (37) eigentlich "NA"
        "type": "ord",
        "imputer": "const",
        "cats": ["Missing", "Po", "Fa", "TA", "Gd", "Ex"]
    },
    "BsmtExposure": {       # NaN: (38) eigentlich "NA"
        "type": "ord",
        "imputer": "const",
        "cats": ["Missing", "No", "Mn", "Av", "Gd"]
    },
    "BsmtFinType1": {       # NaN: (37) eigentlich "NA"
        "type": "ord",
        "imputer": "const",
        "cats": ["Missing", "Unf", "LwQ", "Rec", "BLQ", "ALQ", "GLQ"]
    },
    "BsmtFinSF1": {         # Großteil "0" => imputer??? --- ein Ausreißer
        "type": "num",
        "imputer": "mean"
    },
    "BsmtFinType2": {       # NaN: (38) eigentlich "NA"
        "type": "ord",
        "imputer": "const",
        "cats": ["Missing", "Unf", "LwQ", "Rec", "BLQ", "ALQ", "GLQ"]
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
    "Heating": {            
        "type": "cat",
        "imputer": "unknown"
    },
    "HeatingQC": {
        "type": "ord",
        "imputer": "const",
        "cats": ["Po", "Fa", "TA", "Gd", "Ex"]
    },
    "CentralAir": {         
        "type": "ord",
        "imputer": "const",
        "cats": ["N", "Y"]
    },
    "Electrical": {         # ord? --- 2 Kategorien < 4 entrys --- NaN: (1) 
        "type": "cat",
        "imputer": "unknown",
        "cats": ["FuseP", "Mix", "FuseF", "FuseA", "SBrkr"]
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
        "imputer": "mean",
        "enabled": "True"
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
        "type": "num",
        "imputer": "med"
    },
    "KitchenAbvGr": {       # 3 Ausreißer
        "type": "num",
        "imputer": "med"
    },
    "KitchenQual": {        # "Po" kommt nicht vor
        "type": "ord",
        "imputer": "const",
        "cats": ["Po", "Fa", "TA", "Gd", "Ex"]
    },
    "TotRmsAbvGrd": {        # 2 Ausreißer
        "type": "num",
        "imputer": "med"
    },
    "Functional": {         # "Sal" kommt nicht vor
        "type": "ord",
        "imputer": "const",
        "cats": ["Sal", "Sev", "Maj2", "Maj1", "Mod", "Min2", "Min1", "Typ"]
    },
    "Fireplaces": {         # 5 kleine Aureißer
        "type": "num",
        "imputer": "most_frequent"
    },
    "FireplaceQu": {        # NaN: (690) eigentlich "NA"
        "type": "ord",
        "imputer": "const",
        "cats": ["Missing", "Po", "Fa", "TA", "Gd", "Ex"]
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
        "imputer": "const",
        "cats": ["Missing", "Unf", "RFn", "Fin"]
    },
    "GarageCars": {        
        "type": "num",
        "imputer": "most_frequent"
    },
    "GarageArea": {        # no garage = 0
        "type": "num",
        "imputer": "mean"
    },
    "GarageQual": {         # "Ex" und "Po" < 5 entrys --- NaN: (81) eigentlich "NA"
        "type": "ord",
        "imputer": "const",
        "cats": ["Missing", "Po", "Fa", "TA", "Gd", "Ex"]
    },
    "GarageCond": {         # "Ex", "Po" und "Gd" < 10 entrys --- NaN: (81) eigentlich "NA"
        "type": "ord",
        "imputer": "med",
        "cats": ["Missing", "Po", "Fa", "TA", "Gd", "Ex"]
    },
    "PavedDrive": {
        "type": "ord",
        "imputer": "most_frequent",
        "cats": ["N", "P", "Y"]

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
        "imputer": "const",
        "cats": ["Missing", "Fa", "TA", "Gd", "Ex"]
    },
    "Fence": {              # wirklich ord oder eher cat? --- NaN: (1179) eigentlich "NA"
        "type": "ord",
        "imputer": "const",
        "cats": ["Missing", "MnWw", "GdWo", "MnPrv", "GdPrv"]
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
    },

    ####################################################################
    ########################## new categories ##########################
    ####################################################################

    "HouseAge": {       # YrSold - YearBuilt
        "type": "num",
        "imputer": "med",
        "enabled": "True"
    },
    "AgeRemod": {       # YrSold - YearRemodAdd
        "type": "num",
        "imputer": "med",
        "enabled": "True"
    },
    "TotHouseSF": {     # GrLivArea + TotalBsmtSF 
        "type": "num",
        "imputer": "mean",
        "enabled": "True"
    },
    "TotFinishedSF": {      # TotHouseSF - BsmtUnfSF
        "type": "num",
        "imputer": "mean",
        "enabled": "True"
    }
}

#############################
#############################

def get_feature_by_type(type:str, data_info:dict=data_info):        # Gathers all Features from given category (num/ord/cat) and returns them as a list
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


def get_maplist_for_feature(feature:str, data_info=data_info):      # Gets the maplist for one specific Feature
    leng = len(data_info[feature]["cats"])
    map = []
    for n in range(0,leng):
            map.append(data_info[feature]["cats"][n])
    return map

def get_maplist_for_ord():      # Forms the maplists from all single ordinal Features into the correct format for OrdinalEncoder()
    maplists_by_type = [
        get_maplist_for_feature(feature)
        for feature in get_feature_by_type("ord")
    ]
    return  maplists_by_type

def load_data(daten=daten):        ### Define Features, Target, numerical, categorical ###
    all_features = get_feature_by_type("all")

    X = daten[all_features]

    y = daten["SalePrice"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25, 
        random_state=42
    )
    return X_train, X_test, y_train, y_test 