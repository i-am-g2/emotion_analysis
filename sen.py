file = open ("data.txt","r")
parsed = open ("parsed.txt", "w")
wordlist = file.readlines() 
i = 0
finallist = []
import re
for sentance in wordlist:
	sentance = re.split(r'\s',sentance)
	strin = float(sentance[-2])
	if (strin<0.5):
		continue
	else:
		for words in sentance:
			if (words.startswith('#')):
				sentance.remove(words)
			if (words.startswith('@')):
				sentance.remove(words)
			#if (words.startswith(r'\\')):
			#	sentance.remove(words)
	sentance.pop(0)
	sentance.pop(-2)
	sentance.pop(-1)
	#sentance = sentance.filter()
	sense = sentance.pop()
	sentance.insert(0, sense)
	finallist.append(' '.join(sentance)) 
for x in finallist:
		parsed.write(x)
		parsed.write('\n')
