from flask import request
from machine_learning import algorithms, metrics, preprocess


def select_preprocess_feature(selected_preprocess, df):
    if selected_preprocess == 'drop-null':
        df = preprocess.dropnull(df)

    elif selected_preprocess == 'drop-column':
        columnName = request.form['columnName']
        df = preprocess.dropcolumn(columnName, df)

    elif selected_preprocess == 'encode-columns':
        column = request.form['column']
        category = request.form['category']
        df = preprocess.encode(column, category, df)

    elif selected_preprocess == 'replace-values':
        replaceValueColumnName = request.form['replaceValueColumnName']
        replaceWithValue = request.form['replaceWithValue']
        numValue = 0
        if replaceWithValue == 'other-value':
            numValue = request.form['numValue']
        df = preprocess.replace(
            replaceWithValue, replaceValueColumnName, numValue, df)
    else:
        pass

    return df

def cluster(df, sim_thresh, cluster_size):
    simthr = float(sim_thresh)
    clus = int(cluster_size)
    if simthr == 0:
        clusters = algorithms.kmeans(df, clus)
    else:
        clusters = algorithms.fast_clustering(df, simthr)
    return clusters


def train(df, output, independent, selected_model, test_size):
    split = algorithms.split_data(df, test_size, output, independent)
    model = getattr(algorithms, selected_model)
    train = model(split)
    metric = metrics.rmseerror(train)
    return metric


def information(selected_info, df):
    if selected_info == 'describe':
        data = df.describe()
    return data
