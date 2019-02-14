import numpy as np
import pandas as pd
import scipy, scipy.stats

import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
from pathlib import Path


class DataWrapper:
    def __init__(self):
        self.raw_data = None
        self.clean_data = None
        self.one_hot_list = None
        self.n_unique = None
        self.unique_columns = []

    # opens a file **kwarg possible filetype: 1=CSV 2=Excel 3=JSON
    def read_data(self, *, path, file_type,  **kwargs):
        # file_type = 1
        my_file = Path(path)
        if my_file.is_file():
            if file_type == 1:
                self.raw_data = pd.read_csv(path, **kwargs)
                self.clean_data = self.raw_data.copy()
            elif file_type == 2:
                self.raw_data = pd.read_excel(path, **kwargs)
                self.clean_data = self.raw_data.copy()
            elif file_type == 3:
                self.raw_data = pd.read_json(path, **kwargs)
                self.clean_data = self.raw_data.copy()
        else:
            print("Datei {paths} existiert nicht!".format(paths=path))

    def save_data(self, data, path, **kwargs):
        data.to_csv(path, **kwargs, index=False)
        return pd.read_csv(path, **kwargs)

    def clean(self, *,
                   drop_nan=False,
                   n_unique=False,
                   drop_duplicates=False,
                   drop_columns=False, column_label=None,
                   save_df=False, path='../data/after_cleanup.csv'
                   ):
        if drop_nan:
            self.clean_data.dropna(inplace=True)
        if drop_duplicates:
            self.clean_data.drop_duplicates(inplace=True)

        if drop_columns:
            self.clean_data.drop(column_label, axis=1, inplace=True)
        if save_df:
            self.save_data(self.clean_data, path)
        if n_unique:
            self.n_unique = self.clean_data.nunique()
            for index, value in self.clean_data.nunique().iteritems():
                if value == 1:
                    self.unique_columns.append(index)
            print(self.clean_data.nunique())

    def create_one_hot(self, column_list):
        categorical = pd.get_dummies(self.clean_data[column_list])
        self.one_hot_list = pd.concat([self.clean_data, categorical], axis=1, sort=False)
