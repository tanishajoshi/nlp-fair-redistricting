import pandas as pd
from sklearn.preprocessing import LabelEncoder
import printcode

 
def dropnull(df):
    df = df.dropna()
    printcode.printcode_dropnull()
    return df


def encode(column, category, df):
    if category == 'same-index':
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        printcode.printcode_encode(column)
    else:
        df = pd.get_dummies(df, columns=[column])
        printcode.printcode_getdummies(column)
    return df


def replace(value, column, numValue, df):
    numValue = int(numValue)
    if column == 'All':
        if value == 'mean':
            df = df.fillna(df.mean())
        if value == 'median':
            df = df.fillna(df.median())
        if value == 'mode':
            df = df.fillna(df.mode())
        if value == 'other-value':
            df = df.fillna(numValue)

    else:
        if value == 'mean':
            mean = df[column].mean()
            df[column].fillna(value=mean, inplace=True)
        if value == 'median':
            median = df[column].median()
            df[column].fillna(value=median, inplace=True)
        if value == 'mode':
            mode = df[column].mean()
            df[column].fillna(value=mode, inplace=True)
        if value == 'other-value':
            df[column].fillna(value=numValue, inplace=True)

    return df


def dropcolumn(columnName, df):
    df.drop(columnName, axis=1, inplace=True)
    printcode.printcode_dropcolumn(columnName)
    return df
