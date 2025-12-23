def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    characters = text.split()
    num_characters = len(characters)
    return len(characters)

def get_counts(text):
    lower_case = text.lower()
    counts = {}
    for ch in lower_case:
        if ch not in counts:
            counts[ch] = 1
        else:
            counts[ch] += 1
    return counts 

def sort_on(item):
    return item["num"]


def chars_to_list(counts):
    char_list = []
    for char, value in counts.items():
        # char is the character
        #value is how many times it appears
        char_list.append({"char": char, "num": value})
    char_list.sort(reverse=True, key=sort_on)
    return char_list 






