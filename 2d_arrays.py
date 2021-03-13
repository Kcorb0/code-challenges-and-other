
#how appending lists work


unaltered_array = [1,3,4,5,6]

unaltered_array.append(3)

# The original list that was instantiated has been modified by append
print(unaltered_array)

unaltered_array2 = [4,1,4,5,5]

new_array2 = unaltered_array2 + [14]

print(new_array2)