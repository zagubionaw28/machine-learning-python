# Small LSTM Network to Generate Text for Alice in Wonderland
import numpy as np
from nltk.tokenize import wordpunct_tokenize
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import LSTM
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.utils import to_categorical
# load ascii text and covert to lowercase
filename = "wonderland.txt"
raw_text = open(filename, 'r', encoding='utf-8').read()
raw_text = raw_text.lower()
# create mapping of unique chars to integers
tokenized_text = wordpunct_tokenize(raw_text)
tokens = sorted(list(dict.fromkeys(tokenized_text)))

#print("Tokens: ")
#print(tokens)
tok_to_int = dict((c, i) for i, c in enumerate(tokens))
#print("TokensToNumbers: ")
print(tok_to_int)

# summarize the loaded data
n_tokens = len(tokenized_text)
n_token_vocab = len(tokens)
print("Total Tokens: ", n_tokens)
print("Unique Tokens (Token Vocab): ", n_token_vocab)

# prepare the dataset of input to output pairs encoded as integers
seq_length = 100
dataX = []
dataY = []
for i in range(0, n_tokens - seq_length, 1):
	seq_in = tokenized_text[i:i + seq_length]
	seq_out = tokenized_text[i + seq_length]
	dataX.append([tok_to_int[tok] for tok in seq_in])
	dataY.append(tok_to_int[seq_out])
n_patterns = len(dataX)
print("Total Patterns: ", n_patterns)
# reshape X to be [samples, time steps, features]
X = np.reshape(dataX, (n_patterns, seq_length, 1))
# normalize
X = X / float(n_token_vocab)
# one hot encode the output variable
y = to_categorical(dataY)
# define the LSTM model
model = Sequential()
model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2])))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation='softmax'))
# filename = "big-token-model-30-2.3772.keras"
# model.load_weights(filename)
model.compile(loss='categorical_crossentropy', optimizer='adam')
# define the checkpoint
filepath="big-token-model.keras" #* stała nazwa pliku pozwoli na jego nadpisanie w celu zaoszczędzenia miejsca na dysku.
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]
# fit the model
model.fit(X, y, epochs=5, batch_size=128, callbacks=callbacks_list)

# Total Tokens:  38030
# Unique Tokens (Token Vocab):  3236
# Total Patterns:  37930

# Epoch 1/5
# 297/297 ━━━━━━━━━━━━━━━━━━━━ 0s 514ms/step - loss: 6.4172  
# Epoch 1: loss improved from inf to 6.15412, saving model to big-token-model.keras
# 297/297 ━━━━━━━━━━━━━━━━━━━━ 155s 515ms/step - loss: 6.4163
# Epoch 2/5
# 297/297 ━━━━━━━━━━━━━━━━━━━━ 0s 492ms/step - loss: 5.9698  
# Epoch 2: loss improved from 6.15412 to 5.97523, saving model to big-token-model.keras
# 297/297 ━━━━━━━━━━━━━━━━━━━━ 147s 493ms/step - loss: 5.9698
# token-model.keras
# 297/297 ━━━━━━━━━━━━━━━━━━━━ 148s 498ms/step - loss: 5.9601
# Epoch 4/5
# 297/297 ━━━━━━━━━━━━━━━━━━━━ 0s 489ms/step - loss: 5.9190
# Epoch 4: loss improved from 5.95856 to 5.93433, saving model to big-token-model.keras
# 297/297 ━━━━━━━━━━━━━━━━━━━━ 146s 490ms/step - loss: 5.9191
# Epoch 5/5
# 297/297 ━━━━━━━━━━━━━━━━━━━━ 0s 489ms/step - loss: 5.8869
# Epoch 5: loss improved from 5.93433 to 5.89718, saving model to big-token-model.keras
# 297/297 ━━━━━━━━━━━━━━━━━━━━ 146s 489ms/step - loss: 5.8869


# Przykład co zwraca :
#  'www': 3184, 'x': 3185, 'xi': 3186, 'xii': 3187, 'yard': 3188, 'yards': 3189, 'yawned': 3190, 'yawning': 3191, 'ye': 3192, 'year': 3193, 'years': 3194, 'yelled': 3195, 'yelp': 3196, 'yer': 3197, 'yes': 3198, 'yesterday': 3199, 'yet': 3200, 'you': 3201, 'you_': 3202, 'young': 3203, 'your': 3204, 'yours': 3205, 'yourself': 3206, 'youth': 3207, 'zealand': 3208, 'zigzag': 3209, 'zip': 3210, '—': 3211, '—(': 3212, '—]': 3213, '—‘': 3214, '—’': 3215, '—’”': 3216, '—“': 3217, '—”': 3218, '‘': 3219, '‘’': 3220, '’': 3221, '’!”': 3222, '’?”': 3223, '’—': 3224, '“': 3225, '“—': 3226, '“‘': 3227, '“‘—': 3228, '“’': 3229, '”': 3230, '”)': 3231, '”,': 3232, '”;': 3233, '”—': 3234, '\ufeff': 3235}