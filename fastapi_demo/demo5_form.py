# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import uuid
import os
import base64
from fastapi import Body
from fastapi import FastAPI, File, Form, UploadFile
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/web", StaticFiles(directory="web"), name="web")


@app.post("/files/")
async def create_file(
        file: bytes = File(), fileb: UploadFile = File(), token: str = Form()
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }


@app.get("/")
def read_root():
    return {"code": 0, "msg": "请求成功"}


# file 参数类型是字节 bytes
@app.post("/upfile/")
async def upfile(file: bytes = File(...)):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def uploadfile(image: UploadFile = File(...)):
    try:
        os.makedirs("images", exist_ok=True)
    except Exception as e:
        print(e)
    suffix_arr = image.filename.split(".")
    suffix = suffix_arr[len(suffix_arr) - 1]
    file_name = os.getcwd() + "/images/" + str(uuid.uuid1()) + "." + suffix

    with open(file_name, "wb+") as f:
        f.write(image.file.read())
        f.close()

    return {"filename": file_name}


@app.post("/base64file")
async def uploadbase64file(image=Body(None), suffix=Body(None)):
    imgdata = base64.b64decode(image)
    file_name = os.getcwd() + "/images/" + str(uuid.uuid1()) + "." + suffix
    file = open(file_name, 'wb')
    file.write(imgdata)
    file.close()
    return {"code": 0, "obj": file_name}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8001, debug=True)
