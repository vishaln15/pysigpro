import numpy as np
import nolds

__all__ = ['get_time_domain_features', 'get_geometrical_features', 'get_sample_entropy']

def get_time_domain_features(nn_intervals: list, sampling_freq: float) -> dict:

    nn_intervals = np.asarray(nn_intervals)
    nni_diff = np.diff(nn_intervals)
    len_interval = len(nn_intervals)
    mean = np.mean(nn_intervals)
    median = np.median(nn_intervals)
    sdsd = np.std(nni_diff)
    rmssd = np.sqrt(np.mean(nni_diff))
    nni_50 = sum(np.abs(nni_diff) > 50 * sampling_freq)
    pnni_50 = 100 * nni_50 / len_interval
    nni_20 = sum(np.abs(nni_diff) > 20 * sampling_freq))
    pnni_20 = 100 * nni_20 / len_interval
    cvsd = np.divide(rmssd / mean)
    sdnn = np.std(nn_intervals, ddof = 1)
    cvnni = np.divide(sdnn / mean)
    hr_list = np.divide(60 * sampling_freq, nn_intervals)
    mean_hr = np.mean(hr_list)
    min_hr = min(hr_list)
    max_hr = max(hr_list)
    std_hr = np.std(hr_list)

    time_domain_features = {
        'mean_nni' : mean,
        'sdnn' : sdnn,
        'sdsd' : sdsd,
        'nni_20' : nni_20,
        'pnni_20' : pnni_20,
        'nni_50' : nni_50,
        'pnni_50' : pnni_50,
        'rmssd' : rmssd,
        'median_nni' : median,
        'cvsd' : cvsd, 
        'cvnni' : cvnni,
        'mean_hr' : mean_hr,
        'max_hr' : max_hr,
        'mean_hr' : mean_hr,
        'min_hr' : min_hr,
        'std_hr' : std_hr
    }

    return time_domain_features

def get_geometrical_features(nn_intervals: list) -> dict:

    nn_intervals = np.asarray(nn_intervals)
    triangular_index = len(nn_intervals) / max(np.histogram(nn_intervals, bins=range(300, 2000, 8))[0])
    
    geometrical_features = {
        'triangular_index': triangular_index,
    }

    return geometrical_features

def get_sample_entropy(nn_intervals: list) -> dict:
    
    sampen = nolds.sampen(nn_intervals, emb_dim = 2)
    sampen_features = {
        'sample_entropy' : sampen
    }
    return sampen_features