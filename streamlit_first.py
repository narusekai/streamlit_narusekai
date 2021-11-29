# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 21:10:47 2021

@author: kk819822
"""
import streamlit as st

st.title("あなたの血液型診断")
st.write("あなたの性格は何型？自分の行動に当てはまりそうな選択肢を選んでね")

text = st.text_input('あなたの名前を教えてください')



import numpy as np
first = st.radio(
  "流行は？",
   ('｢これ流行ってるから買ってきた！｣', '｢人と被りたくないから色違いにしよう｣', '｢へー流行ってるんだ｣','「なにそれ」'))

if first == '｢これ流行ってるから買ってきた！｣':
    a = np.array([0, 1, 0, 0])
elif first == '｢人と被りたくないから色違いにしよう｣':
    a = np.array([1, 0, 0, 0])
elif first =='｢へー流行ってるんだ｣':
    a = np.array([0, 0, 1, 0])
else :
    a = np.array([0, 0, 0, 1])

second = st.radio(
  "旅行する時",
   ('｢荷物まとまらない！｣', '｢まず計画表を作ろう｣', 'バス酔い','｢鹿美味しそう｣'))

if second == '｢荷物まとまらない！｣':
    b = np.array([0, 1, 0, 0])
elif second == '｢まず計画表を作ろう｣':
    b = np.array([1, 0, 0, 0])
elif second =='バス酔い':
    b = np.array([0, 0, 1, 0])
else :
    b = np.array([0, 0, 0, 1])
    
third = st.radio(
  "今日部屋行ってもいい？",
   ('｢汚くはないけど物が多い｣', '｢…だめ（部屋汚い）｣', '｢…10分待ってて？｣','｢一緒に掃除して｣'))

if third == '｢汚くはないけど物が多い｣':
    c = np.array([0,1,0,0])
elif third == '｢…だめ（部屋汚い）｣':
    c = np.array([1,0,0,0])
elif third =='｢…10分待ってて？｣｣':
    c = np.array([0,0,1,0])
else :
    c = np.array([0,0,0,1])    

forth = st.radio(
  "整理整頓",
   ('汚くはないけどなんかごちゃごちゃしてる', '｢向きそろってないの嫌｣', '｢…見た？？（ダークマター）｣','｢これ定位置｣'))

if forth == '汚くはないけどなんかごちゃごちゃしてる':
    d = np.array([0,1,0,0])
elif forth == '｢向きそろってないの嫌｣':
    d = np.array([1,0,0,0])
elif forth =='｢…見た？？（ダークマター）｣':
    d = np.array([0,0,1,0])
else :
    d = np.array([0,0,0,1])

fifth = st.radio(
  "遅刻",
   ('｢漫画読んでたら時間過ぎてた｣', '連絡はする', '｢五分は遅刻じゃない｣','｢あ、やべ…ぐー…Z｣'))

if fifth == '｢漫画読んでたら時間過ぎてた｣':
    e = np.array([0,1,0,0])
elif fifth == '連絡はする':
    e = np.array([1,0,0,0])
elif fifth =='｢五分は遅刻じゃない｣':
    e = np.array([0,0,1,0])
else :
    e = np.array([0,0,0,1])
    
six = st.radio(
  "恋愛",
   ('めっちゃ避ける', '好きな人すぐばれる', '押しに弱い','猛アタック'))

if six == 'めっちゃ避ける':
    f = np.array([0,1,0,0])
elif six == '好きな人すぐばれる':
    f = np.array([1,0,0,0])
elif six =='押しに弱い':
    f = np.array([0,0,1,0])
else :
    f = np.array([0,0,0,1])
    
seven = st.radio(
  "怒り方",
   ('語彙力がなくなる', 'めっちゃしゃべる', '黙る','怒るタイミングが人と違う'))

if seven == '語彙力がなくなる':
    g = np.array([0,1,0,0])
elif seven == 'めっちゃしゃべる':
    g = np.array([1,0,0,0])
elif seven =='黙る':
    g = np.array([0,0,1,0])
else :
    g = np.array([0,0,0,1])
    
eight = st.radio(
  "怒られているとき",
   ('逃げる', '｢すみません…｣', '｢はい…はい…（聞いてない）｣','｢（何か嫌なことでもあったのかなぁ）｣'))

if eight == '逃げる':
    h = np.array([0,1,0,0])
elif eight == '｢すみません…｣':
    h = np.array([1,0,0,0])
elif eight =='｢はい…はい…（聞いてない）｣':
    h = np.array([0,0,1,0])
else :
    h = np.array([0,0,0,1])
    
nine = st.radio(
  "SNS",
   ('興味のある内容は直ぐに返信', '意味のない内容は送らない。返事は即答', '返信は遅いか忘れる。スタンプが好き','放置しがちだが返信はする。自分からは送らない'))

if nine == '興味のある内容は直ぐに返信':
    i = np.array([0,1,0,0])
elif nine == '意味のない内容は送らない。返事は即答':
    i = np.array([1,0,0,0])
elif nine =='返信は遅いか忘れる。スタンプが好き':
    i = np.array([0,0,1,0])
else :
    i = np.array([0,0,0,1])
    
HQ = (a+b+c+d+e+f+g+h+i)

if st.button('診断する'):
    if np.argmax(HQ) == 0:
          st.write("　",text,"さんはA型の人間です！")
          from PIL import Image
          img = Image.open('imageA.png')
          st.image(img, use_column_width=True)
    elif np.argmax(HQ) == 1:
          st.write("　",text,"さんはB型の人間です！")
          from PIL import Image
          img = Image.open('imageB.png')
          st.image(img, use_column_width=True)
    elif np.argmax(HQ) == 2:
          st.write("　",text,"さんはO型の人間です！")
          from PIL import Image
          img = Image.open('imageC.png')
          st.image(img, use_column_width=True)
    else:
          st.write("　",text,"さんはAB型の人間です！")
          from PIL import Image
          img = Image.open('imageAB.png')
          st.image(img, use_column_width=True)