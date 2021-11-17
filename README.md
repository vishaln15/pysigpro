# PySigPro

## Description

A one-stop comprehensive Python package that serves as a feature extraction tool which extracts features from various domains. These features are frequently used in algorithms in EEG/ECG signal processing. Powerful feature extraction system is necessary as features provide useful and relative information that aids algorithms in their performance. The raw signals can be split in segments of time, known as a *window*, from which features can be extracted.

## ECG FEATURES

### Time domain features
- MEAN_NNI, SDNN, SDSD, NNI_20, PNNI_20, NNI_50, PNNI_50, RMSSD, MEDIAN_NNI, CVSD, CVNNI, MEAN_HR, MAX_HR, MIN_HR, STD_HR

### Geometrical features
- TRIANGULAR_INDEX

### Entropy features
- SAMPLE_ENTROPY

## EEG FEATURES

### Time domain features
- Mean, Standard deviation, Kurtosis, Skewness, Variance, Mode, Median, Minimum, Maximum, Coefficient of variation, Energy, Average power, RMS value, Line length, Non linear energy, Hjorth parameters : Activity, Mobility, Complexity 

### Entropy domain features
- Shannon entropy, Approximate entropy, Sample entropy, Permutation entropy, Singular value decomposition, Higuchi fractal dimension, Number of zero crossings

## Requirements

- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [numba](http://numba.pydata.org/)
- [scipy](https://www.scipy.org/)
- [scikit-learn](https://scikit-learn.org/)

```
    pip install -r requirements.txt
```    

## Installation
```
    pip install git+https://github.com/vishaln15/pysigpro.git
```

You can also clone the repository:

```
    $ pip install -r requirements.txt
    $ git clone https://github.com/vishaln15/pysigpro.git
    $ python setup.py install
```

## Getting started

## Authors

[**Vishal Nagarajan**](https://github.com/vishaln15)

[**Ashwini Muralidharan**](https://github.com/Ashwiinii)