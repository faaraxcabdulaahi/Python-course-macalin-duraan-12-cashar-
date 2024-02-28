# 5. Operaters = waa xisaabaadka sida isku darka, kala jarka, greater than iyo wixii lamida.

#---------------------------------------------------------------------------------------------------------------
# (1)ARITHMETIC 
#---------------------------------------------------------------------------------------------------------------
'''
+, -, *,  / 
'''

#1=MODULUS = waa soo haraaga soo hara marka laba tiro la isku qaybiyo.

x=5
y=2
print(x%y)

'''
OUTPUT: 1 
'''

'''
% waa calaamadaan, marka waxaa uu samaynayaa 5 buu 2 u qaybinayaa, kadibna waxaa soo baxaya 1 oo ah micnaha 2 lagu dhuftay 2 loo qaybiyay shan, remainderka ama haraagu waa 1. 
'''
#2= Exponentiation- Saar(Micnaha tiradii baad laba jeer isku dhufanayasaa)
x = 2
y = 3
print(x ** y)
'''
OUTPUT: 8
'''

'''
Halkaan maxaa ka dhacay, halkaan waxa ka dhacay ayaa waxaa uu yahay, tirada '2' ay saddex jeer la isku dhuftay, kadibna outputka soo baxay ayaa waxaa uu noqday '8'.
'''

#3=Floor = floorku waxaa weeye waa tiradii adoo laba jeer isku qaybiyay.

x = 15
y = 2
print(x // y)
'''
OUTPUT: 7
'''
#---------------------------------------------------------------------------------------------------------------
#2) COMPARISON
#---------------------------------------------------------------------------------------------------------------
'''
comparison waxaa weeye is barbar dhiga
'''

'''
isku mid : ==
isku mid ma aha: !=
ka badan: >
ka yar: <
La'eg ama ka weyn: >=
la'eg ama ka yar: <=
'''
# Comparison marka la yiraahdo waa intaas aan soo sheegnay

x = 10 
y = 9
# print(x==y) OUTPUTKA : FALSE
# print(x >= y) OUTPUTKA : TRUE

'''
Badanaa waxaa loo adeegsadaa IF STATEMENTIGA.
'''
#---------------------------------------------------------------------------------------------------------------
#3) LOGICAL OPERATERS
#---------------------------------------------------------------------------------------------------------------

'''
Logical operaters waxaa kamida : AND, OR iyo NOT.

Saddexdaas ayay uqaybsamaan logical operatersku. 

Waxyaalo kala duwan ayaad u adeegsan kartaa LOGICAL OPERATERSKA.

Kuligoodna waxaa ay soo saarayaan TRUE iy FALSE. 
'''
#Tusaalaha 1aad
x = 8
y = 9
t = 6
j = 4

if y==x and t==j:
    print("War heedhee kuli waa isku mid")
else:
    print("Maye, Kuli isku mid ma aha")
'''
OUTPUTKA: Maye, kuli isku mid ma aha
'''

#Tusaalaha 2aad

x = 5
y = 5
t = 7
j = 7

if y==x and t==j:
    print("Kuli waa isku mid")
else:
    print("Mayee kuli isku mid ma aha")

'''
OUTPUTKA : kuli waa isku mid
'''

# 1-Not operater = iyadu waa in tirooyinka mid kamid ay false noqdaan, marka OUTPUTKU True buu noqonayaa. 

# Laakiin hadii ay mid uu true yahayna, outpuka FALSE ayuu soo sarayaa. 

#Waxaad oran kartaa waa lidka AND operater, waxayn wadataa () curly parenthesis ama round brackets hadba kaad utaqaanid.
x = 5
y = 6
t = 10
j = 7
if not (y==x and t==j):
    print("Kuli waa isku mid")
else:
    print("Mayee kuli isku mid ma aha")
    
'''
OUTPUTKA: Kuli waa isku mid
'''

#---------------------------------------------------------------------------------------------------------------
#4) IDENTITY OPERATERS
#---------------------------------------------------------------------------------------------------------------
'''
Operaterkaan waa laba un :
1. is : Tan waxaa weeye waxaas bay tahay camal
2. is not : Tana waxaa weeye waxaas ma aha camal.

Kuwaan sidoo kale TRUE iyo FALSE ayay soo celiyaan.

'''
#-------
#(1) IS
#-------
#Tusaalaha 1aad
x = 5
y = 2

print(x is y) # Halkaan micnaha waxaa weeye x waxaa ay lamid tahay y. 

'''
OUTPUTKU : False
'''
#Tusaalaha 2aad

x = 6
y = 6
print(x is y)
'''
OUTPUTKU : True
'''

#----------
#(1) ISNOT
#----------

# Tusaalaha 1aad
x = 5
y = 2

print(x is not y) # Halka yaab baa ka dhacayo isnot iyadu markii ay FALSE tahay ayay TRUE soo saartaa.

'''
OUTPUTKA: True
'''

# Tusaalaha 2aad
x = 5
y = 5

print(x is not y) # hadii labada tiro ay isku mid yihiin, waa ay neceb tahayoo waxay soo saartaa FALSE. 

'''
OUTPUTKA: False
'''
#---------------------------------------------------------------------------------------------------------------
#5) MEMBERSHIP OPERATERS
#---------------------------------------------------------------------------------------------------------------

'''
Kan laftigiisu waxaa uu leeyahay TRUE iyo FALSE oo uu " soo celiyo labadaas mid kamida".

Isaguna waxaa uu uqaybsamaa labo :

1. In = Micnaha waa uu ku jiraa
2. Not in = Ama kuma uu jiro

'''
# Waxaan kuwaan loo adeegsadaa :
#1. Functions
#2. Variables
#3. If statements GUDAHOODA

#--------
#(1) IN
#--------

#Tusaalaha 1aad

x = ["Canbe","Qare"]

y = "Qare"
print(y in x) # Halkaan micnaheeda waxaa weeye listigaan "Qare" ma uu ku jiraa. Markaasna TRUE iyo FALSE mid un ayuu soo saarayaa. 

'''
OUTPUTKA : True (oo micnaheedu yahay waa uu ku jiraa listigaas valuega aad uga yeertay print function)
'''

#Tusaalaha 2aad

x = ["Canbe","Qare"]

y = "Moos"
print(y in x) # Halka kuma uu jiro marka waxaa soo baxaya "laba orgi ku hirdami mayso".

'''
OUTPUTKA : False
''' 

#-----------
#(1) NOT-IN
#-----------
'''
Tan waa in lidkeed oo ah , kuma uu jiro. 
'''

# Khulaasadii IN iy NOT-IN
# Waxaa loo adeegsadaa shaygaan maku dhex jiraa mise kuma dhex jiro.
#Sidoo kale mid kastoo isaga kamida waxaa uu qabtaa shaqo. 