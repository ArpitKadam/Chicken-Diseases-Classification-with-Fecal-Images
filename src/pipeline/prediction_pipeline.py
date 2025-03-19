import numpy as np                                        ## type: ignore
import os
from tensorflow.keras.models import load_model            ## type: ignore
from tensorflow.keras.preprocessing import image          ## type: ignore

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        model = load_model(os.path.join("models", "trained_model.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        prediction = model.predict(test_image)
        result = np.argmax(prediction, axis = 1)
        print(result)

        if result[0] == 1:
            prediction = "Healthy"
            return [{"image": prediction}]
        else:
            prediction = "Coccidiosis (Not Healthy)"
            return [{"image": prediction}]