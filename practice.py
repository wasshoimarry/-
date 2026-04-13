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
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <style>
        body {{
            margin: 0;
            font-family: sans-serif;
            background: white;
        }}

        .wrapper {{
            width: 100%;
            box-sizing: border-box;
        }}

        textarea {{
            width: 100%;
            min-height: 320px;
            padding: 14px;
            font-size: 16px;
            line-height: 1.6;
            border: 1px solid #cfcfcf;
            border-radius: 8px;
            box-sizing: border-box;
            resize: vertical;
            outline: none;
        }}

        textarea:focus {{
            border-color: #ff4b4b;
        }}

        .stats {{
            margin-top: 14px;
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
        }}

        .card {{
            flex: 1;
            min-width: 180px;
            padding: 14px;
            border: 1px solid #e5e5e5;
            border-radius: 10px;
            background: #fafafa;
            box-sizing: border-box;
        }}

        .label {{
            font-size: 14px;
            color: #666;
            margin-bottom: 6px;
        }}

        .value {{
            font-size: 26px;
            font-weight: bold;
            color: #111;
        }}

        .status {{
            margin-top: 14px;
            font-size: 16px;
            font-weight: bold;
        }}

        .ok {{
            color: green;
        }}

        .over {{
            color: red;
        }}

        .empty {{
            color: #666;
        }}
    </style>
</head>
<body>
    <div class="wrapper">
        <textarea id="textInput" placeholder="ここにESの文章を入力してください"></textarea>

        <div class="stats">
            <div class="card">
                <div class="label">現在の文字数</div>
                <div class="value" id="countValue">0</div>
            </div>
            <div class="card">
                <div class="label">残り文字数</div>
                <div class="value" id="remainingValue">{st.session_state.limit}</div>
            </div>
        </div>

        <div class="status empty" id="statusInfo">
            文章を入力するとリアルタイムで更新されます
        </div>
    </div>

    <script>
        const textInput = document.getElementById("textInput");
        const countValue = document.getElementById("countValue");
        const remainingValue = document.getElementById("remainingValue");
        const statusInfo = document.getElementById("statusInfo");
        const limit = {st.session_state.limit};

        function updateCount() {{
            const text = textInput.value;
            const count = text.length;
            const remaining = limit - count;

            countValue.textContent = count;
            remainingValue.textContent = remaining;

            if (count === 0) {{
                statusInfo.textContent = "文章を入力するとリアルタイムで更新されます";
                statusInfo.className = "status empty";
            }} else if (remaining >= 0) {{
                statusInfo.textContent = "制限内です";
                statusInfo.className = "status ok";
            }} else {{
                statusInfo.textContent = Math.abs(remaining) + "文字オーバーです";
                statusInfo.className = "status over";
            }}
        }}

        textInput.addEventListener("input", updateCount);
        updateCount();
    </script>
</body>
</html>
"""

components.html(html_code, height=520, scrolling=False)
