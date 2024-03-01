def days_since_birthday(birthday):
    # Split the birthday string to extract the birth year
    day, month, birth_year = birthday.split('-')
    birth_year = int(birth_year)

    # Get the current year (You'll need to manually update this part each year)
    current_year = 2024  # Example current year

    # Calculate the number of full years passed
    years_passed = current_year - birth_year - 1  # -1 because we're not counting days in birth year and the current year

    # Calculate the number of days (approximation)
    days_passed = years_passed * 365

    return days_passed


# Example usage
birthday = "80-11-2002"
print(days_since_birthday(birthday))
