def update(MovieList):
    counter = 0
    f= open("movies.txt",'w')
    for each in MovieList:
        if counter==0:
            f.write(each[0]+','+each[1]+','+each[2]+','+each[3])
            counter+=1
        else:
            f.write('\n'+each[0]+','+each[1]+','+each[2]+','+each[3])
    f.close()

#rent note
from random import randint
import datetime
def rent_note(rent_list,customer_name):
    ran = str(randint(1,1000))
    fr = open(ran+"rentnote.txt","w")
    fr.write("\t\t  Movie Rental Store ")
    fr.write("\n")
    fr.write("Customer Name: "+customer_name)
    fr.write("\n")
    date_time = datetime.datetime.now()
    fr.write(str(date_time))
    fr.write("\n")
    fr.write("\n\n")
    fr.write("----------------------------------------------------------------------------")
    fr.write("\n")
    fr.write("Movie ID\t\tMovie Name\t\t\tPrice\n")
    print("\n\n")
    fr.write("----------------------------------------------------------------------------")
    fr.write("\n")
    for i in rent_list:
        fr.write(i[0]+"\t\t\t"+i[1]+"\t\t$"+i[2])
        fr.write("\n")
    fr.write("\n")
    fr.write("----------------------------------------------------------------------------")
    #variable to sum price of all the movies
    total=0.0
    for each_row in rent_list:
        a=float(each_row[2])
        total=float(total+a)
    fr.write("Grand Total: $")
    fr.write(str(total))
    fr.close()
    

