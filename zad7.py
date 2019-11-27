forbidden_words = ['się', 'oraz', 'nigdy', 'dlaczego', 'i']

with open('zad7.txt', encoding='utf-8') as in_fd, \
     open('zad7_new.txt', 'w', encoding='utf-8') as out_fd:
    for line in in_fd:
        line_wrods = line.split()
        line_wrods = ['' if lw.lower().strip('.-!?') in forbidden_words else lw for lw in line_wrods]
        new_line = ' '.join(line_wrods)
        out_fd.write(new_line + '\n')
