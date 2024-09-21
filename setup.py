from setuptools import setup, find_packages

setup(
    name='ml_predictor',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'joblib'
    ],
    entry_points={
        'console_scripts': [
            'ml_predictor=ml_predictor.cli:main',
        ],
    },
    # TODO: Add project description
    # TODO: Add author and author_email
    # TODO: Add url to the project repository
)
