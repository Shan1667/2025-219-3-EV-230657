import matplotlib.pyplot as plt
import numpy as np
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pandas as pd 
import numbers
 
 
cred = credentials.Certificate("lcproject2025-7a740-firebase-adminsdk-fbsvc-a987fa3758.json")
firebase_admin.initialize_app(cred, {"databaseURL":'https://lcproject2025-7a740-default-rtdb.europe-west1.firebasedatabase.app/'})
ref = db.reference('/Cleaned_tv_show_data_from_file/')#reference the root node of the database
 
data_for_graphs = ref.get()
realityscore = 0
romancescore = 0
animationscore = 0
documentaryscore = 0
crimescore = 0
westernscore = 0
comedyscore = 0
thrillerscore = 0
scifiscore = 0
dramascore = 0
actionscore = 0
warscore = 0
for value in range(len(data_for_graphs['main_genre'])):
    if data_for_graphs['main_genre'][value] == 'drama':
        dramascore = dramascore + data_for_graphs['score'][value]
    elif data_for_graphs["main_genre"][value] == "action":
        actionscore = actionscore + data_for_graphs["score"][value]
    elif data_for_graphs["main_genre"][value] == "scifi":
        scifiscore = scifiscore + data_for_graphs["score"][value]
    elif data_for_graphs["main_genre"][value] == "comedy":
        comedyscore = comedyscore + data_for_graphs["score"][value]
    elif data_for_graphs['main_genre'][value] == 'western':
        westernscore = westernscore + data_for_graphs['score'][value]
    elif data_for_graphs['main_genre'][value] == "crime":
        crimescore = crimescore + data_for_graphs['score'][value]
    elif data_for_graphs['main_genre'][value] == "war":
        warscore = warscore + data_for_graphs['score'][value]
    elif data_for_graphs['main_genre'][value] == "documentary":
        documentaryscore = documentaryscore + data_for_graphs['score'][value]
    elif data_for_graphs['main_genre'][value] == "animation":
        animationscore = animationscore + data_for_graphs['score'][value]
    elif data_for_graphs['main_genre'][value] == "thriller":
        thrillerscore = thrillerscore + data_for_graphs["score"][value]
    elif data_for_graphs['main_genre'][value] == "romance":
        romancescore = romancescore + data_for_graphs['score'][value]
    elif data_for_graphs["main_genre"][value] == "reality":
        realityscore = realityscore + data_for_graphs["score"][value]
#print(value)
dictionary_for_genre = {"drama":round(dramascore,2), "romance":round(romancescore,2), "war":round(warscore,2), "action":round(actionscore,2), "western":round(westernscore,2), "documentary":round(documentaryscore,2), "scifi":round(scifiscore,2), "animation":round(animationscore,2), "crime":round(crimescore,2), "comedy":round(comedyscore,2), "thriller":round(thrillerscore,2), "reality":round(realityscore,2)}
print(dictionary_for_genre)
plt.bar(dictionary_for_genre.keys(), dictionary_for_genre.values())
plt.ylabel("Total critic score by category")
plt.xlabel("Genre")
plt.title("Tv-Show graph")
plt.show()
ref = db.reference('/Data_for_show_graph/')
ref.set(dictionary_for_genre)
 
##################################################
# Movie show analysis here on 
##################################################
 
 
#cred = credentials.Certificate("lc-project-2025-2269a-firebase-adminsdk-85ep1-946b0c6354.json")
#firebase_admin.initialize_app(cred, {"databaseURL":'https://lc-project-2025-2269a-default-rtdb.europe-west1.firebasedatabase.app/Movies'})
ref = db.reference('/Cleaned_movie_data_from_file/')#reference the root node of the database
 
