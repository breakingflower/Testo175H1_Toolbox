import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import glob

from testo.testo175h1 import Testo175H1

_DATA_ROOT = "/mnt/c/Users/flori/Nextcloud/REMMEN BV/20201005 - Constructie Rubens/ClimateMeasurements"

for csv_path in glob.glob(f"{_DATA_ROOT}/*.csv"): 
    t = Testo175H1(csv_path) 
