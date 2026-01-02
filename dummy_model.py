from sklearn.linear_model import LinearRegression
import joblib
import numpy as np

X = np.array([[1,2,3],[2,3,4],[3,4,5],[4,5,6]])
y = np.array([10,15,20,25])

model = LinearRegression()
model.fit(X,y)

joblib.dump(model, "model.pkl")
print("Model saved as model.pkl")