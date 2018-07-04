import sys # import sys module for <sys.argv> in order to extract input arguments from command-line.

filepath = sys.argv[1]

fo = open(filepath, "r") # open file on read mode.
listWords = fo.read().split(' ') # sperate all words with space character.
dict = {} # initial a dictionary object.

for index, word in enumerate(listWords):
	word = word.strip() # strip all characters.
	if dict.get(word) == None:
		dict[word] = {"index": index, "count": 1} # If this word is shown up in the dictionary first time, we need to record it's index in original text file and initial counter.
	else:
		dict[word]["count"] += 1 #The word is already exist in the dictionary, do count.

#listSortedDict = sorted(dict.items(), cmp=lambda x,y: cmp(x[1]["index"], y[1]["index"])) # a list that contains all of the words' information and sorted by their index.
listSortedDict = sorted(dict.items(), key=lambda x:x[1]["index"]) # a list that contains all of the words' information and sorted by their index.


fo_out = open("./Q1.txt", "w+") # open output file.
for index, item in enumerate(listSortedDict):
	word = item[0]
	count = item[1]['count']
	fo_out.write("%s %d %d" % (word, index, count)) # each line of output file must follow: <Word><space><Index><space><The number of occurences>
	if index < (len( listSortedDict ) - 1):
		fo_out.write("\n") # add newline character if there are more lines to go for output text file.

fo.close()
fo_out.close()