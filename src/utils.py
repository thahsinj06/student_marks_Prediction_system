import os
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
import dill
def save_object(file_path, obj):
    try:
        # Extract directory path from file_path
        dir_path = os.path.dirname(file_path)
        
        # Create the directory if it does not exist
        os.makedirs(dir_path, exist_ok=True)
        
        # Open the file in binary write mode and dump the object
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
            
    except Exception as e:
        raise CustomException(e,sys)