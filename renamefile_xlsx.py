
import os

iskom = ".xlsx"
final = "_2.xlsx"

files = os.listdir()
    
    
for i in files:
    if(iskom in i):
        itog_name = i.replace(iskom, final)
        os.rename(i, itog_name)
        print("Переименован: ",i, " Новое имя: " ,itog_name)
