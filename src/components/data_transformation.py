# transforming the dataset

import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


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
            # we are using the decision tree classifier for this particular project
            # numerical_columns = []
            # categorical_columns = []

            # num_pipeline = Pipeline(
            #     steps = [
            #         ("imputer", SimpleImputer(strategy='median')),
            #         ("scaler", StandardScaler())
            #     ]
            # )

            # cat_pipeline = Pipeline(
            #     steps = [
            #         ('imputer', SimpleImputer(strategy = "most_frequent")),
            #         ('encoder', OneHotEncoder()),
            #         ('Scaler', StandardScaler())
            #     ]
            # )

            # logging.info('Categorical Columns and Numerical encoding completed')

            logging.info('transformation done')
            preprocessor = ColumnTransformer(
                transformers=[],
                remainder="passthrough"
            )

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

            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

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


            ## working on data_transformation component
