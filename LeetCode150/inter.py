def card_game_score(arr):
    maria_score = 0
    alex_score = 0
    flip_deck = False

    for i in range(len(arr)):
        if i % 2 == 0:  # Maria's turn
            maria_score += arr[i]
            if maria_score % 3 == 0 and i != len(arr) - 1:
                flip_deck = not flip_deck
        else:  # Alex's turn
            alex_score += arr[i]
            if alex_score % 3 == 0 and i != len(arr) - 1:
                flip_deck = not flip_deck

        if flip_deck:
            arr = arr[::-1]

    return maria_score - alex_score

# Example usage with the provided array [5, 3, 7, 2, 6, 5]
arr = [5, 3, 7, 2, 6, 5]
result = card_game_score(arr)
print("Fi", result)
