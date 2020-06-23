import numpy as np

class custom_preproc_ln():
    def __init__(self):
        pass
        
    def fit(self,X,y=None):
        return self
    
    def transform(self,X,y=None):
        output = np.array(X)
        output = output.reshape(-1,1)
        return output