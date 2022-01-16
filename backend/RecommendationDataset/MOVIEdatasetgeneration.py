import wget
import pandas as pd
import urllib, json
from tqdm.auto import tqdm
import os
import urllib.parse

#https://api.themoviedb.org/3/find/tt0458290?api_key=38822594572ba49838eb67eec9246d29&external_source=imdb_id



def UpdateDataset():
    # if not os.path.exists(imgFolderCacheName):
    #     os.makedirs(imgFolderCacheName)



    df = pd.read_csv("movies2.csv")
    newdf = pd.DataFrame(columns=['id','name' ,'rating' ,'genre' ,'year' ,'director', 'star','company' ,'runtime'])

    moviesNames = df.name.to_list()
    for i in tqdm(range(len(moviesNames))):
        ApiKey = "38822594572ba49838eb67eec9246d29"
        # print("\n########"+df.loc[df['name'] == moviesNames[i]]['year'].astype(str)[0]+"\n")
        url = "https://api.themoviedb.org/3/search/movie?api_key="+ApiKey+"&query="+urllib.parse.quote(moviesNames[i])+"&page=1&year="+str(df.loc[df['name'] == moviesNames[i]]['year'].values[0])
        response = urllib.request.urlopen(url)
        status_code = response.getcode()
        if(status_code == 404):
            print("\n movie not found :  " + moviesNames[i])
        elif(status_code == 200):
            response = response.read()
            resp_dict = json.loads(response.decode('utf-8'))
            try:
                movieData = resp_dict["results"][0]
                tosaveData = {}
                tosaveData['id'] = movieData['id']
                tosaveData['name'] = moviesNames[i]
                tosaveData['rating'] = df.loc[df['name'] == moviesNames[i]]['rating'].values[0]
                tosaveData['genre'] = df.loc[df['name'] == moviesNames[i]]['genre'].values[0]
                tosaveData['year'] = df.loc[df['name'] == moviesNames[i]]['year'].values[0]
                tosaveData['director'] = df.loc[df['name'] == moviesNames[i]]['director'].values[0]
                tosaveData['star'] = df.loc[df['name'] == moviesNames[i]]['star'].values[0]
                tosaveData['company'] = df.loc[df['name'] == moviesNames[i]]['company'].values[0]
                tosaveData['runtime'] = df.loc[df['name'] == moviesNames[i]]['runtime'].values[0]
                newdf = newdf.append(tosaveData,ignore_index=True)
            except IndexError:
                print("\n movie not found :  " + moviesNames[i])
            if(i%50 == 0):
                newdf = newdf.dropna(axis = 0, how ='any')
                newdf.to_csv('new-movies.csv', index=False)

    newdf.to_csv('new-movies.csv', index=False)




# UpdateDataset()

def dropCol():
    # if not os.path.exists(imgFolderCacheName):
    #     os.makedirs(imgFolderCacheName)



    df = pd.read_csv("new-movies.csv")
    df.drop('name',axis=1, inplace=True)
    df.to_csv("new-movies.csv", index = False)

# dropCol()