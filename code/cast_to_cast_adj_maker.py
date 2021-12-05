import pandas as pd
import json
import xlsxwriter
import copy
import csv

df = pd.read_excel('data/xlsx/cast_list.xlsx')
cast = []
for actor in df["CAST"]:
    cast.append(actor)

movie_cast = {}
with open('data/json/movie_cast_json.txt') as json_file:
    data = json.load(json_file)
    movie_cast = data

empty_casts = {}

for actor in cast:
    empty_casts[actor] = 0

cast_to_cast = {}
for actor in cast:    
    cast_to_cast[actor] = copy.deepcopy(empty_casts)

for source in cast:
    for movie in movie_cast:
        if source in movie_cast[movie]:
            for target in cast:
                if (target in movie_cast[movie]) and (source != target):
                    cast_to_cast[source][target] = cast_to_cast[source][target] + 1

# write to xlsx file
workbook = xlsxwriter.Workbook('data/xlsx/cast_to_cast_adj.xlsx')
worksheet = workbook.add_worksheet()

row,col = 1,0
for actor in cast_to_cast:
    worksheet.write(row, col, actor)
    row+=1
row,col = 0,1
for actor in cast_to_cast:
    worksheet.write(row, col, actor)
    col+=1

row,col = 1, 1
for source_actor in cast:
    col = 1
    for target_actor in cast:
        worksheet.write(row, col, cast_to_cast[source_actor][target_actor])
        col+=1
    row+=1

workbook.close()

#csv write

source_to_target = {}
for actor in cast:    
    source_to_target[actor] = copy.deepcopy(empty_casts)

for source in cast:
    for target in cast:
        if source_to_target[target][source] == 0:
            source_to_target[source][target] = cast_to_cast[source][target]

f = open('data/csv/cast_to_cast.csv', 'w', newline='')
writer = csv.writer(f)
header=["Source", "Target", "Weight", "Label"]
writer.writerow(header)
for source_actor in cast:
    for target_actor in cast:
        if source_to_target[source_actor][target_actor]>0:
            line = [source_actor, target_actor , str(source_to_target[source_actor][target_actor]), str(source_to_target[source_actor][target_actor])]
            writer.writerow(line)
f.close()