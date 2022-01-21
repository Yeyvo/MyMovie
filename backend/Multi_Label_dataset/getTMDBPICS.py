import wget
import pandas as pd
import urllib, json
from tqdm.auto import tqdm
import os

#https://api.themoviedb.org/3/find/tt0458290?api_key=38822594572ba49838eb67eec9246d29&external_source=imdb_id



def genreIdToStr( id):
    if(id == 28):
        return 'Action'
    elif(id == 12):
        return 'Adventure'
    elif(id == 16):
        return 'Animation'
    elif(id == 35):
        return 'Comedy'
    elif(id == 80):
        return 'Crime'
    elif(id == 99):
        return 'Documentary'
    elif(id == 18):
        return 'Drama'
    elif(id == 10751):
        return 'Family'
    elif(id == 14):
        return 'Fantasy'
    elif(id == 36):
        return 'History'
    elif(id == 27):
        return 'Horror'
    elif(id == 10402):
        return 'Music'
    elif(id == 9648):
        return 'Mystery'
    elif(id == 10749):
        return 'Romance'
    elif(id == 878):
        return 'Science Fiction'
    elif(id == 10770):
        return 'TV Movie'
    elif(id == 53):
        return 'Thriller'
    elif(id == 10752):
        return 'War'
    elif(id == 37):
        return 'Western'
    else:
        return 'N/A'

def UpdateDataSet():
    movie_id_arr = []
    movie_title_arr = []
    Action = []
    Adventure = []
    Animation = []
    Biography = []
    Comedy = []
    Crime = []
    Documentary = []
    Drama = []
    Family = []
    Fantasy = []
    History = []
    Horror = []
    Music = []
    Musical = []
    Mystery = []
    NA = []
    News = []
    RealityTV = []
    Romance = []
    SciFi = []
    Short = []
    Sport = []
    Thriller = []
    War = []
    Western = []


    imgFolderCacheName = "PosterCache"
    if not os.path.exists(imgFolderCacheName):
        os.makedirs(imgFolderCacheName)

    imgFolderCacheName = os.getcwd()+"\\" + imgFolderCacheName
    # imgFolderCacheName = imgFolderCacheName.replace("\\", "/")
    basePosterURL = "https://image.tmdb.org/t/p/w370_and_h556_bestv2"
    ApiKey = "38822594572ba49838eb67eec9246d29"

    baseUrl = "https://api.themoviedb.org/3/movie/top_rated?api_key=38822594572ba49838eb67eec9246d29&page="
    region = "&language=en-US&region=US"
    for page in tqdm(range(1,479)):
        url = baseUrl + str(page) + region
        response = urllib.request.urlopen(url)
        status_code = response.getcode()
        if (status_code == 404):
            print("Error opening page ", page)
        elif (status_code == 200):
            response = response.read()
            resp_dict = json.loads(response.decode('utf-8'))
            for data in resp_dict["results"]:
                movie_id_arr.append(data["id"])
                movie_title_arr.append(data["title"])
                wget.download(basePosterURL + data.get('poster_path') , out=imgFolderCacheName + '/' +str(data["id"])+ ".png" )
                genre = list(map(genreIdToStr, data['genre_ids']))
                GenreList = genre
                if "Action" in genre:
                    Action.append(1)
                else:
                    Action.append(0)
                if "Adventure" in genre:
                    Adventure.append(1)
                else:
                    Adventure.append(0)
                if "Animation" in genre:
                    Animation.append(1)
                else:
                    Animation.append(0)
                if "Biography" in genre:
                    Biography.append(1)
                else:
                    Biography.append(0)
                if "Comedy" in genre:
                    Comedy.append(1)
                else:
                    Comedy.append(0)
                if "Crime" in genre:
                    Crime.append(1)
                else:
                    Crime.append(0)
                if "Documentary" in genre:
                    Documentary.append(1)
                else:
                    Documentary.append(0)
                if "Drama" in genre:
                    Drama.append(1)
                else:
                    Drama.append(0)
                if "Family" in genre:
                    Family.append(1)
                else:
                    Family.append(0)
                if "Fantasy" in genre:
                    Fantasy.append(1)
                else:
                    Fantasy.append(0)
                if "History" in genre:
                    History.append(1)
                else:
                    History.append(0)
                if "Horror" in genre:
                    Horror.append(1)
                else:
                    Horror.append(0)
                if "Music" in genre:
                    Music.append(1)
                else:
                    Music.append(0)
                if "Musical" in genre:
                    Musical.append(1)
                else:
                    Musical.append(0)
                if "Mystery" in genre:
                    Mystery.append(1)
                else:
                    Mystery.append(0)
                if "N/A" in genre:
                    NA.append(1)
                else:
                    NA.append(0)
                if "News" in genre:
                    News.append(1)
                else:
                    News.append(0)
                if "Reality-TV" in genre:
                    RealityTV.append(1)
                else:
                    RealityTV.append(0)
                if "Romance" in genre:
                    Romance.append(1)
                else:
                    Romance.append(0)
                if "Sci-Fi" in genre:
                    SciFi.append(1)
                else:
                    SciFi.append(0)
                if "Short" in genre:
                    Short.append(1)
                else:
                    Short.append(0)
                if "Sport" in genre:
                    Sport.append(1)
                else:
                    Sport.append(0)
                if "Thriller" in genre:
                    Thriller.append(1)
                else:
                    Thriller.append(0)
                if "War" in genre:
                    War.append(1)
                else:
                    War.append(0)
                if "Western" in genre:
                    Western.append(1)
                else:
                    Western.append(0)
    movieDf = pd.DataFrame({
        "MoviesId": movie_id_arr,
        "Title": movie_title_arr,
        "GenreList": GenreList,
        "Action": Action,
        "Adventure": Adventure,
        "Animation": Animation,
        "Biography": Biography,
        "Comedy": Comedy,
        "Crime": Crime,
        "Documentary": Documentary,
        "Drama": Drama,
        "Family": Family,
        "Fantasy": Fantasy,
        "History": History,
        "Horror": Horror,
        "Music": Music,
        "Musical": Musical,
        "Mystery": Mystery,
        "N/A": NA,
        "News": News,
        "Reality-TV": RealityTV,
        "Romance": Romance,
        "Sci-Fi": SciFi,
        "Short": Short,
        "Sport": Sport,
        "Thriller": Thriller,
        "War": War,
        "Western": Western,
    })
    print('--------- Download Complete CSV Formed --------')

    movieDf.to_csv('train.csv', index=False)

    print('--------- Download Images ----------------')


    getStatistics()



