from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
import os
import csv
import time
import sys

embedder = SentenceTransformer('all-MiniLM-L6-v2')
dataset_path = sys.path[0] + '/../submission_db.csv'
max_corpus_size = 2000

if not os.path.exists(dataset_path):
    print("Found data set")


# Corpus with example sentences
corpus = set()
with open(dataset_path, encoding='utf8') as fIn:
    reader = csv.DictReader(fIn, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    csv.field_size_limit(100000000)
    numrows = 0
    for row in reader:
        numrows+=1
        entry = row['area_text'] 
        area_name = row['area_name']
        #print(x)
        sents= entry.split('.')
        
        for elem in sents: #sentences
            #print(elem)
            cluster_elem = elem+" "+area_name
            corpus.add(cluster_elem)
            
        #corpus_sentences.add(row['question2'])
        #print(len(corpus_sentences))
        if len(corpus) >= max_corpus_size:
            break
print(numrows)
corpus = list(corpus)
corpus_embeddings = embedder.encode(corpus)

# Perform kmean clustering- num clusters specified beforehand
num_clusters = 5 
clustering_model = KMeans(n_clusters=num_clusters)
clustering_model.fit(corpus_embeddings)
cluster_assignment = clustering_model.labels_

clustered_sentences = [[] for i in range(num_clusters)]
for sentence_id, cluster_id in enumerate(cluster_assignment):
    clustered_sentences[cluster_id].append(corpus[sentence_id])

for i, cluster in enumerate(clustered_sentences):
    print("Cluster ", i+1)
    print(cluster)
    print("")