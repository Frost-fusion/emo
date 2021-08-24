<h1>Emo- Emotion Detection</h1>
<h4>How to create environment and python repository</h4>
<hr>
Download **anaconda manager** for host os from the
<a href="https://www.anaconda.com/products/individual">link </a>

Install anconda manager System-wide or as Admin(All users).

After finishing installation:<br>
Open anaconda prompt as administrator.<br>

run command to create a conda environment for the project.

`conda create --name <env> --file <this file>`<br> 
where `<env>` is name of conda env to create and `<this file>` 
is name of requirement file.

using git clone the repo into your ide (pycharm), load the conda env 
into ide and create configration file as
`emotions.py --train` to train on data and `emotions.py --display`
to identify live data.

<hr>
Accuracy of model using various loss and optimizer function.
@@ loss='categorical_crossentropy', optimizer=tf.keras.optimizers.Nadam(learning_rate=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-07)
448/448 [==============================] - 14s 31ms/step - loss: 0.7229 - accuracy: 0.7324 - val_loss: 1.0764 - val_accuracy: 0.6218

@@loss='categorical_crossentropy', optimizer=tf.keras.optimizers.Adam(learning_rate=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-07)
448/448 [==============================] - 11s 25ms/step - loss: 0.9753 - accuracy: 0.6358 - val_loss: 1.0653 - val_accuracy: 0.5968

@@loss='categorical_crossentropy', optimizer=tf.keras.optimizers.Adamax(learning_rate=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-07)
448/448 [==============================] - 11s 25ms/step - loss: 1.0400 - accuracy: 0.6085 - val_loss: 1.0936 - val_accuracy: 0.5871


@@loss='sparse_categorical_crossentropy', optimizer=tf.keras.optimizers.Adamax(learning_rate=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-07
448/448 [==============================] - 14s 31ms/step - loss: 1.0347 - accuracy: 0.6171 - val_loss: 1.1034 - val_accuracy: 0.5818

@@loss='sparse_categorical_crossentropy', optimizer=tf.keras.optimizers.Adam(learning_rate=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-07
448/448 [==============================] - 14s 31ms/step - loss: 0.9253 - accuracy: 0.6512 - val_loss: 1.0545 - val_accuracy: 0.6105

@@loss='sparse_categorical_crossentropy', optimizer=tf.keras.optimizers.Nadam(learning_rate=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-07
448/448 [==============================] - 14s 31ms/step - loss: 0.8193 - accuracy: 0.6924 - val_loss: 1.0368 - val_accuracy: 0.6150


@@loss='MeanSquaredError', optimizer=tf.keras.optimizers.Nadam(learning_rate=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-07
448/448 [==============================] - 14s 32ms/step - loss: 0.0669 - accuracy: 0.6573 - val_loss: 0.0752 - val_accuracy: 0.5951

@@loss='MeanSquaredError', optimizer=tf.keras.optimizers.Adam(learning_rate=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-07
448/448 [==============================] - 11s 25ms/step - loss: 0.0706 - accuracy: 0.6285 - val_loss: 0.0764 - val_accuracy: 0.5869br>


<br><hr>
Running Output
![Annotation 2021-08-02 204521](https://user-images.githubusercontent.com/52329399/130586928-a04c90af-d2d6-47ab-9cd7-57f1293588ae.png)
![Annotation 2021-08-02 204540](https://user-images.githubusercontent.com/52329399/130586971-c31667a2-ae51-4db1-83bc-6b68bfdea044.png)

