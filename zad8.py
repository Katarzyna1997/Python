forbidden_words = {
    'i': 'oraz', 
    'oraz': 'i', 
    'nigdy': 'prawie nigdy', 
    'dlaczego': 'czemu',
}


def remove_words(item):
    this_item = item.lower().strip('.-!?')
    return  forbidden_words[this_item] if this_item in forbidden_words.keys() else item


with open('zad8.txt', encoding='utf-8') as in_fd, \
     open('zad8_new.txt', 'w', encoding='utf-8') as out_fd:
     for line in in_fd:
        line_words = line.split()
        line_words = map(remove_words, line_words)
        out_fd.write(' '.join(line_words)+ '\n')
