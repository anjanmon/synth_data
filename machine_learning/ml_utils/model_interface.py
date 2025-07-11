
from sklearn.base import BaseEstimator
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
import numpy as np
from sklearn.exceptions import NotFittedError




class Models(BaseEstimator):
    def __init__(self, model:BaseEstimator):
        self.model = model
        self.is_fitted = False
        self.prediciton = None
    
    def fit(self, X,y):
        self.model.fit()
        is_fitted = True

    def predict(self, X) -> np.array:
        if not self.is_fitted:
            raise NotFittedError("Cannot call 'predict' before fitting the model. Use 'fit(X, y)' first to train the model.")
        self.predict_output = self.model.predict(X)

        return self.predict_output


    