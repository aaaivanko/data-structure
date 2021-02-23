
# 5. Write a Python program to count the number of strings where the
# string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

def count_number(my_list):
    total = 0
    for item in my_list:
        if item[0] == item[-1] and len(item):
            total += 1
    return total

print(count_number(['abc', 'xyz', 'aba', '1221']))
