import numpy as np
from numpy.ma import outerproduct
import pandas as pd

__all__ = ['remove_ecg_outliers']

def remove_ecg_outliers(rr_intervals: list, low_rri: float = 300, high_rri: float = 2000, verbose: bool = False) -> list:
    
    refined_rr_intervals = [rri if rri <= high_rri and rri >= low_rri else np.nan for rri in rr_intervals]

    if verbose:
        outliers = []
        for rri in rr_intervals:
            if rri >= high_rri or rri <= low_rri:
                outliers.append(rri)
            
        nan_count = sum(np.isnan(refined_rr_intervals))
        if nan_count == 0:
            print(f'{nan_count} outlier(s) have been deleted.')
        
        else:
            print(f'{nan_count} outlier(s) have been deleted.')
            print(f'The outlier(s) value(s) are : {outliers}')
    
    return refined_rr_intervals

def is_outlier(curr_rri: float, next_rri: float, method: str = 'malik'):
    
    outlier = abs(curr_rri - next) <= 0.2 * curr_rri
    return outlier

def remove_ectopic_beats(rr_intervals: list, verbose: bool = False, method: str = 'malik') -> list:

    outlier_count = 0
    previous_outlier = False
    nn_intervals = [rr_intervals[0]]
    for i, rr_interval in enumerate(rr_intervals[:-1]):

        if previous_outlier:
            nn_intervals.append(rr_intervals[i + 1])
            previous_outlier = False
            continue

        if is_outlier(rr_interval, rr_intervals[i + 1]):
            nn_intervals.append(rr_intervals[i + 1])
        else:
            nn_intervals.append(np.nan)
            outlier_count += 1
            previous_outlier = True

    if verbose:
        print(f'{outlier_count} ectopic beat(s) have been deleted with {method} rule.')

    return nn_intervals