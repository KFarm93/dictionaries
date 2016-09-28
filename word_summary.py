txt = open('programmers_blues.txt')
txtLines = txt.readlines()

wordCount = {}

for line in txtLines:
    for word in line.split():
        word = word.replace('.', '').replace('(', '').replace(')', '')
        wordCount[word] = wordCount.get(word, 0) + 1

    for word, count in wordCount.items():
        print "%d %s's" % (count, word)
