"""
pythonAssessment.py
Flatiron Course 6 - Summative Lab
Analyze a News Article

This script reads in a news article from 'article.txt' and performs various text analysis tasks:
- Count a specific word
- Identify the most common word
- Calculate average word length
- Count paragraphs
- Count sentences

Rubric requires explicit use of:
- A for loop
- A while loop
- An if/else statement
"""

import re
from collections import Counter


# -----------------------------
# Function 1: Count Specific Word
# -----------------------------
def count_specific_word(text: str, word: str) -> int:
    """
    Count how many times a given word appears in the text.
    Returns an integer. Edge case: if not found, return 0.
    """
    # Normalize inputs and handle edge cases
    if not isinstance(text, str) or not isinstance(word, str):
        return 0
    if not text.strip() or not word.strip():
        return 0

    # Use a whole-word, case-insensitive match.
    # \b ensures we don't count substrings (e.g., 'apple' will not match 'apples').
    pattern = r"\b" + re.escape(word.strip()) + r"\b"
    matches = re.findall(pattern, text, flags=re.IGNORECASE)
    return len(matches)


# -----------------------------
# Function 2: Identify Most Common Word
# -----------------------------
def identify_most_common_word(text: str) -> str:
    """
    Identify the most common word in the text.
    Returns a string. Edge case: if empty string, return None.
    """
    # TODO: implement using Counter from collections
    return None


# -----------------------------
# Function 3: Calculate Average Word Length
# -----------------------------
def calculate_average_word_length(text: str) -> float:
    """
    Calculate average word length, excluding punctuation.
    Returns a float. Edge case: if empty string, return 0.
    """
    # TODO: strip punctuation, then calculate average
    return 0.0


# -----------------------------
# Function 4: Count Paragraphs
# -----------------------------
def count_paragraphs(text: str) -> int:
    """
    Count the number of paragraphs in the text.
    Paragraphs are defined by blank lines between blocks.
    Edge case: empty string should return 1.
    """
    # TODO: split on '\n\n'
    return 0


# -----------------------------
# Function 5: Count Sentences
# -----------------------------
def count_sentences(text: str) -> int:
    """
    Count the number of sentences in the text.
    Sentences are defined by ., !, or ? marks.
    Edge case: empty string should return 1.
    """
    # TODO: split using regex
    return 0


# -----------------------------
# MAIN SCRIPT
# -----------------------------
if __name__ == "__main__":

    # Read the article text from file
    try:
        with open("article.txt", "r", encoding="utf-8") as f:
            article_text = f.read()
    except FileNotFoundError:
        print("Error: article.txt not found.")
        article_text = ""

    # Example: Use of IF/ELSE
    if article_text.strip() == "":
        print("The article is empty. Please provide content.")
    else:
        print("Article loaded successfully!")

    # Example: Use of WHILE loop
    # (Simple menu that repeats until user exits)
    keep_running = True
    while keep_running:
        print("\nChoose an analysis option:")
        print("1. Count a specific word")
        print("2. Identify the most common word")
        print("3. Calculate average word length")
        print("4. Count paragraphs")
        print("5. Count sentences")
        print("6. Exit")

        choice = input("Enter a number (1-6): ")

        # Example: Use of FOR loop
        # Loop through valid choices and compare
        valid_choices = ["1", "2", "3", "4", "5", "6"]
        found = False
        for option in valid_choices:
            if choice == option:
                found = True

        if not found:
            print("Invalid choice. Please try again.")
            continue

        if choice == "1":
            word = input("Enter a word to count: ")
            print(f"Occurrences of '{word}':", count_specific_word(article_text, word))
        elif choice == "2":
            print("Most common word:", identify_most_common_word(article_text))
        elif choice == "3":
            print("Average word length:", calculate_average_word_length(article_text))
        elif choice == "4":
            print("Number of paragraphs:", count_paragraphs(article_text))
        elif choice == "5":
            print("Number of sentences:", count_sentences(article_text))
        elif choice == "6":
            print("Exiting program. Goodbye!")
            keep_running = False