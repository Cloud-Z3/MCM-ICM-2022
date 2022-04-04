# import pandas as pd
# import numpy as np
from collections import Counter
import os
# from Q1_lib import *
from copy import deepcopy
from Q1_3_subnet_description import *

nodefile = f'./Data/p1/1_nodes.csv'
edgefile = f'./Data/p1/0_network_draw.csv'
for item in zip(['flow_centrality', 'average_path_length', 'cluster_coffecient'], descript(nodefile, edgefile)):
    print(item)
