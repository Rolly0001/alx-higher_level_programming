def safe_print_list(my_list=[], x=0):
    printed_count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            printed_count += 1
    except IndexError:
        pass  # If index i is out of range, it will exit the loop
    
    print()  # Print newline after all elements
    
    return printed_count
