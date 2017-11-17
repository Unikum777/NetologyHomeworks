import chardet
import glob

def read_words_from_file(filename):
    result = dict()
    with open(filename, 'rb') as f:
        data = f.read()
        encoding = chardet.detect(data)
        text = data.decode(encoding['encoding'])
        
        print ('File nme = {0}, encoding = {1}'.format(filename, encoding['encoding']))

        for item in text.split(" "):
            if (len(item)< 6):
                continue
            if (item in result.keys()):
                result[item] += 1
            else:
                result[item] = 1
    return result

def print_top_10_words(words):
    count = 0
    for w in sorted(words, key=words.get, reverse=True):
        print (w, words[w])
        count += 1
        if (count == 10):
            break;

for filename in glob.glob('*.txt'):
    words = read_words_from_file(filename)
    print_top_10_words(words)
    print()
