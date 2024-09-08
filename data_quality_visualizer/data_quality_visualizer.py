import pandas as pd
import numpy as np

class DataQualityVisualizer:
    def __init__(self, df):
        self.df = df
        
    def check_null_values(self):
        """
        Checks for null values in the DataFrame and returns the result.

        This method evaluates whether any null values are present in the DataFrame.
        It returns a dictionary with the test result and the total number of null values if any are found.

        Returns:
        dict: A dictionary with the keys 'test_status' and 'null_count'.
              'test_status' is either 'Passed' or 'Failed', and 'null_count' contains
              the total number of null values if the test failed.
        """
        result = {}

        has_null_values = self.df.isnull().values.any()

        if has_null_values:
            null_count = self.df.isnull().sum().sum()
            result['test_status'] = 'Failed'
            result['null_count'] = null_count
        else:
            result['test_status'] = 'Passed'
            result['null_count'] = 0

        return result
