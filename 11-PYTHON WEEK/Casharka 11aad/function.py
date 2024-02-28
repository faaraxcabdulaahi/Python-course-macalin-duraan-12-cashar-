# Functionku shaqo ma qabanayo laakiin instructions ayaad siinaysaa oo instructionkaas ayuu raacayaa
#_______________________________________________________________________________________________________________
'''
Functionka waa ereyga ay python ku garan lahayd waa DEF. 

OO def ayaad qoraysaa kadibna magaca functionka, kadibna qaansooyinka ayaad galinaysaa. 
'''

def magaca():
    print("hello world ") # Marka intaa kadib functionka waa in hoos looga yeeraa
magaca() 

#---------------------------------------------------------------------------------------------------------------
#ARGUMENT
#---------------------------------------------------------------------------------------------------------------

def salaam(name): #salaam oo function name ah waxaa uu leeyahay parameter. 
    print("ASC", name)
salaam("Faarax")

'''
Xisaab anagoo argumentigaas u adeegsanayna
'''
def add(x):
    print(10+x)
add(5) # Halkaan waxaan leenahay x waxaad ka dhigtaa 5. 

#---------------------------------------------------------------------------------------------------------------
#MULTUPLE ARGUMENTS IN FUNCTIONS
#---------------------------------------------------------------------------------------------------------------
def salaam(first_name, last_name):
    print("ASC", first_name, last_name)
salaam("Faarax","Cabdulaahi")

#---------------------------------------------------------------------------------------------------------------
#ARBITRARY - WAXAA LOO ADEEGSADAA HADAADAN HUBIN INT WAX AAD MEESHA MEESHA GALINAYSID
#---------------------------------------------------------------------------------------------------------------

def MyKids(*kids): # * calaamadaan waxaa ay usheegaysaa in waxa meesha ku jira ay yihiin ARBITRARY ARGUMENT. 
    print("My youngest kid is "+ kids[0]) # Halkaan waxa la samaynayaa waxaa ay tahay in lagu yiri waxaad soo daabacdaa in cunugayga 1aad uu yahay cunuga 0[zero] wata.
MyKids("Cismaan","Ciise")

#---------------------------------------------------------------------------------------------------------------
#KEYWORD ARGUMENT (KWARGS)
#---------------------------------------------------------------------------------------------------------------
def MyKids(child1, child2): 
    print("My youngest kid is "+ child1) 
MyKids("Cismaan","Caasho") # Argumentigaan kan kaga horeeya waxaa uu kaga duwanyahay isagu arguments malaha. 



#---------------------------------------------------------------------------------------------------------------
#ARBITRARY KEYWORD ARGUMENT
#---------------------------------------------------------------------------------------------------------------
def kids(**kids): # Kii hore waxaa uu kaga duwanyahay waxaa weeye, isaga waxaa ku jirta laba xidig, halkaa kii hore ay ku jirtay hal xidig.
    print('her first name is' + kids["first_name"])
    print('her first name is' + kids["last_name"])
kids(first_name ="Nasteexo",last_name="Cali")



#---------------------------------------------------------------------------------------------------------------
#RETURN VALUE
#---------------------------------------------------------------------------------------------------------------
def func1(x):
    return 5*x
print(func1(7))#Printigaan waxaa loo adeegsadaa banaanka functionka.


#🚀Waxaa jira habkale oo valuega loo soo celiyo. 
def fun1(x,y):
    return x*y
print(fun1(7,5))


#---------------------------------------------------------------------------------------------------------------
#DEFAULT PARAMETER
#---------------------------------------------------------------------------------------------------------------

def wadan(wadan="somalia"):
    print("Iam from " + wadan)
wadan() #Waa default oo hadaadan sidaan udayno waxaan u printigreynaynaa IM FROM SOMALIA. 

wadan("Kenya") #Overwritten waa ku samayn karnaa function namekaas default parameterka wata anagoo argument cusub siinayna, kaasoo ah kenya. 


#---------------------------------------------------------------------------------------------------------------
#LAMBDA FUNCTION/EXPRESSIONS
#---------------------------------------------------------------------------------------------------------------

#👉Lambda is small anonymous functions. 

#lambda argument : expressions

x = lambda a: a + 10 #Halkaan hadaan sharaxo waxaa weeye (a) koowaad waxaa ay ka dhigan tahay ARGUMENT, halka (a) labaad ay tahay expression.

print(x(5)) #Oo halkaan hadaad eegtid booska 5 waxaa soo galaysa a, oo outputka soo baxaya waa 15. 

#⚡=> Lambda waxaa la adeegsadaa barnaamijkaada marakkada doonayn inuusan space badan uusan qaadan. 


#👇Tusaale kale oo lambda expression ah
x = lambda a, b : a * b
print(x(9,10)) #

#__________________
#   POWER OF LAMBDA
#__________________
#😁Function within function
def myfun(n):
    return lambda a : a * n
double = myfun(6)#Functionkaan myfun la yiraahdo hadba tirada la geliyo waa ku laba laabmaysaa.
print(double)
