import sys
import pandas as pd
import numpy as np

from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = 'artifact/model.pkl'
            preprocessor_path = 'artifact/preprocessor.pkl'
            model= load_object(file_path= model_path)
            preprocessor= load_object(file_path= preprocessor_path)

            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e,sys)


# responsible for mapping all the inputs from frontend to backend
class CustomData:
    def __init__(self, 
                 lat: float,
                 long: float,
                 cropA: float,
                 cropB: float,
                 cropC: float,
                 cropD: float,
                 cropE: float):
        self.lat = lat
        self.long = long
        self.cropA = cropA
        self.cropB = cropB
        '''
        
        '''
        pass


    def get_data_as_data_frame(self):
        '''
        Return all the input in form of dataframe
        '''
        try:
            custom_data_input_dict = {
                'lat':[self.lat],
                'long':[self.long],
                'CropA':[self.CropA],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)        
        
    