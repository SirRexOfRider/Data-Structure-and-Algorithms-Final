import Library as Lib
import csv


#Open csv file and clean it
with open("books.csv", encoding = "utf-8") as f:
    
    #Read csv files and add them to a data list
    #Gets rid of the new lines
    reader = csv.reader(f)
    data = list(reader)
    
    data.pop(0)
    for x in range(len(data)):
        data[x].append(x + 1)
        
    print(len(data))
    
    
    
    
    

        




#Length of 1339060
#Horray for play should be the last book in database
LMS = Lib.Library(data)

#LINEAR SEARCH
print(f"TIME TAKEN FOR LINEAR: {LMS.Linear_search(1339060)}")

#BINARY
print(f"TIME TAKEN FOR BINARY: {LMS.Binary_search(1339060)}")

#BINARY SEARCH
print()