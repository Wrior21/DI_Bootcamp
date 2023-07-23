for letter in 'harry':
    if letter == 'r': 
        pass
    print(letter, end='')

    #split the code

# for letter in 'leonardo':
#     if letter == 'r':
#          break   
#     print(letter, end='')
    
#     #split the code


# for number in '12345':
#     if number == '3':
#         break
#     print(number, end='')
    
#     #split the code

#Access the vaue of key "history"
sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}
​
print(sample_dict['class']['student']['marks']['history'])
​
# Delete set of keys from Python Dictionary
​
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
​
}
keys_to_remove = ["name", "salary"]
​
for key in keys_to_remove:
    if key in sample_dict:
        del sample_dict[key]
print(sample_dict)


sample_dict={"class": 
             {"student":
              {"name":"mike",
               "marks":{
             "physics":70,
             "history":80
    }
      }
         }
}
print(sample_dict['class']['student']['marks']['history'])

sample_dict= { 
    "name:": 'Kelly'
    "age": 25 , 
    "salary": 8000
    "city": "new york"
} 
for key in keys_to_remove: 
    if key in sample_dict: 
        del sample_dict:[key]
print(sample_dict)

# for key in keys_to_remove: 
#     if key in sample_dict:
#         del sample_dict:[key]
# print(sample_dict)

