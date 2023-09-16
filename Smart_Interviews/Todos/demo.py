def optimized_calculate_less_than_counts(input_array):
    # Create a sorted copy of the input array
    sorted_array = sorted(input_array)
    
    # Create a dictionary to store the count of elements less than each element
    counts_dict = {}
    
    for i, num in enumerate(sorted_array):
        if i == 0:
            counts_dict[num] = 0
        else:
            if num == sorted_array[i - 1]:
                counts_dict[num] = counts_dict[sorted_array[i - 1]]
            else:
                counts_dict[num] = i
    
    # Create the output array using the counts_dict
    output_array = [counts_dict[num] for num in input_array]
    
    return output_array

# Example 1
input_array1 = [3, 6, 9]
output1 = optimized_calculate_less_than_counts(input_array1)
print(output1)  # Output should be [1, 2, 2]

# Example 2
input_array2 = [2, 2, 4, 6]
output2 = optimized_calculate_less_than_counts(input_array2)
print(output2)  # Output should be [2, 2, 3, 4]
