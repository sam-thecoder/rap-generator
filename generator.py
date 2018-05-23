from keras.models import load_model
import sys
import io
import numpy as np
maxlen = 50

start_text = sys.argv[1]
try:
    diversity = int(sys.argv[2])
except Exception as e:
    diversity =  0.3

try:
    length = int(sys.argv[2])
except Exception as e:
    length = 400

model = load_model('dropout_model.hd5')

#some dependencies
path = 'lyrics.txt'
with io.open(path, encoding='utf-8') as f:
    text = f.read().lower()

chars = sorted(list(set(text)))

char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))

def sample(preds, temperature=1.0):
    # helper function to sample an index from a probability array
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

def generate_rap(sentence, diversity=0.3, length=400):
    len_sentence = len(sentence)

    if len_sentence > 40:
        sentence = sentence[:41]
    elif len_sentence < 40:
        diff = maxlen - len_sentence
        extra = ' ' * diff
        sentence = extra + sentence

    generated = ''
    print('----- Generating with seed: "' + sentence + '"')
    for i in range(length):
        x_pred = np.zeros((1, maxlen, len(chars)))
        for t, char in enumerate(sentence):
            x_pred[0, t, char_indices[char]] = 1.

        preds = model.predict(x_pred, verbose=0)[0]
        next_index = sample(preds, diversity)
        next_char = indices_char[next_index]

        generated += next_char
        sentence = sentence[1:] + next_char

        sys.stdout.write(next_char)
        sys.stdout.flush()
    print('\n')

if __name__ == "__main__":
	generate_rap(start_text, diversity, length)
