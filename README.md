<div align="center">
    <img src="images/PySigPro_logo.png" width="150" height="150"/>
</div>
<h1 align="center">PySigPro</h1>

<p align="center">
    ![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)

    [![GitHub license](https://img.shields.io/github/license/vishaln15/pysigpro)](https://github.com/vishaln15/pysigpro)

    [![Status](https://img.shields.io/badge/status-work%20in%20progress-blue)](https://github.com/vishaln15/pysigpro/graphs/commit-activity)

</p>

## Description

**PySigPro** is a *work in progress* one-stop comprehensive Python package that serves as a feature extraction tool which extracts features from various domains. These features are frequently used in algorithms for [ECG](https://github.com/vishaln15/pysigpro/tree/main/pysigpro/ecg)/[EEG](https://github.com/vishaln15/pysigpro/tree/main/pysigpro/eeg) signal processing. Powerful feature extraction system is necessary as features provide useful and relative information that aids algorithms in their performance. The raw signals can be split in segments of time, termed as a *window*, from which features can be extracted.

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
- [nolds](https://pypi.org/project/nolds/)

```
    $ pip install -r requirements.txt
```    

## Installation
```
    $ pip install git+https://github.com/vishaln15/pysigpro.git
```

You can also clone the repository:

```
    $ git clone https://github.com/vishaln15/pysigpro.git
    $ pip install -r requirements.txt
    $ python setup.py install
```

## Authors

[**Vishal Nagarajan**](https://github.com/vishaln15)

[**Ashwini Muralidharan**](https://github.com/Ashwiinii)