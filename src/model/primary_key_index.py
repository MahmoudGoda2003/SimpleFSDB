# Import necessary modules
import sys
import os

# Append the parent directory of the current file to sys.path
sys.path.append(os.path.dirname(__file__).replace("model", ''))

# Import the Index class
from model.index import *

# Define a PrimaryKeyIndex class that inherits from Index
class PrimaryKeyIndex(Index):
    def __init__(self, primary_key_name, table_metadata):
        # Call the constructor of the parent class (Index)
        super().__init__(primary_key_name, table_metadata)

    # Override the serialize method (no action for PrimaryKeyIndex)
    def serialize(self):
        pass

    # Override the add_value method (no action for PrimaryKeyIndex)
    def add_value(self):
        pass

    # Override the __update_value__ method (no action for PrimaryKeyIndex)
    def __update_value__(self, value_name, primary_keys):
        pass

    # Override the remove_value method (no action for PrimaryKeyIndex)
    def remove_value(self):
        pass
