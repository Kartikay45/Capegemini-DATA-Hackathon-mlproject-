# transforming the dataset

import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.preprocessing import FunctionTransformer


from src.exception import CustomException
from src.logger import logging
import os

from src.utils import save_object

@dataclass
class DataTransformationConfig:
    '''
    Data Transformation- file path
    '''
    preprocessor_obj_file_path = os.path.join('artifact','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    
    def get_data_transformer_object(self):
        try:
            # Transformation functions
            def calculate_x(lat, lon):
                return np.cos(np.radians(lat)) * np.cos(np.radians(lon))

            def calculate_y(lat, lon):
                return np.cos(np.radians(lat)) * np.sin(np.radians(lon))

            def calculate_z(lat):
                return np.sin(np.radians(lat))
           
           
            pipeline = Pipeline([
                ('transformer', FunctionTransformer(
                    func=lambda X: np.column_stack([
                        calculate_x(X.iloc[:, 0], X.iloc[:, 1]),
                        calculate_y(X.iloc[:, 0], X.iloc[:, 1]),
                        calculate_z(X.iloc[:, 0])
                    ]),
                    validate=False
                ))
            ])

            # Create the ColumnTransformer
            preprocessor = ColumnTransformer(
                transformers=[
                    ('coordinates', pipeline, ['Latitude', 'Longitude'])
                ],
                remainder='passthrough'
            )
            logging.info('transformation done')
            return preprocessor

        except Exception as e:
            raise CustomException(e,sys)


    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info('Read train and test data completed')
            

            logging.info('Obtaining preprocessing object')
            preprocessing_obj = self.get_data_transformer_object()

            target_column_name = 'Crop-Scope1-MMT'
            # numerical_columns = []

            input_feature_train_df = train_df.drop(columns = [target_column_name], axis = 1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns = [target_column_name], axis = 1)
            target_feature_test_df = test_df[target_column_name]

            logging.info(f"applying preprocessing object on training and testing dataframe")

            # calling the pickle file for the transformation:
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            # Create a new DataFrame with transformed coordinates
            transformed_train_df = pd.DataFrame(
            input_feature_train_arr,
            columns=['x', 'y', 'z','Corn','barley','rice','sugar','wheat'],
            index=train_df.index)

            transformed_test_df = pd.DataFrame(
            input_feature_test_arr,
            columns=['x', 'y', 'z','Corn','barley','rice','sugar','wheat'],
            index=test_df.index)

            # Drop the original latitude and longitude columns
            # train_df = train_df.drop(['Latitude', 'Longitude'], axis=1)
            # test_df = test_df.drop(['Latitude', 'Longitude'], axis=1)

            # # Concatenate the new DataFrame with the transformed coordinates
            # train_df = pd.concat([transformed_train_df,train_df], axis=1)
            # test_df = pd.concat([transformed_test_df,test_df], axis=1)
            
            train_arr = np.c_[np.array(transformed_train_df), np.array(target_feature_train_df)]
            test_arr = np.c_[np.array(transformed_test_df), np.array(target_feature_test_df)]
            logging.info(f"saved the preprocessing object")

            # wrote this function in utils
            save_object(
                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessing_obj
            )

            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )




        except Exception as e:
            raise CustomException(e,sys)

