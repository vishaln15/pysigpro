import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

version = '0.0.3'

setuptools.setup(
    name='pysigpro',
    version=version,
    author='Vishal Nagarajan',
    author_email='nagarajanvishal@gmail.com',
    description='ECG/EEG Signal Feature Extraction Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/vishaln15/pysigpro',
    project_urls = {
        "Bug Tracker": "https://github.com/vishaln15/pysigpro/issues"
    },
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=['numpy', 'numba', 'scipy', 'pandas', 'scikit-learn', 'nolds'],
)