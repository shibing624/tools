# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import streamlit as st
import time

with st.spinner("Wait for it..."):
    for i in range(100):
        print("hello")
        time.sleep(0.01)

st.success("Done!")
