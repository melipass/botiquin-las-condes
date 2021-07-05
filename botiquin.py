import pandas as pd
from unicodedata import normalize
import ssl
from datetime import datetime
import os


ssl._create_default_https_context = ssl._create_unverified_context

def obtain_table():
    table = pd.read_html('https://www.lascondes.cl/salud/destacados/el-botiquin-de-las-condes.html')
    return table[0]

def change_data_capture(df):
    last_file = os.listdir('data/')[-2]
    old_df = pd.DataFrame(pd.read_csv('data/' + last_file))
    old_df = old_df.drop(old_df.columns[0], axis=1)
    print(old_df)
    print(df)
    print(df.equals(old_df))
    print(not df.equals(old_df))
    return not df.equals(old_df)

df = obtain_table()
if (change_data_capture(df)):
    date = datetime.today().strftime(r'%Y-%m-%d')
    df.to_csv('data/' + date + '.csv')
    print('New data added to repository.')
else:
    print('No new data.')
