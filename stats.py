def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_count(char_dict):
    sorted_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            sorted_list.append({"char": char, "count": count})
    sorted_list.sort(reverse=True, key=lambda item: item["count"])
    return sorted_list

