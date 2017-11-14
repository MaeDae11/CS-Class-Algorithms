def sum_of_numbers(max):
  sum = 0
  for i in range(max):
    if i % 3 == 0 or i % 5 == 0:
      sum += i

  return sum
    
print sum_of_numbers(10)

# this function runs quicker as it does not have to loop through each number
def sum_divisible_by(number, max):
  sum = 0
  for i in range(0, max, number):
    sum += i
  return sum

print sum_divisible_by(3, 50)


def sum_numbers_best(number, max):
  n = int((max-1) / number)
  sum = number * (n * (n +1)) / 2
  return int(sum)

print sum_numbers_best(2, 50000)
# if a number % 3 = 0, true
# if a number % 5 = 0, true
# if a number % 3 && 5, true
# range([start], stop[, step])