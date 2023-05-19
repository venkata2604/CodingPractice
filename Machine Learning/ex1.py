import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import numpy as np
music_data = pd.read_csv('C:\\Users\\avskr\\My Jupyter Data\\music.csv')
print(music_data)
x = music_data.drop(columns=['genre'])
y = music_data['genre']
print(x, y)

model = DecisionTreeClassifier()
model.fit(x, y)
predictions = model.predict([[21, 1], [22, 0]])
print(predictions)