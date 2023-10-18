#  lists and strings

a = "span" #this is a string 
b = list(a) #covert the strign to list 
print(b)
# ['s', 'p', 'a', 'n']->this is the output 


# if you do not want to do this then and eanted to each word should be in the list 
# use split in this case 
a = "span" #this is a string 
b = a.split() #covert the strign to list 
print(b)
# ['span'] -> this is the output 

a = 'span-span-span'
delimeter = '-'
b = a.split(delimeter)
print(b)
# ['span', 'span', 'span']

a = 'span-span-span'
delimeter = 'a'
b = a.split(delimeter)
print(b)
# ['sp', 'n-sp', 'n-sp', 'n']

# by using joint ->covert lsit to string 
print(delimeter.join(b))
