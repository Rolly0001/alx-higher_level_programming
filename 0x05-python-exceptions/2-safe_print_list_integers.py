def safe_print_list_integers(my_list=[], x=0):
    printed_count = 0
    try:
        for i in range(x):
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
                printed_count += 1
    except IndexError:
        pass  # If index i is out of range, it will exit the loop
    
    print()  # Print newline after all integers
    
    return printed_count
