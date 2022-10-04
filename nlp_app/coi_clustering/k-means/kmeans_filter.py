import csv 
import sys
import pandas as pd
import os

dataset_path = sys.path[0] + '/../submission_db.csv'
max_corpus_size = 4000

if not os.path.exists(dataset_path):
    print("Found data set")


df = pd.read_csv(dataset_path)
newdp = df.iloc[:, 5]

newdp.to_csv('filter.csv')

"""
corpus_sentences = set()
with open('filter.csv', encoding='utf8') as fIn:
    reader = csv.DictReader(fIn, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    csv.field_size_limit(100000000)
    numrows = 0
    for row in reader:
        numrows+=1
        entry = row['area_text']
        corpus_sentences.add(entry)
        if len(corpus_sentences) >= max_corpus_size:
            break
print(numrows)
corpus = list(corpus)
corpus_embeddings = embedder.encode(corpus)

# Perform kmean clustering- num clusters specified beforehand
num_clusters = 10
clustering_model = KMeans(n_clusters=num_clusters)
clustering_model.fit(corpus_embeddings)
cluster_assignment = clustering_model.labels_

clustered_sentences = [[] for i in range(num_clusters)]
for sentence_id, cluster_id in enumerate(cluster_assignment):
    clustered_sentences[cluster_id].append(corpus[sentence_id])

for i, cluster in enumerate(clustered_sentences):
    print("Cluster ", i+1, " ", len(cluster), "Elements")
    print(cluster)
    print("")
"""