data_for_graphs = ref.get()
romancescore = 0
animationscore = 0
documentaryscore = 0
crimescore = 0
westernscore = 0
comedyscore = 0
thrillerscore = 0
scifiscore = 0
dramascore = 0
actionscore = 0
fantasyscore = 0
warscore = 0
musicalscore = 0
sportscore = 0
horrorscore = 0
for value in range(len(data_for_graphs['main_genre'])):
    if data_for_graphs['main_genre'][value] == 'drama':
        dramascore = dramascore + data_for_graphs['score'][value]
    elif data_for_graphs["main_genre"][value] == "action":
        actionscore = actionscore + data_for_graphs["score"][value]
    elif data_for_graphs["main_genre"][value] == "scifi":
        scifiscore = scifiscore + data_for_graphs["score"][value]
    elif data_for_graphs["main_genre"][value] == "comedy":
        comedyscore = comedyscore + data_for_graphs["score"][value]
    elif data_for_graphs['main_genre'][value] == 'western':
        westernscore = westernscore + data_for_graphs['score'][value]
    elif data_for_graphs['main_genre'][value] == "crime":
        crimescore = crimescore + data_for_graphs['score'][value]
    elif data_for_graphs['main_genre'][value] == "war":
        warscore = warscore + data_for_graphs['score'][value]
    elif data_for_graphs['main_genre'][value] == "documentary":
        documentaryscore = documentaryscore + data_for_graphs['score'][value]
    elif data_for_graphs['main_genre'][value] == "animation":
        animationscore = animationscore + data_for_graphs['score'][value]
    elif data_for_graphs['main_genre'][value] == "thriller":
        thrillerscore = thrillerscore + data_for_graphs["score"][value]
    elif data_for_graphs['main_genre'][value] == "romance":
        romancescore = romancescore + data_for_graphs['score'][value]
    elif data_for_graphs["main_genre"][value] == "horror":
        horrorscore = horrorscore + data_for_graphs["score"][value]
    elif data_for_graphs["main_genre"][value] == "sports":
        sportscore = sportscore + data_for_graphs["score"][value]
    elif data_for_graphs["main_genre"][value] == "musical":
        musicalscore = musicalscore + data_for_graphs["score"][value]
    elif data_for_graphs["main_genre"][value] == "fantasy":
        fantasyscore = fantasyscore + data_for_graphs["score"][value]   
#print(value)
dictionary_for_genre = {"drama":round(dramascore,2), "romance":round(romancescore,2), "war":round(warscore,2), "action":round(actionscore,2), "western":round(westernscore,2), "documentary":round(documentaryscore,2), "scifi":round(scifiscore,2), "animation":round(animationscore,2), "crime":round(crimescore,2), "comedy":round(comedyscore,2), "thriller":round(thrillerscore,2), "horror":round(horrorscore,2), "musical":round(musicalscore,2), "sports":round(sportscore,2), "fantasy":round(fantasyscore,2)}
print(dictionary_for_genre)
plt.bar(dictionary_for_genre.keys(), dictionary_for_genre.values())
plt.ylabel("Total critic score by category")
plt.xlabel("Genre")
plt.title("Movies graph")
plt.show()
ref = db.reference('/Data_for_movie_graph/')
ref.set(dictionary_for_genre)
 
#######################################################
### MOST POPULAR AND LEAST POPULAR TV-SHOWS BY YEAR ###
#######################################################
 
ref = db.reference('/Cleaned_tv_show_data_from_file/release_year')
TVreleaseYear = ref.get()
#print(len(TVreleaseYear))
TVreleaseYear_temp = list(TVreleaseYear)
ref = db.reference('/Cleaned_tv_show_data_from_file/title')
TVtitles = ref.get()
#print(len(TVtitles))
 
ref  = db.reference('/Cleaned_tv_show_data_from_file/number_of_votes')
TVvote = ref.get()
# print(TVscore)
 
