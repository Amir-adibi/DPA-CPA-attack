import os
from AccessData import *
from Plot import *
from Attack import *

data_directory = Path("preprocessed_data")
data = AccessData()

if not os.listdir(data_directory):  # data_directory is empty
    data.save_traces()
    data.save_plaintext()

traces, plaintexts = data.get_data()

# plotting
plt = Plot(traces, False)
plt.plot()

# attacking
atck = Attack(traces, plaintexts)
atck.attack()

