import requests
from bs4 import BeautifulSoup
from dateutil.parser import parse
import concurrent.futures
import pandas as pd


# Maximum number of threads that will be spawned
MAX_THREADS = 50


movie_title_arr = []
movie_year_arr = []
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

movie_synopsis_arr =[]
image_url_arr  = []
image_id_arr = []

def getMovieTitle(header):
    try:
        return header[0].find("a").getText()
    except:
        return 'NA'

def getReleaseYear(header):
    try:
        return header[0].find("span",  {"class": "lister-item-year text-muted unbold"}).getText()
    except:
        return 'NA'

def getGenre(muted_text):
    try:
        return muted_text.find("span",  {"class":  "genre"}).getText()
    except:
        return 'NA'

def getsynopsys(movie):
    try:
        return movie.find_all("p", {"class":  "text-muted"})[1].getText()
    except:
        return 'NA'

def getImage(image):
    try:
        return image.get('loadlate')
    except:
        return 'NA'

def getImageId(image):
    try:
        return image.get('data-tconst')
    except:
        return 'NA'


def main(imdb_url):
    response = requests.get(imdb_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Movie Name
    movies_list = soup.find_all("div", {"class": "lister-item mode-advanced"})

    for movie in movies_list:
        header = movie.find_all("h3", {"class": "lister-item-header"})
        muted_text = movie.find_all("p", {"class": "text-muted"})[0]
        imageDiv = movie.find("div", {"class": "lister-item-image float-left"})
        image = imageDiv.find("img", "loadlate")

        #  Movie Title
        movie_title = getMovieTitle(header)
        movie_title_arr.append(movie_title)

        #  Genre  of movie
        genre = getGenre(muted_text)
        if "Action" in genre:
            Action.append(1)
        else :
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

        image_id = image.get('data-tconst')
        image_id_arr.append(image_id)

# An array to store all the URL that are being queried
imageArr = []

# Maximum number of pages one wants to iterate over
MAX_PAGE =51

# Loop to generate all the URLS.
for i in range(0,MAX_PAGE):
    totalRecords = 0 if i==0 else (250*i)+1
    print(totalRecords)
    imdb_url = f'https://www.imdb.com/search/title/?release_date=2020-01-02,2021-02-01&user_rating=4.0,10.0&languages=en&count=250&start={totalRecords}&ref_=adv_nxt'
    imageArr.append(imdb_url)

def download_stories(story_urls):
    threads = min(MAX_THREADS, len(story_urls))
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(main, story_urls)

# Call the download function with the array of URLS called imageArr
download_stories(imageArr)

# Attach all the data to the pandas dataframe. You can optionally write it to a CSV file as well
movieDf = pd.DataFrame({
    "image_id": image_id_arr,
    "Title": movie_title_arr,
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

movieDf.to_csv('NewDataset.csv', index=False)
movieDf.head()



