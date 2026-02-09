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
   },
    {
        "q": "図のような回路で、端子a-b間の合成抵抗[Ω]は。",
        "choices": ["イ. 1", "ロ. 2", "ハ. 3", "ニ. 4"],
        "correct": "ロ",
        "source": "出典：令和7年度下期 第二種電気工事士試験（学科）"
    },
    {
        "q": "抵抗R[Ω]に電圧V[V]を加えると電流I[A]が流れ、P[W]の電力が消費される。抵抗Rを示す式として誤っているものは。",
        "choices": ["イ. P/I", "ロ. P/I²", "ハ. √P", "ニ. V/I"],
        "correct": "イ",
        "source": "出典：令和7年度下期 第二種電気工事士試験（学科）"
    },
    {
        "q": "電熱器により60kgの水の温度を20K上昇させるのに必要な電力量[kW·h]は。水の比熱4.2kJ/(kg·K)、効率100%。",
        "choices": ["イ. 1.0", "ロ. 1.2", "ハ. 1.4", "ニ. 1.6"],
        "correct": "ハ",
        "source": "出典：令和7年度下期 第二種電気工事士試験（学科）"
    },
    {
        "q": "図のような正弦波交流回路の電源電圧vに対する電流iの波形として正しいものは。",
        "choices": ["イ.（位相が進む波形）", "ロ.（別の波形）", "ハ.（別の波形）", "ニ.（別の波形）"],
        "correct": "イ",
        "source": "出典：令和7年度下期 第二種電気工事士試験（学科）"
    },
    {
        "q": "図のような三相負荷に三相交流電圧を加えたとき、各線に20Aの電流が流れた。線間電圧E[V]は。",
        "choices": ["イ. 120", "ロ. 173", "ハ. 208", "ニ. 240"],
        "correct": "ハ",
        "source": "出典：令和7年度下期 第二種電気工事士試験（学科）"
    },
    {
        "q": "図の三相3線式回路で×印の箇所が断線した場合、負荷の全消費電力[kW]は。負荷抵抗30Ω。",
        "choices": ["イ. 0.7", "ロ. 0.9", "ハ. 1.3", "ニ. 2.0"],
        "correct": "ニ",
        "source": "出典：令和7年度下期 第二種電気工事士試験（学科）"
    },
    {
        "q": "図の単相3線式回路で電線1本あたりの抵抗0.2Ωのとき、a-b間の電圧[V]は。",
        "choices": ["イ. 96", "ロ. 100", "ハ. 102", "ニ. 106"],
        "correct": "ハ",
        "source": "出典：令和7年度下期 第二種電気工事士試験（学科）"
    },
    {
        "q": "低圧屋内配線の合成樹脂管工事で、直径2.0mmの600Vビニル絶縁電線を4本収めた場合、電線1本当たりの許容電流[A]は。",
        "choices": ["イ. 17", "ロ. 19", "ハ. 22", "ニ. 24"],
        "correct": "ハ",
        "source": "出典：令和7年度下期 第二種電気工事士試験（学科）"
    },
    {
        "q": "図のように定格電流50Aの過電流遮断器で保護された幹線から分岐し、7mの位置に過電流遮断器を施設するとき、a-b間の電線の許容電流の最小値[A]は。",
        "choices": ["イ. 12.5", "ロ. 17.5", "ハ. 22.5", "ニ. 27.5"],
        "correct": "ロ",
        "source": "出典：令和7年度下期 第二種電気工事士試験（学科）"
    },
    {
        "q": "低圧屋内配線の分岐回路の設計で、配線用遮断器・電線の太さ・コンセントの組合せとして適切なものは。",
        "choices": ["イ.（組合せA）", "ロ.（組合せB）", "ハ.（組合せC）", "ニ.（組合せD）"],
        "correct": "ハ",
        "source": "出典：令和7年度下期 第二種電気工事士試験（学科）"
    }
]

# --- 最初の1回だけシャッフル ---
if "questions" not in st.session_state:
    st.session_state.questions = questions.copy()
    random.shuffle(st.session_state.questions)

# --- index 初期化 ---
if "index" not in st.session_state:
    st.session_state.index = 0

current = st.session_state.questions[st.session_state.index]

st.write("### 問題")
st.write(current["q"])
if "img" in current:
    st.image(current["img"])

# --- 回答済みフラグ ---
if "answered" not in st.session_state:
    st.session_state.answered = False

selected = st.radio("選択肢を選んでね", current["choices"], index=None)

# --- 回答ボタン ---
if st.button("回答する") and not st.session_state.answered:
    if selected is None:
        st.warning("選択肢を選んでね！")
    else:
        st.session_state.selected = selected
        st.session_state.answered = True
        st.rerun()

# --- 回答後の表示 ---
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


