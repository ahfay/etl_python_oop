from connection import Conn
from ekstrak import FromDataframe
from transform import Transform
from load import Load

if __name__ == '__main__':
    print('[CONNECTION] Start')
    conn = Conn().conn_psg()
    print('[CONNECTION] Connect To PostgreSQL')
    print('[====================]')

    print('[EKSTRAK] Start')
    path = 'source/nyc_tlc_yellow_trips_2018_subset_1.csv'
    file = FromDataframe(file=path)
    print('[EKSTRAK] From {}'.format(path))
    df = file.df()
    print('[EKSTRAK] End')
    print('[====================]')

    print('[TRANSFORM] Start')
    transform = Transform(df)
    print('[TRANSFORM] Split Column pickup_datetime')
    pickup_datetime = transform.split_datetime('pickup_datetime',pemisah='T')
    print('[TRANSFORM] Split Column dropoff_datetime')
    dropoff_datetime = transform.split_datetime('dropoff_datetime',pemisah='T')
    print('[TRANSFORM] Drop Columns Old')
    new_df = transform.drop_column_old(['pickup_datetime','dropoff_datetime'])
    print('[TRANSFORM] Assign New Column')
    new_df = new_df.assign(
        pickup_date = pickup_datetime[0],
        pickup_time = pickup_datetime[1],
        dropoff_date = dropoff_datetime[0],
        dropoff_time = dropoff_datetime[1]
    )
    print('[TRANSFORM] End')
    print('[====================]')
    
    print('[LOAD] Start')
    print('[LOAD] to PostgreSQL')
    Load(conn=conn).dataframe_to_psg(df=new_df, name_table='etl_clean')
    print('[LOAD] End')



