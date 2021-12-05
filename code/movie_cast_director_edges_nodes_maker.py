import json
import csv

movie_cast_director = {}
with open('data/json/movie_cast_director_json.txt') as json_file:
    data = json.load(json_file)
    movie_cast_director = data
print(movie_cast_director)

#csv write
#node list
f = open('data/csv/movie_cast_dir_list.csv', 'w', newline='')
writer = csv.writer(f)
header=["Id","Label","Genre"]
writer.writerow(header)
for movie in movie_cast_director:
    line = [movie, movie, "movie"]
    writer.writerow(line)
directors = []
for movie in movie_cast_director:
    if movie_cast_director[movie]["director"] not in directors:
        directors.append( movie_cast_director[movie]["director"])
cast = []
for movie in movie_cast_director:
    for actor in movie_cast_director[movie]["cast"]:
        if actor not in cast:
            cast.append(actor)
actor_and_director = []
for director in directors:
    if director in cast:
        actor_and_director.append(director)
        cast.remove(director)
        directors.remove(director)
for director in directors:
    line = [director, director, "director"]
    writer.writerow(line)
for act_dir in actor_and_director:
    line = [act_dir, act_dir, "actor-director"]
    writer.writerow(line)
for actor in cast:
    line = [actor, actor, "actor"]
    writer.writerow(line)
f.close()

# edge list
f = open('data/csv/movie_director_cast_edges.csv', 'w', newline='')
writer = csv.writer(f)
header=["Source", "Target", "Weight"]
writer.writerow(header)
for movie in movie_cast_director:
    line = [movie, movie_cast_director[movie]["director"] , "1"]
    writer.writerow(line)
for movie in movie_cast_director:
    for actor in movie_cast_director[movie]["cast"]:
        if actor != movie_cast_director[movie]["director"]:
            line = [movie, actor , "1"]
            writer.writerow(line)
f.close()