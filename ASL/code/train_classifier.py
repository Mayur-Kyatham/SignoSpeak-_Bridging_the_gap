import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np


data_dict = pickle.load(open('./data.pickle', 'rb'))

for i in np.asarray(data_dict['data']):
    print(i.shape)

data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])

x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

x_train_flat = x_train.reshape(x_train.shape[0], -1)   # NEW LINES
x_test_flat = x_test.reshape(x_test.shape[0], -1)       # NEW LINES

model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced', n_jobs=-1)

model.fit(x_train, y_train)

y_predict = model.predict(x_test)

score = accuracy_score(y_predict, y_test)

print('{}% of samples were classified correctly !'.format(score * 100))

with open('model.p', 'wb') as f:
    pickle.dump({'model': model, 'labels_dict': {0: 'A', 1: 'B', 2: 'C', 3: 'D'}}, f)  # <<<<<<<<<< ADD ALPHABET HERE >>>>>>>>

f.close()
