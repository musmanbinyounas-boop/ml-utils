from ml_utils.preprocessor import normalize, split_data


def test_normalize_output_range():
    """Every normalized value should be between 0.0 and 1.0."""
    data = [10, 20, 30, 40, 50]
    result = normalize(data)
    for val in result:
        assert 0.0 <= val[0] <= 1.0, f"Value {val[0]} is out of range!"


def test_normalize_length():
    """Output should have the same number of items as input."""
    data = [5, 15, 25]
    result = normalize(data)
    assert len(result) == len(data)


def test_split_data_sizes():
    """With 100 items and test_size=0.2, expect 80 train and 20 test."""
    X = list(range(100))
    y = list(range(100))
    X_train, X_test, y_train, y_test = split_data(X, y)
    assert len(X_train) == 80
    assert len(X_test) == 20