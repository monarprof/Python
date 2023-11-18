# var1=15
# var2=4
# print(var1+var2)
# print(var1-var2)
# print(var1*var2)
# print(var1/var2)
# print(var1%var2)
# print(var1**var2)


text = "The mesmerizing sunset painted the sky with hues of orange and pink, casting a warm glow over the tranquil beach."
# # Print the word - mesmerizing 
# #print(text[4:15])


# # Print everything after word - mesmerizing    
# #print(text[15:])

# # Print the word - beach
# # Function which returns last word
# def lastWord(text):
   
#     # split by space and converting 
#     # string to list and
#     lis = list(text.split(" "))
     
#     # length of list
#     length = len(lis)
     
#     # returning last element in list
#     return lis[length-1]

# print(lastWord(text))


# # Print the word - tranquil
#  def lastWord(text):
   
#     # split by space and converting 
#     # string to list and
lis = lis(text.split(" "))
     
#     # length of list
length = len(lis)
     
#     # returning last element in list
return lis[length-2]

print(lastWord(text))
