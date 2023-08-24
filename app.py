import uvicorn
from fastapi import FastAPI, File, UploadFile, Request
from Model import ChestScanModel
from app_components import read_imagefile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()
model = ChestScanModel()

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "pythonProject/static"),
    name="static",
)

templates = Jinja2Templates(directory="templates")

@app.post("/predict")
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


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


if __name__=='__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)