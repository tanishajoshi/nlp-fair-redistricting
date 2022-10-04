from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sentence_transformers import SentenceTransformer, util
from sklearn.cluster import KMeans
import time
import printcode

model = SentenceTransformer('all-MiniLM-L6-v2')
MAX_CORPUS_SIZE = 808

def fast_clustering(data, sim_thresh):
    numrows = 0
    thresh = float(sim_thresh)
    corpus = set()
    print("Start clustering")
    start_time = time.time()
    for i in range(len(data)):
        numrows+=1
        entry = data.loc[i, "area_text"]
        print('reached here')
        corpus.add(entry)
        if len(corpus) >= MAX_CORPUS_SIZE:
            break
    print("numrows", numrows)
    corpus = list(corpus)
    corpus_embeddings = model.encode(corpus, batch_size=64, show_progress_bar=True, convert_to_tensor=True)
    clusters = util.community_detection(corpus_embeddings, threshold=thresh, min_community_size=5)
    print("Clustering done after {:.2f} sec".format(time.time() - start_time))
    for i, cluster in enumerate(clusters):
        print("\nCluster {}, #{} Elements ".format(i+1, len(cluster)))
        for sentence_id in cluster[:]:
            print("\t", corpus[sentence_id])
    return clusters

def kmeans(data, cluster_size):
    corpus = set()
    num_clusters = int(cluster_size)
    numrows = 0
    for i in range(len(data)):
        numrows+=1
        entry = data.loc[i, "area_text"]
        corpus.add(entry)
        if len(corpus) >= MAX_CORPUS_SIZE:
            break
    corpus = list(corpus)
    corpus_embeddings = model.encode(corpus)
    clustering_model = KMeans(n_clusters=num_clusters)
    clustering_model.fit(corpus_embeddings)
    cluster_assignment = clustering_model.labels_
    clustered_entries = [[] for i in range(num_clusters)]
    for sentence_id, cluster_id in enumerate(cluster_assignment):
        clustered_entries[cluster_id].append(corpus[sentence_id])
        for i, cluster in enumerate(clustered_entries):
            print("Cluster ", i+1, " ", len(cluster), "Elements")
            print(cluster)
            print("")
    return clustered_entries

def split_data(data, test_size, output, independent):
    test_size = int(test_size)/100
    y = data[output]
    X = data.drop(output, axis=1)
    if independent != '':
        independent = ' '.join(independent.split())
        independent = list(independent.split(", "))
        X = data[independent]
        print(X)
        print(independent)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size)
    printcode.printcode_splitdata(independent, output, test_size)
    return(X_train, X_test, y_train, y_test)


def linear_regression(split):
    X_train, X_test, y_train, y_test = split
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_test)
    printcode.printcode_linearregression()
    return y_test, y_pred


def logistic_regression(split):
    X_train, X_test, y_train, y_test = split
    classifier = LogisticRegression()
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    printcode.printcode_logisticregression()
    return y_test, y_pred


def naive_bayes(split):
    X_train, X_test, y_train, y_test = split
    classifier = GaussianNB()
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    printcode.printcode_naivebayes()
    return y_test, y_pred


def svc(split):
    X_train, X_test, y_train, y_test = split
    classifier = SVC(kernel='linear', random_state=0)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    printcode.printcode_svc()
    return y_test, y_pred

