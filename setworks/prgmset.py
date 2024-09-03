#set==============
name={"hari","sukmar","hello","hello"}
print(name)
#s=set()
#print(type(s))
#duplicates not allowed
#cannot fetch a object using index position in set object
#mutable we can add or remove the elements in the list




# names.add("kochi")  #to add an element to set a object
# print(names)

# names.clear()      #removes all elements from object ,empty set remains
# print(names)


# names.pop()        #which removes a random element from the set object 
# print(names)

# names.discard("hello")    #remove an element from the set if its a memeber in the object 
# print(names)


names={"hello","hari","chennai","kollam"}
new_names=["hp", "dell","hello","lenovo"]
new_set=names.symmetric_difference(new_names)
print(new_set)
#union
#difference