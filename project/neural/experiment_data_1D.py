from keras.layers import Dense
from keras.utils import plot_model


from project.generator.gen1D.dataset_generator_1D import data
from keras.models import Sequential
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split

dataset = pd.read_csv('toast_data.csv', delimiter=',', error_bad_lines=False)

X = dataset.iloc[:, 0:9].values
Y = dataset.iloc[:, 9].values

# encoding categorical data
lbl_encoder = LabelEncoder()
for i in range(0, 9):
    X[:, i] = lbl_encoder.fit_transform(X[:, i])

# Dummy variable trap???
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Standardization
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# NN
model = Sequential()

model.add(Dense(units=5, kernel_initializer='uniform', activation='relu', input_dim=9))
model.add(Dense(units=5, kernel_initializer='uniform', activation='relu'))
model.add(Dense(units=1, kernel_initializer='uniform', activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(X_train, Y_train, batch_size=10, epochs=10)

plot_model(model, to_file='model.png')

y_pred = model.predict(X_test)
y_pred = (y_pred > 0.5)

a = 1
