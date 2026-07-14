import pickle

model=pickle.load(open("model.pkl","rb"))
scaler=pickle.load(open("scaler.pkl","rb"))

def predict(student):

    student=scaler.transform([student])

    result=model.predict(student)

    return result[0]
