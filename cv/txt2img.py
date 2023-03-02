# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

from diffusers import StableDiffusionPipeline
import torch

model_id_or_path = "xiaolxl/Gf_style2"

pipe = StableDiffusionPipeline.from_pretrained(model_id_or_path, torch_dtype=torch.float16)
pipe = pipe.to("cuda")
pipe.safety_checker = lambda images, **kwargs: (images, False)

prompt = "best quality, masterpiece, highres, chinese dress,Beautiful face,1girl beside the window,sunshine, side light, overexposure,1girl,(solo),(upper body)"
negative_prompt = """(((simple background))),monochrome ,lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, ugly, pregnant,vore,duplicate,morbid,mut ilated,tran nsexual, hermaphrodite,long neck,mutated hands,poorly drawn hands,poorly drawn face,mutation,deformed, (((missing arms))),(((missing legs))), (((extra arms))),(((extra legs))),pubic hair, plump,bad legs,error legs, bad feet, loli, little girl"""


generator = torch.Generator("cuda").manual_seed(2)

images = pipe(prompt, height=512, width=512, num_inference_steps=50, guidance_scale=6, negative_prompt=negative_prompt,
    num_images_per_prompt=1, generator=generator).images

image = images[0]
image.save("./txt2img_girl_gf2_2.png")
