import numpy as np
import pandas as pd 
import joblib
np.random.seed(3)


def prep(X):
    bol = ['hypertension', 'heart_disease']
    num = ['age', 'bmi', 'HbA1c_level', 'blood_glucose_level']
    cat = ['gender', 'smoking_history']
    X_bol = X[bol].values
    X_num = X[num].values
    X_cat = X[cat].values
    min_max = joblib.load('/home/kevo/Escritorio/mlds6/tdsp_template_grupo8/scripts/preprocessing/min_max_scaler.pkl')
    one_h = joblib.load('/home/kevo/Escritorio/mlds6/tdsp_template_grupo8/scripts/preprocessing/one_hencoder.pkl')
    X_num_minmax = min_max.transform(X_num)
    X_cat_onehot = one_h.transform(X_cat)
    X_fin = np.concatenate((X_num_minmax, X_bol ,X_cat_onehot),axis=1) 
    print(X_fin)
    return X_fin

