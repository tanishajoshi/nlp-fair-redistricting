import pandas as pd
from machine_learning import preprocess

# sample
df = pd.read_csv('test/test_dataframes/Data.csv')
df1 = pd.read_csv('test/test_dataframes/Data1.csv')
df2 = pd.read_csv('test/test_dataframes/Data2.csv')
 

def test_dropnull():
    assert sum(preprocess.dropnull(df).isna().sum()) == 0
    assert sum(preprocess.dropnull(df1).isna().sum()) == 0

def testencode():
    dataframe = preprocess.encode('Age', 'same-index', df2)
    dataframe2 = preprocess.encode('Country', 'multi-index', df)

    assert len(list(dataframe.select_dtypes(
        include=['object']).columns)) == 1
    assert len(list(dataframe2.select_dtypes(
        include=['object']).columns)) == 1

def testdropcolumn():
    dataframe = preprocess.dropcolumn('Age', df)
    for col in dataframe.columns:
        assert col != 'Age'
