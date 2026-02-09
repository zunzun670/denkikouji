import streamlit as st
import random

questions = [
   {
              "q":"一般住宅の屋内配線で「VVFケーブル」を使用する目的として最も適切なのはどれ？",
"choices": [ 
           "1: 高電圧を長距離送電するため", 
           "2: 屋内の固定配線に使うため", 
           "3: 地中に直接埋設するため", 
           "4: 防爆エリアで使用するため" 
],
"correct": "2",
"info": "VVFケーブルは住宅などの屋内の固定配線に使われるケーブルだね！絶縁体と被覆が一体化していて施工しやすいのが特徴だよ。"
    },
   
  { 
       "q": "電線の太さを表す単位はどれ？", 
"choices": [ 
         "1: mm²", 
         "2: kg", 
         "3: V", 
         "4: A" 
], 
"correct": "1", 
"info": "電線の太さはmm²（平方ミリメートル）で表すよ。太さが大きいほど電流を多く流せるんだ。" 
    } ,
   
{ "q": "一般的な住宅用コンセント回路（20A）の電線太さとして正しいのはどれ？", 
"choices": [ 
      "1: 1.6mm", 
      "2: 2.0mm", 
      "3: 3.2mm", 
      "4: 5.5mm" 
], 
 "correct": "2", 
 "info": "住宅の20Aコンセント回路は2.0mmのVVFケーブルを使うのが一般的だよ。" 
   },

{ "q": "漏電遮断器（ELB）の主な役割はどれ？", 
"choices": [ 
   "1: 過電流を防止する", 
   "2: 雷サージを防止する", 
   "3: 漏電を検出して回路を遮断する", 
   "4: 電圧を安定させる" ], 
 "correct": "3", 
 "info": "漏電遮断器は漏電を検出して回路を遮断し、感電や火災を防ぐための装置だよ。" 
   },

{ "q": "三路スイッチを使う目的として正しいのはどれ？", 
 "choices": [ 
    "1: 2つの場所から1つの照明を操作するため", 
    "2: 3つの照明を同時に点灯させるため", 
    "3: 3相電源を切り替えるため", 
    "4: 非常用照明を制御するため" ], 
 "correct": "1", 
 "info": "三路スイッチは階段や廊下など、2か所から1つの照明を操作したいときに使うよ。" 
    },

   { "q": "この図記号が示す機器はどれ？", 
    "img": "images1.jpg", 
    "choices": [ 
       "1: 配線用遮断器（ブレーカ）", 
       "2: 漏電遮断器", 
       "3: 変圧器", 
       "4: 電力量計" 
    ], 
"correct": "1", 
"info": "この図記号は配線用遮断器（ブレーカ）だよ。過電流を防ぐために使われる保護装置だね。" 
   }
]

random.shuffle(questions)

if "index" not in st.session_state:
           st.session_state.index = 0

current = questions[st.session_state.index] 

st.write("### 問題") 
st.write(current["q"])
if "img" in current: st.image(current["img"])


if "answered" not in st.session_state:
    st.session_state.answered = False


selected = st.radio("選択肢を選んでね", current["choices"], index=None)


if st.button("回答する"):
    if selected is None:
        st.warning("選択肢を選んでね！")
    else:
        st.session_state.answered = True
        st.session_state.selected = selected  # ★ここが重要！


if st.session_state.answered:
    if st.session_state.selected.startswith(current["correct"]):
        st.success("正解！😊")
        st.info(current["info"])
    else:
        st.error("ざんねん😭")

    
    if st.button("次へ"):
        st.session_state.index += 1
        st.session_state.answered = False
        st.rerun()
