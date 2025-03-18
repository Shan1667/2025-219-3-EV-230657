import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pandas as pd 
import numbers
df = pd.read_csv("C:\\Users\\20SShahid.ACC\\Downloads\\Best Movies Netflix.csv")
print(df.info())
df.columns = df.columns.str.lower()
print(df.info())
df = df.drop('number_of_votes', axis=1) 
#df = df.drop('index', axis=1)
#print(df.info())
df.to_csv('Best Movies Netflix all time cleaned.csv', index=False)
print(df.head())
missing_values = df.isnull().sum()

# print(missing_values)

data_for_movies = df.to_dict()
#for key, value in data_for_movies.items():
#    print(key,value)

cred = credentials.Certificate("lcproject2025-7a740-firebase-adminsdk-fbsvc-a987fa3758.json")
firebase_admin.initialize_app(cred, {"databaseURL":'https://lcproject2025-7a740-default-rtdb.europe-west1.firebasedatabase.app/'})
ref = db.reference('/Cleaned_movie_data_from_file')#reference the root node of the database
 
ref.set(data_for_movies)