import pytest
import pandas as pd
import numpy as np
from ml_predictor.model import MLPredictor, load_data

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'feature1': np.random.rand(100),
        'feature2': np.random.rand(100),
        'target': np.random.rand(100)
    })

def test_preprocess_data(sample_data):
    predictor = MLPredictor()
    X, y = predictor.preprocess_data(sample_data)
    assert isinstance(X, np.ndarray)
    assert isinstance(y, pd.Series)
    assert X.shape[0] == y.shape[0]

def test_train_and_predict(sample_data):
    predictor = MLPredictor()
    X, y = predictor.preprocess_data(sample_data)
    predictor.train(X, y)
    predictions = predictor.predict(X)
    assert len(predictions) == len(y)

def test_evaluate(sample_data):
    predictor = MLPredictor()
    X, y = predictor.preprocess_data(sample_data)
    predictor.train(X, y)
    mse, r2 = predictor.evaluate(X, y)
    assert isinstance(mse, float)
    assert isinstance(r2, float)
    assert 0 <= r2 <= 1

def test_save_and_load_model(sample_data, tmp_path):
    predictor = MLPredictor()
    X, y = predictor.preprocess_data(sample_data)
    predictor.train(X, y)
    
    model_file = tmp_path / "model.joblib"
    predictor.save_model(model_file)
    assert model_file.exists()
    
    new_predictor = MLPredictor()
    new_predictor.load_model(model_file)
    assert new_predictor.model is not None

def test_load_data(tmp_path):
    # Create a temporary CSV file
    df = pd.DataFrame({
        'feature1': np.random.rand(10),
        'feature2': np.random.rand(10),
        'target': np.random.rand(10)
    })
    csv_file = tmp_path / "test_data.csv"
    df.to_csv(csv_file, index=False)
    
    # Test load_data function
    loaded_data = load_data(csv_file)
    assert isinstance(loaded_data, pd.DataFrame)
    assert loaded_data.shape == (10, 3)
