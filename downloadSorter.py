#!/usr/bin/env python
import shutil
import os
import time

'''
Sorts all files in your downloads folder into different folders for different file types
'''

file_types = [".docx", ".exe", ".folder", ".gif", ".jar", ".jpg", ".mp3", ".mp4",
              ".pdf", ".png", ".py", ".rar", ".txt", ".zip"] #these are the different folders that are avaliable to be sorted into
                                                             #name the folders after these without the "."
count = 0
total = 0
found = []
last_percentage = 0
destination =  ("E:\\Downloads\\sorted\\") #the folder where the file type folders are
source = os.listdir("E:\\Downloads\\") #your downloads file dir
number_of_files = len(source)

while True: #option to choose if the dir needs to sorted once, or every 1 second
    try:
        print("Live Sort (0) or 1 time sort (1)")
        operation = int(input(""))
        if operation == 1 or operation == 0:
            break
        else:
            print("Thats not an option")
    except ValueError:
        print("Thats not a number")

if operation == 1: #one time sort
    for file in source:
        known = False
        file_source = "E:\\Downloads\\" + file
        for typ in file_types: 
            if file.endswith(typ): #if a match is found, the file is moved to its category using shutil.copy
                count += 1
                known = True
                found.append(typ)
                typ = typ.replace(".", "")
                acc_destination = destination + typ + "\\"
                shutil.copy(file_source, acc_destination)
                
        if os.path.isdir(file_source) and file != "sorted": #if its not a file but a folder, its moved to the folder category
            count += 1
            acc_destination = destination + "folder" + "\\" + file
            try:
                shutil.copytree(file_source, acc_destination)
            except FileExistsError:
                print("File exsists already")
                
        elif known == False: #otherwise its moved to the unknown file type folder, eg WAV files
            acc_destination = destination + "unknown" + "\\"
            try:
                shutil.copy(file_source, acc_destination)
            except:
                pass
            count += 1

        total += 1
        percentage = round((total / number_of_files) * 100)
        
        if (percentage % 1) == 0 and percentage != 0 and percentage != last_percentage: #prints its progress in the operation
            last_percentage = percentage
            print(str(percentage) + "%")

else: #for live sort
    
    while True: #endless loop
        source = os.listdir("E:\\Downloads\\")
        source.remove("desktop.ini")
        source.remove("sorted")
        number_of_files = len(source)
        if number_of_files > 0: #if theres a file in the dir
            for file in source:
                known = False
                file_source = "E:\\Downloads\\" + file
                for typ in file_types: #if its a valid file type its moved to the correct folder, as long as it doesnt already exsist
                    if file.endswith(typ): 
                        known = True
                        found.append(typ)
                        typ = typ.replace(".", "")
                        acc_destination = destination + typ + "\\"
                        try:
                            shutil.move(file_source, acc_destination)
                            print("Normal File Moved -", file)
                        except shutil.Error:
                            print("File exsists already")

                if os.path.isdir(file_source) and file != "sorted": #if its a folder its moved to the folder folder
                    acc_destination = destination + "folder" + "\\" + file
                    try:
                        if file == "sorted":
                            print("ffs2")
                        shutil.move(file_source, acc_destination)
                        print("Folder Moved -", file)
                    except FileExistsError:
                        print("File exsists already")
                elif known == False and file != "desktop.ini" and file != "sorted": #if its unknown and its not the hidden desktop.ini file its moved to unknown
                    acc_destination = destination + "unknown" + "\\"
                    try:
                        shutil.move(file_source, acc_destination)
                        print("Unknown File Moved -", file)
                    except shutil.Error:
                        print("File exsists already")       
        time.sleep(1) #time between scans
