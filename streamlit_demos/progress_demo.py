# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import streamlit as st
import time

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

total_num = 5
for i in range(total_num):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Processing {i + 1}/{total_num}')
    bar.progress(int((i + 1) / total_num * 100))
    time.sleep(0.01)
