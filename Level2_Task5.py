#Write a Python program that reads a textfile and counts the occurrences of eachword in the file. Display the results inalphabetical order along with their respective counts.


from collections import Counter
# Function to count word occurrences in a text file
def count_word(filename):
    print("Inside count_word_occurrences")  # Debug print
    with open("C:/Users/lenovo/OneDrive/Desktop/Cognifyz_Task/demofile.txt", 'r') as file:
        text = file.read()
        words = text.split()
        word_count = Counter(words)
        return word_count
    

# Function to display word occurrences in alphabetical order
def display_word(word_count):
    sorted_word_count = sorted(word_count.items())
    for word, count in sorted_word_count:
        print(f'{word}: {count}')

# Main program
if __name__ == "__main__":
    filename = "C:/Users/lenovo/OneDrive/Desktop/Cognifyz_Task/demofile.txt"  # Replace with the path to your text file
    word_count = count_word(filename)
    display_word(word_count)
