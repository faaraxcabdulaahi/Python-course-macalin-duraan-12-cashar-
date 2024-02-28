# if else statements

# Logical condition

'''
Equal ==
Not equal !=
Less than <
Less than or equal <=
Greater than >
Greater than or equal >=
AND, OR
IS
'''

a = 5
b = 4

if a < b:
    print("a is greater than b")# Printiga aad arkaysid waxaa uu ku jiraa wax la yiraahdo INDENT, indent waxaa weeye spaceka u dhaxeeya, spaceka ka hooseeya, WAANA HABKA AY USHAQAYSO PYTHON. 
else:
    print("b is greater than a")
    
#elif

x = 99
y = 99
if x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
else:
    print("None of that")
    
# And Condition
a = 55
b = 58
c = 66
if a > b and c >b: # Labadaan xaaladood waxaa khasab ah in labaduba ay khasab ahaadaan.
    # Hadii mid kamida ay false noqoto else buu ugudbayaa.  
    print('a is greater than b and c')
else:
    print("b and c are greater than a")

# Or 
'''
Iyadu waxaa weeye mid un inuu sax ahaado weeye. 
'''

a = 70
b = 78
c = 72

if a > b or c >a:
    print('A is greater thanb b and c is greater A')
else:
    print("b is greater tha a ")
    
# is
'''
is waa equal camal
'''
a = [1,2,3,4]
b = [1,2,3,4]

# marka statementigaan true waa inay soo print gareyso. 
# is micnaha way tahay weeye. 
print(id(a))
print(id(b))
