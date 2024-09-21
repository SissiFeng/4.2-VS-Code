# Your own Python Package Development

## 📚 Introduction

This assignment is designed to guide you through the process of developing a complete Python package for machine learning prediction. You will create a package named `ml_predictor`, implement its core functionality, write tests, set up the package structure, and finally publish it to PyPI.

## 🎯 Objectives

By completing this assignment, you will:

1. Understand the structure of a Python package
2. Implement a basic machine learning predictor
3. Write and run unit tests
4. Create a command-line interface (CLI) for your package
5. Prepare your package for distribution
6. Publish your package to PyPI

## 🛠️ Project Structure

```
ml_predictor/
│
├── src/
│   └── ml_predictor/
│       ├── __init__.py
│       ├── model.py
│       └── cli.py
│
├── tests/
│   ├── test_model.py
│   └── test_cli.py
│
├── setup.py
├── README.md
├── LICENSE
└── MANIFEST.in
```

## 📝 Assignment Steps

### Step 1: Set Up the Project

1. Use PyScaffold to create the initial project structure:
   ```
   pip install pyscaffold
   putup ml_predictor
   cd ml_predictor
   ```

2. Familiarize yourself with the created directory structure.

### Step 2: Implement the Core Functionality

1. Open `src/ml_predictor/model.py`.
2. Implement the `MLPredictor` class with methods for data preprocessing, model training, prediction, and evaluation.
3. Implement the `load_data` function to read data from a CSV file.


### Step 3: Write Unit Tests

1. Open `tests/test_model.py`.
2. Write unit tests for each method in the `MLPredictor` class.
3. Run the tests using pytest:
   ```
   pytest tests/test_model.py
   ```

### Troubleshooting

If you encounter issues with model evaluation, particularly if you get negative R² scores, consider the following debugging steps:

1. Review the `evaluate` method in your `MLPredictor` class. Ensure you're calculating MSE and R² scores correctly.

2. Add print statements in the `evaluate` method to output predictions and actual values. This can help understand why R² might be negative.

3. Remember that a negative R² usually means the model performs worse than simply predicting the mean. This might indicate that your model isn't fitting the data correctly.

4. Double-check your data preprocessing steps. Make sure you're handling features and target variables correctly and applying appropriate scaling.

5. Consider using cross-validation for model evaluation instead of evaluating only on the training data. This can provide a more reliable performance estimate.

6. If the issue persists, try testing your model with a simpler dataset to see if you can get expected results.

Remember, debugging machine learning models is an iterative process. Keep trying different approaches until you resolve the issue. This process will help you better understand the importance of model evaluation and debugging in machine learning projects.


### Step 4: Implement the CLI

1. Open `src/ml_predictor/cli.py`.
2. Implement the command-line interface for training and prediction.
3. Test the CLI manually with sample data.

### Step 5: Write CLI Tests

1. Open `tests/test_cli.py`.
2. Write tests for the CLI functionality.
3. Run the CLI tests:
   ```
   pytest tests/test_cli.py
   ```

### Step 6: Prepare for Distribution

1. Update `setup.py` with your package information.
2. Create a `README.md` file with usage instructions.
3. Choose a license and create a `LICENSE` file.
4. Create a `MANIFEST.in` file if you have additional non-Python files to include.

### Step 7: Build and Publish

1. Build your package:
   ```
   python setup.py sdist bdist_wheel
   ```
2. Install twine:
   ```
   pip install twine
   ```
3. Upload your package to PyPI:
   ```
   twine upload dist/*
   ```

### Step 8: Verify Installation

1. Install your package from PyPI:
   ```
   pip install ml_predictor
   ```
2. Test the installed package to ensure it works correctly.

## 📊 Grading

Your assignment will be graded based on:

- Correct implementation of the `MLPredictor` class (30%)
- Passing unit tests for the model (20%)
- Correct implementation of the CLI (20%)
- Passing CLI tests (10%)
- Successful publication to PyPI (10%)
- Code quality and documentation (10%)

## 🆘 Getting Help

If you encounter any issues or have questions:
1. Review this README and the TODO comments in the code files.
2. Check the PyScaffold and PyPI documentation.
3. Reach out to your instructor or teaching assistant for clarification.

Good luck with your project! 🚀
