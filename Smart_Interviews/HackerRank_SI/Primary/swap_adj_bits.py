def swap(num):
    even_bits = num & 0xAAAAAAAA  # Mask for even bits (1010 1010 1010 1010)
    odd_bits = num & 0x55555555   # Mask for odd bits  (0101 0101 0101 0101)


    even_shifted = even_bits >> 1  # Shift even bits to the right
    odd_shifted = odd_bits << 1    # Shift odd bits to the left
    print(even_bits, odd_bits, even_shifted, odd_shifted)
    swapped_num = even_shifted | odd_shifted  # Combine the swapped bits

    return swapped_num

t = int(input())
for _ in range(t):
    n = int(input())
    print(swap(n))