import streamlit as st
import random

# --- 1. ページ設定 & モダンCSS ---
st.set_page_config(page_title="電工二種 合格ナビ", page_icon="⚡")

st.markdown("""
    <style>
    /* 全体の背景色 */
    .stApp {
        background-color: #f8f9fa;
    }
    /* 問題ボックスのデザイン */
    .question-container {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        border-left: 5px solid #4CAF50;
        margin-bottom: 20px;
    }
    /* 解説ボックス */
    .info-container {
        background-color: #e8f4ea;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #2e7d32;
        margin-top: 15px;
    }
    /* ラジオボタンの行間調整 */
    div[role='radiogroup'] > label {
        line-height: 2;
        padding: 8px;
        border-radius: 5px;
        transition: 0.3s;
    }
    div[role='radiogroup'] > label:hover {
        background-color: #f1f3f5;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. モード管理の初期化 ---
if "mode" not in st.session_state:
    st.session_state.mode = "top"  # 最初はトップ画面

# --- 3. 画面分岐 ---

# A. トップ画面（入口）
if st.session_state.mode == "top":
    st.title("⚡ 第二種電気工事士 合格ナビ")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🟢 まずはここから", use_container_width=True):
# --- ここで初期化を行う！ ---
         data = [
    {
        "q":"一般住宅の屋内配線で「VVFケーブル」を使用する目的として最も適切なのはどれ？",
        "choices": [ "イ: 高電圧を長距離送電するため", "ロ: 屋内の固定配線に使うため", "ハ: 地中に直接埋設するため", "ニ: 防爆エリアで使用するため" ],
        "correct": "ロ",
        "info": "VVFケーブルは住宅などの屋内の固定配線に使われるケーブルだね！絶縁体と被覆が一体化していて施工しやすいのが特徴だよ。"
    },    { 
        "q": "電線の太さを表す単位はどれ？", 
        "choices": [ "イ: mm²", "ロ: kg", "ハ: V", "ニ: A" ], 
        "correct": "イ", 
        "info": "電線の太さはmm²（平方ミリメートル）で表すよ。太さが大きいほど電流を多く流せるんだ。" 
    } ,    
    { "q": "一般的な住宅用コンセント回路（20A）の電線太さとして正しいのはどれ？", 
        "choices": [ "イ: 1.6mm", "ロ: 2.0mm", "ハ: 3.2mm", "ニ: 5.5mm" ], 
        "correct": "ロ", 
        "info": "住宅の20Aコンセント回路は2.0mmのVVFケーブルを使うのが一般的だよ。" 
    },
    { "q": "漏電遮断器（ELB）の主な役割はどれ？", 
        "choices": [ "イ: 過電流を防止する", "ロ: 雷サージを防止する", "ハ: 漏電を検出して回路を遮断する", "ニ: 電圧を安定させる" ], 
        "correct": "ハ", 
        "info": "漏電遮断器は漏電を検出して回路を遮断し、感電や火災を防ぐための装置だよ。" 
    },
    { "q": "三路スイッチを使う目的として正しいのはどれ？", 
        "choices": [ "イ: 2つの場所から1つの照明を操作するため", "ロ: 3つの照明を同時に点灯させるため", "ハ: 3相電源を切り替えるため", "ニ: 非常用照明を制御するため" ], 
        "correct": "イ", 
        "info": "三路スイッチは階段や廊下など、2か所から1つの照明を操作したいときに使うよ。" 
    },
    { "q": "この図記号が示す機器はどれ？", 
        "img": "images1.jpg", 
        "choices": [ "イ: 配線用遮断器（ブレーカ）", "ロ: 漏電遮断器", "ハ: 変圧器", "ニ: 電力量計" ], 
        "correct": "イ", 
        "info": "この図記号は配線用遮断器（ブレーカ）だよ。過電流を防ぐために使われる保護装置だね。" 
    },
     {
        "q": "一般家庭の屋内配線図において、「●」で表されるものは次のうちどれですか？",
        "img": "images4.jpg", 
        "choices": ["イ. 壁付コンセント", "ロ. タンブラスイッチ（点滅器）", "ハ. 引掛シーリング（照明器具の取付部）", "ニ. ジョイントボックス"],
        "correct": "ロ. タンブラスイッチ（点滅器）",
        "info": "部屋の電気をパチッとつけたり消したりするスイッチの記号は、「●」で表されるよ。\nちなみに「○」のように中が白い丸は、接続点（ジョイントボックス）などを指すことが多いので、色の塗られ方に注意しよう。",
    }
    ]
st.session_state.questions = data.copy() # ここで session_state に入れる
            random.shuffle(st.session_state.questions)
            st.session_state.index = 0
            st.session_state.answered = False
            st.session_state.score = 0
            st.session_state.combo = 0
            
            st.session_state.mode = "quiz" # モード切替
            st.rerun()

    with col2:
        if st.button("🔵 過去問に挑戦", use_container_width=True):
# --- 過去問用のデータで初期化 ---
        data = [ 
     { "q": "図のような回路で、端子a-b間の合成抵抗[Ω]は。",
        "img": "images2.jpg", 
        "choices": ["イ. 1", "ロ. 2", "ハ. 3", "ニ. 4"],
        "correct": "ロ",
        "info": "左右が対称だから中央の3Ωには電流が流れず、回路は左右の枝だけで考えられるように簡略化できるよ！その結果、全体の合成抵抗は2Ωになるね。", 
        "source": "出典：令和7年度下期 第二種電気工事士試験（学科）"
    },
    {
        "q": "抵抗Ｒ[Ω]に電圧Ｖ[V]を加えると電流Ｉ[A]が流れ、Ｐ[W]の電力が消費される。抵抗Ｒを示す式として誤っているものは",
        "choices": ["イ. PI/V", "ロ. P/I²", "ハ. V²/P", "ニ. V/I"],
        "correct": "イ",
        "info": "電力Pは V×I だから、抵抗Rは V/I、V²/P、P/I² のいずれかで表せるよ。P/I は電圧になってしまうため誤りだね。",
        "source": "出典：令和7年度下期 第二種電気工事士試験（学科）"
    },
    {
        "q": "電熱器により60kgの水の温度を20K上昇させるのに必要な電力量[kW·h]は。ただし、水の比熱4.2kJ/(kg·K)とし、熱効率は100%とする。",
        "choices": ["イ. 1.0", "ロ. 1.2", "ハ. 1.4", "ニ. 1.6"],
        "correct": "ハ",
        "info": "水を20 K上昇させるのに必要な熱量は60×4.2×20=5040 kJ となり、これは 1.4kW･h に相当するよ。熱効率100％なので、この値がそのまま必要な電力量になるんだ。",
        "source": "出典：令和7年度下期 第二種電気工事士試験（学科）"
    },
    {
        "q": "図のような三相負荷に三相交流電圧を加えたとき、各線に20Aの電流が流れた。線間電圧E[V]は。",
        "img": "images3.jpg", 
        "choices": ["イ. 120", "ロ. 173", "ハ. 208", "ニ. 240"],
        "correct": "ハ",
        "info": "デルタ結線では、線間電圧と相電圧が同じになります。抵抗1つあたりの相電圧は V=I*R ですが、相電流は線電流の1/√3になる点に注意。V= (20/√3)*6 = 120/√3 ≈ 69.2V...（※解説詳細はお好みで調整してください）",
        "source": "出典：令和7年度下期 第二種電気工事士試験（学科）"
    },
    {
        "q": "図の三相3線式回路で×印の箇所で断線した場合、負荷の全消費電力[kW]は。ただし、負荷の抵抗は30Ωとし、配線の抵抗は無視し、電源電圧は一定とする。",
        "img": "images4.jpg", 
        "choices": ["イ. 0.7", "ロ. 0.9", "ハ. 1.3", "ニ. 2.0"],
        "correct": "ニ",
        "info": "デルタ結線で1本の線が切れると、残った2つの抵抗にそれぞれ200Vが加わるよ。1.33kW × 2 = 2.0kW となるんだ。",
        "source": "出典：令和7年度下期 第二種電気工事士試験（学科）"
    }
]
        st.session_state.questions = data.copy()
        random.shuffle(st.session_state.questions)
        st.session_state.index = 0
        st.session_state.answered = False
        st.session_state.score = 0
        st.session_state.combo = 0
            
        st.session_state.mode = "quiz"
        st.rerun()

# --- 3. セッション管理の初期化 ---
if "questions" not in st.session_state:
    st.session_state.questions = questions.copy()
    random.shuffle(st.session_state.questions)
    st.session_state.index = 0
    st.session_state.answered = False
    st.session_state.score = 0
    st.session_state.combo = 0

# 終了判定
if st.session_state.index >= len(st.session_state.questions):
    st.balloons()
    st.title("🎉 全問終了！")
    st.metric("最終スコア", f"{st.session_state.score} / {len(st.session_state.questions)}")
    if st.button("もう一度挑戦する"):
        del st.session_state.questions
        st.rerun()
    st.stop()

current = st.session_state.questions[st.session_state.index]

# --- 4. ヘッダー & プログレス ---
st.title("⚡ 第二種電気工事士 学科対策")
progress = (st.session_state.index) / len(st.session_state.questions)
st.progress(progress)
col_stat1, col_stat2 = st.columns(2)
col_stat1.write(f"問題: {st.session_state.index + 1} / {len(st.session_state.questions)}")
col_stat2.write(f"🔥 現在のコンボ: {st.session_state.combo}")

# --- 5. 問題表示部 ---
st.markdown(f"""
    <div class="question-container">
        <h3>Q. {current['q']}</h3>
    </div>
    """, unsafe_allow_html=True)

if "source" in current:
    st.caption(current["source"])

if "img" in current:
    try:
        st.image(current["img"], use_container_width=True)
    except:
        st.warning("画像が見つかりませんでした")

# --- 6. 回答選択 ---
# 回答後は選択不可にするため、disabledを制御
selected = st.radio(
    "選択肢を選んでね", 
    current["choices"], 
    index=None, 
    key=f"q_{st.session_state.index}",
    disabled=st.session_state.answered
)

# --- 7. アクションボタン ---
if not st.session_state.answered:
    if st.button("回答を確定する", type="primary"):
        if selected is None:
            st.warning("どれか選んでね！")
        else:
            st.session_state.selected = selected
            st.session_state.answered = True
            st.rerun()
else:
    # 回答後の表示
    is_correct = st.session_state.selected.startswith(current["correct"])
    
    if is_correct:
        st.balloons()
        st.success("✨ 正解！その調子！ ✨")
        if st.session_state.combo == 0: # 最初の1回
             st.session_state.score += 1
        st.session_state.combo += 1
    else:
        st.error(f"残念！ 正解は「{current['correct']}」でした。")
        st.session_state.combo = 0

    # 解説カード
    st.markdown(f"""
        <div class="info-container">
            <strong>💡 解説:</strong><br>{current['info']}
        </div>
        """, unsafe_allow_html=True)

    if st.button("次の問題へ ➔"):
        if is_correct:
            st.session_state.score += 1
        st.session_state.index += 1
        st.session_state.answered = False
        st.rerun()

# --- フッター ---
st.divider()
st.caption("Keep it up! 毎日コツコツが合格への近道です。")
