# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description:
"""
import torch

torch.hub._validate_not_a_forked_repo = lambda a, b, c: True
# 模型
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5n - yolov5x6, custom

# 图像
img = 'zidane.jpg'  # or file, Path, PIL, OpenCV, numpy, list

# 推理
results = model(img)

# 结果
print(results.print())  # or .show(), .save(), .crop(), .pandas(), etc.
results.save(save_dir="zidane_saved", exist_ok=True)

print(results.pandas().xyxy[0])

json_r = results.pandas().xyxy[0].to_json(orient="records")  # JSON img1 predictions
print(json_r, type(json_r))
