from sentence_transformers import SentenceTransformer, util
import os
import csv
import time
#Compute Fast Clusters By Entry in "area_text" column in COI csv
#punc = '''!()-[]{};:'",<>./?@#$%^&*_~'''

# Model for computing sentence embeddings. We use one trained for similar questions detection
model = SentenceTransformer('all-MiniLM-L6-v2')

# We download data from https://raw.githubusercontent.com/mggg/coi-products/main/Missouri/submission_db.csv
# and find similar entries in it

dataset_path = "submission_db.csv"
max_corpus_size = 808 # Num entries = 808


# Check if the dataset exists. If not, download and extract
# Download dataset if needed
if not os.path.exists(dataset_path):
    print("Found data set")

# Get all unique sentences from the file
corpus_sentences = set()
with open(dataset_path, encoding='utf8') as fIn:
    reader = csv.DictReader(fIn, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    csv.field_size_limit(100000000)
    numrows = 0
    for row in reader:
        numrows+=1
        entry = row['area_text']
        location = row['area_name']
        corpus_sentences.add(entry)
        if len(corpus_sentences) >= max_corpus_size:
            break

print("numrows= ", numrows)
corpus_sentences = list(corpus_sentences)
print("num entries = ", len(corpus_sentences))
print("Encode the corpus. This might take a while")
corpus_embeddings = model.encode(corpus_sentences, batch_size=64, show_progress_bar=True, convert_to_tensor=True)


print("Start clustering")
start_time = time.time()
init_max_size = 100
#Two parameters to tune:
#min_cluster_size: Only consider cluster that have at least 25 elements
#threshold: Consider sentence pairs with a cosine-similarity larger than threshold as similar
clusters = util.community_detection(corpus_embeddings, threshold=0.7, min_community_size=5, init_max_size=100)

print("Clustering done after {:.2f} sec".format(time.time() - start_time))

#Print cluster elements

for i, cluster in enumerate(clusters):
    print("\nCluster {}, #{} Elements ".format(i+1, len(cluster)))
    for sentence_id in cluster[:]:
        print("\t", corpus_sentences[sentence_id])
