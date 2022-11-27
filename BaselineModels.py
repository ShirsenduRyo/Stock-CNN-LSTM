from tensorflow.keras.models import Model

def SimpleNN():
    model = tf.keras.Sequential(name = "Simple Neural Network")
    model.add(keras.layers.Dense(10, input_shape=[window], activation="relu"))
    model.add(keras.layers.Dense(10, activation="relu"))
    model.add(keras.layers.Dense(1))
    
    model.compile(loss=tf.keras.losses.MeanSquaredError(),
              optimizer=Adam(1e-4),
              metrics=['mae'])
    
    return model