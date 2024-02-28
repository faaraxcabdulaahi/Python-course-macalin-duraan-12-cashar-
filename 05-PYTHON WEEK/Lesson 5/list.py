 # LIST
'''
List is ordered collection, changeble, duplicate.

Listiga waxaad ku dari kartaa DATA TYPESKA kale. 
'''
fruit = ["Mango","Apple","Grapes"]
print(fruit)

'''
OUTPUTKA : ['Mango', 'Apple', 'Grapes']
'''
#--------
# 1)INDEX
#--------
#Listigu waxaa uu leeyahay INDEX kaasoo ah , lambar lagu garto mid kasta meesha uu ku jiro.

#Waxaana uu indexku ka bilaabmaa Eber(Zero).

# Oo markaad Access garaynaysid waxaad adeegsanaysaa Indexka

'''
Tusaale : Mango waa (0), Apple waa (1), Grapes waa (2). 
'''
print(fruit[0])

'''
OUTPUTKA : Mango
'''
#--------
# 2)SLICING
#--------
'''
Slicing waa jar jarid 
'''
fruit = ["Mango","Apple","Grapes","Black berry"]
print(fruit[-1]) # -1 micnaheedu waxaa weeye listiga kan ugu dambeeya isii. 

'''
OUTPUTKA : Black berry
'''

# Hadaad doonaysid kan ugu dambeeya inaad ka reebtid waxaad adeegsataa calaamadaan (: kadibna lambarka aadan rabin inuu listigaaga la socdo).

# Tusaale

fruit = ["Mango","Apple","Grapes","Black berry"]
print(fruit[:-1]) # halkaan waxa ka dhacaya ayaa waxa uu yahay, listiga waxaa laga reebay black berry.

'''
OUTPUTKA: ["Mango","Apple","Grapes","Black berry"]
'''

# Hadaad doonaysid inaad listiga 1aad kaliya aad soo daabacatid, waa sidaan (1:0), ebertu(0) waa optional.
fruit = ["Mango","Apple","Grapes","Black berry"]

print(fruit[1:0]) # Halkaan waxaa uu ka bilaabayaa Apple, halka uu ka tagayo, MANGO.

'''
OUTPUTKA : ["Apple","Grapes","Black berry"]
'''

#--------
# 3)RANGE
#--------
'''
waxaa weeye tirada aad uga baahantahay ee listigaaga
'''

fruit = ["Mango","Apple","Grapes","Black berry"]

print(fruit[0:3]) # halkaan waxa ka dhacay ayaa waxa uu yahay, waxaa uu soo qaadanayaa Mango iyo Apple, hadaad u baahantahay grapes inaad ku dartid Tirada (3) ka dhigtay (4 ka dhig).

'''
OUTPUTKA : ["Mango","Apple"]
'''

# SIDA LISTIGA  ITEMKIISA WAX LOOGA BADALO

fruit = ["Mango","Apple","Grapes","Black berry"]

fruit[1] = "Pineapple"

print(fruit) # Halkaan waxa ka dhacaya ayaa waxa uu yahay APPLE ayaa waxa lagu badalayaa PINEAPPLE, micnaha booskii ay apple ku jirtay ayaa waxaa la galinayaa Pineapple.

# SIDA LOOP LOOGU SAMEEYO LISTIGA
fruit = ["Mango","Apple","Grapes","Black berry"]
for x in fruit :
    print(x)

'''
OUTPUTKA :
 
Mango
Apple
Grapes
Black berry

'''
for index, x in enumerate (fruit) :
    print(index, x)
    
'''
OUTPUTKA :

0 Mango
1 Apple
2 Grapes
3 Black berry

'''

# SIDA LOO OGAADO IN MEESH LIST UU ITEM KU JIRO
fruit = ["Banana", "Mango","Apple","Grapes","Black berry"]
if "Banana" in fruit:
    print("Banana is in list")
else:
    print("It is not in the list")
    
'''
OUTPUTKA : Banana is in list
'''

# LISTIGU INTUU DHEERAR DHAN YAHAY

print(len(fruit)) # halkaan waxaa uu kuu soo saarayaa inta item ee ku jira listiga tiradiisa. 

'''
OUTPUTKA : 5
'''

# SIDEE ITEM LIST LOOGU DARAA

#1-Habka 1aad waa APPEND :
fruit = ["Banana", "Mango","Apple","Grapes","Black berry"]

fruit.append("Apple") # Halkaan waxa ka dhacay ayaa waxa uu yahay, in Apple uu listiga ka maqnaa kadibna uu gadaal uga daray. 

