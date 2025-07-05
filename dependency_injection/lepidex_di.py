from fastapi import Depends, UploadFile, File
from repositories import LepidexImpl

def get_lepidex():
    return LepidexImpl()

async def prediction_di(lepidex: LepidexImpl = Depends(get_lepidex), image: UploadFile = File(...)):
    return await lepidex.predict(image=image)