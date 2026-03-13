import pytest

@pytest.fixture
def sample_numbers():
    """Provide sample number data."""
    return list(range(10))

@pytest.fixture
def sample_user():
    """Provide sample user data."""
    return {
        "id": 1,
        "name": "Alice",
        "email": "alice@example.com"
    }

@pytest.fixture
def sample_dataset():
    """Provide dataset for generator tests."""
    return range(100)
