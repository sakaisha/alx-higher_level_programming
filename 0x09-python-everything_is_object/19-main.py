#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

Original_List = [1, 2, 3]
print("Original List:", Original_List)

Copied_List = copy_list(Original_List)

print("Original List:", Original_List)
print("Copied List:", Copied_List)

print("Are the lists equal?", Copied_List == Original_List)
print("Are the lists identical?", Copied_List is Original_List)
