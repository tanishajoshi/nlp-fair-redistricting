import subprocess
"""
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'top2vec'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'top2vec[sentence_encoders]'])
"""
#subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
#'tensorflow tensorflow_hub tensorflow_text'])

from top2vec import Top2Vec
import os
import csv
import sys


"""
Top2Vec is an algorithm for topic modeling and semantic search. It automatically 
detects topics present in text and generates jointly embedded topic, document and 
word vectors. We used this for raw COI submission data entries and discovered a total
of 3 underlying topics within the dataset. 


"""

dataset_path = sys.path[0] + '/../submission_db.csv'
max_corpus_size = 2000 #total entries 
if not os.path.exists(dataset_path):
    print("Can't find data set")

#extract only unique entries in file
corpus = set()
with open(dataset_path, encoding='utf8') as fIn:
    reader = csv.DictReader(fIn, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    csv.field_size_limit(100000000)
    numrows = 0
    for row in reader:
        numrows+=1
        entry = row['area_text'] 
        #print(x)
        sents= entry.split('.')
        for elem in sents: #sentences
            #print(elem)
            corpus.add(elem)
        #corpus_sentences.add(row['question2'])
        #print(len(corpus_sentences))
        if len(corpus) >= max_corpus_size:
            break
print(numrows)
corpus = list(corpus)
model = Top2Vec(corpus)
"""
models can be trained and saved.
model.save("filename")
model = Top2Vec.load("filename")
"""
#pretrained embedding model for univ sent. encoder
model = Top2Vec(corpus, embedding_model='universal-sentence-encoder')

num_topics = model.get_num_topics()
print("Number of topics discovered", num_topics)

#return num of entries most similar to each topic in decreasing order of size
"""
topic_sizes: The number of documents most similar to each topic.
topic_nums: The unique index of every topic will be returned.
"""
topic_sizes, topic_nums = model.get_topic_sizes()
print(topic_sizes, topic_nums)

#return the topics in decreasing size
"""
topic_words: For each topic the top 50 words are returned, 
in order of semantic similarity to topic.

word_scores: For each topic the cosine similarity scores of the top 50 
words to the topic are returned.

topic_nums: The unique index of every topic will be returned.
"""
topic_words, word_scores, topic_nums = model.get_topics()
print(topic_words, word_scores, topic_nums)


#Search for topics most similar to a keyword (not sure abt this one)
# topic_words, word_scores, topic_scores, topic_nums = model.search_topics(keywords=["health"], num_topics=5)
for topic in topic_nums:
    model.generate_topic_wordcloud(topic)
