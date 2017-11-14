def bubble_sort(a):
  # must start off with swapped = True
  swapped = True
  # continue looping while swapped is true
  while swapped:
    swapped = False
    for i in range(len(a) - 1):
      if a[i] > a[i+1]:
        # long way of doing the swap
        # temp = a[i]
        # a[i] = a[i + 1]
        # a[1 =1] = temp

        # mutli variable assignment
        a[i], a[i+1] = a[i+1], a[i]
        swapped = True
  return a



array = [5, 3, 2, 4, 1]
sorted_array = bubble_sort(array)
print sorted_array

# 

