import data

def allMovie(arg):
    for i in range(len(arg)):
        name = arg[i]['name']
        for key in arg[i]:
            if key == "imdb" and arg[i][key] > 5.5:
                print(f"Movie: {name}\t\t imdb: {arg[i][key]}")
    
allMovie(data.movies)