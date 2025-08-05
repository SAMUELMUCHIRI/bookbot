def count_words(text):
    words = text.split()
    return len(words)

def num_appear(text):
    new_dict={
                'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 
                'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 
                'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 
                'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
            }
    text= text.lower()
    
    for char in text:
        if char in new_dict:
            new_dict[char] += 1
    
    return new_dict

def sort_on(items):
    return items['num']

def sorted_stats(text):
    new_list = []
    for key, value in text.items():
        new_list.append({'alphabet' :key, 'num'  : value})


    new_list.sort( reverse=True , key=sort_on)
    return new_list
def report_stats(count ,sorted_list):
    print("============ BOOKBOT ============\n"
    "Analyzing book found at books/frankenstein.txt...\n"
    "----------- Word Count ----------\n"
    f"Found {count} total words\n"
    "--------- Character Count -------\n"
    )
    for item in sorted_list:
        print(f"{item['alphabet']}: {item['num']}")

    


    