def UpdateDataImages():


    df = pd.read_csv("train.csv")

    moviesId = df.MoviesId.to_list()
    imgFolderCacheName = "PosterCache"
    if not os.path.exists(imgFolderCacheName):
        os.makedirs(imgFolderCacheName)

    imgFolderCacheName = os.getcwd()+"\\" + imgFolderCacheName
    # imgFolderCacheName = imgFolderCacheName.replace("\\", "/")
    basePosterURL = "https://image.tmdb.org/t/p/w370_and_h556_bestv2"
    ApiKey = "38822594572ba49838eb67eec9246d29"
    NoPosters = []

    for i in tqdm(range(len(moviesId))):
        if(not os.path.exists(imgFolderCacheName + '/' +str(moviesId[i])+ ".png")) : 
            poster_url = "https://api.themoviedb.org/3/find/"+str(moviesId[i])+"?api_key="+ApiKey+"&external_source=imdb_id"
            urlFile = urllib.request.urlopen(poster_url).read()
            # print(URLFILE)
            resp_dict = json.loads(urlFile)
            if(len(resp_dict["movie_results"])>0):
                linkdata = resp_dict.get("movie_results")[0].get('poster_path')
                if(linkdata is None):
                    print("\n Movie Poster not Found (None) : " + str(moviesId[i]))
                    NoPosters.append(moviesId[i])
                    df.drop(index=i, axis=0, inplace=True)
                else :
                    poster_filename = wget.download(basePosterURL + linkdata , out=imgFolderCacheName + '/' +str(moviesId[i])+ ".png" )
                    
                # os.rename(poster_filename, imgFolderCacheName +'/' + moviesId[i]+ '.png')
                # print(poster_filename)
            else:
                print("\n Movie not found : " + str(moviesId[i]))
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
    movie_list = [i.replace(']','').replace('[','').replace('\'','').replace(" ","").split(",") for i in movie["GenreList"]]
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

UpdateDataSet()
