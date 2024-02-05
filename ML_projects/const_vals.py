# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/CONSTANTS.ipynb.

# %% auto 0
__all__ = ['RANDOM_STATE', 'N_JOBS', 'VERBOSE', 'RANDOM_GRID_RFR', 'SPACE_RFR', 'N_ITERATIONS_RFR', 'CV_RFR']

# %% ../nbs/CONSTANTS.ipynb 3
from skopt.space import Real, Integer
from skopt.utils import use_named_args
from sklearn.model_selection import cross_val_score

# %% ../nbs/CONSTANTS.ipynb 4
RANDOM_STATE = 42 
N_JOBS = -1 
VERBOSE = 1

# %% ../nbs/CONSTANTS.ipynb 5
RANDOM_GRID_RFR={'bootstrap': [True, False],
                'max_depth': [20, 40, 70, 80],
                'max_features': ['auto', 'sqrt'],
                'min_samples_leaf': [1, 2, 4],
                'min_samples_split': [2, 5, 10],
                'n_estimators': [200, 400, 600, 800]}

SPACE_RFR  = [Integer(1, 20, name='max_depth'),
              Integer(1 ,10  , name ='min_samples_leaf'),
              Integer(1 ,10  , name ='min_samples_split'), 
              Integer(100 ,800  , name ='n_estimators')]   


N_ITERATIONS_RFR = 100
CV_RFR = 3

