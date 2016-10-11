import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")



PST = PunktSentenceTokenizer()

tokenized = PST.tokenize(open("test.txt").read())

def proces_content():
	try:

		for i in tokenized:
			words = nltk.word_tokenize(i)
			tagged = nltk.pos_tag(words)
			print(tagged)
	except Exception as e:
		print(str(e))

proces_content()
