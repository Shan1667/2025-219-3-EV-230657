import matplotlib.pyplot as plt
import numpy as np
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pandas as pd 
import numbers


cred = credentials.Certificate("lc-project-2025-2269a-firebase-adminsdk-85ep1-946b0c6354.json")
firebase_admin.initialize_app(cred, {"databaseURL":'https://lc-project-2025-2269a-default-rtdb.europe-west1.firebasedatabase.app/Movies'})
ref = db.reference('/main_genre')#reference the root node of the database
 
y = ref.get()
comedy = 0
print(type(y))
print(y)
for main_genre in y:
    comedy = comedy + 1


plt.style.use('_mpl-gallery')

# make data:
x = 0.5 + np.arange(8)
y = [4.8, 5.5, 3.5, 4.6, 6.5, 6.6, 2.6, 3.0]

# plot
fig, ax = plt.subplots()

ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()