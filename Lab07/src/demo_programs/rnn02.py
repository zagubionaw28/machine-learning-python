import numpy as np
from keras.models import Sequential
from keras.layers import Dense, SimpleRNN


def create_RNN(hidden_units, dense_units, input_shape, activation):
    model = Sequential()
    model.add(SimpleRNN(hidden_units, input_shape=input_shape, 
                        activation=activation[0]))
    model.add(Dense(units=dense_units, activation=activation[1]))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

demo_model = create_RNN(2, 1, (3,1), activation=['linear', 'linear'])

wx = demo_model.get_weights()[0]
wh = demo_model.get_weights()[1]
bh = demo_model.get_weights()[2]
wy = demo_model.get_weights()[3]
by = demo_model.get_weights()[4]

print('wx = ', wx, ' wh = ', wh, ' bh = ', bh, ' wy =', wy, 'by = ', by)

x = np.array([1, 2, 3])
# Reshape the input to the required sample_size x time_steps x features 
x_input = np.reshape(x,(1, 3, 1))
y_pred_model = demo_model.predict(x_input)


m = 2
h0 = np.zeros(m)
h1 = np.dot(x[0], wx) + h0 + bh
h2 = np.dot(x[1], wx) + np.dot(h1,wh) + bh
h3 = np.dot(x[2], wx) + np.dot(h2,wh) + bh
o3 = np.dot(h3, wy) + by

print('h1 = ', h1,'h2 = ', h2,'h3 = ', h3)

print("Prediction from network ", y_pred_model)
print("Prediction from our computation ", o3)

# super().__init__(**kwargs)
# wx =  [[-0.9257599  -0.96423554]]  wh =  [[ 0.4424572  0.8967896]
#  [ 0.8967896 -0.4424572]]  bh =  [0. 0.]  wy = [[-0.36782062]
#  [-0.19549525]] by =  [0.]
# 1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 109ms/step
# h1 =  [[-0.92575991 -0.96423554]] h2 =  [[-3.12584538 -2.33205   ]] h3 =  [[-6.25169074 -4.66409998]]
# Prediction from network  [[3.2113101]]
# Prediction from our computation  [[3.21131015]]