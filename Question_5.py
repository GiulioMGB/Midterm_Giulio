def count_bBob_occurrences(text):
    count = 0
    # The length of the pattern we're looking for is at least 4 ("bBob")
    for i in range(len(text) - 3):
        # Check if the current substring starts with 'b' and ends with 'Bob'
        if text[i] == 'b' and text[i+1:i+4] == 'Bob':
            count += 1
    return count

# Example usage
text = "bBob is talking to bBobby and then bBob walks away."
matches = count_bBob_occurrences(text)
print(matches)