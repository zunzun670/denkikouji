import streamlit as st 
st.title("電気工事士2種・クイズ")

question="一般住宅の屋内配線で「VVFケーブル」を使用する目的として最も適切なのはどれ？"
choices=["あ. 高電圧を長距離送電するため", 
         "い. 屋内の固定配線に使うため", 
         "う. 地中に直接埋設するため", 
         "え. 防爆エリアで使用するため" ] 
correct = "い"

st.write("### 問題") 
st.write(question)

selected = st.radio("選択肢を選んでね", choices)

if selected:
if selected.startswith(correct):
    st.success("正解！☺") 
    st.info("VVFケーブルは住宅などの屋内の固定配線に使われるケーブルだね！絶縁体と被覆が一体化していて施工しやすいのが特徴だよ。") 
else: st.error("ざんねん😭")
