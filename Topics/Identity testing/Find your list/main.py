def find_my_list(lists, my_list):
    for ix, lst in enumerate(lists):
        # Change the next line
        if id(my_list) == id(lst):
            return ix
    return None