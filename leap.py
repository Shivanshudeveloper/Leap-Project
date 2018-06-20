# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 06:02:00 2018

@author: Shivanshu
"""
# imports are here
import datetime

# Functions are define here
def file_input(x,y):
    with open("file_001_#name.txt","a")as f1:
        f1.write(x+" created on "+y+"\n")
        f1.close

def file_open(filename,date_time,Mode):
    with open("file_001_#name.txt","a")as f1:
        f1.write(filename+"open on"+date_time+" as "+Mode)

def file_open2(filename,date_time,Mode):
    with open("file_001_#name.txt","a")as f1:
        f1.write(filename+"open on"+date_time+" as "+Mode)
# ---------------------------------------------------        

print("Welcome\nLeap 1.0.0v\nAn approch to create a Object Oriented Data by using python")
print("and testing that file on MongoDB database.\n")
now = datetime.datetime.now()
date_now=str(now)


while True:
    print("Press 1 For JSON File\n")
    print("Press 2 For OOD in JSON File")
    user_input = str(input("-->>> "))
    # Choose your file format
    # In JSON Format
    if user_input=="1":
        while True:
            print("Press 1 For New File\n")
            print("Press 2 For Open File\n")
            print("Type --help for help\n")
            
            user_input2 = str(input("-->>> "))
            
            if user_input2=="1":
                user_input_filename = str(input("New File Name: "))
                #Function call for take records of file
                file_input(user_input_filename,date_now)
                
                with open(user_input_filename+".json","w")as f:
                    dist = str(input("Collection/Table Name: "))
                    d=dist
                    key = str(input("Topic Name: "))
                    value = str(input("Value: "))
                    dist={key:value}
                    # Code for JSON file is here
                    
                    
                    while True:
                        user_input_option = str(input("Continue Writting: Y/n"))
                        
                        if user_input_option=="Y":
                            key = str(input("Topic Name: "))
                            value = str(input("Value: "))
                            dist[key] = value
                            print(str(dist))
                            
                        
                        elif user_input_option=="n":
                            f.write("db."+d+".insert("+str(dist)+")\n")
                            f.close()
                            break
                        
                        
            elif user_input2=="quit()":
                break
            # Code for Opening the file
            elif user_input2=="2":
                user_input_filename2 = str(input("File Name: "))
                print("Do you want to Write or Read W/r") # Choose either read or write
                user_input_option2 = str(input("W/r "))

                if user_input_option2=="W":
                    with open(user_input_filename2+".json","a")as f:
                            dist = str(input("Collection/Table Name: "))
                            d=dist
                            key = str(input("Topic Name: "))
                            value = str(input("Value: "))
                            dist={key:value}
                            

                            while True:
                                # Check weather to continue or not
                                user_input_option3 = str(input("Continue Writting: Y/n"))
                                if user_input_option3=="Y":
                                    key = str(input("Topic Name: "))
                                    value = str(input("Value: "))
                                    dist[key] = value
                                    print(str(dist))

                                elif user_input_option3=="n":
                                    f.write("db."+d+".insert("+str(dist)+")\n")
                                    file_open(user_input_filename2,date_now,"Write Mode")
                                    f.close()
                                    break
                            
                        
                                

                            
                        
                elif user_input_option2=="r":
                    with open(user_input_filename2+".json","r")as f:
                        print(f.read())
                        file_open2(user_input_filename2,date_now,"Read Mode")
                        f.close()
                 

    elif user_input=="quit()":
        break

    # Object Oriented Database by JSON File
    elif user_input=="2":
        while True:
            print("Press 1 For New File\n")
            print("Press 2 For Open File\n")
            print("Type --help for help\n")
            
            user_input2 = str(input("-->>> "))
            
            if user_input2=="1":
                user_input_file_name = str(input("File Name: "))
                
                with open(user_input_file_name+".json","w")as f:
                    dist = str(input("Collection/Table Name: "))
                    d=dist
                    key = str(input("Topic Name: "))
                    value = str(input("Value: "))
                    # Conversion in Object Data format
                    key_formated1 = "Content:[{"+key+":{ "
                    value_formated1 = value+"}"
                    # Formated Values
                    dist = {key_formated1:value_formated1}

                    dist_str = str(dist)
                    dist_str = dist_str.replace("'","")
                    
                        
                    
                    # Code for OOD is here
                    while True:
                        user_input_option = str(input("Continue Writting: Y/n"))
                        
                        if user_input_option=="Y":
                            key = str(input("Topic Name: "))
                            value = str(input("Value: "))
                            key_formated2 = key+':{ '
                            value_formated2 = value+'}'
                            # Formated Values
                            dist[key_formated2] = value_formated2
                            dist_str2 = str(dist)
                            dist_str2 = dist_str2.replace("'","")
                            print(str(dist_str2))
                            
                        
                        elif user_input_option=="n":
                            f.write("db."+d+".insert("+str(dist)+")") # The change for Object Oriented Data is made here
                            break
                    
                
                
            
            
        
                            
                        
                    
                    
                    
                    
                    
