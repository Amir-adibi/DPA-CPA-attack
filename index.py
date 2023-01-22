from AccessData import *
import numpy as np
import os

data_directory = Path("preprocessed_data")
data = AccessData()

if not os.listdir(data_directory):  # data_directory is empty
    data.save_traces()
    data.save_plaintext()

traces, plaintexts = data.get_data()

