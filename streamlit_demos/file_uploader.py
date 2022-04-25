# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import streamlit as st
import time
import os
pwd = os.path.dirname(os.path.realpath(__file__))
style_file = st.file_uploader("请上传风格化图片")

if style_file:
    stringio = style_file.getvalue()
    style_file_path = 'style_file/' + style_file.name
    with open(style_file_path, 'wb') as f:
        f.write(stringio)

st.write('高分辨率风格化demo')
if st.button('开始进行风格化处理'):
    my_bar = st.progress(10)

    UHD_content_folder_path = 'PytorchWCT/content/UHD_content'
    output_path = os.path.join(pwd, "../10_cv/data_enhancement/data/grassland1.jpeg")
    time.sleep(4)
    for i in range(0, 100, 10):
        my_bar.progress(i + 1)
    my_bar.progress(100)
    st.write('风格化之后的图片')
    st.image(output_path)

image_slot = st.empty()

if style_file:
    stringio = style_file.getvalue()
    style_file_path = 'style_file/' + style_file.name
    with open(style_file_path, 'wb') as f:
        f.write(stringio)
    image_slot.image(style_file_path)
