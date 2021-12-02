from imdb import IMDb
import xlsxwriter

# create an instance of the IMDb class
ia = IMDb()

top = ia.get_top250_movies()

# get movies and directors
movie_director = []
for x in top[0:50]:
    movie = ia.get_movie(x.movieID)
    movie_director.append((str(x), movie["directors"][0]["name"]))
    print((str(x), movie["directors"][0]["name"])) #takes only one director
print(movie_director)

# write to xlsx file
workbook = xlsxwriter.Workbook('data/xlsx/movie_director.xlsx')
worksheet = workbook.add_worksheet()

row = 2
for mov_dir in movie_director:
    worksheet.write("A" + str(row), mov_dir[0])
    row += 1

for mov_dir in movie_director:
    worksheet.write("B" + str(row), mov_dir[1])
    row += 1

workbook.close()