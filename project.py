
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.model_selection import RandomizedSearchCV


class my_model():

    def preprocess(self, X):

        X = X['description'] + " " + X['title'] + " " + X['requirements']
        X = X.str.lower()
        X = X.str.replace('[^\w\s]', '') # remove punctuation
        X = X.str.replace('\d{1,}', '') # remove digits
        X = X.str.replace('_+', '') # remove underscore
        X = X.str.replace('\s\w\s', '') # remove single characters
        X = X.str.replace('\s{2,}', '') # remove multiple spaces

        return X

    def fit(self, X, y):

        X = self.preprocess(X)

        self.preprocessor = TfidfVectorizer(stop_words='english', norm='l2', use_idf=True, smooth_idf=True,
                                            ngram_range=(1, 4))

        xx = self.preprocessor.fit_transform(X)

        self.pac = PassiveAggressiveClassifier(class_weight="balanced")
        pac_parameters = {'random_state': [5, 10, 15, 20], 'C': [0.25, 0.5, 0.75, 1], 'shuffle': [True, False]}

        self.rscv = RandomizedSearchCV(self.pac, pac_parameters, random_state=42, n_jobs=-1)
        self.rscv.fit(xx, y)

        return

    def predict(self, X):

        X = self.preprocess(X)

        xx = self.preprocessor.transform(X)

        predictions = self.rscv.predict(xx)

        return predictions
