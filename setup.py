import setuptools
import re

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

version = re.search('^__version__\s*=\s*\'(.*)\'', open('pysigpro/__init__.py').read(), re.M).group(1)

setuptools.setup(
    name='pysigpro',
    version=version,
    author='Vishal Nagarajan',
    author_email='nagarajanvishal@gmail.com',
    description='ECG/EEG Signal Feature Extraction Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/vishaln15',
    project_urls = {
        "Bug Tracker": "https://github.com/vishaln15/pysigpro/issues"
    },
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=['numpy', 'numba', 'scipy', 'pandas', 'scikit-learn', 'nolds'],
)