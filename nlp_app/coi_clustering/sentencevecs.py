from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
model = SentenceTransformer('bert-base-nli-mean-tokens')
sentences = [
    "Working families in northern Columbia, many with kids who attend Derby Ridge and Blue Ridge schools ",
    "This is a community of families who care about their neighborhood,  education and schools, hospitals and health care.", 
    "People in this area enjoy using bicycles for commuting and recreation.",
    "Lots of folks go to the dog park and trails, very few sidewalks, very car heavy, no public transit, tons of dump truck traffic on creasy springs and good amount of public workers and building trades.",
    "Shared interests include tourism, historical preservation, education and youth activities, infrastructure, community spaces, local hospital, concern for flooding, hunting/fishing, some concern for social and racial justice.",
    "Public schools like Ridgeway Elementary and Hickman High School attract settling families and kids to the area, bringing more support for local businesses.",
    "No hospital services, deep racial divides, low income in small communities with the wealth in the rural farming areas, schools are fairly good in the communities.",
    "The closer to Downtown, the more you see undergraduate student housing though there are still residential neighborhoods, concerns can vary from accessibility of schools to housing affordability and renters rights."
]

sentence_vecs = model.encode(sentences)
print(sentence_vecs)
print(sentence_vecs.size)
print(sentence_vecs.shape) # returns (x,y) each one of the x sentences is being rep'd by a dense vector containing y values

# calculate cosine similarity
s1 = cosine_similarity([sentence_vecs[0]], sentence_vecs[:])
s2 = cosine_similarity([sentence_vecs[1]], sentence_vecs[:])
s3 = cosine_similarity([sentence_vecs[2]], sentence_vecs[:])
s4 = cosine_similarity([sentence_vecs[3]], sentence_vecs[:])
s5 = cosine_similarity([sentence_vecs[4]], sentence_vecs[:])
s6 = cosine_similarity([sentence_vecs[5]], sentence_vecs[:])
s7 = cosine_similarity([sentence_vecs[6]], sentence_vecs[:])
s8 = cosine_similarity([sentence_vecs[7]], sentence_vecs[:])

arr1 = np.array(s1)
arr2 = np.array(s2)
arr3 = np.array(s3)
arr4 = np.array(s4)
arr5 = np.array(s5)
arr6 = np.array(s6)
arr7 = np.array(s7)
arr8 = np.array(s8)
print(arr1)
print(arr2)
print(arr3)
print(arr4)
print(arr5)
print(arr6)
print(arr7)
print(arr8)



