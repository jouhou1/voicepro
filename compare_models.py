import os
import numpy as np
import pandas as pd
from pycaret.regression import *

mfcc_data = pd.read_csv('mfcc.csv')
#前準備
reg = setup(data=mfcc_data, target='target')
#機械学習
compare_models()