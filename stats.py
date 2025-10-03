def get_num_words(text):
    words = text.split()
    return len(words)

def get_times_characters(text):
    times_characters = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in times_characters:
            times_characters[lower_char] += 1
        else:
            times_characters[lower_char] = 1
    return times_characters

def get_sorted_characters(times_characters):
   sorted_characters = []
   for char, count in times_characters.items():
       sorted_characters.append({"char": char, "num": count})
   return sorted(sorted_characters, key=lambda item: item["num"], reverse=True)