import numpy as np
import pandas as pd
from pycaret.regression import *

mfcc_data = pd.read_csv('mfcc_test.csv')
#前準備
reg = setup(data=mfcc_data, target='target')
#機械学習
qda = create_model('qda', verbose=False)
tuned_qda = tune_model(qda, optimize='AUC')
predict_model(tuned_qda)