import pandas as pd
from unicodedata import normalize
import ssl
from datetime import datetime


ssl._create_default_https_context = ssl._create_unverified_context
table = pd.read_html('https://www.lascondes.cl/salud/destacados/el-botiquin-de-las-condes.html')
df = table[0]
date = datetime.today().strftime(r'%Y-%m-%d')
df.to_csv('data/' + date + '.csv')