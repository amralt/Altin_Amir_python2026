import this
from collections import Counter
from string import punctuation

def count_words():
    count = Counter()
    with open("zen.txt", 'r') as f:
        for line in f.readlines():
            for ch in punctuation:
                line = line.replace(ch, '')
            line = line.strip().lower()
            line = line.split()
            count.update(line)
    
        
    return count.most_common(10)

print(count_words())
