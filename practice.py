import streamlit as st
from st_keyup import st_keyup

st.set_page_config(page_title="就活用 文字数カウントツール", layout="centered")

st.title("就活用 文字数カウントツール")
st.caption("入力しながら文字数をリアルタイムでカウントします")

limit_options = [200, 300, 400, 500]

if "limit" not in st.session_state:
    st.session_state.limit = 300

st.write("### 文字数上限を選択")
cols = st.columns(len(limit_options))
for i, value in enumerate(limit_options):
    if cols[i].button(f"{value}字", use_container_width=True):
        st.session_state.limit = value

limit = st.number_input(
    "文字数上限を手入力",
    min_value=1,
    value=st.session_state.limit,
    step=50,
)
st.session_state.limit = int(limit)

text = st_keyup(
    "文章を入力してください",
    value="",
    key="es_text",
    placeholder="ここにESの文章を入力してください",
)

count = len(text)
remaining = st.session_state.limit - count

col1, col2 = st.columns(2)
with col1:
    st.metric("現在の文字数", count)
with col2:
    st.metric("残り文字数", remaining)

progress = min(count / st.session_state.limit, 1.0)
st.progress(progress)

if count == 0:
    st.info("文章を入力すると文字数がリアルタイムで表示されます")
elif count <= st.session_state.limit:
    st.success("制限内です")
else:
    st.error(f"{abs(remaining)}文字オーバーです")
