# start = 20
# n_start = 20

# while start > 2520:
#   if n_start % start == 0:
#     start -= 1
#     n_start += 1
#   else:
#     n_start += 20
#     start = 20
    
# print(n_start)


def find_common(n):
  highest_value = n # Highest value in the num we are looking to divide
  lowest_multiple = n # Lowest number that can be divided by all numbers in the range evenly

  while highest_value > 2: 
    if lowest_multiple % highest_value == 0:
      highest_value -= 1
    else:
      lowest_multiple += n
      highest_value = n

  return lowest_multiple

print(find_common(18))

  
