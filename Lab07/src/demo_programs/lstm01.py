from pandas import read_csv
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import math
import matplotlib.pyplot as plt

# Parameter split_percent defines the ratio of training examples
def get_train_test(url, split_percent=0.8):
    df = read_csv(url, usecols=[1], engine='python')
    data = np.array(df.values.astype('float32'))
    scaler = MinMaxScaler(feature_range=(0, 1))
    data = scaler.fit_transform(data).flatten()
    n = len(data)
    # Point for splitting data into train and test
    split = int(n*split_percent)
    train_data = data[range(split)]
    test_data = data[split:]
    return train_data, test_data, data
 
# Prepare the input X and target Y
def get_XY(dat, time_steps):
    Y_ind = np.arange(time_steps, len(dat), time_steps)
    Y = dat[Y_ind]
    rows_x = len(Y)
    X = dat[range(time_steps*rows_x)]
    X = np.reshape(X, (rows_x, time_steps, 1))    
    return X, Y
 
def create_LSTM(hidden_units, dense_units, input_shape, activation):
    model = Sequential()
    model.add(LSTM(hidden_units, input_shape=input_shape))
    model.add(Dense(units=dense_units, activation=activation))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model
 
def print_error(trainY, testY, train_predict, test_predict):    
    # Error of predictions
    train_rmse = math.sqrt(mean_squared_error(trainY, train_predict))
    test_rmse = math.sqrt(mean_squared_error(testY, test_predict))
    # Print RMSE
    print('Train RMSE: %.3f RMSE' % (train_rmse))
    print('Test RMSE: %.3f RMSE' % (test_rmse))    
 
# Plot the result
def plot_result(trainY, testY, train_predict, test_predict):
    actual = np.append(trainY, testY)
    predictions = np.append(train_predict, test_predict)
    rows = len(actual)
    plt.figure(figsize=(15, 6), dpi=80)
    plt.plot(range(rows), actual)
    plt.plot(range(rows), predictions)
    plt.axvline(x=len(trainY), color='r')
    plt.legend(['Actual', 'Predictions'])
    plt.xlabel('Observation number after given time steps')
    plt.ylabel('Sunspots scaled')
    plt.title('Actual and Predicted Values. The Red Line Separates The Training And Test Examples')
    filename = 'lstm_plot.png'
    plt.savefig(filename)
    plt.close()

sunspots_url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/monthly-sunspots.csv'
time_steps = 12
train_data, test_data, data = get_train_test(sunspots_url)
trainX, trainY = get_XY(train_data, time_steps)
testX, testY = get_XY(test_data, time_steps)
 
# Create model and train
model = create_LSTM(hidden_units=5, dense_units=1, input_shape=(time_steps,1), 
                   activation='tanh')
model.fit(trainX, trainY, epochs=20, batch_size=1, verbose=2)
 
# make predictions
train_predict = model.predict(trainX)
test_predict = model.predict(testX)
 
# Print error
print_error(trainY, testY, train_predict, test_predict)
 
#Plot result
plot_result(trainY, testY, train_predict, test_predict)


# Epoch 1/20
# 187/187 - 1s - 7ms/step - loss: 0.0254
# Epoch 2/20
# 187/187 - 0s - 2ms/step - loss: 0.0105
# Epoch 3/20
# 187/187 - 0s - 2ms/step - loss: 0.0061
# Epoch 4/20
# 187/187 - 0s - 2ms/step - loss: 0.0050
# Epoch 5/20
# 187/187 - 0s - 2ms/step - loss: 0.0050
# Epoch 6/20
# 187/187 - 0s - 2ms/step - loss: 0.0044
# Epoch 7/20
# 187/187 - 0s - 2ms/step - loss: 0.0047
# Epoch 8/20
# 187/187 - 0s - 2ms/step - loss: 0.0045
# Epoch 9/20
# 187/187 - 0s - 2ms/step - loss: 0.0045
# Epoch 10/20
# 187/187 - 0s - 2ms/step - loss: 0.0043
# Epoch 11/20
# 187/187 - 0s - 2ms/step - loss: 0.0042
# Epoch 12/20
# 187/187 - 0s - 2ms/step - loss: 0.0042
# Epoch 13/20
# 187/187 - 0s - 2ms/step - loss: 0.0040
# Epoch 14/20
# 187/187 - 0s - 2ms/step - loss: 0.0039
# Epoch 15/20
# 187/187 - 0s - 3ms/step - loss: 0.0040
# Epoch 16/20
# 187/187 - 0s - 2ms/step - loss: 0.0039
# Epoch 17/20
# 187/187 - 1s - 3ms/step - loss: 0.0040
# Epoch 18/20
# 187/187 - 0s - 3ms/step - loss: 0.0039
# Epoch 19/20
# 187/187 - 0s - 3ms/step - loss: 0.0039
# Epoch 20/20
# 187/187 - 0s - 3ms/step - loss: 0.0038
# 6/6 ━━━━━━━━━━━━━━━━━━━━ 0s 23ms/step 
# 2/2 ━━━━━━━━━━━━━━━━━━━━ 0s 4ms/step 
# Train RMSE: 0.060 RMSE
# Test RMSE: 0.088 RMSE