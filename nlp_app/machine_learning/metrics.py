from sklearn.metrics import mean_absolute_error


def rmseerror(train):
    y_test, y_pred = train
    error = mean_absolute_error(y_test, y_pred)
    return error
