import pytest
import pandas as pd
from src.main import dumb


@pytest.fixture
def df():
    filename = './test/data_test/data.csv'
    df = pd.read_csv(filename)
    return df


def test_readcsv(df):
    assert df.shape[0] == 37


def test_function_from_main():
    assert dumb(3) == 6
