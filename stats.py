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

def sort_counts(dic):
    unkeyed_counts = []
    list_of_dic = []
    
    for key in dic:
        unkeyed_counts.append(dic[key])
    unkeyed_counts.sort(reverse=True)
    for n in unkeyed_counts:
        for key in dic:
            if dic[key] == n and key.isalpha():
                list_of_dic.append({key:n})
    return list_of_dic