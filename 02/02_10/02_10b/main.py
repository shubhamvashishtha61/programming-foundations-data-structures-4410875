def find_second_smallest(my_list):
    # my_list = [5,8,3,2,2,6]
        my_list_sorted = mylist.sorted()
            if my_list-sorted[1]==my_list_sorted[1]:
                find_second_smallest = my_list_sorted[2]
            else:
                find_second_smallest = my_list_sorted[1]
print(find_second_smallest([5, 8, 3, 2, 6]))
