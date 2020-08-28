#to display the list of movie available to customer
def display_list(details):       # creating function to display list
    print("------------------------------------------------------------------------------")
    print("Movie ID\tName of Movies\t\t\tPrice\t\t\tquantity") #Displays the given heading 
    print("==============================================================================")
    for m in details:
        print(m[0],"\t\t",m[1],"\t\t\t",m[2],"\t\t\t",m[3]) #Displays the respective data from index
    print('\n')
    print("------------------------------------------------------------------------------")
