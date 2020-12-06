'''
Recommender systems abstract classes.
Inspired by sklearn _base.py
'''
#%% Modules
#standard
from abc import ABC, abstractmethod
import numpy as np

#personal
from node import UserNode, MovieNode
from context import userData


#%% Trivial Recommandation System
class _RecSystem(ABC):
    '''
    Abstract class for recommender systems.
    '''
    def __init__(self):
        pass

    @abstractmethod
    def fit(self, edges):
        pass

    @abstractmethod
    def predict(self, userIds: np.array, *args)-> np.array:
        pass
    pass



class _Clf(_RecSystem):
    '''
    Classifier recommendation system
    '''
    def __init__(self):
        super().__init__()
        pass

    @abstractmethod
    def predict(self, edges, nRec, nHidden = -1)->np.array:
        '''recommends nRec movies to each user whose id is in the edges
        
        Parameters
        -------
            userIds : np.array or dict
                Providing  a dict of form {id : UserNode(id)} as given by the graph
                should be possible.

            nRec: int
                number of recommendations the clf should do.

            nHidden: int
                useful for scoring. Default value should not be changed

        Returns
        -------
            (pred, userKeys) : tuple
                pred: np.array of shape (nUsers, nRec)
                    containing the ids of the predictions
                userKeys: list
                    id of the users in edges. In ascending order.
                    (will be compared when scoring)
        '''
        pass
    pass
