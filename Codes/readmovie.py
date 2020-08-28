#opening, reading and converting file to 2d list
def readmovie():            #function to read file
    file = open("movies.txt","r") #opening movie.txt opened in read mode
    content = file.readlines()
    list_movie = []             #empty list is created
    for each in content:
        list_movie.append(each.split(","))#to add each elements in the empty list created
    file.close()                #closing the text file
    return list_movie



