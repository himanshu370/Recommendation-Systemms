from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from starlette.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
from similarity1 import similar_k
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
    top,bottom = similar_k(image_id,k)

    topwear_image = {
        "id1":str(top[0]),
        "id2":str(top[1]),
        "id3":str(top[2]),
        "id4":str(top[3]),
        "id5":str(top[4])
    }

    bottomwear_image = {
        "id1":str(bottom[0]),
        "id2":str(bottom[1]),
        "id3":str(bottom[2]),
        "id4":str(bottom[3]),
        "id5":str(bottom[4])
    }

    return templates.TemplateResponse("temp1.html",{"request":request,"original_image":original_image,"topwear_image":topwear_image,"bottomwear_image":bottomwear_image})

    