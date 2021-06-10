# pip install spacy-universal-sentence-encoder
# python -m spacy download en_core_web_lg
# python -m spacy download en_core_web_sm

# load as before
import spacy
nlp = spacy.load('en_core_web_lg')
nlp.add_pipe('universal_sentence_encoder')

# get two documents
doc_1 = nlp('Inspect the shape of the Doc')
doc_2 = nlp('Hello there, how are you doing today?')
# Inspect the shape of the Doc, Span and Token vectors
print(doc_1.vector.shape) # the full document representation
print(doc_1[3], doc_1[3].vector.shape) # the word "how"
print(doc_1[3:6], doc_1[3:6].vector.shape) # the span "how are you"

# or use the similarity method that is based on the vectors, on Doc, Span or Token
print(doc_1.similarity(doc_2[0:7]))