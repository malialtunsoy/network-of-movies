from imdb import IMDb
import xlsxwriter
import json

# create an instance of the IMDb class
ia = IMDb()

top = ia.get_top250_movies()

# get movies and cast
movie_cast = {}
for x in top[0:50]:
    movie = ia.get_movie(x.movieID)
    movie_cast[str(x)] = []
    for actor in movie.get('cast'):
        print(str(actor))
        movie_cast[str(x)].append(str(actor))

# write to xlsx file
workbook = xlsxwriter.Workbook('data/xlsx/movie_cast.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 0
for movie in movie_cast:
    worksheet.write(row, col, movie)
    for actor in movie_cast[movie]:
        row += 1
        worksheet.write(row, col, actor)
    row = 0
    col += 1

workbook.close()

# write to JSON file
with open('data/json/movie_cast_json.txt', 'w') as outfile:
    json.dump(movie_cast, outfile)