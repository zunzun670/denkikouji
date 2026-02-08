import streamlit as st

questions = [
   {
              "q":"一般住宅の屋内配線で「VVFケーブル」を使用する目的として最も適切なのはどれ？",
"choices": [ 
           "1: 高電圧を長距離送電するため", 
           "2: 屋内の固定配線に使うため", 
           "3: 地中に直接埋設するため", 
           "4: 防爆エリアで使用するため" 
],
"correct": "2" 
"info":"VVFケーブルは住宅などの屋内の固定配線に使われるケーブルだね！絶縁体と被覆が一体化していて施工しやすいのが特徴だよ。"
    }
]

if "index" not in st.session_state:
           st.session_state.index = 0

current = questions[st.session_state.index] 

st.write("### 問題") 
st.write(current["q"])

selected = st.radio("選択肢を選んでね", current["choices"], index=None)

if selected:
    if selected.startswith(current["correct"]):
        st.success("正解！☺")
        st.info(current["info"])
    else: st.error("ざんねん😭")

if st.button("次へ"): 
    st.session_state.index += 1
    if st.session_state.index >= len(questions): 
               st.session_state.index = 0 # 最後まで行ったら最初に戻る
    st.experimental_rerun()
