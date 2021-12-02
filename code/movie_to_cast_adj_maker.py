import json
import xlsxwriter
import csv

movie_cast = {}
with open('data/json/movie_cast_json.txt') as json_file:
    data = json.load(json_file)
    movie_cast = data

cast = []

for movie in movie_cast:
    for actor in movie_cast[movie]:
        if actor not in cast:
            cast.append(actor)

cast_starring_count = {}
for actor in cast:
    cast_starring_count[actor] = 0

for movie in movie_cast:
    for actor in movie_cast[movie]:
        cast_starring_count[actor] += 1

cast_starring_more_than_ones = []
for actor in cast_starring_count:
    if cast_starring_count[actor] > 1:
        cast_starring_more_than_ones.append(actor)

print(len(cast_starring_more_than_ones))

# write to xlsx file
workbook = xlsxwriter.Workbook('data/xlsx/movie_cast_adj.xlsx')
worksheet = workbook.add_worksheet()

row = 1
col = 0
for movie in movie_cast:
    worksheet.write(row, col, movie)
    row +=1

row = 0
col = 1
for actor in cast_starring_more_than_ones:
    worksheet.write(row, col, actor)
    row += 1
    for movie in movie_cast:
        if actor in movie_cast[movie]:
            worksheet.write(row, col, 1)
        else:
            worksheet.write(row, col, 0)
        row += 1
    col +=1
    row = 0

workbook.close()

# write to cast xlsx file
workbook = xlsxwriter.Workbook('data/xlsx/cast_list.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 0
worksheet.write(row, col, "CAST")
row = 1
for actor in cast_starring_more_than_ones:
    worksheet.write(row, col, actor)
    row +=1
workbook.close()

#csv write
f = open('data/csv/cast_list.csv', 'w', newline='')
writer = csv.writer(f)
header=["Id","Label"]
writer.writerow(header)
for actor in cast_starring_more_than_ones:
    line = [actor, actor]
    writer.writerow(line)
f.close()