import os
import sys
from dataclasses import dataclass

from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)

from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_model

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifact','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info('splitting train and test input data')
            X_train, y_train, X_test, y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            models = {
                "linear_regressor": LinearRegression(),
            }

            # params = {
            #     "decision_tree":{
            #         'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
            #         'splitter': ['best','random'],
            #         'max_features':['sqrt','log2']
            #     }
            # }


            model_report: dict = evaluate_model(X_train= X_train, y_train = y_train, 
                                                X_test = X_test, y_test=y_test,
                                                models= models, params = None)
            
            # Get the best model Score:
            best_model_score = max(sorted(model_report.values()))

            # Get the best model from the dictionary:
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]

            # set the threshold for best model
            if best_model_score < 0.7:
                raise CustomException('No Best model found')
            logging.info('Best found model on training and test dataset')
            
            save_object(
                file_path = self.model_trainer_config.trained_model_file_path,
                obj= best_model
            )

            predicted = best_model.predict(X_test)
            r2_square = r2_score(y_test, predicted)
            logging.info('returning the r2_score')
            return r2_square
        

        except Exception as e:
            raise CustomException(e, sys)

