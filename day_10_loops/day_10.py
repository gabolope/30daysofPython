# Exercises: Level 1
# 1 Iterate 0 to 10 using for loop, do the same using while loop.
for num in range(11):
    print('#1a:', num)

num = 0
while num <= 10:
    print('#1b:',num)
    num += 1

# 2 Iterate 10 to 0 using for loop, do the same using while loop.
for num in range(10, -1, -1):
    print('#2a:', num)

num = 10
while num >= 0:
    print('#2b:', num)
    num -= 1

# 3 Write a loop that makes seven calls to print(), so we get on the output the following triangle:
  #
  ##
  ###
  ####
  #####
  ######
  #######

hash_str = '#'
while len(hash_str) <= 7:
    print('#3:', hash_str)
    hash_str += '#'

# 4 Use nested loops to create the following:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
count = 0
while count < 8:
    hash_str = '#'
    for i in range(8):
        hash_str += ' #'
    count += 1 
    print('#4:', hash_str)
