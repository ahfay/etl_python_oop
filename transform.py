

class Transform():
    def __init__(self, dataframe):
        self.df = dataframe
    
    def split_datetime(self, column_datetime, pemisah):
        date_time_str = self.df[column_datetime].astype('str')
        date_time_expand = date_time_str.str.split(pemisah,expand=True)
        return date_time_expand
    
    def drop_column_old(self, column_old):
        return self.df.drop(column_old, axis=1)
    

