def get_num_words(text):
    return len(text.split())

def frequency_counter(text):
    counter = {}
    
    for char in text:
        if char.lower() not in counter:
            counter[char.lower()] = 1
        else:
            counter[char.lower()] += 1
    
    return counter

def sort_on(items):
    return list(items.values())[0]

def sort_dict(dict):
    new_list = []
    
    for key in dict:
        new_list.append({ key : dict[key] })
    
    return sorted(new_list, reverse=True, key=sort_on)

def print_report(total_words, words_list):
    print(f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {total_words} total words
--------- Character Count -------""")
    
    for value in words_list:
        for k, v in value.items():
            if k.isalpha():
                print(f"{k}: {v}")
    
    print("============= END ===============")