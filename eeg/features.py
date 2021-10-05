import numpy as np
from numba import jit
import scipy
import statistics
import utils


__all__ = ['get_time_domain_features', 'get_entropy_features']

def get_time_domain_features(x):

    mean = np.mean(x)
    stddev = np.stddev(x)
    kurtosis = scipy.stats.kurtosis(x)
    variance = np.var(x)
    mode = statistics.mode(x)
    median = statistics.median(x)
    minimum = min(x)
    maximum = max(x)
    coefficient_of_variation = np.stddev(x) / np.mean(x)
    rms = np.sqrt(np.mean(x**2))
    hjorthActivity = variance
    hjorthMobility = np.sqrt(np.var(np.gradient(x)) / np.var(x))
    hjorthComplexity = utils.hMob(np.gradient(x)) / utils.hMob(x)

    time_domain_features = {
        'mean' : mean,
        'stddev' : stddev,
        'kurtosis' : kurtosis,
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