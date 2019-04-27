# find similar documents

# def find_similar_pairs(docs):
#     ids = [i for i in docs.keys()]
#     n = len(docs)
#     pairs = []
# 
#     for i in range(n-1):
#         a = docs[ids[i]]
#         a.sort()
#         for j in range(i+1, n):
#             b = docs[ids[j]]
#             b.sort()
# 
#             sim = similarity(a, b)
# 
#             if sim > 0:
#                 pairs.append((ids[i], ids[j], sim))
# 
#     return pairs
# 
# def similarity(a, b):
#     n = len(a)
#     m = len(b)
#     i = 0
#     j = 0
# 
#     n_inter = 0
# 
#     while i < n and j < m:
#         if a[i] == b[j]:
#             n_inter += 1
#             i += 1
#             j += 1
#         elif a[i] > b[j]:
#             j += 1
#         else:
#             i += 1
# 
#     return n_inter / (n + m - n_inter)
from collections import defaultdict

# O(kD), k = max number of words in a doc, D = number of docs
def find_similar_pairs(docs):
    # invert matrix O(kD)
    word_to_docs = defaultdict(lambda: [])
    for did, words in docs.items():
        for w in words:
            word_to_docs[w].append(did)

    # count intersections O(kD)
    inter_dict = defaultdict(lambda: defaultdict(lambda: 0))
    for _, doc_ids in word_to_docs.items():
        n = len(doc_ids)
        for i in range(n-1):
            id1 = doc_ids[i]
            for j in range(i+1, n):
                id2 = doc_ids[j]
                inter_dict[id1][id2] += 1

    # calc similarities O(KD)
    pairs = []
    for id1, others in inter_dict.items():
        for id2, n_inter in others.items():
            n1 = len(docs[id1])
            n2 = len(docs[id2])
            sim = n_inter / (n1 + n2 - n_inter)
            pairs.append((id1, id2, sim))

    return pairs

docs = {
    13: [14, 15, 100, 9, 3],
    16: [32, 1, 9, 3, 5],
    19: [15, 29, 2, 6, 8, 7],
    24: [7, 10]
}
pairs = find_similar_pairs(docs)
print(pairs)
