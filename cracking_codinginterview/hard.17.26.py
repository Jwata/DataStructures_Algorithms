a = [1, 3]

def find_similar_pairs(docs):
    ids = [i for i in docs.keys()]
    n = len(docs)
    pairs = []

    for i in range(n-1):
        a = docs[ids[i]]
        a.sort()
        for j in range(i+1, n):
            b = docs[ids[j]]
            b.sort()

            sim = similarity(a, b)

            if sim > 0:
                pairs.append((ids[i], ids[j], sim))

    return pairs

def similarity(a, b):
    n = len(a)
    m = len(b)
    i = 0
    j = 0

    n_inter = 0

    while i < n and j < m:
        if a[i] == b[j]:
            n_inter += 1
            i += 1
            j += 1
        elif a[i] > b[j]:
            j += 1
        else:
            i += 1

    return n_inter / (n + m - n_inter)

docs = {
    13: [14, 15, 100, 9, 3],
    16: [32, 1, 9, 3, 5],
    19: [15, 29, 2, 6, 8, 7],
    24: [7, 10]
}
pairs = find_similar_pairs(docs)
print(pairs)
