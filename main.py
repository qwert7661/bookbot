import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)



from stats import *



def get_file_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        return f.read()

def main():
    
    
    filepath = sys.argv[1]
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    full_text_string = get_file_text(filepath)
    
    print("-------Total WordCount ----------")
    num_words = get_num_words(full_text_string)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    character_counts = count_characters(full_text_string)
    sorted_counts = sort_counts(character_counts)
    for item in sorted_counts:
        for key in item:
            print(f"{key}: {item[key]}")
    
    print("-------Individual Word Count-----")
    word_counts = count_words(full_text_string)
    sorted_words = sort_counts(word_counts)
    counter = 0
    for item in sorted_words:
        for key in item:
            print(f"{key:<17}: {item[key]:>4}",end=' | ')
            counter += 1
            if counter > 8: 
                counter = 0
                print()


    word_pairs = get_word_pairs(full_text_string)
    counted_word_pairs = count_word_pairs(word_pairs)
    sorted_word_pair_counts = sort_counts_for_word_pairs(counted_word_pairs)
    trimmed_word_pair_counts = remove_unique_word_pairs(sorted_word_pair_counts)
    
    print("-------- Non-Unique Word Pairs ---")
    counter = 0
    for item in trimmed_word_pair_counts:
        for key in item:
            print(f"{key:<30}: {item[key]:>3}",end=' | ')
            counter += 1
            if counter > 5:
                counter = 0
                print()
    
    # print(trimmed_word_pair_counts)




main()
