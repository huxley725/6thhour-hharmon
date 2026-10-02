#Name:Huxley Harmon
#Class: 6th Hour
#Assignment: HW9

#1. Print Hello World!
print("Hello World")
#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
superhero_dictionary = {
    "captain america":"Steve Rogers",
    "ironman":"tony stark",
    "batman":[1,7,4]}

#3. Print the keys of the dictionary from #2.
print(superhero_dictionary.keys())
#4. Print the values of the dictionary from #2
print(superhero_dictionary.values())
#5. Print one of the three numbers from the list by itself
print(superhero_dictionary["batman"][3])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
superhero_dictionary.update({"spider-man":"peter parker"})
#7. Print the entire dictionary from #2 with the updated key and value.
print(superhero_dictionary)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
brody_dictionary ={
"brody_1":{
"name":"owen"
"year":2011,
 "last_name":"jones",
}
"brody_2":{
    "name":"brody"
    "year":2012,
}
#9. Print the names of all three classmates on the same line.
print(brody_dictionary["brody_1"],brody_dictionary"brody_2"].brody_dictionary_"brody_3"]
#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.