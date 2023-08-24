import tensorflow as tf
import numpy as np


class ChestScanModel:
    '''
    class that loads pretrained and saved model and then uses it to predict the lung cancer diagnosis based on a CT Scan.
    In this case, the model was trained in google collab, see TrainModel.ipynb.

    '''
    def __init__(self):
        path = r'C:\Users\jgrajek\ChestCancer\my_model5_xception.keras'
        self.model = tf.keras.models.load_model(path, compile=False)
        self.model.compile()


    def predict_diagnosis(self, img):
        classes = {0: 'adenocarcinoma', 1: 'large cell carcinoma', 2: 'normal', 3: 'squamous cell carcinoma'}
        img_size = 460

        img = img.convert('RGB') #images might be RGBA or grayscale, the model expects RGB
        img = np.asarray(img.resize((img_size, img_size)))
        img = np.expand_dims(img, axis=0) #model was trained with mini-batches
        idx = np.argmax(self.model.predict(img)) #model returns class probaibilities, we are interested in the most probable class
        res = classes.get(idx)
        return res
