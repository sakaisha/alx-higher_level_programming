#!/usr/bin/python3

from copy_list import copy_list

def main():
    original_list = [1, 2, 3, 4, 5]
    copied_list = copy_list(original_list)
    
    print("Original List:", original_list)
    print("Copied List:", copied_list)

if __name__ == "__main__":
    main()
