import wget
import pandas as pd
import urllib, json
from tqdm.auto import tqdm
import os

#https://api.themoviedb.org/3/find/tt0458290?api_key=38822594572ba49838eb67eec9246d29&external_source=imdb_id

imgFolderCacheName = "PosterCache"

def UpdateDataImages():
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


def getStatistics(): #to run on localMachine 

    import numpy as np
    import matplotlib.pyplot as plt
    ''' Set up dataframe Display the data '''
    # Show Dateframe All right 
    pd.set_option('display.max_rows',None)
    # Show Dateframe All columns ( Parameter set to None Represents the display of all lines , You can also set your own number )
    pd.set_option('display.max_columns',None)
    # Set up Dataframe Display length of data , The default is 50
    pd.set_option('max_colwidth',200)
    # prohibit Dateframe Word wrap ( Set to Flase Don't wrap ,True conversely )
    pd.set_option('expand_frame_repr', False)

    movie = pd.read_csv('train.csv')
    movie_list = [i.replace(']','').replace('[','').replace('\'','').replace(" ","").split(",") for i in movie["Genre"]]
    single_movie_list = [j for i in movie_list for j in i]
    #2、 Then we need to know how many different kinds of movies there are , Then de duplicate the whole list 
    fin_movie_list = np.unique(single_movie_list)
    print(fin_movie_list)
    #3、 We generate a two-dimensional matrix to store statistical information , The number of rows is the total number of rows of data , Columns represent different kinds of movie names ,i That's ok j The column represents i Has the row ever appeared j Columns of data 
    zeros_matrix = np.zeros([movie.shape[0], fin_movie_list.shape[0]])
    data_matrix = pd.DataFrame(zeros_matrix, columns=fin_movie_list)
    # Traverse movie_list Get the movie name of each line of the original data 
    # Add... To the corresponding movie name in the corresponding position 1, Count the number of times 
    for i in range(len(movie.Id.to_list())):
        # str_list = movie_list[i]
        data_matrix.loc[i, movie_list[i]] = 1

    #4、 Sum each column of the matrix , Get the total number of times each movie appears , And then sort it 
    genre = data_matrix.sum().sort_values(ascending=True)
    # print(genre)
    genre.plot(kind="bar", colormap="cool", figsize=(30, 15), fontsize=16)

    # genre.plot(kind="bar", colormap="cool", figsize=(30, 15), fontsize=16)

    plt.show()

# getStatistics()

