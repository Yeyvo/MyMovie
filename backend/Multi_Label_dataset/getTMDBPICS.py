import wget
import pandas as pd
import urllib, json
from tqdm.auto import tqdm
import os

#https://api.themoviedb.org/3/find/tt0458290?api_key=38822594572ba49838eb67eec9246d29&external_source=imdb_id

imgFolderCacheName = "PosterCache"


if not os.path.exists(imgFolderCacheName):
    os.makedirs(imgFolderCacheName)



df = pd.read_csv("train.csv")

moviesId = df.Id.to_list()
imgFolderCacheName = os.getcwd()+"\\PosterCache"
# imgFolderCacheName = imgFolderCacheName.replace("\\", "/")
basePosterURL = "https://image.tmdb.org/t/p/w370_and_h556_bestv2"
ApiKey = "38822594572ba49838eb67eec9246d29"
NoPosters = []

for i in tqdm(range(len(moviesId))):
    if(not os.path.exists(imgFolderCacheName + '/' +moviesId[i]+ ".png")) : 
        poster_url = "https://api.themoviedb.org/3/find/"+moviesId[i]+"?api_key="+ApiKey+"&external_source=imdb_id"
        urlFile = urllib.request.urlopen(poster_url).read()
        # print(URLFILE)
        resp_dict = json.loads(urlFile)
        if(len(resp_dict["movie_results"])>0):
            linkdata = resp_dict.get("movie_results")[0].get('poster_path')
            if(linkdata is None):
                print("\n Movie Poster not Found (None) : " + moviesId[i])
                NoPosters.append(moviesId[i])
                df.drop(index=i, axis=0, inplace=True)
            else :
                poster_filename = wget.download(basePosterURL + linkdata , out=imgFolderCacheName + '/' +moviesId[i]+ ".png" )
            # os.rename(poster_filename, imgFolderCacheName +'/' + moviesId[i]+ '.png')
            # print(poster_filename)
        else:
            print("\n Movie not found : " + moviesId[i])
            NoPosters.append(moviesId[i])
            df.drop(index=i, axis=0, inplace=True)
        # elif(len(resp_dict["movie_results"])>0):
        #     print()
    

# for i in tqdm(range(len(NoPosters))):
#     # df = df.drop(df.query("id == "+NoPosters[i]+"")).sample(frac=0.90).index)
#     # try:
#         df = df.drop([df.Id == NoPosters[i]].index, axis=0)
#     # except:
#     #     print("\n Problem With : " + NoPosters[i])
df.to_csv('new-train.csv', index=False)




# print(df)



