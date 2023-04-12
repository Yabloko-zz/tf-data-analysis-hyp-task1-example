import pandas as pd
import numpy as np


chat_id = 38897891 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    
    import scipy.stats as st
    x = x_success / x_cnt
    y = y_success / y_cnt
    sd = np.sqrt((x * (1 - x) / x_cnt) + (y * (1 - y) / y_cnt))
    t = np.abs(y - x) / sd
    res = t > st.norm.ppf(1 - 0.09/2)
    return res
