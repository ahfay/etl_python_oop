class Load():
    def __init__(self, conn):
        self.conn = conn

    def dataframe_to_psg(self, df, name_table):
        df.to_sql(name_table, self.conn, if_exists='replace', index=False)
        self.conn.close()