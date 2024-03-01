def find_b_bob_occurrences(text):
    # Initialize a count variable to keep track of matches
    count = 0

    # Convert the text to lowercase to make the search case-insensitive
    text = text.lower()

    # Loop through each character in the text
    for i in range(len(text)):
        # Check if the current character is 'b'
        if text[i] == 'b':
            # Look ahead in the text for the substring ending with "bob"
            # We use a loop to check each subsequent character until we find "bob"
            for j in range(i + 1, len(text)):
                # If we find a substring that ends with "bob", increase the count
                if text[j:j + 3] == 'bob':
                    count += 1
                    break  # Exit the inner loop once a match is found

    return count
