import requests
from bs4 import BeautifulSoup
import csv


result = requests.get("https://pmg.org.za/hansards/?filter%5Byear%5D=2019&filter%5Bhouse_id%5D=3")
src = result.content
soup = BeautifulSoup(src, 'lxml')

#find the div container which holds the element
results = soup.find_all("div",{"class":"hansard-stub"})

# write to file
filename = "task1hansard1.csv"
f = open(filename,"w")

headers= "hansard_number, hansard_name, hansard_date\n"

f.write(headers)

 # loop through  the webpage 
for result in results:   
    
    hansard_number = result.h4.a["href"]
    print(hansard_number) 
    
    hansard_name = result.h4.a.text
    print(hansard_name)
    
    hansard_date = result.div.text
    print(hansard_date)

    print()

    f.write(hansard_number +"," + hansard_name + "," + hansard_date +"\n")
f.close()  
