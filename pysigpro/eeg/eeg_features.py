import numpy as np
from numba import jit
import scipy
import statistics
from utils import *


__all__ = ['get_time_domain_features', 'get_entropy_features', 'get_frequency_domain_features']

def get_time_domain_features(x: list) -> dict:

    assert x is not None, "Invalid signal provided"

    x = np.asarray(x)
    mean = np.mean(x)
    stddev = np.std(x)
    kurtosis = scipy.stats.kurtosis(x)
    skewness = scipy.stats.skew(x)
    variance = np.var(x)
    mode = statistics.mode(x)
    median = statistics.median(x)
    minimum = min(x)
    maximum = max(x)
    coefficient_of_variation = np.std(x) / np.mean(x)
    sqr = x**2
    energy = sum(sqr)
    avg_power = np.mean(sqr)
    rms = np.sqrt(avg_power)
    hjorthActivity = variance
    hjorthMobility = np.sqrt(np.var(np.gradient(x)) / np.var(x))
    hjorthComplexity = hMob(np.gradient(x)) / hMob(x)
    line_length = sum([abs(x[i] - x[i-1]) for i in range(1, len(x))])
    non_linear_energy = sum([(x[i])**2 - x[i+1]*x[i-1] for i in range(1, len(x)-1)])

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
        'energy' : energy,
        'average_power' : avg_power,
        'rms' : rms,
        'hjorthActivity' : hjorthActivity,
        'hjorthMobility' : hjorthMobility,
        'hjorthComplexity' : hjorthComplexity,
        'line_length' : line_length,
        'non_linear_energy' : non_linear_energy,
    }

    return time_domain_features

def get_entropy_features(x: list, order = 3, delay = 1, metric = 'chebyshev') -> dict:

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
    
    ran_order = range(order)
    hashmult = np.power(order, ran_order)
    assert delay > 0, "delay must be greater than zero."
    sorted_idx = embed(x, order=order, delay=delay).argsort(kind='quicksort')
    hashval = (np.multiply(sorted_idx, hashmult)).sum(1)
    _, c = np.unique(hashval, return_counts=True)
    p = np.true_divide(c, c.sum())
    pe = -xlogx(p).sum()

    mat = embed(x, order=order, delay=delay)
    W = np.linalg.svd(mat, compute_uv=False)
    W /= sum(W)
    svd_e = -xlogx(W).sum()

    N = len(data)
    kMax = N // 4
    hfd = np.array((-np.log(np.arange(2,kMax+1)),np.ones(kMax-1))).transpose()

    nzc = np.diff(np.signbit(x), axis=axis).sum()

    entropy_features = {
        'shannon_entropy' : shannon_entropy,
        'approximate_entropy' : approximate_entropy,
        'sample_entropy' : sample_entropy,
        'permutation_entropy' : pe,
        'singular_value_decomposition' : svd_e,
        'higuchi_fractal_dimension' : hfd,
        'number_of_zero_crossings' : nzc
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