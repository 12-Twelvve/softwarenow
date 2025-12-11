# Question 4 
# Create a program that asks the user to input a sentence, and display: 
# • Count total words 
# • Find the longest word 
# • Display the sentence in: 
# o All uppercase 
# o All lowercase 
# o Title case (first letter of each word capitalized) 
# o Reversed 
 
# Example: 
# Input: "The quick brown fox" 
 
# Output: 
# Total words: 4 
# Longest word: Quick (5 letters) 
# Uppercase: THE QUICK BROWN FOX 
# Lowercase: the quick brown fox 
# Title case: The Quick Brown Fox 
# Reversed: xof nworb kciuq ehT 
def main():
    sentence = input("Enter the sentence: ")
    words = sentence.split()
    total_words = len(words)
    longest_word = max(words, key=len) if words else ""
    print(f"Total words: {total_words}")
    if longest_word:
        print(f"Longest word: {longest_word} ({len(longest_word)} letters)")
    print(f"Uppercase: {sentence.upper()}")
    print(f"Lowercase: {sentence.lower()}")
    print(f"Title case: {sentence.title()}")
    print(f"Reversed: {sentence[::-1]}")
if __name__ == "__main__":
    main()