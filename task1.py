class CountVectorizer:

    def __init__(self):
        self._vocabulary = {}

    def fit_transform(self, corpus):

        features = set()
        
        # заполняем множество уникальными словами из корпуса
        for doc in corpus:
            features.update(doc.lower().split())

        # ключи - слова, значение - списки, 
        # где на i-м месте встречаемость слова в i-м предложении
        for feat in features:
            self._vocabulary[feat] = []

        for doc in corpus:
            for word in self._vocabulary:
                self._vocabulary[word].append(doc.lower().split().count(word))

        termdoc_matr = []

        for i in range(len(corpus)):
            termdoc_matr.append([])
            for word_count in self._vocabulary.values():
                termdoc_matr[i].append(word_count[i])

        return termdoc_matr   
       
        # n_docs = len(corpus)
        # feature_names = set()

        # for doc in corpus:
        #     feature_names.update(doc.lower().split())

        # feature_names = list(feature_names)
        # self.feature_names = feature_names
        # termdoc_matr = [[0 for i in feature_names] for j in range(n_docs)]
        
        # for i, doc in enumerate(corpus):    
        #     for j, feature in enumerate(feature_names):
        #         termdoc_matr[i][j] = doc.lower().split().count(feature)

        # return termdoc_matr

    def get_feature_names(self):
        return list(self._vocabulary.keys())

corpus = [
    'Crock Pot Pasta Never boil pasta again',
    'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]
vectorizer = CountVectorizer()
count_matrix = vectorizer.fit_transform(corpus)
print(count_matrix)
print(vectorizer.get_feature_names())