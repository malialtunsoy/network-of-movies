import pandas as pd
import xlsxwriter
import csv

df = pd.read_excel('data/xlsx/movie_director.xlsx')
movie_director = {}
movies = df["Movie"]
directors = df["Director"]
for index in range(50):
    movie_director[movies[index]] = directors[index]

for movie in movie_director:
    print(movie, movie_director[movie])

non_duplicate_directors = list(dict.fromkeys(directors))
director_movie = {}
for director in non_duplicate_directors:
    directors_movies = []
    for movie in movie_director:
        if movie_director[movie] == director:
            directors_movies.append(movie)
    director_movie[director] = directors_movies
    print(director, directors_movies)

# write to xlsx file
workbook = xlsxwriter.Workbook('data/xlsx/movie_director_adj.xlsx')
worksheet = workbook.add_worksheet()

row = 1
col = 0
for movie in movies:
    worksheet.write(row, col, movie)
    row +=1

row = 0
col = 1
for director in non_duplicate_directors:
    worksheet.write(row, col, director)
    row += 1
    for movie in movies:
        if movie in director_movie[director]:
            worksheet.write(row, col, 1)
        else:
            worksheet.write(row, col, 0)
        row += 1
    col +=1
    row = 0

workbook.close()

# write to cast xlsx file
workbook = xlsxwriter.Workbook('data/xlsx/director_list.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 0
worksheet.write(row, col, "DIRECTOR")
row = 1
for director in non_duplicate_directors:
    worksheet.write(row, col, director)
    row +=1
workbook.close()

#csv write
f = open('data/csv/director_list.csv', 'w', newline='')
writer = csv.writer(f)
header=["Id","Label"]
writer.writerow(header)
for director in non_duplicate_directors:
    line = [director, director]
    writer.writerow(line)
f.close()
