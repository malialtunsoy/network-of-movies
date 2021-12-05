import json
import csv
import copy

movie_cast_director = {}
with open('data/json/movie_cast_director_json.txt') as json_file:
    data = json.load(json_file)
    movie_cast_director = data

directors_cast = {}
for movie in movie_cast_director:
    directors_cast[movie_cast_director[movie]["director"]] = []

for movie in movie_cast_director:
    for actor in movie_cast_director[movie]["cast"]:
        if actor not in directors_cast[movie_cast_director[movie]["director"]]:
            directors_cast[movie_cast_director[movie]["director"]].append(actor)

empty_directors = {}
for director in directors_cast:
    empty_directors[director] = 0
director_to_director = {}

for director in directors_cast:
    director_to_director[director] = copy.deepcopy(empty_directors)

for target_director in directors_cast:
    for source_director in directors_cast:
        if source_director != target_director:
            for actor in directors_cast[target_director]:
                if actor in directors_cast[source_director]:
                    director_to_director[source_director][target_director] += 1

print(director_to_director)
print(len(director_to_director))
print(director_to_director)
directors = []
for director in directors_cast:
    directors.append(director)        

#csv write
# edge list
f = open('data/csv/director_edges.csv', 'w', newline='')
writer = csv.writer(f)
header=["Source", "Target", "Weight", "Label"]
writer.writerow(header)
for i in range(len(director_to_director)):
    for j in range(len(director_to_director)-i):
        if director_to_director[directors[i]][directors[j]] > 0:
            line = [directors[i], directors[j] ,director_to_director[directors[i]][directors[j]],director_to_director[directors[i]][directors[j]]]
            writer.writerow(line)
f.close()