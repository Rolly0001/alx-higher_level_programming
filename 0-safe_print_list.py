def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass
    finally:
        print("")  # Ensure a new line is printed at the end
    return count

# Example usage:
my_list = [1, 2, 3, "a", "b", "c"]
print("Number of elements printed:", safe_print_list(my_list, 10))
