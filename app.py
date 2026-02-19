import streamlit as st
import random

# --- 1. ページ設定 ---
st.set_page_config(page_title="電工二種 合格ナビ", page_icon="⚡", layout="wide")

# --- 2. CSS（余白対策 ＋ 解説枠の復活） ---
st.markdown("""
<style>
/* スマホの巨大な余白を消す */
[data-testid="stAppViewMain"] .main .block-container {
    padding: 1.5rem 1rem !important;
    max-width: 100% !important;
}

/* 問題ボックス（緑の左線） */
.question-container {
    background-color: #ffffff;
    padding: 1.5rem;
    border-radius: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    border-left: 8px solid #4CAF50;
    margin-bottom: 20px;
    width: 100%;
}

/* 解説ボックス（濃い緑の枠を復活！） */
.info-container {
    background-color: #e8f4ea;
    padding: 1.5rem;
    border-radius: 10px;
    border-left: 8px solid #2e7d32;
    margin-top: 15px;
    width: 100%;
}

/* 選択肢の調整 */
div[role='radiogroup'] > label {
    line-height: 2;
    padding: 10px;
    border-radius: 8px;
    transition: 0.3s;
    background-color: #ffffff;
    border: 1px solid #eee;
    margin-bottom: 5px;
}
</style>
""", unsafe_allow_html=True)

# --- 3. セッション初期化 ---
if "mode" not in st.session_state:
    st.session_state.mode = "top"

# --- 4. 画面分岐 ---
if st.session_state.mode == "top":
    st.title("⚡ 第二種電気工事士 合格ナビ")
    st.write("おつかれさま！どのモードで練習する？")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🟢 まずはここから", use_container_width=True):
            data = [
                {"q":"一般住宅の屋内配線で「VVFケーブル」を使用する目的として最も適切なのはどれ？", "choices": [ "イ: 高電圧を長距離送電するため", "ロ: 屋内の固定配線に使うため", "ハ: 地中に直接埋設するため", "ニ: 防爆エリアで使用するため" ], "correct": "ロ", "info": "VVFケーブルは住宅などの屋内の固定配線に使われるケーブルだよ。"},
                {"q": "電線の太さを表す単位はどれ？", "choices": [ "イ: mm²", "ロ: kg", "ハ: V", "ニ: A" ], "correct": "イ", "info": "電線の太さはmm²（平方ミリメートル）で表すよ。"},
                {"q": "一般的な住宅用コンセント回路（20A）の電線太さとして正しいのはどれ？", "choices": [ "イ: 1.6mm", "ロ: 2.0mm", "ハ: 3.2mm", "ニ: 5.5mm" ], "correct": "ロ", "info": "住宅の20Aコンセント回路は2.0mmのVVFケーブルを使うのが一般的だよ。"},
                {"q": "漏電遮断器（ELB）の主な役割はどれ？", "choices": [ "イ: 過電流を防止する", "ロ: 雷サージを防止する", "ハ: 漏電を検出して回路を遮断する", "ニ: 電圧を安定させる" ], "correct": "ハ", "info": "漏電遮断器は漏電を検出して回路を遮断し、感電を防ぐ装置だよ。"},
                {"q": "三路スイッチを使う目的として正しいのはどれ？", "choices": [ "イ: 2つの場所から1つの照明を操作するため", "ロ: 3つの照明を同時に点灯させるため", "ハ: 3相電源を切り替えるため", "ニ: 非常用照明を制御するため" ], "correct": "イ", "info": "三路スイッチは2か所から操作したいときに使うよ。"},
                {"q": "一般家庭の屋内配線図において、「●」で表されるものはどれ？", "choices": ["イ. 壁付コンセント", "ロ. タンブラスイッチ", "ハ. 引掛シーリング", "ニ. ジョイントボックス"], "correct": "ロ", "info": "スイッチの記号は「●」だよ。"}
            ]
            st.session_state.questions = data
            random.shuffle(st.session_state.questions)
            st.session_state.index, st.session_state.score, st.session_state.combo = 0, 0, 0
            st.session_state.answered = False
            st.session_state.mode = "quiz"
            st.rerun()

    with col2:
        if st.button("🔵 過去問に挑戦", use_container_width=True):
            data = [ 
                {"q": "端子a-b間の合成抵抗[Ω]は。", "choices": ["イ. 1", "ロ. 2", "ハ. 3", "ニ. 4"], "correct": "ロ", "info": "全体の合成抵抗は2Ωになるよ。"},
                {"q": "抵抗Ｒを示す式として誤っているものは", "choices": ["イ. PI/V", "ロ. P/I²", "ハ. V²/P", "ニ. V/I"], "correct": "イ", "info": "P/I は電圧になってしまうため誤りだよ。"},
                {"q": "水の温度を20K上昇させるのに必要な電力量[kW·h]は。", "choices": ["イ. 1.0", "ロ. 1.2", "ハ. 1.4", "ニ. 1.6"], "correct": "ハ", "info": "計算すると1.4kW･hになるよ。"}
            ]
            st.session_state.questions = data
            random.shuffle(st.session_state.questions)
            st.session_state.index, st.session_state.score, st.session_state.combo = 0, 0, 0
            st.session_state.answered = False
            st.session_state.mode = "quiz"
            st.rerun()

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
    st.title("⚡ 合格ナビ")
    st.progress(st.session_state.index / len(st.session_state.questions))
    
    st.markdown(f'<div class="question-container"><h3>Q. {current["q"]}</h3></div>', unsafe_allow_html=True)

    selected = st.radio("選択肢を選んでね", current["choices"], index=None, key=f"q_{st.session_state.index}", disabled=st.session_state.answered)

    if not st.session_state.answered:
        if st.button("回答を確定する", type="primary"):
            if selected:
                st.session_state.selected = selected
                st.session_state.answered = True
                st.rerun()
    else:
        is_correct = st.session_state.selected.startswith(current["correct"])
        if is_correct:
            st.success("✨ 正解！ ✨")
            st.session_state.score += 1
            st.session_state.combo += 1
        else:
            st.error(f"残念！ 正解は「{current['correct']}」でした。")
            st.session_state.combo = 0

        st.markdown(f'<div class="info-container"><strong>💡 解説:</strong><br>{current["info"]}</div>', unsafe_allow_html=True)

        if st.button("次の問題へ ➔"):
            st.session_state.index += 1
            st.session_state.answered = False
            st.rerun()

st.divider()
st.caption("千里の道も一歩から")
