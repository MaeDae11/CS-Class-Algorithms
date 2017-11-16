# Given an array of Numbers (unknown)
# 1. what is the least occuring number?
# 2. return true if there are any duplicates

unknown_array_test = [2,2,2,2,3,3,3,4,4,5,5,5,6,6,7,7,7]

my_dictionary = {}

for num in unknown_array_test:
  if num in my_dictionary:
    my_dictionary[num] += 1
  elif num not in my_dictionary:
    my_dictionary[num] = 1

least_occurance_arr = []
duplicates_arr = []

# for key in my_dictionary:
#   if my_dictionary[key] == 1:
#     least_occurance_arr.append(key)
#   elif my_dictionary[key] > 1:
#     duplicates_arr.append(key)
lowest_count = None

for key in my_dictionary:
  if lowest_count == None:
    lowest_count = my_dictionary[key]
  elif my_dictionary[key] <= lowest_count:
    lowest_count = my_dictionary[key]

for key, value in my_dictionary.iteritems():
  if value == lowest_count:
    least_occurance_arr.append(key)

print least_occurance_arr





# least_occurance_arr.append(my_dictionary[lowest])
   
    