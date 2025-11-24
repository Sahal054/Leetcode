# for i in range (0,4):
#     for j in range (0,4):
#         print("*")
#     print()
# ****
# ****
# ****
# ****    


# for i in range (0,6):
#     for j in range (i):
#         print('*',end ='')
#     print()    
# *
# **
# ***
# ****
# *****


# for i in range(7):
#     for j in range(1,i):
#         print(j, end= '')

#     print()    
# 1
# 12
# 123
# 1234
# 12345

# for i in range(6):
#     for j in range(i):
#         print(i, end ='')

#     print()  
# 1
# 22
# 333
# 4444
# 55555

# def pattern_5_inverted_triangle(rows=5):
#     """
#     Prints an inverted right-angled triangle of stars.
#     *****
#     ****
#     ***
#     **
#     *
#     """
#     print("--- Pattern 5: Inverted Triangle ---")
#     # Loop backwards from the number of rows down to 1
#     for i in range(rows, 0, -1):
#         print('*' * i)
#     print("\n")


# def pattern_6_inverted_number_triangle(rows=5):
#     """
#     Prints an inverted right-angled triangle of numbers.
#     12345
#     1234
#     123
#     12
#     1
#     """
#     print("--- Pattern 6: Inverted Number Triangle ---")
#     # Outer loop for each row, counting down from 5 to 1
#     for i in range(rows, 0, -1):
#         # Inner loop to print numbers from 1 up to the current row number 'i'
#         for j in range(1, i + 1):
#             print(j, end='')
#         # Print a newline to move to the next row
#         print()
#     print("\n")


# def pattern_7_pyramid(rows=5):
#     """
#     Prints a pyramid of stars.
#         *
#        ***
#       *****
#      *******
#     *********
#     """
#     print("--- Pattern 7: Pyramid ---")
#     # Loop for each row
#     for i in range(rows):
#         # Calculate spaces needed before the stars
#         spaces = ' ' * (rows - i - 1)
#         # Calculate stars needed for the current row
#         stars = '*' * (2 * i + 1)
#         print(spaces + stars)
#     print("\n")


# def pattern_8_inverted_pyramid(rows=5):
#     """
#     Prints an inverted pyramid of stars.
#     *********
#      *******
#       *****
#        ***
#         *
#     """
#     print("--- Pattern 8: Inverted Pyramid ---")
#     # Loop for each row
#     for i in range(rows):
#         # Calculate spaces needed before the stars
#         spaces = ' ' * i
#         # Calculate stars needed for the current row
#         stars = '*' * (2 * (rows - i) - 1)
#         print(spaces + stars)
#     print("\n")