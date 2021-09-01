import os
from initial import now
import pandas as pd

def upsert_refresh_data(now = now):
    os.makedirs(os.path.expanduser('~/cobliBI'), exist_ok=True)
    df = pd.DataFrame([now])
    df.to_csv(os.path.expanduser('~/cobliBI/data_file.csv'), index = False)

save_last_refresh_function_name = 'upsert_refresh_data'