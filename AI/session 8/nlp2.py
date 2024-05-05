import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

def preprocess(text):
    tokens = word_tokenize(text)
    tagged_words = pos_tag(tokens)
    return tagged_words

def main():
    text = input("Enter a sentence: ")
    processed_text = preprocess(text)
    print("Processed Text:", processed_text)

if __name__ == "__main__":
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    main()