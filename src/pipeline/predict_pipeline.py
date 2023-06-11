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
                 cropa_area: float,
                 cropb_area: float,
                 cropc_area: float,
                 cropd_area: float,
                 crope_area: float):
        self.lat = lat
        self.long = long
        self.cropa_area = cropa_area
        self.cropb_area = cropb_area
        self.cropc_area = cropc_area
        self.cropd_area = cropd_area
        self.crope_area = crope_area


    def get_data_as_data_frame(self):
        '''
        Return all the input in form of dataframe
        '''
        try:
            custom_data_input_dict = {
                'Unnamed: 0':23,
                'Longitude':[self.lat],
                'Latitude':[self.long],
                'CORN, GRAIN - ACRES HARVESTED':[self.cropa_area],
                'BARLEY - ACRES HARVESTED':[self.cropb_area],
                'RICE - ACRES HARVESTED':[self.cropc_area],
                'SUGARCANE, SUGAR - ACRES HARVESTED':[self.cropd_area],
                'WHEAT - ACRES HARVESTED':[self.crope_area],
                
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)        
        
    