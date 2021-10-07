import numpy as np
import pandas as pd
from numba import jit
import scipy
import statistics
from utils import *


__all__ = ['get_time_domain_features', 'get_entropy_features', 'get_frequency_domain_features']

def get_time_domain_features(x: list) -> dict:

    assert x is not None, "Invalid signal provided"

    x = np.asarray(x)
    mean = np.mean(x)
    stddev = np.stddev(x)
    kurtosis = scipy.stats.kurtosis(x)
    skewness = scipy.stats.skew(x)
    variance = np.var(x)
    mode = statistics.mode(x)
    median = statistics.median(x)
    minimum = min(x)
    maximum = max(x)
    coefficient_of_variation = np.stddev(x) / np.mean(x)
    rms = np.sqrt(np.mean(x**2))
    hjorthActivity = variance
    hjorthMobility = np.sqrt(np.var(np.gradient(x)) / np.var(x))
    hjorthComplexity = hMob(np.gradient(x)) / hMob(x)

    time_domain_features = {
        'mean' : mean,
        'stddev' : stddev,
        'kurtosis' : kurtosis,
        'skewness' : skewness,
        'variance' : variance,
        'mode' : mode,
        'median' : median,
        'minimum' : minimum,
        'maximum' : maximum,
        'coefficient_of_variation' : coefficient_of_variation,
        'rms' : rms,
        'hjorthActivity' : hjorthActivity,
        'hjorthMobility' : hjorthMobility,
        'hjorthComplexity' : hjorthComplexity
    }

    return time_domain_features

def get_entropy_features(x: list, order = 3, metric = 'chebyshev') -> dict:

    assert x is not None, "Invalid signal provided"

    x = np.asarray(x)
    shannon_entropy = scipy.stats.entropy(pd.Series(x).value_counts())
    phi = app_samp_entropy(x, order=order, approximate=True)
    approximate_entropy = np.subtract(phi[0], phi[1])

    if metric == 'chebyshev' and x.size < 5000:
        sample_entropy = _numba_sampen(x, order=order, r=(0.2 * x.std(ddof=0)))
    else:
        phi = app_samp_entropy(x, order=order, metric=metric,
                                approximate=False)
        sample_entropy = -np.log(np.divide(phi[1], phi[0]))

    entropy_features = {
        'shannon_entropy' : shannon_entropy,
        'approximate_entropy' : approximate_entropy,
        'sample_entropy' : sample_entropy,
    }

    return entropy_features

def get_frequency_domain_features(x: list, band = None, fs = None) -> dict:

    assert x is not None, "Invalid signal provided"
    assert fs is not None, "Sampled Frequency must be provided."

    fs = float(fs)
    x = abs(np.fft.fft(x))
    power = np.empty(len(band) - 1)
    
    if band is None:
        band = [0.5, 4, 7, 12, 30]
    
    try:
        for index in range(0, len(band) - 1):
            curr_freq = float(band[index])
            next_freq = float(band[index + 1])
            power[index] = sum(
                x[int(np.floor(curr_freq / fs * len(x))): 
                    int(np.floor(next_freq / fs * len(x)))]
            )

    except ValueError:
        raise ValueError("Incorrect Sampling Frequency")

    power_ratio = power / sum(power)

    frequency_features = {
        'power' : power,
        'power_ratio': power_ratio
    }

    return frequency_features