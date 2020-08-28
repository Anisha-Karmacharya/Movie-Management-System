#list where all the movies chosed by customer is added
#program to rent the movie
def rent_movie(MovieList): #function created to rent movie
    M_cart = [] # empty list is created
    counter = 0
    a = "y"
    while a == "y":
        movie_id = input("Enter the ID of movie you would like to rent:")
        for each in MovieList:
            if movie_id.upper() == each[0]: # checking the movie id
                counter+=1
                if int(each[3])>0: #checking the quantity of movies 
                    cart = []
                    quantity =  int(each[3])
                    each[3] = str(quantity-1) # decrease the value of the movie
                    cart.append(each)
                    for each in cart:
                        M_cart.append(each)
                        print (M_cart)
                        print("You,ve successfully rented the movie.")
                else:
                    print("Sorry , the movie is out of stock")
        if counter == 0:
            print("Invalid movie ID  !!!")
        a = input("Do you wanna add next movie:(y/n)")
    return(M_cart)
