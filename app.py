import streamlit as st
import random

# --- 1. ページ設定（ワイドモードにする） ---
st.set_page_config(page_title="電工二種 合格ナビ", page_icon="⚡", layout="wide")

# --- 2. モダンCSS（スマホ余白対策版） ---
st.markdown("""
    <style>
    /* 1. Reset Streamlit default margins */
    [data-testid="stAppViewMain"] .main .block-container {
        padding: 1rem 0.5rem !important;
        max-width: 100% !important;
        margin: 0 !important;
    }
    
    .stApp {
        background-color: #f8f9fa;
    }

    /* 2. Question card design */
    .question-container {
        background-color: #ffffff;
        padding: 1.2rem;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        border-left: 8px solid #4CAF50;
        margin: 0 0 20px 0 !important;
        width: 100% !important;
        box-sizing: border-box;
    }

    /* 3. Radio button customization */
    div[role="radiogroup"] {
        display: flex;
        flex-direction: column;
        gap: 10px;
        width: 100% !important;
    }
    div[role='radiogroup'] > label {
        background-color: #ffffff;
        border: 1px solid #dee2e6;
        padding: 15px !important;
        border-radius: 10px;
        width: 100% !important;
        margin: 0 !important;
        display: flex !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }

    /* 4. Full width for buttons and images */
    .stButton > button, .stImage > img {
        width: 100% !important;
    }
    
    h1, h2, h3 {
        word-break: break-all;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. モード管理の初期化 ---
if "mode" not in st.session_state:
    st.session_state.mode = "top"

# --- 4. 画面分岐 ---

# A. トップ画面
if st.session_state.mode == "top":
    st.title("⚡ 第二種電気工事士 合格ナビ")
    st.write("ようよう、今日も勉強お疲れ様！どのモードで練習する？")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🟢 まずはここから", use_container_width=True):
            data = [
                {
                    "q":"一般住宅の屋内配線で「VVFケーブル」を使用する目的として最も適切なのはどれ？",
                    "choices": [ "イ: 高電圧を長距離送電するため", "ロ: 屋内の固定配線に使うため", "ハ: 地中に直接埋設するため", "ニ: 防爆エリアで使用するため" ],
                    "correct": "ロ",
                    "info": "VVFケーブルは住宅などの屋内の固定配線に使われるケーブルだよ。"
                },
                { 
                    "q": "電線の太さを表す単位はどれ？", 
                    "choices": [ "イ: mm²", "ロ: kg", "ハ: V", "ニ: A" ], 
                    "correct": "イ", 
                    "info": "電線の太さはmm²（平方ミリメートル）で表すよ。" 
                },
                { "q": "一般的な住宅用コンセント回路（20A）の電線太さとして正しいのはどれ？", 
                    "choices": [ "イ: 1.6mm", "ロ: 2.0mm", "ハ: 3.2mm", "ニ: 5.5mm" ], 
                    "correct": "ロ", 
                    "info": "住宅の20Aコンセント回路は2.0mmのVVFケーブルを使うのが一般的だよ。" 
                },
                { "q": "漏電遮断器（ELB）の主な役割はどれ？", 
                    "choices": [ "イ: 過電流を防止する", "ロ: 雷サージを防止する", "ハ: 漏電を検出して回路を遮断する", "ニ: 電圧を安定させる" ], 
                    "correct": "ハ", 
                    "info": "漏電遮断器は感電や火災を防ぐための装置だよ。" 
                },
                { "q": "三路スイッチを使う目的として正しいのはどれ？", 
                    "choices": [ "イ: 2つの場所から1つの照明を操作するため", "ロ: 3つの照明を同時に点灯させるため", "ハ: 3相電源を切り替えるため", "ニ: 非常用照明を制御するため" ], 
                    "correct": "イ", 
                    "info": "三路スイッチは2か所から1つの照明を操作したいときに使うよ。" 
                },
                {
                    "q": "一般家庭の屋内配線図において、「●」で表されるものは次のうちどれですか？",
                    "choices": ["イ. 壁付コンセント", "ロ. タンブラスイッチ（点滅器）", "ハ. 引掛シーリング（照明器具の取付部）", "ニ. ジョイントボックス"],
                    "correct": "ロ",
                    "info": "スイッチの記号は「●」で表されるよ。"
                }
            ]
            st.session_state.questions = data
            random.shuffle(st.session_state.questions)
            st.session_state.index = 0
            st.session_state.answered = False
            st.session_state.score = 0
            st.session_state.combo = 0
            st.session_state.mode = "quiz"
            st.rerun()

    with col2:
        if st.button("🔵 過去問に挑戦", use_container_width=True):
            data = [ 
                { "q": "図のような回路で、端子a-b間の合成抵抗[Ω]は。",
                    "choices": ["イ. 1", "ロ. 2", "ハ. 3", "ニ. 4"],
                    "correct": "ロ",
                    "info": "全体の合成抵抗は2Ωになるよ。"
                },
                {
                    "q": "抵抗Ｒ[Ω]に電圧Ｖ[V]を加えると電流Ｉ[A]が流れ、Ｐ[W]の電力が消費される。抵抗Ｒを示す式として誤っているものは",
                    "choices": ["イ. PI/V", "ロ. P/I²", "ハ. V²/P", "ニ. V/I"],
                    "correct": "イ",
                    "info": "P/I は電圧になってしまうため誤りだよ。"
                },
                {
                    "q": "電熱器により60kgの水の温度を20K上昇させるのに必要な電力量[kW·h]は。ただし、水の比熱4.2kJ/(kg·K)とし、熱効率は100%とする。",
                    "choices": ["イ. 1.0", "ロ. 1.2", "ハ. 1.4", "ニ. 1.6"],
                    "correct": "ハ",
                    "info": "必要な電力量は 1.4kW･h になるよ。"
                }
            ]
            st.session_state.questions = data
            random.shuffle(st.session_state.questions)
            st.session_state.index = 0
            st.session_state.answered = False
            st.session_state.score = 0
            st.session_state.combo = 0
            st.session_state.mode = "quiz"
            st.rerun()

# B. クイズ画面
elif st.session_state.mode == "quiz":
    if st.session_state.index >= len(st.session_state.questions):
        st.balloons()
        st.title("🎉 全問終了！")
        st.metric("最終スコア", f"{st.session_state.score} / {len(st.session_state.questions)}")
        if st.button("トップに戻る"):
            st.session_state.mode = "top"
            st.rerun()
        st.stop()

    current = st.session_state.questions[st.session_state.index]

    st.title("⚡ 第二種電気工事士 学科対策")
    st.progress(st.session_state.index / len(st.session_state.questions))
    st.write(f"問題: {st.session_state.index + 1} / {len(st.session_state.questions)}  |  🔥 コンボ: {st.session_state.combo}")

    st.markdown(f'<div class="question-container"><h3>Q. {current["q"]}</h3></div>', unsafe_allow_html=True)

    selected = st.radio("選択肢を選んでね", current["choices"], index=None, key=f"q_{st.session_state.index}", disabled=st.session_state.answered)

    if not st.session_state.answered:
        if st.button("回答を確定する", type="primary"):
            if selected is None:
                st.warning("どれか選んでね！")
            else:
                st.session_state.selected = selected
                st.session_state.answered = True
                st.rerun()
    else:
        is_correct = st.session_state.selected.startswith(current["correct"])
        if is_correct:
            st.success("✨ 正解！ ✨")
        else:
            st.error(f"残念！ 正解は「{current['correct']}」でした。")

        st.markdown(f'<div class="info-container"><strong>💡 解説:</strong><br>{current["info"]}</div>', unsafe_allow_html=True)

        if st.button("次の問題へ ➔"):
            if is_correct:
                st.session_state.score += 1
                st.session_state.combo += 1
            else:
                st.session_state.combo = 0
            st.session_state.index += 1
            st.session_state.answered = False
            st.rerun()

st.divider()
st.caption("Keep it up! ようよう、合格目指して頑張ろう！")
