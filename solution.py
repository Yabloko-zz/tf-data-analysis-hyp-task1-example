import pandas as pd
import numpy as np


chat_id = 38897891 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    from scipy.stats import norm
    
    f = x_success / x_cnt
    s = y_success / y_cnt
    btw = np.sqrt((f * (1 - f) / x_cnt) + (s * (1-s) / y_cnt))
    res = (s - f) / btw > norm.ppf(1-0.09)
    return res
