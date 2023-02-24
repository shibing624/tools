# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

from diffusers import StableDiffusionPipeline
import torch

model_id = "andite/anything-v4.0"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "hatsune_miku,(((masterpiece))), (((best quality))), ((ultra-detailed)), (illustration), (1 girl), (solo), ((an extremely delicate and beautiful)), beauty girl,"
image = pipe(prompt).images[0]

image.save("./hatsune_miku.png")
