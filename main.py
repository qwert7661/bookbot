import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)



from stats import get_num_words
from stats import count_characters
from stats import sort_counts

def get_file_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        return f.read()

def main():
    
    
    filepath = sys.argv[1]
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    full_text_string = get_file_text(filepath)
    
    print("----------- Word Count ----------")
    num_words = get_num_words(full_text_string)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    character_counts = count_characters(full_text_string)
    sorted_counts = sort_counts(character_counts)
    
    for item in sorted_counts:
        for key in item:
            print(f"{key}: {item[key]}")

main()
