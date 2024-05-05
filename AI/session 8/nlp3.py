import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk

# Download NLTK resources if not already downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def process_text(text):
    # Tokenize the text into words
    tokens = word_tokenize(text)
    
    # Tag parts of speech for each word
    tagged_words = pos_tag(tokens)
    
    # Extract named entities
    named_entities = ne_chunk(tagged_words)
    
    return tagged_words, named_entities

def main():
    text = input("Enter a sentence: ")
    tagged_words, named_entities = process_text(text)
    
    print("\nTagged Words:")
    print(tagged_words)
    
    print("\nNamed Entities:")
    print(named_entities)

    """
	CC: coordinating conjunction (and, but, or)
CD: cardinal digit (one, two, three)
DT: determiner (the, a, an)
EX: existential there (there)
FW: foreign word (e.g., bonjour)
IN: preposition/subordinating conjunction (in, on, at)
JJ: adjective (big, tall, green)
JJR: adjective, comparative (bigger, taller)
JJS: adjective, superlative (biggest, tallest)
LS: list marker (1., 2., A., B.)
MD: modal (can, could, might)
NN: noun, singular or mass (dog, cat, love)
NNS: noun, plural (dogs, cats, loves)
NNP: proper noun, singular (John, Mary)
NNPS: proper noun, plural (Smiths, Johnsons)
PDT: predeterminer (all, both, half)
POS: possessive ending (’s, 's)
PRP: personal pronoun (I, you, he)
PRP$: possessive pronoun (my, your, his)
RB: adverb (quickly, very, well)
RBR: adverb, comparative (faster, better)
RBS: adverb, superlative (fastest, best)
RP: particle (up, off, out)
SYM: symbol (+, $, %)
TO: to (to)
UH: interjection (oh, wow, hey)
VB: verb, base form (eat, sleep, walk)
VBD: verb, past tense (ate, slept, walked)
VBG: verb, gerund/present participle (eating, sleeping)
VBN: verb, past participle (eaten, slept)
VBP: verb, non-3rd person singular present (eat, sleep)
VBZ: verb, 3rd person singular present (eats, sleeps)
WDT: wh-determiner (which, that)
WP: wh-pronoun (what, who, whom)
WP$: possessive wh-pronoun (whose, whose)
WRB: wh-adverb (where, when, why)
"""
if __name__ == "__main__":
    main()
