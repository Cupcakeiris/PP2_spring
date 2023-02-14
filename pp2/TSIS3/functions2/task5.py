import data

def catMovie(arg, x):
    lst = []
    for i in range(len(arg)):
        for key in arg[i]:
            if key == "imdb":
                imdb = arg[i][key]
            if key == "category" and arg[i][key] == x:
                lst.append(imdb)
    return lst

def average(arg):
    sum = 0
    for i in arg:
        sum+=i
    print(sum/len(arg))
    

x = input("Input category name: ")
average(catMovie(data.movies, x))