#Exercise 1: Convert lists into dictionairies 
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

zippinglists = zip(keys,values)
print(zippinglists)
empty_dict={}

# for item in zippinglists: 
#     print(item)
    
#     empty_dict.update({item[0]:item[1]})
# print(empty_dict)

open_dict=dict(zippinglists)
print(open_dict)

#Exercise 2  Cinemax
# How much does each family have to pay 
# I am speeding up in class.

# Age = 3 then free
# Age = 3 + 12 then 10
# Age = >12 then 15
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
#each family member pays

for family_member in {'rick',43,'beth',13,'morty',5,'summer',8}:
if "rick43":
 print('rick pays $15')
 
elif "beth_43":
 print("Beth pays $15")

elif "morty_5":
 print("Morty pays $10")

else ("summer_8"):
 print("summmer pays $10")

#bonus completed 
#'total cost of the family'

total_cost = ('rick $15')+('beth $15')+('morty $10')+('summer $10')
print(total_cost) 
    
Family_dictionary = input("What is your families names?") + ("what are your ages?")   
print ("family_dictionary")


#Exercise 3 Zara
#brand 1.
Brand = {'Name': 'Zara', 'creation date': '1975', 'creator_mane': '1975', 'type_of_clothes': 'men, women, children, home', 'interntional_competiotrs': 'gap' ,'h&m', 'Benetton' 'number_stores': '7000' ,'major_color' : 'france blue, spain red, us pink, green'}
print(Brand)

#2. 
Brand['number of stores': '2']
print['number of stores': '2']

Brand['type_of_clothes': 'Zaras has clients that are in classes from men, women, children and the home industry']
print['type_of_clothes': 'Zaras has clients that are in classes from men, women, children and the home industry']

Brand['country_creation':'spain']
input['country_creation':'spain']

keys = Brand['international_competitors']
Brand['international_competitors': 'desigual']
input['international_competitors': 'desigual']

del Brand['creation date']

Brand['international_competitors':'benetton']
print['international_competitors':'benetton']

Brand['major_color':'france blue','spain red','US pink','green']
print['major_color':'france blue','spain red','US pink','green']

print[keys:Brand]

More_on_zara={'creation_date': '1975', 'number_of_stors':'10000'}

for Brand in More_on_zara

Brand = {'Name': 'Zara', 'creation date': '1975', 'creator_mane': '1975', 'type_of_clothes': 'men, women, children, home', 'interntional_competiotrs': 'gap', 'h&m', 'Benetton' 'number_stores': '7000' ,'major_color' : 'france blue, spain red, us pink, green'}
Brand.update{More_on_zara}

print['number_stores','whhat just happenned']

#Exercise 4  Disney Characters

users = [Mickey,Minnie,Donald,Ariel,Pluto]
Analyse these results 

#1

print(disney_users_A)
{'Mickey 0', 'Minnie 1', 'Donald 2', 'Ariel 3', 'Pluto 4'}

#2

print(disney_users_B)
{'0 Mickey','1 Minnie', '2 Donald', '3 Ariel', '4 Pluto'}

#3 

print(disney_users_C)
{'Ariel 0', 'Donald 1', 'Mickey 2', 'Minnie 3', 'Pluto 4'}

for x in disney_users_A
if x == 'Minnie 1''Mickey 0':
 print[x]

else:"we doing this"

for y in disney_users_B

print[y]

sorted(disney_users_C)
print[disney_users_C]



