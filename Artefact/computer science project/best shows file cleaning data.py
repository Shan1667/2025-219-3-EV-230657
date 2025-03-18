import pandas as pd 
import numbers
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
df = pd.read_csv("C:\\Users\\20SShahid.ACC\\Downloads\\Best Shows Netflix.csv")
print(df.info())
df.columns = df.columns.str.lower()
print(df.info())
df = df.drop('main_production', axis=1) 
df = df.drop('index', axis=1)
print(df.info())
df.to_csv('Best Shows Netflix_cleaned.csv', index=False)
print(df.info())
missing_values = df.isnull().sum()

print(missing_values)

x = df.to_dict()
cred = credentials.Certificate("lcproject2025-7a740-firebase-adminsdk-fbsvc-a987fa3758.json")
firebase_admin.initialize_app(cred, {"databaseURL":'https://lcproject2025-7a740-default-rtdb.europe-west1.firebasedatabase.app/'})
ref = db.reference('/Cleaned_tv_show_data_from_file')#reference the root node of the database
 
ref.set(x)
print(x)