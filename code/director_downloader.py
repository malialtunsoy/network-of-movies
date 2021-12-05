from imdb import IMDb
import xlsxwriter
import json

# create an instance of the IMDb class
ia = IMDb()

top = ia.get_top250_movies()

# get movies and directors
movie_director = []
for x in top[0:50]:
    movie = ia.get_movie(x.movieID)
    director_name = ""
    if len(movie["directors"]) > 1:
        for director in movie["directors"]:
            director_name += director["name"] + "-"
        director_name = director_name[0:len(director_name)-1]
    else:
        director_name = movie["directors"][0]["name"]    
    movie_director.append((str(x), director_name))
    print((str(x), director_name)) #takes only one director
print(movie_director)

# write to xlsx file
workbook = xlsxwriter.Workbook('data/xlsx/movie_director.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write("A1", "Movie")
worksheet.write("B1", "Director")
row = 2
for mov_dir in movie_director:
    worksheet.write("A" + str(row), mov_dir[0])
    row += 1
row = 2
for mov_dir in movie_director:
    worksheet.write("B" + str(row), mov_dir[1])
    row += 1

workbook.close()

# write to JSON file
movies_directors = {}
for movie in movie_director:
    movies_directors[movie[0]] = movie[1]
with open('data/json/movie_director_json.txt', 'w') as outfile:
    json.dump(movies_directors, outfile)