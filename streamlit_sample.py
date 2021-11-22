# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 19:02:19 2021

@author: kk819822
"""

import streamlit as st
st.title("初めてのstreamlit")
st.write("これから作品を作っていきます。")

text = st.text_input('あなたの名前を教えてください')
"あなたの名前は、",text,"です"

condition = st.slider('あなたの今の調子は?',0, 100, 50)
'コンディション:',condition

option = st.selectbox(
'好きな数字を教えてください',
list(['1番','2番','3番','4番'])
)
'あなたが選択したのは,',option,'です'

from PIL import Image
img = Image.open('イラスト25.png')
st.image(img, caption="墓守", use_column_width=True)