"""
Author: [Your Name]
Assignment: String Manipulation Project
Class: Software Engineering Bootcamp
Date: [Current Date]
Description: This program performs various string manipulations such as counting characters,
             words, vowels, and replacing substrings in a given user input string.
"""

# Input function
def get_input():
    user_input = input("Enter a string: ")
    return user_input

# Length of input string( character count)
def character_count(intput_string):
    return len(intput_string)

# word count function
def word_count(input_string):
    words = input_string.split()
    return len(words)


#vowels count fucntion
def vowel_count(input_string):
    vowels = 'aeiouAEIOU'
    count = 0

    for char in input_string:
        if char in vowels:
            count += 1
    return count


# article count function
def article_count(input_string):
    article = ['a', 'an', 'the']
    words = input_string.lower().split()
    count = 0

    for word in words:
        if word in article:
            count += 1
    return count

#Replace string function
def replace_string(original_string, old_string, new_string):
    return original_string.replace(old_string, new_string)


# Main function
def main():
    # Get user input
    input_string = get_input()

    # Perform string manipulation
    total_characters = character_count(input_string)
    total_words = word_count(input_string)
    total_vowels = vowel_count(input_string)
    total_articles = article_count(input_string)

    # Replace string
    old_substring = input("Enter the substring to replace: ")
    new_substring = input("Enter the new substring: ")
    replaced_string = replace_string(input_string, old_substring, new_substring)


    # Display resutls  # Display results
    print("\n--- String Manipulation Results ---")
    print(f"Total characters: {total_characters}")
    print(f"Total words: {total_words}")
    print(f"Total vowels: {total_vowels}")
    print(f"Total articles: {total_articles}")
    print(f"Replaced string: {replaced_string}")


# Run the main function
if __name__ == "__main__":
    main()


