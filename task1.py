class CountVectorizer:

    def __init__(self):
        self._vocabulary = set()

    def fit_transform(self, corpus):

        for doc in corpus:
            self._vocabulary.update(doc.lower().split())

        termdoc_matr = [[0 for _ in self._vocabulary] for _ in corpus]
        
        for i, doc in enumerate(corpus):  
            for j, feature in enumerate(self._vocabulary):
                termdoc_matr[i][j] = doc.lower().split().count(feature)

        return termdoc_matr

    def get_feature_names(self):
        return list(self._vocabulary)

corpus = [
    'Crock Pot Pasta Never boil pasta again',
    'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]

vectorizer = CountVectorizer()
count_matrix = vectorizer.fit_transform(corpus)
print(count_matrix)
print(vectorizer.get_feature_names())
