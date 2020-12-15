# Class for a testo 175 h1 datafile

import pandas as pd

class Testo175H1: 
    _created_by = "Testo 175 H1"

    def __init__(self, csv_path):
        self.data = pd.read_csv(csv_path) 

    def __repr__(self):
        return f"Measurement from {Testo175H1._created_by} on {self.date} containing {len(self.data)} entries."

    @property
    def mean(self): 
        return self.data.mean(axis=1)

    @property
    def minmax(self):
        return self.data.min(), self.data.max() 

    
