import uvicorn
from fastapi import FastAPI, File, UploadFile
from Model import ChestScanModel
from app_components import read_imagefile

app = FastAPI()
model = ChestScanModel()

@app.post("/predict/image")
async def predict_api(file: UploadFile = File(...)):
    '''
    read image from file upload (should be a chest CT scan) and predict tumor class based on the image
    '''
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg or png format!"
    image = read_imagefile(await file.read())
    res = model.predict_diagnosis(image)
    return {'prediction': res}


if __name__=='__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)