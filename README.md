# PySigPro

## Description

A one-stop comprehensive Python package that serves as a feature extraction tool which extracts features from various domains. These features are frequently used in algorithms in EEG/ECG signal processing. Powerful feature extraction system is necessary as features provide useful and relative information that aids algorithms in their performance. The raw signals can be split in segments of time, known as a “window”, from which features can be extracted.

## EEG Features

### TIME DOMAIN FEATURES
- Mean
- Standard deviation
- Kurtosis
- Skewness
- Variance
- Mode
- Median
- Minimum
- Maximum
- Coefficient of variation
- Energy
- Average power
- RMS value
- Hjorth parameter : Activity
- Hjorth parameter : Mobility
- Hjorth parameter : Complexity
- Line length
- Non linear energy

### ENTROPY DOMAIN FEATURES
- Shannon entropy
- Approximate entropy
- Sample entropy
- Permutation entropy
- Singular value decomposition
- Higuchi fractal dimension
- Number of zero crossings

## ECG Features

### Time Domain Features
- MEAN_NNI 
- SDNN
- SDSD
- NNI_20
- PNNI_20
- NNI_50
- PNNI_50
- RMSSD
- MEDIAN_NNI
- CVSD
- CVNNI
- MEAN_HR
- MAX_HR
- MIN_HR
- STD_HR

### Geometrical Features
- TRIANGULAR_INDEX

### Entropy Features
- SAMPLE_ENTROPY

## Dependencies

- [pandas] (https://pandas.pydata.org/)
- [numpy] (https://numpy.org/)
- [numba] (http://numba.pydata.org/)
- [scipy] (https://www.scipy.org/)
- [scikit-learn] (https://scikit-learn.org/)

## Installation

pip install pysigpro

## Getting started



