import pandas as pd

class FromDataframe():
    def __init__(self, file, sep=None, parse_dates=None,):
        self.name_file = file
        self.sep = sep
        self.parse_dates = parse_dates
    
    def df(self):
        return pd.read_csv(self.name_file, self.sep, self.parse_dates, engine='python')
    