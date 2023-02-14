import data

def singleMovie(arg, x):
    index = 0
    for i in range(len(arg)):
        if arg[i]['name'] == x:
            index = i
            break
    
    for key in arg[index]:
        if key == "imdb" and arg[i][key] > 5.5:
            print( True)
            return 0
    print (False)
    return 0
    
x = input("Input movie name: ")
singleMovie(data.movies, x)