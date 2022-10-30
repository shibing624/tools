# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
# -*- coding:utf-8 -*-
import uuid
import uvicorn
import os
import base64
from loguru import logger
from fastapi import Body
from fastapi import FastAPI, File, UploadFile
from starlette.responses import RedirectResponse
from PIL import Image

app = FastAPI()


@app.get("/")
def root():
    response = RedirectResponse(url="/docs")
    return response


@app.post("/uploadfile/")
async def uploadfile(image: UploadFile = File(...)):
    try:
        if not os.path.exists("images"):
            os.makedirs("images")
    except Exception as e:
        print(e)
    suffix_arr = image.filename.split(".")
    suffix = suffix_arr[len(suffix_arr) - 1]
    file_name = os.getcwd() + "/images/" + str(uuid.uuid1()) + "." + suffix

    with open(file_name, "wb+") as f:
        f.write(image.file.read())
        logger.debug(f"{file_name} upload success.")
    try:
        img = Image.open(file_name)
        width, height = img.size
        channel_mode = img.mode
        imgGrey = img.convert('L')
        img_grey_file_name = os.getcwd() + "/images/img_gray_" + str(uuid.uuid1()) + "." + suffix
        imgGrey.save(img_grey_file_name)
        logger.info('saved img_grey_file_name: %s' % img_grey_file_name)

        face_locations = f"{width},{height}"
        if os.path.exists(file_name):
            os.remove(file_name)
        if len(face_locations) > 0:
            return {"code": 0, "obj": face_locations}
        else:
            return {"code": 1, "obj": face_locations}
    except Exception as e:
        return {"code": 1, "obj": [], "msg": str(e)}


@app.post("/base64file")
async def base64file(image=Body(None), suffix=Body(None)):
    if not suffix:
        suffix = 'jpg'
    imgdata = base64.b64decode(image)
    file_name = os.getcwd() + "/images/" + str(uuid.uuid1()) + "." + suffix
    with open(file_name, "wb") as f:
        f.write(imgdata)
        logger.debug(f"{file_name} upload success.")
    try:
        img = Image.open(file_name)
        width, height = img.size
        channel_mode = img.mode
        imgGrey = img.convert('L')
        img_grey_file_name = os.getcwd() + "/images/img_gray_" + str(uuid.uuid1()) + "." + suffix
        imgGrey.save(img_grey_file_name)

        face_locations = f"{width},{height}"
        if os.path.exists(file_name):
            os.remove(file_name)
        if len(face_locations) > 0:
            return {"code": 0, "obj": face_locations}
        else:
            return {"code": 1, "obj": face_locations}
    except Exception as e:
        return {"code": 1, "obj": [], "msg": str(e)}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001, debug=True)
