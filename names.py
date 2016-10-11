import nltk 
from nltk.tag.perceptron import PerceptronTagger
from nameparser.parser import HumanName
import matplotlib

# tagger = PerceptronTagger(load=False)
# tagger.load('model.perc.dutch_tagger_small.pickle')
# with open('sample.txt', 'r') as f:
# #     sample = f.read()

sample = open('sample.txt').read()
# sentences = nltk.sent_tokenize(sample)
# tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
# tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
# chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)

# def extract_entity_names(t):
#     entity_names = []

#     if hasattr(t, 'label') and t.label:
#         if t.label() == 'NE':
#             entity_names.append(' '.join([child[0] for child in t]))
#         else:
#             for child in t:
#                 entity_names.extend(extract_entity_names(child))

#     return entity_names

# entity_names = []

# for tree in chunked_sentences:
#     # Print results per sentence
#     # print extract_entity_names(tree)

#     # print(tree)

#     entity_names.extend(extract_entity_names(tree))

# # Print all entity names
# # print(entity_names)

# # Print unique entity names
# print(set(entity_names))


from nltk.tag.stanford import NERTagger
nltk.tag.stanford as st

tagger = st.StanfordNERTagger(PATH_TO_GZ, PATH_TO_JAR)





import os
java_path = "/Java/jdk1.8.0_45/bin/java.exe"
os.environ['JAVAHOME'] = java_path
st = NERTagger('../ner-model.ser.gz','../stanford-ner.jar')

tagging = st.tag(sample.split())   










# kan deze nog niet gebruiken omdat deze andere POS-tags teruggeeft dan nltk.pos_tag
# tagged_sentences = [tagger.tag(sentence) for sentence in tokenized_sentences]
# print(tagged_sentences)

# for sentence in sentences:
#     words = nltk.word_tokenize(sentence)
#     tagged = nltk.pos_tag(words)
#     chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP.?><NN>?}"""
#     chunkParser = nltk.RegexpParser(chunkGram)
#     chunked = chunkParser.parse(tagged)
#     chunked.draw()







# def get_human_names(text):
#     tokens = nltk.tokenize.word_tokenize(text)
#     pos = nltk.pos_tag(tokens)
#     sentt = nltk.ne_chunk(pos, binary = False)
#     person_list = []
#     person = []
#     name = ""
#     for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
#         for leaf in subtree.leaves():
#             person.append(leaf[0])
#         if len(person) > 1: #avoid grabbing lone surnames
#             for part in person:
#                 name += part + ' '
#             if name[:-1] not in person_list:
#                 person_list.append(name[:-1])
#             name = ''
#         person = []

#     return (person_list)

# text = """
# Deze beschikking is gegeven door de vice-president E.J. Numann als voorzitter en de raadsheren C.A. Streefkerk, A.H.T. Heisterkamp, C.E. Drion en G. de Groot, en in het openbaar uitgesproken door de raadsheer G. de Groot op 4 april 2014.
# """


# names = get_human_names(text)
# print("LAST, FIRST")
# for name in names: 
#     last_first = HumanName(name).last + ', ' + HumanName(name).first
#     print(last_first)