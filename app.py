import streamlit as st

question = "一般住宅の屋内配線で「VVFケーブル」を使用する目的として最も適切なのはどれ？" 
choices = { 
           "1": "高電圧を長距離送電するため", 
           "2": "屋内の固定配線に使うため", 
           "3": "地中に直接埋設するため", 
           "4": "防爆エリアで使用するため" }
correct = "2" 

st.write("### 問題") 
st.write(question) 

selected_key = st.radio("選択肢を選んでね", list(choices.keys()))

if selected_key is not None: 
    if selected_key == "2"
           st.success("正解！☺") 
           st.info("VVFケーブルは住宅などの屋内の固定配線に使われるケーブルだね！絶縁体と被覆が一体化していて施工しやすいのが特徴だよ。") 
    else: st.error("ざんねん😭")
