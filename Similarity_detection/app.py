from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from starlette.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
from similarity import similar_k
import cv2

app = FastAPI()

app.mount("/celio", StaticFiles(directory="celio"), name="celio")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def wel(request:Request):
    return {"Hello welcome to Fashion Recommendation system"}


@app.get("/{image_id}/{k}",response_class=HTMLResponse)
async def root(request:Request,image_id:str,k:int):

    original_image = {
        "id" : image_id
    }

    print(image_id)
    recod = similar_k(image_id,k)

    recommended_image = {
        "id1":str(recod[0]),
        "id2":str(recod[1]),
        "id3":str(recod[2]),
        "id4":str(recod[3]),
        "id5":str(recod[4])
    }

    return templates.TemplateResponse("temp.html",{"request":request,"original_image":original_image,"recommended_image":recommended_image})

    