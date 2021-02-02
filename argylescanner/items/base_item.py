"""
Base Item module
"""
import os
import pickle
from pydantic import BaseModel

class BaseItem(BaseModel):
    """
    Base Item class
    """

    def serialize(self, file_name):
        """
        serialize object and store in pickle file
        """
        if not os.path.exists('pickles'):
            os.makedirs('pickles')
        with open("pickles/" + file_name + '.pickle', 'wb') as f:
            pickle.dump(self, f)

def deserialize(file):
    """
    deserialize object given a data argument
    """
    return pickle.load(file)