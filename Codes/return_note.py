#updating 2D list
def update(MovieList):
    counter = 0
    f= open("movies.txt","w")
    for each in MovieList:
        if counter==0:
            f.write(each[0]+','+each[1]+','+each[2]+','+each[3])
            counter+=1
        else:
            f.write(each[0]+','+each[1]+','+each[2]+','+each[3]) 
    f.close()

#return note
from random import randint
import datetime

def return_note(customer_name,return_list):
    ran = str(randint(1,1000))
    fr = open(ran+"returnnote.txt","w")
    fr.write("------------------------------------------------------------------------------")
    fr.write("\n")
    fr.write("\t\t\t\t Movie Rental Store \n\n")
    fr.write("-----------------------------------------------------------------------------")
    fr.write("\n")
    fr.write("Customer Name:"+customer_name)
    fr.write('\t\t')
    date_time = datetime.datetime.now()
    fr.write(str(date_time))
    fr.write("\n")
    fr.write("--------------------------------------------------------------------")
    fr.write("\n")
    fr.write("Movie ID\t Movie Name\tPrice\tDays\tFine\t")
    fr.write("\n")
    for r in return_list:
        fr.write(r[0]+"\t\t"+r[1]+"\t"+r[2]+"\t"+r[-2]+"\t$"+r[-1])
        fr.write("\n")
        fr.write("------------------------------------------------------------------------------")
        fr.write("\n")
    # To calculate sum of price and fine
    total = 0.0
    for a in return_list:
        cal_fine =float(a[-1])
        cal_price = float(a[-3])
        total = total+cal_fine+cal_price
    total = round(total,2)
    fr.write("\n")
    fr.write("Grand Total:$")
    fr.write(str(total))
    fr.close()
    

        
       
