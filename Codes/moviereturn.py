
#returning movie
def movie_return(MovieList):
    #list where all the movies returned are added
    Return = []
    counter = 0
    movie_id = input("Enter the ID of movie you are about to return:")
    for each in MovieList:
        if each[0] == movie_id.upper():#matching the id
            counter += 1
            #increasing the quantity by 1
            quantity =  int(each[3])
            each[3] = str(quantity+1)
            rent_days = 1
            while rent_days == 1:
                try:
                    days = int(input("Enter the number of days you have rented the movie:"))
                    M_return = []
                    for item in each:
                        M_return.append(item)
                    #Calculating fine
                    if days>10:
                        fine = (days-10)*(0.5*float(M_return[-1]))
                        fine = round(fine,2)
                    else:
                        fine = 0
                    M_return.append(str(days))
                    M_return.append(str(fine))
                    Return.append(M_return)
                    print(M_return)
                    print("You have successfully returned the movie.")
                    rent_days = 0
                except:
                    print("Try again")
    if counter == 0:
        print("The ID you've entered does not match with any of the movie ID.")
    return Return

                            
                            
                        
