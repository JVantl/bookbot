def word_count(text):
        words = text.split()
        return len(words)

def characters(text):
    character_count = {}
    for c in text:
        lowered = c.lower()
        if lowered in character_count:
            character_count [lowered] += 1
        else: 
            character_count [lowered] = 1
    return character_count
def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    
