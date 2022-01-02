import sqlite3

#connecter à la base de données
conn=sqlite3.connect('movies.db')
print ("Opened database successfully")

#créer un curseur
cur=conn.cursor()

#supprimer la table si elle existe
cur.execute('DROP TABLE IF EXISTS movies_list')

#créer la table
cur.execute('''
    CREATE TABLE movies_list(
    
    movie_title text,
    released_year INTEGER,
    runtime text,
    genre text,
    rating real,
    overview text,
    director text,
    star text,
    no_vote INTEGER,
    id_movies INTEGER

)''')
print ("Table created successfully")

#insérer des valeurs dans la table movies_list

movie_list=[
    ('The Shawshank Redemption',1994,'142 min','Drama',9.3,'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.','Frank Darabont','Tim Robbins',28341469,1),
    ('The Godfather',1972,'175 min','Crime, Drama',9.2,"An organized crime dynasty's aging patriarch transfers control of his clandestine empire to his reluctant son.",'Francis Ford Coppola','Marlon Brando',134966411,2),
    ('The Dark Knight',2008,'152 min','Action, Crime, Drama',9,'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.','Christopher Nolan','Christian Bale',53858444,3),
    ('The Godfather: Part II',1974,'202 min','Crime, Drama',9,'The early life and career of Vito Corleone in 1920s New York City is portrayed, while his son, Michael, expands and tightens his grip on the family crime syndicate.','Francis Ford Coppola','Al Pacino',57300000,4),
    ('12 Angry Men',1957,'96 min','Crime, Drama',9,'A jury holdout attempts to prevent a miscarriage of justice by forcing his colleagues to reconsider the evidence.','Sidney Lumet','Henry Fonda',436000,5),
    ('The Lord of the Rings: The Return of the King',2003,'201 min','Action, Adventure, Drama',8.9,"Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.",'Peter Jackson','Elijah Wood',642758,6),
    ]

cur.executemany("INSERT INTO movies_list VALUES (?,?,?,?,?,?,?,?,?,?)",movie_list)
print("insertion accomplie")

#cur.execute("select * from movies_list")
#print(cur.fetchall())

#commit notre commande
conn.commit()

#fermer la connection
conn.close()

