# Download dataset from kaggle with the link https://www.kaggle.com/datasets/ankitbansal06/retail-orders


# extract file from zip file
import zipfile
zip_ref = zipfile.ZipFile('archive (24).zip')
zip_ref.extractall() # extract file to dir
zip_ref.close() # close file


# read data from file and handle null values
import pandas as pd
df = pd.read_csv('orders.csv', na_values=['Not Available','unknown' ])
df['Ship Mode'].unique()


# rename columns names .. make them lowe case and replace soace with underscores
#df.columns = df.columns.str.lower()
#df.columns = df.columns.str.replace(' ','_')
#df.columns
df.head()


#derive new columns discount , sale price and profit
#df['discount']=df['list_price']*df['discount_percent']*.01
#df['sale_price']= df['list_price']-df['discount']
df['profit']=df['sale_price']-df['cost_price']
df


#convert order date from object data type to datetime
df['order_date']=pd.to_datetime(df['order_date'],format="%Y-%m-%d")
df


#drop cost price list price and discount percent columns
df.drop(columns=['list_price','cost_price','discount_percent'],inplace=True)


# Connect to Postgres sql database
from sqlalchemy import create_engine
# Define your database connection
engine = create_engine("postgresql://postgres:{PASSWORD}@localhost:5432/postgres")



# Load data into PostgreSQL (replace or append)
df.to_sql('orders', engine, if_exists='replace', index=False, schema='public')


