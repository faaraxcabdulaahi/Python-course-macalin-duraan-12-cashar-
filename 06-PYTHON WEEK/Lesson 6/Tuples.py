# WAA MAXAY TUPLE ?
'''
👍Waa meel xog lagu kaydsado. 
👍Lama badali karo(Unchangeable immutable). 

(labadaas erey waa isku mid oo tuple wax lagama badali karo waxna laguma dari karo.)

👍Wayna is daba joogtaa(Indexed).
'''

'''
📰 Xog markaadan rabin mustaqbalka inaadan badalin, waa markaas marka tupleka la adeegsado. 
'''

# Waxay kukala duwan yihiin 
'''
-----                          -----
TUPLE                           LIST
-----                          ------
()                              []
Len                             len
loop                            loop
Methods-less                    Methods-More
Unchangeable                    Add, remove
'''

#Method waxaa la yiraahdaa wax yaalaha lagu badali karo xogta sida remove ama add la yiraahdo, Xogtaas oo noqon karta List ama Tuple. 

# TUPLE

# x=[1,2,3]
# print(dir(x))

# LIST
# x=(1,2,3)
# print(dir(x))

#------------------------------------------------------
#TUPLE
#------------------------------------------------------
fruit = ("Mango","Apple","Banana")

print(fruit[1])

'''
OUTPUTKA : Apple
'''

#TUPLEKA ISBADAL LAGUMA SAMAYN KARO, LAAKIN WAXAA JIRA HAB ISBADAL LOOGU SAMAYN KARO OO LA YIRAAHDO ("WORK-AROUND")
'''
HABKAAS OO AH IN AAD TUPLEKA LIST UBADASHID KADIBNA AAD WAX KA BADASHID, OO WAX KU DARTID WAXNA KA JARTID, KADIBNA TUPLEKA BAAD KUSOO CELINAYSAA. 
'''
fruit = ("Mango","Apple","Banana")

x = list (fruit) # Sida Tuple list loogu badalo. 

x[0]="Canbe" # Sida tuplekii listiga loogu badalay, isbadal loogu sameeyo. 

y = tuple(x) # Sida listiga Tuple dib loogu badalo. 

print(y)
'''
OUTPUTKA: ('Canbe', 'Apple', 'Banana')
'''
#------
#LOOPS
#------

fruit = ("Mango","Apple","Banana")
for x in fruit:
    print(x)
'''
OUTPUTKA : 

Mango
Apple
Banana

'''

#INDEX
fruit = ("Mango","Apple","Banana")
for index, x in enumerate(fruit): # enumerateku waxaa uu kaa caawinayaa markaad rabtid index inaad soo bixisid. 
    print(index, x) 
'''
OUTPUTKA : 

0 Mango
1 Apple
2 Banana
'''

# SIDEE LOO OGAADA IN ITEM UU KU JIRO TUPLEKA
fruit = ("Mango","Apple","Banana")
if "Apple" in fruit:
    print("Yes")
else:
    print("No")
    
'''
OUTPUTEKA : Yes
'''

# HUBI INAAD COMMA KU DARTID

one_fruit = ('Apple',)
print(type(one_fruit))

'''
OUTPUTEKA : <class 'tuple'>
'''

# Maxaa dhacaya hadaad comma ka tagtid bal aan fiirino
one_fruit = ('Apple')
print(type(one_fruit))
'''
OUTPUTEKA : <class 'str'>
'''

# Markaad wax ka tirtiraysid Tupleka, mid mid ugama delete kartid ee waa inaad kuligiis delete ku samaysaa. 

# del one_fruit
# print(one_fruit)
'''
OUTPUTEKA : one_fruit' is not defined
'''

# SIDEE LABA TUPLE LA ISUGU DARAA
x = ("cali","salaad","geele")
y = ("maxamed","maxamuud")
print(x+y) # habka 1aad ee la isugu daro
'''
OUTPUTEKA : 
('cali', 'salaad', 'geele', 'maxamed', 'maxamuud')
'''

#ama 

z = x+y # habka 2aad ee la isugu daro iyado variable cusub la samaynayo. 
print(z)

'''
OUTPUTEKA : 
('cali', 'salaad', 'geele', 'maxamed', 'maxamuud')
'''

#UNPACKING SIDEE LOO SAMEEYAA

'''
TUSAALE : Waxaan rabnaa arday xogtiisa inaan diyaarino
'''
Ardey = ("Faarax","Python","99")
(name, subject, age) = Ardey
print(name, subject, age) # Habkaan ayaa unpacking la dhahaa.

'''
Unpacking waxaa la adeegsadaa markaad doonaysid inaad information badan inaad isku aadisid
'''