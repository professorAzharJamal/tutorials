import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, LSTM, Embedding, Dropout, add
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Assume the following dummy data
captions = {
    'image1.jpg': ['startseq a dog is running endseq', 'startseq dog running endseq'],
    'image2.jpg': ['startseq a cat is sleeping endseq', 'startseq cat sleeping endseq']
}

# Load pre-trained CNN (VGG16) for feature extraction
def extract_features(image_path):
    model = VGG16()
    model = Model(inputs=model.inputs, outputs=model.layers[-2].output)
    image = load_img(image_path, target_size=(224, 224))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)
    feature = model.predict(image, verbose=0)
    return feature

# Prepare image features
image_features = {}
for img in captions.keys():
    image_features[img] = extract_features(img)

# Prepare tokenizer for captions
all_captions = []
for key in captions.keys():
    for cap in captions[key]:
        all_captions.append(cap)

tokenizer = Tokenizer()
tokenizer.fit_on_texts(all_captions)
vocab_size = len(tokenizer.word_index) + 1
max_length = max(len(cap.split()) for cap in all_captions)

# Create input-output sequences for training
def create_sequences(tokenizer, max_length, desc_list, photo):
    X1, X2, y = [], [], []
    for desc in desc_list:
        seq = tokenizer.texts_to_sequences([desc])[0]
        for i in range(1, len(seq)):
            in_seq, out_seq = seq[:i], seq[i]
            in_seq = pad_sequences([in_seq], maxlen=max_length)[0]
            out_seq = to_categorical([out_seq], num_classes=vocab_size)[0]
            X1.append(photo)
            X2.append(in_seq)
            y.append(out_seq)
    return np.array(X1), np.array(X2), np.array(y)

# Prepare data
X1, X2, y = [], [], []
for key, desc_list in captions.items():
    photo = image_features[key][0]
    in_img, in_seq, out_word = create_sequences(tokenizer, max_length, desc_list, photo)
    X1.append(in_img)
    X2.append(in_seq)
    y.append(out_word)
X1, X2, y = np.vstack(X1), np.vstack(X2), np.vstack(y)

# Define the image captioning model
inputs1 = Input(shape=(4096,))
fe1 = Dropout(0.5)(inputs1)
fe2 = Dense(256, activation='relu')(fe1)

inputs2 = Input(shape=(max_length,))
se1 = Embedding(vocab_size, 256, mask_zero=True)(inputs2)
se2 = Dropout(0.5)(se1)
se3 = LSTM(256)(se2)

decoder1 = add([fe2, se3])
decoder2 = Dense(256, activation='relu')(decoder1)
outputs = Dense(vocab_size, activation='softmax')(decoder2)

model = Model(inputs=[inputs1, inputs2], outputs=outputs)
model.compile(loss='categorical_crossentropy', optimizer='adam')

# Train the model
model.fit([X1, X2], y, epochs=10, batch_size=64)

# Function to generate caption for an image
def generate_caption(model, tokenizer, photo, max_length):
    in_text = 'startseq'
    for i in range(max_length):
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        sequence = pad_sequences([sequence], maxlen=max_length)
        yhat = model.predict([photo, sequence], verbose=0)
        yhat = np.argmax(yhat)
        word = [word for word, index in tokenizer.word_index.items() if index == yhat]
        if not word:
            break
        word = word[0]
        in_text += ' ' + word
        if word == 'endseq':
            break
    return in_text

# Example usage
image_path = 'image1.jpg'
photo = extract_features(image_path)
caption = generate_caption(model, tokenizer, photo, max_length)
print(f'Generated caption: {caption}')
