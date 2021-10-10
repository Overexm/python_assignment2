from src import *

some_data = WebScrapper.getData()
print("Please choose")
print("1.With parameter")
print("2.Without")
check = input("Choose:")
if check == '1':
    curName = input("Enter currency name:")
    scrapper = WebScrapper.getDateByRequest(curName)
    for i in scrapper:
        print(i)
elif check == '2':
    for i in some_data:
        print(i)