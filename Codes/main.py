#importing modules
from display_list import display_list
from readmovie import readmovie
from movie_rent import rent_movie
from moviereturn import movie_return
import rent_note
import return_note


#capturing 2D list in a variable
MovieList = readmovie()

#creating global variable list for adding movies that customer rents and returns
rent_list = []
return_list = []
 
#============================Welcome Message==================================#
print("\t \t Welcome to Movie Rental Store \t \t")
customer_name = str(input("Please enter your name:"))
print ("\t \t WELCOME!!"+ customer_name+ "\t \t")

#=============================Display Option==================================#
print(""" \t\t
================================MOVIE RENTAL MENU==============================
                               1. Movies available.
                               2. Rent a movie.
                               3. Return a movie.
                               4. Exit
===============================================================================""")
success = True
while success ==True :
        option = int(input("Hello "+customer_name+", please enter a number:"))
        print('\n')
        if option == 1:
            print ("These are the movies we have:")
            display_list(MovieList)
        elif option == 2:
            display_list(MovieList)
            rent_list = rent_movie(MovieList)
            print(rent_list)
        elif option == 3:
            display_list(MovieList)
            return_list = movie_return(MovieList)
            print(return_list)
        elif option == 4:
            if len(rent_list)>0:
                rent_note.update(MovieList)
                rent_note.rent_note(rent_list,customer_name)
                    
            if len(return_list)>0:
                return_note.update(MovieList)
                return_note.return_note(customer_name,return_list)       
            success = False
            exit() 
        else:
            print("Invalid input. Choose a number between 1 to 4 ")
    
        
