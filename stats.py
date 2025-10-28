def get_num_words(string):
    split_string = string.split()
    num_words = len(split_string)
    return num_words

def count_characters(string):
    character_counts = {}
    string = string.lower()
    for c in string:
        if c not in character_counts:
            character_counts[c] = 0
        character_counts[c] += 1
    return character_counts

def count_words(string):
    word_counts = {}
    string = string.lower()
    split_string = string.split()
    for w in split_string:
        if w not in word_counts:
            word_counts[w] = 0
        word_counts[w] += 1
    return word_counts

def get_word_pairs(string):
    
    def remove_backslash_n(string):
        string = string.replace("\n", " ")
        return string
    
    string = remove_backslash_n(string)
    string = string.lower()
    
    cleaned_string = ''
    for c in string:
        if c.isalpha() or c == ' ' or c == "’" or c == "'" or c == "-" or c == '‟':
            cleaned_string += c
    

    word_pairs = []
    word_pair = ''
    space_counter = 0
    for c in cleaned_string:
        if c == " ":
            space_counter += 1
        if space_counter < 2:
            word_pair += c
        else:
            space_counter = 0
            word_pairs.append(word_pair)
            word_pair = ''
    
    def remove_blank_word_pairs(word_pairs):
        true_word_pairs = []
        
        for item in word_pairs:
            is_word_pair = False
            for c in item:
                if c != ' ' and c != '’' and c != "'" and c != "-" and c != '‟':
                    is_word_pair = True
            if is_word_pair:
                true_word_pairs.append(item)
        return true_word_pairs
    word_pairs = remove_blank_word_pairs(word_pairs)
    
    return word_pairs

def count_word_pairs(word_pairs):
    word_pair_counts = {}
    for pair in word_pairs:
        if pair not in word_pair_counts:
            word_pair_counts[pair] = 0
        word_pair_counts[pair] += 1
    return word_pair_counts

def sort_counts(dic):
    list_from_dic = []
    
    for key in dic:
        if key.isalpha():
            list_from_dic.append({key:dic[key]})

    def get_count(item):
        for k in item:
            return item[k]

    list_from_dic.sort(reverse=True, key=get_count)

    return(list_from_dic)

def sort_counts_for_word_pairs(dic):
    list_from_dic = []
    for key in dic:
        list_from_dic.append({key:dic[key]})
    def get_count(item):
        for k in item:
            return item[k]
    list_from_dic.sort(reverse=True, key=get_count)
    return(list_from_dic)

def remove_unique_word_pairs(lis):
    trimmed = []
    for dic in lis:
        for key in dic:
            if dic[key] > 1:
                trimmed.append({key:dic[key]})
    return trimmed