import pytest
from unittest.mock import patch
from ml_predictor.cli import main
import pandas as pd

@pytest.fixture
def mock_data():
    return pd.DataFrame({'feature1': [1, 2, 3], 'feature2': [4, 5, 6], 'target': [7, 8, 9]})

def test_train_command(mock_data):
    with patch('sys.argv', ['ml_predictor', 'train', '--data', 'test_data.csv', '--model', 'test_model.joblib']):
        with patch('ml_predictor.model.MLPredictor.train') as mock_train:
            with patch('ml_predictor.model.MLPredictor.save_model') as mock_save:
                main(test_mode=True)
                mock_train.assert_called_once()
                mock_save.assert_called_once()
    print("Train command test passed successfully!")

def test_predict_command(mock_data):
    with patch('sys.argv', ['ml_predictor', 'predict', '--data', 'test_data.csv', '--model', 'test_model.joblib']):
        with patch('ml_predictor.model.MLPredictor.load_model') as mock_load:
            with patch('ml_predictor.model.MLPredictor.predict', return_value=[1, 2, 3]) as mock_predict:
                main(test_mode=True)
                mock_load.assert_called_once()
                mock_predict.assert_called_once()
    print("Predict command test passed successfully!")

def test_invalid_command():
    with pytest.raises(SystemExit):
        with patch('sys.argv', ['ml_predictor', 'invalid_command']):
            main(test_mode=True)
    print("Invalid command test passed successfully!")

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
