# ____________________________________________________________________________________________________________
# DICTIONARY = un-ordered, changeble, index
#_____________________________________________________________________________________________________________

#------------------------------------------------------------------------------------------------------------
# Making dictionary
#------------------------------------------------------------------------------------------------------------
# student = {"name":,"faarax","email":,"faarax@gmail.com","age":,78}
# # Qaabkaan kalena waa loo samayn karaa dictionary
# student = dict(name="faarax",email="faarax@gmail.com",age=78)

#------------------------------------------------------------------------------------------------------------
# #Accesing an item
#------------------------------------------------------------------------------------------------------------
# x = student ["email"]
# print(x) # Mid ogoow oo kan aad access garaynaysid key ayaa la yiraahda
# #habkaloo method loo adeegsanayana waa ay jirtaa 
# x = student.get("email")
# print(x)

#------------------------------------------------------------------------------------------------------------
#Changing an item 
#------------------------------------------------------------------------------------------------------------
# student = {"name":"faarax","age":78}
# student["name"] = "cismaan"
# print(student)

#------------------------------------------------------------------------------------------------------------
# Sidee loop, iteration ama dulmar loogu sameeyaa
#------------------------------------------------------------------------------------------------------------
# student = {"name":"faarax","email":"faarax@gmail.com","age":78}
# for x in student:
    
#     # print(x) # Halkaan waxaa la print gareynayaa VALUEGA. 
    
#     print(student[x]) # halkaan waxaa printi gareynayaa, KEYGA. 

#------------------------------------------------------------------------------------------------------------
# Printing both key and value
#------------------------------------------------------------------------------------------------------------

# student = {"name":"faarax","email":"faarax@gmail.com","age":78}
# for x, y in student.items():
#     print(x,y)
    
#------------------------------------------------------------------------------------------------------------
# Checking if an item is in the dictionary
#------------------------------------------------------------------------------------------------------------
# student = {"name":"faarax","email":"faarax@gmail.com","age":78}
# if "email" in student:
#     print("Yes")
# else:
#     print("No")

#------------------------------------------------------------------------------------------------------------
#Checking the length of the dictionary
#------------------------------------------------------------------------------------------------------------
# student = {"name":"faarax","email":"faarax@gmail.com","age":78}
# print(len(student)) # kadibna waxaa uu kuu soo saarayaa itemyada ku jira, kuwaasoo saddex ah waana NAME, EMAIL IYO AGE. 

#------------------------------------------------------------------------------------------------------------
# How to add an item to dictionary
#------------------------------------------------------------------------------------------------------------
'''
Tusaale : Waxaan rabnaa subject inaan ku darno.
'''
# student = {"name":"faarax","email":"faarax@gmail.com","age":78}
# student ["subject"] = "Programming"
# print(student)
#------------------------------------------------------------------------------------------------------------
# Removing item from a dictionar
#------------------------------------------------------------------------------------------------------------

# student = {"name":"faarax","email":"faarax@gmail.com","age":78}
# student.pop("age") # halkaan si aad  item usaartid keyga waa inaad gelisaa. 
# print(student)

# # Del
# student = {"name":"faarax","email":"faarax@gmail.com","age":78}
# del student # delete dictionary
# print(student)

# Clear= waxaa la adeegsadaa marka aad rabtid inaadan wax ba delet gareyn balse aad rabtid inaad in ka tirtirtid
# student = {"name":"faarax","email":"faarax@gmail.com","age":78}
# student.clear() # empty dictionary
# print("Student:",student)

#------------------------------------------------------------------------------------------------------------
# Making a nested 
#------------------------------------------------------------------------------------------------------------

student ={
    "student1":{
                "name":"faarax",
                "email":"faarax@gmail.com",
                "age":78,
                "Subject":"English",
                "enrolled":True
            },
    "student2":{
                "name":"Cali",
                "email":"Cali@gmail.com",
                "age":56,
                "subjects":"Math",
                "Enrolled":False
                
            }
} 

print(student) # Nestedku waxaa uu muhiim u yahay, markaad samaynaysid systemyada DATABASKEKA. 

