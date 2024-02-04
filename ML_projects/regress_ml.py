# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/train_ml_regression.ipynb.

# %% auto 0
__all__ = ['TrainRegression']

# %% ../nbs/train_ml_regression.ipynb 3
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor
from . import const_vals as CONST

# %% ../nbs/train_ml_regression.ipynb 4
class TrainRegression():
       
       def __init__(self,
               df_path : str , # path to dataframe to be used to train. File should be CSV file
               ground_truth_col: str, # name of the column with true data to train
               test_size : float , #size of data to be used for test 

               columns_to_remove : list[str]=None , #columns not to use for trainning the model. These columns will be removed.
               ):
             self.df_path = df_path
             self.columns_to_remove = columns_to_remove
             self.ground_truth_col = ground_truth_col
             self.test_size = test_size
             self.x_train, self.x_test, self.y_train, self.y_test =self._load_df_split_data()
             

       def _load_df_split_data(self):
               
               self.df = pd.read_csv(self.df_path)
               #load dataframe
               if self.columns_to_remove!= None:
                     self.df = self.df.drop(self.columns_to_remove,axis=1)
          
               # split to x,y and train test data
               self.x = self.df.drop(self.ground_truth_col,axis=1)
               self.y = self.df[self.ground_truth_col].values

               #split data to train and test
               self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(
                      self.x, self.y, test_size=self.test_size, random_state=42)

               return self.x_train, self.x_test, self.y_train, self.y_test
       
       def train_model(self):
              
              # create base model
              rf = RandomForestRegressor()

              rf_random = RandomizedSearchCV(estimator = rf, 
                                             param_distributions = CONST.random_grid_rf,
                                               n_iter = CONST.n_iteration_rf,
                                                 cv = CONST.cv_rf, 
                                                 verbose=CONST.VERBOSE , 
                                                 random_state=CONST.RANDOM_STATE , 
                                                 n_jobs = CONST.N_JOBS)
                      



