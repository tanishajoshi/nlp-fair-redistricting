def printcode_readcsv(filename):
    lines = ['import pandas as pd\n', f'df = pd.read_csv({filename})']
    with open('code.txt', 'a', encoding='utf-8') as file:
        for line in lines:
            file.write(line)
            file.write('\n')


def printcode_dropnull():
    lines = ['df = df.dropna()']
    with open('code.txt', 'a', encoding='utf-8') as file:
        for line in lines:
            file.write(line+'\n')

def printcode_kmeans():
    lines = ['from sentence_transformers import SentenceTransformer', 
    'from sklearn.cluster import KMeans']  
    with open('code.txt', 'r+', encoding='utf-8') as file:
        content = file.read()
        for line in lines:
            if line not in content:
                if 'import' in line:
                    file.seek(0)
                    file.write(line+'\n')
                    file.write(content+'\n')
                else:
                    file.write(line+'\n')

def printcode_fast():
    lines = ['from sentence_transformers import SentenceTransformer, util', 
    'import time']
    with open('code.txt', 'r+', encoding='utf-8') as file:
        content = file.read()
        for line in lines:
            if line not in content:
                if 'import' in line:
                    file.seek(0)
                    file.write(line+'\n')
                    file.write(content+'\n')
                else:
                    file.write(line+'\n')

def printcode_encode(column):
    lines = ['from sklearn.preprocessing import LabelEncoder',
             'le = LabelEncoder()',
             f"df[{column}] = le.fit_transform(df[{column}])"]

    with open('code.txt', 'r+', encoding='utf-8') as file:
        content = file.read()
        for line in lines:
            if line not in content:
                if 'import' in line:
                    file.seek(0)
                    file.write(line+'\n')
                    file.write(content+'\n')
                else:
                    file.write(line+'\n')


def printcode_getdummies(column):
    lines = [f'df = pd.get_dummies(df, columns=[{column}])']
    with open('code.txt', 'r+', encoding='utf-8') as file:
        content = file.read()
        for line in lines:
            if line not in content:
                file.write(line)
                file.write('\n')


def printcode_dropcolumn(columnName):
    lines = [f'df.drop("{columnName}", axis=1, inplace=True)']
    with open('code.txt', 'r+', encoding='utf-8') as file:
        content = file.read()
        for line in lines:
            if line not in content:
                file.write(line)
                file.write('\n')


def printcode_splitdata(independent, output, test_size):
    lines = ['from sklearn.model_selection import train_test_split',
             f'X = df[{independent}]', f"y = df['{output}']",
             f'X_train, X_test, y_train, y_test= train_test_split(X, y, test_size={test_size})']

    with open('code.txt', 'r+', encoding='utf-8') as file:
        content = file.read()
        for line in lines:
            if line not in content:
                if 'import' in line:
                    file.seek(0)
                    file.write(line+'\n')
                    file.write(content+'\n')
                else:
                    file.write(line+'\n')


def printcode_linearregression():
    lines = ['from sklearn.linear_model import LinearRegression',
             'regressor = LinearRegression()', 'regressor.fit(X_train, y_train)',
             'y_pred = regressor.predict(X_test)']

    with open('code.txt', 'r+', encoding='utf-8') as file:
        content = file.read()
        for line in lines:
            if line not in content:
                if 'import' in line:
                    file.seek(0)
                    file.write(line+'\n')
                    file.write(content+'\n')
                else:
                    file.write(line+'\n')


def printcode_logisticregression():
    lines = ['from sklearn.linear_model import LogisticRegression',
             'classifier = LogisticRegression()', 'classifier.fit(X_train, y_train)',
             'y_pred = classifier.predict(X_test)']

    with open('code.txt', 'r+', encoding='utf-8') as file:
        content = file.read()
        for line in lines:
            if line not in content:
                if 'import' in line:
                    file.seek(0)
                    file.write(line+'\n')
                    file.write(content+'\n')
                else:
                    file.write(line+'\n')


def printcode_naivebayes():
    lines = ['from sklearn.naive_bayes import GaussianNB',
             'classifier = GaussianNB()', 'classifier.fit(X_train, y_train)',
             'y_pred = classifier.predict(X_test)']

    with open('code.txt', 'r+', encoding='utf-8') as file:
        content = file.read()
        for line in lines:
            if line not in content:
                if 'import' in line:
                    file.seek(0)
                    file.write(line+'\n')
                    file.write(content+'\n')
                else:
                    file.write(line+'\n')

def printcode_svc():
    lines = ['from sklearn.svm import SVC',
             "classifier = SVC(kernel='linear', random_state=0)",
             'classifier.fit(X_train, y_train)', 'y_pred = classifier.predict(X_test)']

    with open('code.txt', 'r+', encoding='utf-8') as file:
        content = file.read()
        for line in lines:
            if line not in content:
                if 'import' in line:
                    file.seek(0)
                    file.write(line+'\n')
                    file.write(content+'\n')
                else:
                    file.write(line+'\n')
