import pandas as pd
import numpy as np

class DataQualityVisualizer:
    def __init__(self, df):
        self.df = df
        
    def check_null_values(self):
        """
        Checks for null values in the DataFrame and prints the result.

        This method evaluates whether any null values are present in the DataFrame. 
        It prints the test result and the total number of null values if any are found.

        Returns:
        None
        """
        print("[=================================================================]")
        print("")
        
        # Check for the presence of null values in the DataFrame
        has_nulls = self.df.isnull().values.any()
        
        if has_nulls:
            # Calculate the total number of null values
            null_sum = self.df.isnull().sum().sum()
            print("TEST CASE NULL VALUES: Failed")
            print(f"Total number of null values: {null_sum}")
            print("Please address these null values to ensure data completeness.")
        else:
            print("TEST CASE NULL VALUES: Passed")
            print("No null values found. The dataset is complete.")
        
        print("")
        print("[=================================================================]")