ref  = db.reference('/Cleaned_tv_show_data_from_file/number_of_votes')
TVvotes = ref.get()
# print(TVvotes)
TVUniqueYears = {}
TVTitleByYear = {}
TVvotesByYear = {}
# print(TVtitles.index('Merlin'))
for year in TVreleaseYear_temp:
    if year in TVTitleByYear:
        # print(type(year))
        #if year == 2008:
        print(TVtitles[TVreleaseYear.index(year)])
        TVTitleByYear[year].append(TVtitles[TVreleaseYear.index(year)])
        TVvotesByYear[year].append(TVvote[TVreleaseYear.index(year)])
    else:
        TVTitleByYear[year] = [TVtitles[TVreleaseYear.index(year)]]
        TVvotesByYear[year] = [TVvote[TVreleaseYear.index(year)]]
        TVUniqueYears[year] = {'Best_title':'','Worst_title':'','Best_number_of_votes':'','Worst_number_of_votes':''}
    title = TVtitles.pop(TVtitles.index(TVtitles[TVreleaseYear.index(year)]))
    score = TVvote.pop(TVvote.index(TVvote[TVreleaseYear.index(year)]))
    years = TVreleaseYear.pop(TVreleaseYear.index(year))
    # if year == 2022:
    #     print(title, score,years)

for key in TVUniqueYears:
    TVUniqueYears[key]['Best_number_of_votes']=max(TVvotesByYear[key])
    TVUniqueYears[key]['Worst_number_of_votes']=min(TVvotesByYear[key])
    TVUniqueYears[key]['Best_title']=TVTitleByYear[key][TVvotesByYear[key].index(max(TVvotesByYear[key]))]
    TVUniqueYears[key]['Worst_title']=TVTitleByYear[key][TVvotesByYear[key].index(min(TVvotesByYear[key]))]

#print(TVTitleByYear)
#print(TVScoreByYear)


print(TVUniqueYears[2022])


print("------------------------------------------------------------------------------------------------------------------------")
#############################################################
### MOST POPULAR MOVIES AND LEAST POPULAR MOVIES BY YEAR  ###
#############################################################
 
ref  = db.reference('/Cleaned_movie_data_from_file/release_year')
MVreleaseYear = ref.get()

MVreleaseYear_temp = list(MVreleaseYear)
 
ref  = db.reference('/Cleaned_movie_data_from_file/number_of_votes')
MVscore = ref.get()

 
 
ref  = db.reference('/Cleaned_movie_data_from_file/title')
MVtitle = ref.get()
#print(len(MVtitle))
MVUniqueYears = {}
MVTitleByYear = {}
MVvotesByYear = {}
for year in MVreleaseYear_temp:
    if year in MVTitleByYear:
          MVTitleByYear[year].append(MVtitle[MVreleaseYear.index(year)])
          MVvotesByYear[year].append(MVscore[MVreleaseYear.index(year)])
    else:
        MVTitleByYear[year] = [MVtitle[MVreleaseYear.index(year)]]
        MVvotesByYear[year] = [MVscore[MVreleaseYear.index(year)]]
        MVUniqueYears[year] = {'Best_title':'','Worst_title':'','Best_number_of_scores':'','Worst_number_of_scores':''}
    title = MVtitle.pop(MVtitle.index(MVtitle[MVreleaseYear.index(year)]))
    number_of_votes = MVscore.pop(MVscore.index(MVscore[MVreleaseYear.index(year)]))
    years = MVreleaseYear.pop(MVreleaseYear.index(year))
    #if year == 2008:
    #print(title, number_of_votes,years)

for key in MVUniqueYears:
    MVUniqueYears[key]['Best_number_of_votes']=max(MVvotesByYear[key])
    MVUniqueYears[key]['Worst_number_of_votes']=min(MVvotesByYear[key])
    MVUniqueYears[key]['Best_title']=MVTitleByYear[key][MVvotesByYear[key].index(max(MVvotesByYear[key]))]
    MVUniqueYears[key]['Worst_title']=MVTitleByYear[key][MVvotesByYear[key].index(min(MVvotesByYear[key]))]
# print(MVTitleByYear)
# print(MVScoreByYear)

#print(MVUniqueYears[2008])

ref = db.reference('/Best_and_worst_genres_for_movies/')
ref.set(MVUniqueYears)

ref = db.reference('/Best_and_worst_genres_for_Tv_Shows/')
ref.set(TVUniqueYears)