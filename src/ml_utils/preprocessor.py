from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split


def normalize(data):
    """
    Normalize a list of numbers to a 0-1 range using MinMaxScaler.
    Example: [10, 20, 30] becomes [[0.0], [0.5], [1.0]]
    """
    scaler = MinMaxScaler()
    return scaler.fit_transform([[x] for x in data])


def split_data(X, y, test_size=0.2, random_state=42):
    """
    Split features (X) and labels (y) into training and testing sets.
    By default, 80% goes to training and 20% to testing.
    """
    return train_test_split(X, y, test_size=test_size, random_state=random_state)