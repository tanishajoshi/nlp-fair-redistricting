from sentence_transformers import SentenceTransformer, util
import os
import csv
import time

#punc = '''!()-[]{};:'",<>./?@#$%^&*_~'''

# Model for computing sentence embeddings. We use one trained for similar questions detection
model = SentenceTransformer('all-MiniLM-L6-v2')

# We donwload the Quora Duplicate Questions Dataset (https://www.quora.com/q/quoradata/First-Quora-Dataset-Release-Question-Pairs)
# and find similar question in it
#url = "http://qim.fs.quoracdn.net/quora_duplicate_questions.tsv"
dataset_path = "submission_db.csv"
max_corpus_size = 2000 # We limit our corpus to only the first 50k questions


# Check if the dataset exists. If not, download and extract
# Download dataset if needed
if not os.path.exists(dataset_path):
    print("Found data set")

# Get all unique sentences from the file
corpus_sentences = set()
with open(dataset_path, encoding='utf8') as fIn:
    reader = csv.DictReader(fIn, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    csv.field_size_limit(100000000)
    for row in reader:
        x = row['area_text'] 
        #print(x)
        sens= x.split('.')
        for elem in sens: #sentences
            #print(elem)
            corpus_sentences.add(elem)
            
        #corpus_sentences.add(row['question2'])
        #print(len(corpus_sentences))
        if len(corpus_sentences) >= max_corpus_size:
            break

corpus_sentences = list(corpus_sentences)
print("Encode the corpus. This might take a while")
corpus_embeddings = model.encode(corpus_sentences, batch_size=64, show_progress_bar=True, convert_to_tensor=True)


print("Start clustering")
start_time = time.time()

#Two parameters to tune:
#min_cluster_size: Only consider cluster that have at least 25 elements
#threshold: Consider sentence pairs with a cosine-similarity larger than threshold as similar
clusters = util.community_detection(corpus_embeddings, min_community_size=5, threshold=0.7)

print("Clustering done after {:.2f} sec".format(time.time() - start_time))

#Print for all clusters the top 3 and bottom 3 elements
for i, cluster in enumerate(clusters):
    print("reached here")
    print("\nCluster {}, #{} Elements ".format(i+1, len(cluster)))
    for sentence_id in cluster[:]:
        print("\t", corpus_sentences[sentence_id])
    print("\t", "...")
    #for sentence_id in cluster[-3:]:
        #print("\t", corpus_sentences[sentence_id])