print(fruit) 
'''

OUTPUTKA : 

['Banana', 'Mango', 'Apple', 'Grapes', 'Black berry', 'Apple']

'''

#1-Habka 2aad waa INSERT :
fruit = ["Banana", "Mango","Apple","Grapes","Black berry"]

fruit.insert(0, "Apple")

print(fruit)

'''

OUTPUTKA : 
['Apple', 'Banana', 'Mango', 'Apple', 'Grapes', 'Black berry']

'''
 #LIST LIST LAG DARAYO
'''
 Marka list list lagu darayo waxaa la adeegsadaa EXTEND halkii la adeegsan lahaa INSERT iyo wixii lamida. 
 
'''
fruit = ["Banana", "Mango","Apple","Grapes","Black berry"]

fruit2 = ["Apple","Blueberry"]
fruit.extend(fruit2)
print(fruit)
'''
OUTPUTKA : 

['Banana', 'Mango', 'Apple', 'Grapes', 'Black berry', 'Apple', 'Blueberry']

'''
# SIDOO KALE ADOO EXTEND ADEEGSAN WAXAAD ADEEGSAN KARTAA CALAAMADA UU AAD PRINT FUNCTIONKA KU DHEX QORAYSID. 

'''

'''

fruit = ["Banana", "Mango","Apple","Grapes","Black berry"]

fruit2 = ["Apple","Blueberry"] 

print(fruit+fruit2) # Tanina waa hab-kaloo list list loogu dari karo.

 
'''
OUTPUTKA : 

['Banana', 'Mango', 'Apple', 'Grapes', 'Black berry', 'Apple', 'Blueberry']

'''

# MARKA LISTIGA WAX LAGA BIXINAYO 
'''
1. remove()
2. Pop() kan waxaa meesha ka bixinayaa kan ug dambeeya.
'''

# SIDA REVERSE LOO SAMEEY
'''
1. reverse()
kaliya waxaa qortaa reverse function;

fruit.reverse()


'''

# SIDA SORT GAREEYAA HABKA ISKU XIGITAANKA ALIF BEETADAA.

'''
1. sort()
'''

# SIDA LOO SORT GAREEYA LOONA REVERSE GAREEYAA
'''
fruit.sort(reverse=True):

Halkaan sort ayuu samaynayaa, kadibna reverse.

kan waxaa loo adeegsadaa kuna uu fiican yahay lambariska.
'''
nums = [1,2,3,4,5,6,7,8]
nums.sort(reverse=True)
print(nums)

'''
OUTPUTKA : [8, 7, 6, 5, 4, 3, 2, 1]
'''

# Max, Min, Sum = Waa functiono python ku jira

#------
#1-Min
#------
nums = [1,2,3,4,5,6,7,8]
print(min(nums)) # Halkaan waxaa lasoo saarayaa tirada ugu yar
'''
OUPUTKA : 1
'''
#------
#2-Max
#------
nums = [1,2,3,4,5,6,7,8]

print(max(nums)) #Kana waxaa uu kuusoo saarayaa xarafka ugu weyn. 

'''
OUTPUTKA : 8
'''

#------
#3-Sum
#------

nums = [1,2,3,4,5,6,7,8]

print(sum(nums)) # Halkaana waxaa uu noo soo saarayaa isku darka tirada listiga ku jirta.

'''
OUTPUTKA : 36
'''

# SIDEE LIST STRING LOOGA DHIGI KARAA

fruit = ["Banana", "Mango","Apple","Grapes","Black berry"]

fruit_str = " , ".join(fruit)

print(fruit_str) # Halkaan micnaheedu waxaa weeye, waxaa noo soo printi garaysaa listigaas oo STRING AH ASTAANTA HAKAD (,) AY UDHAXAYSO. 

'''
OUTPUTKA: 
Banana , Mango , Apple , Grapes , Black berry
'''

#HADII AAD RABTID DIB INAAD UGU CELISID 
fruit = ["Banana", "Mango","Apple","Grapes","Black berry"]

fruit_list = fruit_str.split(" , ")

print(fruit_list) # Halkaan waxaa ka dhacay ayaa waxaa uu yahay, waxaan ku niri shay kasta oo kolmo wata (""), astaanta hakadna (,) usii dheertahay, waxaad ka dhigtaa list.

'''
OUTPUTKA : ['Banana', 'Mango', 'Apple', 'Grapes', 'Black berry']
'''
