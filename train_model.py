import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

data = {
    "length": [54, 23, 120, 45, 200, 30, 15, 140],
    "dots": [3, 1, 6, 2, 8, 1, 1, 7],
    "ip": [1, 0, 1, 0, 1, 0, 0, 1],
    "https": [0, 1, 0, 1, 0, 1, 1, 0],
    "at": [1, 0, 1, 0, 1, 0, 0, 1],
    "label": [1, 0, 1, 0, 1, 0, 0, 1]
}

df = pd.DataFrame(data)

X = df.drop("label", axis=1)
y = df["label"]

model = RandomForestClassifier()
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ model.pkl created")
