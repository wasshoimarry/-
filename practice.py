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
            margin: 0;
            font-family: sans-serif;
        }}
        .wrapper {{
            width: 100%;
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
            outline: none;
        }}
        textarea:focus {{
            border-color: #ff4b4b;
        }}
        .info {{
            margin-top: 12px;
            font-size: 16px;
        }}
        .ok {{
            color: green;
            font-weight: bold;
        }}
        .over {{
            color: red;
            font-weight: bold;
        }}
        .empty {{
            color: #666;
        }}
    </style>
</head>
<body>
    <div class="wrapper">
        <textarea id="textInput" placeholder="ここにESの文章を入力してください"></textarea>
        <div class="info" id="countInfo">文字数: 0 / {st.session_state.limit}</div>
        <div class="info" id="remainingInfo">残り文字数: {st.session_state.limit}</div>
        <div class="info empty" id="statusInfo">文章を入力するとリアルタイムで文字数が表示されます</div>
    </div>

    <script>
        const textInput = document.getElementById("textInput");
        const countInfo = document.getElementById("countInfo");
        const remainingInfo = document.getElementById("remainingInfo");
        const statusInfo = document.getElementById("statusInfo");
        const limit = {st.session_state.limit};

        function updateCount() {{
            const text = textInput.value;
            const count = text.length;
            const remaining = limit - count;

            countInfo.textContent = `文字数: ${{count}} / ${{limit}}`;
            remainingInfo.textContent = `残り文字数: ${{remaining}}`;

            if (count === 0) {{
                statusInfo.textContent = "文章を入力するとリアルタイムで文字数が表示されます";
                statusInfo.className = "info empty";
            }} else if (count <= limit) {{
                statusInfo.textContent = "制限内です";
                statusInfo.className = "info ok";
            }} else {{
                statusInfo.textContent = `${{Math.abs(remaining)}}文字オーバーです`;
                statusInfo.className = "info over";
            }}
        }}

        textInput.addEventListener("input", updateCount);
        updateCount();
    </script>
</body>
</html>
"""

components.html(html_code, height=460, scrolling=False)
