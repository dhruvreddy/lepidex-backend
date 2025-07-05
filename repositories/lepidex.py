from abc import ABC, abstractmethod

import keras
import numpy as np
from PIL import Image
from typing import Dict
from fastapi import UploadFile, File, status
from tensorflow.keras.models import load_model

from schemas import Butterfly


class Lepidex(ABC):
    @abstractmethod
    async def predict(self, image: UploadFile = File(...)) -> Dict:
        pass

class LepidexImpl(Lepidex):
    def __init__(self):
        self.model = load_model("butterfly_v1.keras")

    async def predict(self, image: UploadFile = File(...)) -> Dict:
        try:
            image = Image.open(image.file).resize(size=[256, 256])
            image_array = np.array(image)
            final_image = np.expand_dims(image_array, axis=0)
            prediction = self.model.predict(final_image)
            prediction_argmax = np.argmax(prediction)
            return {
                "butterfly": Butterfly.butterfly_data[prediction_argmax]
            }

        except Exception as e:
            return {
                "status": status.HTTP_400_BAD_REQUEST,
                "error": f"Error at LepidexImpl, {e}"
            }