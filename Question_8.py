def is_valid_url(url):
    # Check if the URL starts with http:// or https://
    if not (url.startswith('http://') or url.startswith('https://')):
        return False
    # Check if there is at least one dot in the URL
    if '.' not in url:
        return False
    # Check if there are any spaces in the URL
    if ' ' in url:
        return False
     # If all checks passed, the URL meets our basic criteria
    return True


# Example usage
print(is_valid_url("http://example.com"))  # Should return True
print(is_valid_url("https://example"))  # Should return False because there's no dot
print(is_valid_url("htt://example.com"))  # Should return False because it doesn't start with http:// or https://
print(is_valid_url("http://example.com withspace"))  # Should return False because it contains a space
