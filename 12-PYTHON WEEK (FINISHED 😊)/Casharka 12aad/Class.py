# Python = Object oriented programming language
'''
Object oriented waxaa la oran karaa in luuqadaan wax yaalaha ay ka koobantahay ay yihiin objects, Marka OBJECT waxaa uu leeyahay, PROPERTIES iyo METHODS.   

PROPERTIES:                     METHODS: Waa  
>Properties waa 
waxyaaluhuu leeyahay 
guriga sida; Midabka, 
Daaqadaha. 
                               >actions waa shay wax 
                               laga badali karo, sida 
                               nalka guriga. 


Marka waa OJECT ORIENTED, Classna Waa OBJECT Oriented, marka laba networking fiican ka dhexeeya weeye. 

'''

#Almost everything in python is object with properties and methods. 

#Class = Blueprint (Class waa naqshada, kadibna naqshadaas waxyaalle kale ayaad kasii samayn kartaa. )

# class person:
    #pass # pass waxaad adeegsanaysaa hadaad    rabtid functionka inaad dib uga soo laabatid. 
    # x = 5
# p1 = person()
# print(p1.x)

# Habkale oo INIT FUNCTION AH :
'''
Init waxaa loo soo gaabiyay Initialization.

Init marka loo yeerayo waa inaa function samaysid sida DEF.
'''

class Person:
    def __init__(self, name, age) :
        self.name=name
        self.age=age
        
#     def salaam(self): #Ereygaas selfi hadii la geliyo waxaa weeye, functionkaan waxaa uu xiriir la leeyahay Class. 
        
    #    print("Hello my name is " + self.name,)
       
       # Functionkaan method baa la dhahaa, badanaa waxaa uu ku jiraa Classeska. 
        
p1 = Person("Abdi",30)
# print(p1.name,p1.age)


#Marka functionkaas loo yeerayo waa in calaamadiisa() la raaciyo. 
# print(p1.salaam())

# Hoos sidaad uga jeedid none ayuu natusayaa, sababtuna wax kale ma ahee, waxaa weeye waxaan adeegsanay, FUNCTIONKA PRINT, Markaas printi waan iska bixin karnaa


#da'dada classka QOF ku jira hadaad rabtid inaad badashid waxaad
# p1.age = 32
# print(p1.age)

#Propety hadaad doonaysid inaad Masaxdid adeegso function la yiraahdo Del. 
# del p1.age
# print(p1.age)

#Class Class ku hoos jira, waxaa la dhahaa classkaas Inheritence, C

#Subclass/Parent-Child Class/Inheritance

'''
Dhaxlida ama Inheritance waxaa laga wadaa classkaan waxaa adeegsanayaa Classka aabaha ah waxyaabaha uu haysto, wixiisan waa uu ku darsanyaa. 

Sida arintaas ay udhacayso waxaa weeye, waxaad samaynaysaa FUNCTIONKA DEFAULTIGAA EE INIT. 
'''


class Student(Person):
    def __init__(self, name, age, graduationayear):
        super().__init__(name,age)
        self.graduationyear = graduationayear
    def welcome(self):
        print("Congratulation " , self.name , "Welcome to the class of " , self.graduationyear)
    # Markaa intaa kadib waxaa la samaynayaa INSTANCE OF STUDENT.
    
student1 = Student("faarax", 25, 2023)

# halkaan faaidadeeda waxaa weeye arday kale waaad ku dari kartaa. 

student2 = Student("Cismaab",22,2024)

student1.welcome()
student2.welcome()

#Initialition luuqadaha kale constructive baa loo yaqaanaa