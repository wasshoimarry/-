import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="就活用 文字数カウントツール", layout="centered")

if "limit" not in st.session_state:
    st.session_state.limit = 300

st.title("就活用 文字数カウントツール")
st.caption("入力しながらリアルタイムで文字数をカウントします")

limit_options = [200, 300, 400, 500]

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

html_code = f"""
<!DOCTYPE html>
<html>
<head>
<style>
    body {{
        font-family: sans-serif;
        margin: 0;
    }}
    textarea {{
        width: 100%;
        min-height: 320px;
        padding: 14px;
        font-size: 16px;
        line-height: 1.6;
        border: 1px solid #ccc;
        border-radius: 8px;
        box-sizing: border-box;
        resize: vertical;
    }}
    .stats {{
        margin-top: 14px;
        font-size: 18px;
        font-weight: bold;
    }}
    .status {{
        margin-top: 10px;
        font-size: 16px;
    }}
    .ok {{
        color: green;
    }}
    .over {{
        color: red;
    }}
</style>
</head>
<body>

<textarea id="textInput" placeholder="ここにESの文章を入力してください"></textarea>

<div class="stats" id="countInfo">
    現在の文字数: 0文字
</div>

<div class="stats" id="remainingInfo">
    残り文字数: {st.session_state.limit}文字
</div>

<div class="status" id="statusInfo">
    制限内です
</div>

<script>
    const textInput = document.getElementById("textInput");
    const countInfo = document.getElementById("countInfo");
    const remainingInfo = document.getElementById("remainingInfo");
    const statusInfo = document.getElementById("statusInfo");
    const limit = {st.session_state.limit};

    function updateCount() {{
        const count = textInput.value.length;
        const remaining = limit - count;

        countInfo.innerHTML = "現在の文字数: " + count + "文字";
        remainingInfo.innerHTML = "残り文字数: " + remaining + "文字";

        if (remaining >= 0) {{
            statusInfo.innerHTML = "制限内です";
            statusInfo.className = "status ok";
        }} else {{
            statusInfo.innerHTML = Math.abs(remaining) + "文字オーバーです";
            statusInfo.className = "status over";
        }}
    }}

    textInput.addEventListener("input", updateCount);
</script>

</body>
</html>
"""

components.html(html_code, height=520)
