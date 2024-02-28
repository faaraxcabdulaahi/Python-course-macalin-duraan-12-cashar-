# While loop = loop until false, it is used when you don't know the end
# _________________________________________________________________________

i = 0
while i < 10:
    print(i)# Halkaan waxa dhacaya ayaa waxa uu yahay waa uu iska soconayaa ilaa aan ka taabano CTRL+C. 
    
    i +=1 # Halkaan waxaa laga wadaa markasta oo ay i is badasho waxaad ku dartaa hal. OO tiradu waxaa weeye 0+1 =1, 1+1=2 ilaa dhamaad. 
    # Marka waxaa uu noo printi garaynayaa 0 to 9. 
    #Sababta uusan 10ka ugu darin waxaa weeye waxaan niri less than. 
    # Tiradaas hadaadan gelin waxaa dhacaya in loopku kaa noqonayo INFINITE LOOP. 
    #Infinite loop waxaa weeye programkuu wadayaa. 
'''
Halkaan waxaa weeyee i ku bilow laakin int ay i ka yartahay 10, toban kuma jirto. 
'''

# Waxaa jira wax la yiraahdo BREAK and CONTINUE. 

i = 1
while i < 10:
    print(i)
    if i == 4: # mar walba in crementigu waa inuu meesha jooga hadii kale waxaad galaysaa infinite loop. 
        print("Found")
        break # Break waxaa la adeegsadaa in markaa rabtid shay adoo raadinayaa markaad heshid inaad ka baxdid. 
    # Tusaale data base ayaad loop garaynaysaa kadib waxaad leedahay hadii databaseka loop kaan laga helo fadlan loopka ka bax 
    
    i += 5 # increment ayaa la yiraahdaa
    
    
# CONTINUE 
'''
Continue isagu break waxaa uu kaga duwan yahay waxaa weeye, isagu waa uu sii soconayaa, 
'''
i = 1
while i < 10:
    print(i)
    i += 1
    if i == 4:  
        print("Found")
        continue
    
#-------------------------------------------------------------
# Else
i = 1
while i < 5:
    print(i, "Is less than 5")
    i += 1
else:
    print(i, "is not in the list " )
        
        
#__________________________________________________________________________________________
#FOR LOOP = iterate over sequence (Tan micnaheeda waxaa weeye kusoo celceli wax yaabo.)
'''
Marka forloopku wixii aad udhiibtay buu ku qaadayaa, wuuna kusoo celcelinayaa mid kastana mar ayuu ku siinayaa
'''

fruits = ["Apple","Banana","Cherry"]
for item in fruits:
    print(item) # kan waxaa uu samaynayaa wax walba oo meesha ku jira ay midba mar print gareynayaa. 
    
    # While loop waxaa ay for loop uga duwantahay, markasta wixii waa inaad adigu taqaanid, si aad u run gareysid.
    
# Loop over a string
#-------------------
for x in "banana ":
    print(x) # Waxaa uu samaynayaa Mooska xarfahiisa ayuu noo print gareynayaa one by one. 
    
'''
Sida while loop uu break u leeyahay ayuu For loop break u leeyahay. 
'''

# BREAK AND CONTINUE FOR LOOP
fruit = ["Apple","Banana","Cherry"]
for x in fruit:
    print(x)
    if x == "Banana": 
        print("Found the banana that you want it to be print")
        break # Break waxaa uu ka jaraya wixii waxa aad u baahantahay in la printi gareeyo dhinaca ka xigo. 
        
'''
Halkaan waxa dhacay ayaa waxa uu yahay waxaa naloo soo printi gareeyay ilaa Banana.

Micnaha ilaa banana buu rabay waana uu helay ilaa banana, marka wixii ka dambeeya maxaa ka galay. 
'''

# CONTINUE WITH FORLOOP
fruit = ["Apple","Banana","Cherry"]
for x in fruit:
    print(x)
    if x=="Banana":
        print("😊 Waa la helay banaana")


# Mida kaloo la rabo inaan ka hadalno waa range, range aad ayuu muhiim ugu yahay markii la yimaado FOR LOOP. 

# RANGE

for x in range(6): # Midaan
# for x in range(1,7): # Iyo tan isku output baa soo baxaya. 
    
    print(x) # Halkaan waxa ka dhacaya ayaa waxa uu yahay waxaa lasoo printigaraynayaa, 1 ilaa 5. 
    
for x in range(1, 20, 3):
    print(x) # Markaan waxaa la adeegsaday tira kabood. 

# NESTED FOR LOOP

'''
NESTED FOR LOOP WAXAA LOO ADEEGSADAA WAX YAALO BADAN.

NESTED FOR LOOP HABKAY USHAQAYSO XOOGAA WAA AY ADAGTAHAY. 
'''

colors=["Red","Yellow","Orange"]
fruit = ["Apple","Banana","Cherry"]

for x in colors:
    for y in fruits:
        print(x,y) #Markasta oo X la run gareeyo for looptaan baa run gareysmayso, Taas inaad fahantid weeye. 
        # Algarothimtaa ayaad ku ogaan doontaa sida for loop la isku dhex galiyo. 
    
    
#---------------------------------------------------------------------
# ENUMERATE - waxaa weeye counter  (micnaha waxaa uu xisaabinayaa wax kasta oo aad dareemaysid).

 
fruits = ['Apple','Banana','Cherry']
for counter, x in enumerate(fruits): # Waxaa la adeegsadaa markaad rabtid index inaad soo saartid.
    
# Enumerateku waa built in function oo ay python leedahay, aadna ayuu kuu anfcaya mararka qaar hadaad doonaysid inaad adeegsatid. 
    print(counter) 
