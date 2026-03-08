import streamlit as st
import random

# --- 1. ページ設定（スマホ最適化の要） ---
st.set_page_config(page_title="電工二種 合格ナビ", page_icon="⚡", layout="wide")

# --- 2. スマホ余白解消 ＆ 正解モーション用CSS ---
st.markdown("""
    <style>
    /* スマホの巨大な左右余白を完全に削る */
    [data-testid="stAppViewMain"] .main .block-container {
        padding: 1rem 0.5rem !important;
        max-width: 100% !important;
        margin: 0 !important;
    }

    /* 正解時のキラキラ・ふわっとアニメーション */
    @keyframes shine-pop {
        0% { transform: scale(0.98); opacity: 0; box-shadow: 0 0 0px #4CAF50; }
        50% { transform: scale(1.02); opacity: 1; box-shadow: 0 0 20px #4CAF50; }
        100% { transform: scale(1); opacity: 1; box-shadow: 0 0 5px #4CAF50; }
    }
    .キラキラ正解 {
        animation: shine-pop 0.6s ease-out forwards;
        padding: 1.2rem;
        border-radius: 12px;
        background-color: #f0fff4;
        border: 3px solid #4CAF50;
        color: #1b5e20;
        font-weight: bold;
        text-align: center;
        margin-bottom: 1rem;
    }

    /* 全体の背景色 */
    .stApp {
        background-color: #f8f9fa;
    }
/* 問題ボックス */
        .question-container {
            background-color: #ffffff;
            padding: 1.2rem;
            border-radius: 15px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            border-left: 5px solid #4CAF50;
            margin-bottom: 10px;
            width: 100%;
            box-sizing: border-box;
        }

        /* ★ここを追加！問題文の文字サイズを調整（選択肢より約2pt大きく） */
        .question-container h3 {
            font-size: 1.15rem !important; 
            margin: 0;
            line-height: 1.4;
        }
    /* 解説ボックス */
    .info-container {
        background-color: #e8f4ea;
        padding: 1.2rem;
        border-radius: 10px;
        border-left: 5px solid #2e7d32;
        margin-top: 15px;
        width: 100%;
        box-sizing: border-box;
    }
    /* ボタンを横いっぱいに広げて余白を埋める */
    .stButton > button {
        width: 100% !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. モード管理の初期化 ---
if "mode" not in st.session_state:
    st.session_state.mode = "top"

# --- 3. 画面分岐 ---

if st.session_state.mode == "top":
    st.title("⚡ 第二種電気工事士 合格ナビ")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🟢 まずはここから", use_container_width=True):
            data = [
                {
                    "q":"一般住宅の屋内配線で「VVFケーブル」を使用する目的として最も適切なのはどれ？",
                    "choices": [ "イ: 高電圧を長距離送電するため", "ロ: 屋内の固定配線に使うため", "ハ: 地中に直接埋設するため", "ニ: 防爆エリアで使用するため" ],
                    "correct": "ロ",
                    "info": "VVFケーブルは住宅などの屋内の固定配線に使われるケーブルだね！絶縁体と被覆が一体化していて施工しやすいのが特徴だよ。"
                },
                { 
                    "q": "電線の太さを表す単位はどれ？", 
                    "choices": [ "イ: mm²", "ロ: kg", "ハ: V", "ニ: A" ], 
                    "correct": "イ", 
                    "info": "電線の太さはmm²（平方ミリメートル）で表すよ。太さが大きいほど電流を多く流せるんだ。" 
                },
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
                    "q": "一般家庭の屋内配線図において、「●」で表されるものは次のうちどれか？",
                    "choices": ["イ. 壁付コンセント", "ロ. タンブラスイッチ（点滅器）", "ハ. 引掛シーリング（照明器具の取付部）", "ニ. ジョイントボックス"],
                    "correct": "ロ. タンブラスイッチ（点滅器）",
                    "info": "部屋の電気をパチッとつけたり消したりするスイッチの記号は、「●」で表されるよ。  \nちなみに「○」のように中が白い丸は、接続点（ジョイントボックス）などを指すことが多いので、色の塗られ方に注意しよう。",
                },
        {
        "q": "コンセントの刃受の形で、接地極付接地端子付コンセントの図記号（ET）に「E」を付け加えた「EET」と表記されるものは、次のうちどれ？",
        "choices": [
            "イ. 接地極のみが付いているコンセント",
            "ロ. 接地極と接地端子の両方が付いているコンセント",
            "ハ. 漏電遮断器が付いているコンセント",
            "ニ. 抜け止め形のコンセント"
        ],
        "correct": "ロ",
        "info": "「E」は接地極（Earth）、「T」は接地端子（Terminal）のことだよ。EETは、アースの棒を差す穴（極）と、アース線をねじ止めする場所（端子）の両方があるタイプのことだね！キッチンなどの水回りでよく見かけるよ。"
    },
{
        "q": "一般用電気工作物の検査において、回路の絶縁抵抗を測定するために使用する測定器はどれ？",
        "choices": [
            "イ. クランプメータ",
            "ロ. 回路計（テスタ）",
            "ハ. 絶縁抵抗計（メガー）",
            "ニ. 接地抵抗計"
        ],
        "correct": "ハ",
        "info": "電気が漏れていないか（絶縁が保たれているか）を調べるには、「絶縁抵抗計」を使うよ。現場では「メガー」とも呼ばれる必須アイテムだね！"
    },
    {
        "q": "ビニル外装ケーブル（VVF）を直接壁面に固定して配線する場合、支持点間の距離は最大何m以下にする必要がある？",
        "choices": [
            "イ. 1.0m",
            "ロ. 1.5m",
            "ハ. 2.0m",
            "ニ. 3.0m"
        ],
        "correct": "ハ",
        "info": "VVFケーブルの支持点間距離は「2m以下」と決まっているよ！  \nちなみに管（金属管など）を使うと距離が変わるから注意だよ。"
    },
     {
        "q": "三相誘導電動機の回転方向を逆にするための正しい方法はどれ？",
        "choices": [
            "イ. 電源の3線のうち、2線を入れ替える",
            "ロ. 電源の3線すべてを入れ替える",
            "ハ. 電圧を2倍にする",
            "ニ. コンデンサを直列に繋ぐ"
        ],
        "correct": "イ",
        "info": "三相交流で動くモーター（誘導電動機）は、3本ある線のうち「どれか2本」を入れ替えるだけで、磁界の回る方向が逆になって回転が反対になるんだ。全部入れ替えると元に戻っちゃうから注意してね！"
    } ,
        {
        "q": "一般用電気工作物の電路において、地絡（漏電）が生じた際に自動的に電路を遮断する装置はどれ？",
        "choices": [
            "イ. 配線用遮断器",
            "ロ. 漏電遮断器",
            "ハ. 電磁接触器",
            "ニ. リモコンリレー"
        ],
        "correct": "ロ",
        "info": "漏電を検知して火災や感電を防ぐのは「漏電遮断器」の役割だよ。配線用遮断器（ブレーカ）は「電気の使いすぎ（過電流）」を守るものだから、違いをしっかり押さえておこうね！"
    },
        {
        "q": "電気工事士法において、第二種電気工事士が従事できる電気工事の範囲として正しいものはどれ？",
        "choices": [
            "イ. 600V以下で受電する一般用電気工作物",
            "ロ. すべての自家用電気工作物",
            "ハ. 最大電力500kW未満の自家用電気工作物",
            "ニ. 鉄道の信号回路工事のみ"
        ],
        "correct": "イ",
        "info": "第二種電気工事士は、一般家庭や商店などの「一般用電気工作物」の工事ができるよ。ビルなどの自家用電気工作物は、500kW未満であっても第一種や認定が必要になるから注意してね。"
    },
        {
        "q": "厚鋼電線管（ねじなし電線管を除く）の相互を接続する場合に使用する材料はどれ？",
        "choices": [
            "イ. カップリング",
            "ロ. ブッシング",
            "ハ. ロックナット",
            "ニ. サドル"
        ],
        "correct": "イ",
        "info": "管と管を繋ぐのは「カップリング」だよ。ブッシングは管の端で電線を保護するもの、ロックナットは管をボックスに固定するもの、サドルは管を壁に固定するものだよ。用途をセットで覚えよう！"
    },
        {
        "q": "回路計（テスタ）を用いて測定できる項目として、誤っているものはどれ？",
        "choices": [
            "イ. 直流電圧",
            "ロ. 交流電圧",
            "ハ. 抵抗",
            "ニ. 絶縁抵抗"
        ],
        "correct": "ニ",
        "info": "テスタは電圧や抵抗の「目安」を測るのには便利だけど、1MΩを超えるような大きな「絶縁抵抗」を測るには専用の絶縁抵抗計（メガー）が必要なんだ"
    },
        {
        "q": "単相3線式100/200Vの屋内配線において、中性線に接続してはいけないものはどれ？",
        "choices": [
            "イ. 接地線",
            "ロ. 過電流遮断器（ヒューズ）",
            "ハ. 連結端子",
            "ニ. 白色の絶縁電線"
        ],
        "correct": "ロ",
        "info": "中性線にヒューズを入れてそれが切れると、100Vの機器に200Vがかかって壊れちゃう（事故になる）可能性があるんだ。だから中性線には過電流遮断器を設置してはいけない決まりになっているよ！"
        },
        {
        "q": "一般住宅の100V屋内配線で、壁に埋め込んで使用するスイッチを固定するために使われる材料はどれ？",
        "choices": [
            "イ. スイッチボックス",
            "ロ. アウトレットボックス",
            "ハ. プルボックス",
            "ニ. ジョイントボックス"
        ],
        "correct": "イ",
        "info": "壁の中でスイッチやコンセントを固定するのは「スイッチボックス」だよ。アウトレットボックスは電線の接続や、照明器具の取り付けなどに幅広く使われる箱のことだね！"
    },
    {
        "q": "電気工事において、回路の電圧を測定するために使用する測定器の名称と、その接続方法の組み合わせとして正しいものは？",
        "choices": [
            "イ. 電圧計 ー 回路に直列に接続する",
            "ロ. 電圧計 ー 回路に並列に接続する",
            "ハ. 電流計 ー 回路に直列に接続する",
            "ニ. 電流計 ー 回路に並列に接続する"
        ],
        "correct": "ロ",
        "info": "電圧は「並列（横からまたぐ感じ）」、電流は「直列（回路の途中に入る感じ）」で測るのが鉄則だよ"
      },
      {
        "q": "「VVF」という名称の電線において、最初の「V」が表している絶縁材料はどれ？",
        "choices": [
            "イ. ポリエチレン",
            "ロ. ゴム",
            "ハ. ビニル",
            "ニ. 架橋ポリエチレン"
        ],
        "correct": "ハ",
        "info": "Vは「ビニル」の頭文字だよ！VVFは『ビニル絶縁・ビニルシース・平形ケーブル』の略なんだ"
    },    
    {
        "q": "合成樹脂製可とう電線管（PF管）をコンクリート内に埋設する場合に使用できる管の種類はどれ？",
        "choices": [
            "イ. CD管のみ",
            "ロ. PF管のみ",
            "ハ. CD管およびPF管の両方",
            "ニ. 金属管のみ"
        ],
        "correct": "ハ",
        "info": "コンクリート内にはCD管（オレンジ色）とPF管（白色など）の両方が使えるよ。ただし、露出配線には紫外線に強いPF管しか使えないからね"
    }
            ]
            st.session_state.questions = data.copy()
            random.shuffle(st.session_state.questions)
            st.session_state.index, st.session_state.score, st.session_state.combo = 0, 0, 0
            st.session_state.answered = False
            st.session_state.mode = "quiz"
            st.rerun()

    with col2:
        if st.button("🔵 過去問に挑戦", use_container_width=True):
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
                    "info": "電力Pは V×I だから、抵抗Rは V/I、V²/P、P/I² のいずれかで表せるよ。P/I は電圧になるため誤りだね。",
                    "source": "出典：令和7年度下期 第二種電気工事士試験（学科）"
                },
                {
                    "q": "電熱器により60kgの水の温度を20K上昇させるのに必要な電力量[kW·h]は。ただし、水の比熱4.2kJ/(kg·K)とし、熱効率は100%とする。",
                    "choices": ["イ. 1.0", "ロ. 1.2", "ハ. 1.4", "ニ. 1.6"],
                    "correct": "ハ",
                    "info": "水を20 K上昇させるのに必要な熱量は60×4.2×20=5040kJとなり、これは 1.4kW･h に相当するよ。熱効率100％なので、この値がそのまま必要な電力量になるんだ。",
                    "source": "出典：令和7年度下期 第二種電気工事士試験（学科）"
                },
                {
                    "q": "図のような三相負荷に三相交流電圧を加えたとき、各線に20Aの電流が流れた。線間電圧E[V]は。",
                    "img": "images3.jpg", 
                    "choices": ["イ. 120", "ロ. 173", "ハ. 208", "ニ. 240"],
                    "correct": "ハ",
                    "info": "デルタ結線では、線間電圧と相電圧が同じになるよ。抵抗1つあたりの相電圧は V=I*Rだけど、相電流は線電流の1/√3になる点に注意。",
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
            st.session_state.index, st.session_state.score, st.session_state.combo = 0, 0, 0
            st.session_state.answered = False
            st.session_state.mode = "quiz"
            st.rerun()

elif st.session_state.mode == "quiz":
    if st.session_state.index >= len(st.session_state.questions):
        st.balloons()
        st.title("🎉 全問終了！")
        st.metric("最終スコア", f"{st.session_state.score} / {len(st.session_state.questions)}")
        if st.button("もう一度挑戦する", use_container_width=True):
            st.session_state.mode = "top"
            st.rerun()
        st.stop()

    current = st.session_state.questions[st.session_state.index]
    st.title("⚡ 学科対策")
    st.progress(st.session_state.index / len(st.session_state.questions))
    
    col_stat1, col_stat2 = st.columns(2)
    col_stat1.write(f"問題: {st.session_state.index + 1} / {len(st.session_state.questions)}")
    col_stat2.write(f"🔥 コンボ: {st.session_state.combo}")

    st.markdown(f'<div class="question-container"><h3>Q. {current["q"]}</h3></div>', unsafe_allow_html=True)
    if "source" in current: st.caption(current["source"])

    if "img" in current:
        try:
            st.image(current["img"], use_container_width=True)
        except:
            st.warning("画像が見つかりませんでした")

# ラベルを消して、選択肢を表示（変数の名前をcurrentに合わせたよ）
    selected = st.radio(
        "選択肢を選んでね", 
        current["choices"], 
        index=None, 
        key=f"q_{st.session_state.index}", 
        disabled=st.session_state.answered,
        label_visibility="collapsed"
    )

    # ここからのインデント（左の空白）を合わせるのが大事！
    if not st.session_state.answered:
        if st.button("回答を確定する", type="primary", use_container_width=True):
            if selected:
                st.session_state.selected = selected
                st.session_state.answered = True
                st.rerun()
            else:
                st.warning("どれか選んでね！")
    else:
        is_correct = st.session_state.selected.startswith(current["correct"])
        if is_correct:
            # スマホでも見えるキラキラふわっと演出
            st.markdown('<div class="キラキラ正解">✨ 正解！おめでとう！ ✨</div>', unsafe_allow_html=True)
            st.balloons()
            st.session_state.score += 1
            st.session_state.combo += 1
        else:
            st.error(f"残念！ 正解は「{current['correct']}」でした。")
            st.session_state.combo = 0

        st.markdown(f'<div class="info-container"><strong>💡 解説:</strong><br>{current["info"]}</div>', unsafe_allow_html=True)

        if st.button("次の問題へ ➔", use_container_width=True):
            st.session_state.index += 1
            st.session_state.answered = False
            st.rerun()

st.divider()
st.caption("keep it up! 毎日コツコツが合格への近道です")
