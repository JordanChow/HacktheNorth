import sys
sys.path.append("./EmoPy/src")
from fermodel import FERModel
POSSIBLE_EMOTIONS =  ['surprise', 'sadness', 'disgust']

print('Predicting...')


def predict_Image(target_emotions,img):
    model = FERModel(target_emotions, verbose=True)
    model.predict(img)
