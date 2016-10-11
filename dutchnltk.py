from nltk.tag.perceptron import PerceptronTagger

# This may take a few minutes. (But once loaded, the tagger is really fast!)
tagger = PerceptronTagger(load=False)
tagger.load('model.perc.dutch_tagger_large.pickle')

# Tag a sentence.
tagger.tag('Alle vogels zijn nesten begonnen , behalve ik en jij .'.split())