# Sets
'''
Sets waa hab loo qaabeeyo xog.
Sets= waa Unordered, Unindexed, Unique, Uneditable
'''
# fruit={"Apple","Banana","Mango","Blackberry"}

#Accessing
'''
Sidee loo dhex gala (Accessing) maadaama setsku uusan index lahayn.

Markaad Accessgaraynaysid Loop adeegso.
'''
# for x in fruit:
#     print(x)
    
# Checking
# fruit={"Apple","Banana","Mango","Blackberry"}
# print("Banana" in fruit)# Waxaa la fiirinayaa in Bananan uu ku jiro, marka haduu ku jiro, TRUE ama False bay noo soo celinaysaa.

# Sets waxbaad ku dari kartaa ee wax kama badali kartid. 
# fruit={"Apple","Banana","Mango","Blackberry"}
# fruit.add("orange")
# print(fruit) # Outputku index malaha, midakalana waa un-ordered. 

#Wax yaalo badan markaad setka ku daraysid 
# fruit={"Apple","Banana","Mango","Blackberry"}
# fruit.update(["orange",'Grapes'])
# print(fruit)

#Sidee wax looga bixiyaa
# Habka 1aad :
# fruit={"Apple","Banana","Mango","Blackberry"}
# fruit.remove("Banana")
# print(fruit)

#Habka 2aad
# fruit={"Apple","Banana","Mango","Blackberry"}
# fruit.discard("Grapes")
# print(fruit) #Halkaan waxbaa meesh ka maqan ma oranayo ee outputkuu kuusoo tuurayaa., Micnaha waxbaa khaldan ma oranayo, ee wax aan meesha ku jrin buu meesha ka bixinayaa, waxaad oron kartaa maantoo dhan "Hal buu bacaad ku lisayaa. " 
'''
Discardku waxaa uu ku fiicanyahay wax aan listiga ku jirin inuu ka saaro, wax error ahna uusan kuu soo saarin. 
'''



# Habka 3aad
# fruit={"Apple","Banana","Mango","Blackberry"}
# fruit.pop()# popku waxaa uu bixiayaa kan ugu dambeeya. 
# kan laftigiisu ordered ma aha ee kan ugu dambeeya ayuu ka bixinayaa, si randomly ayuu wax uga bixinayaa  "Micnaha midka ugu dambeeya bixin uu mayee, hadba kuu jeclaystuu bixinayaa, waayo index ma lah, marka waxaa lagu taliyaa inaan ka la adeegsan marka xog lala macaamilayo. "
# print(fruit) 

# Sidee la isugu xiraa laba set

# fruit={"Apple","Banana","Mango","Blackberry"}
# fruit2={"Grapes","Pineapple","Lemon","Grapes"}
# fruit3={"Pappay","Strawberry","Milk","Ovacado"}

# fruit4 = fruit.union(fruit2,fruit3)
# print(fruit4)

'''
UNIONKU : Faaidada uu leeyahay waxaa weeye waxaa uu meesha ka bixinayaa wixii ISKU EG (DUPLICATE) 
'''
# union function removing duplicate lists(Sets) while adding two sets
# fruit={"Apple","Banana","Mango","Blackberry"}
# fruit2={"Grapes","Banana"}

# fruit3 = fruit.union(fruit2)
# print(fruit3)

# Sidoo kale UPDATE waad oran kartaa meeshaad UNION oran lahayd. 
fruit={"Apple","Banana","Mango","Blackberry"}
fruit2={"Grapes","Banana"}

fruit.update(fruit2)
print(fruit) # Marka waxaa uu na tusayaa listiga ORIGINALKA ah.  sidoo kalana wax yaalaha DUPLICATE ahna waa uu iska ilaalinayaa. 

'''
SETKU WAXAA UU KU ANFACAYAA MARKAAD RABTID XOG UNIQUE(GAAR AH) INAAD XARAYSID. 
'''