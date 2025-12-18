# Copyright Luu Anh Hoang THPT NGUYEN CONG HOAN

import streamlit as st

st.set_page_config(page_title="AutoSafe Bot", layout="centered")

# --- DATABASE ---
DATA = {
    "xe_nang": """
### QUY TRÌNH VẬN HÀNH XE NÂNG
1. Kiểm tra phanh, lốp và hệ thống thủy lực trước khi chạy.
2. Không nâng hàng quá tải trọng quy định.
3. Khi di chuyển phải hạ thấp càng nâng để giữ trọng tâm.
4. Tắt máy, hạ càng sát đất và rút chìa khóa khi đỗ xe.
    """,
    "bao_ho": """
### TRANG BỊ BẢO HỘ (PPE)
1. Mũ bảo hộ: Bảo vệ đầu khỏi vật rơi từ trên cao.
2. Giày bảo hộ: Loại có mũi sắt chống dập ngón và đế chống trượt.
3. Kính bảo hộ: Sử dụng khi cắt, mài hoặc tiếp xúc hóa chất.
4. Găng tay: Sử dụng loại phù hợp (chống cắt hoặc chống hóa chất).
    """,
    "sac_binh": """
### AN TOÀN SẠC BÌNH ẮC QUY
1. Sạc tại nơi thông thoáng, xa nguồn lửa hoặc tia lửa điện.
2. Mở nắp hộc bình để thoát khí Hydro trong quá trình sạc.
3. Chỉ châm thêm nước cất, không châm quá vạch quy định.
4. Tuyệt đối không chạm vào điện khi tay đang ướt.
    """
}

# --- LOGIC XỬ LÝ ---
def get_answer(text):
    text = text.lower()
    if any(k in text for k in ["xe nâng", "xe nang", "lái xe"]):
        return DATA["xe_nang"]
    elif any(k in text for k in ["bảo hộ", "bao ho", "mũ", "giày", "găng"]):
        return DATA["bao_ho"]
    elif any(k in text for k in ["sạc", "sac", "ắc quy", "ac quy", "bình"]):
        return DATA["sac_binh"]
    return "Vui lòng nhập từ khóa chính xác như: xe nâng, bảo hộ, sạc bình."

# Khởi tạo các biến lưu trữ
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "AutoSafe Bot xin chào! Bạn cần hỗ trợ gì?"}]

if "input_value" not in st.session_state:
    st.session_state.input_value = ""

# --- Theme Hiển Thị CỰC VÍP ---
st.title("AUTOSAFE BOT")

# Hiển thị đoạn để sủaa
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
def suggest_text(keyword):
    st.session_state.input_value = keyword
st.write("---")
cols = st.columns([1, 1, 1, 3])
with cols[0]:
    if st.button("xe nâng"): suggest_text("xe nâng")
with cols[1]:
    if st.button("bảo hộ"): suggest_text("bảo hộ")
with cols[2]:
    if st.button("sạc bình"): suggest_text("sạc bình")

# note text vào đây
prompt = st.chat_input("Nhập tin nhắn...", key="chat_widget")
if st.session_state.input_value and not prompt:
    prompt = st.session_state.input_value
    st.session_state.input_value = "" # Xóa đi để lần sau không bị lặp
    #send the input
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    res = get_answer(prompt)
    st.session_state.messages.append({"role": "assistant", "content": res})
    with st.chat_message("assistant"):
        st.markdown(res)
    st.rerun()

    # hêt con mẹ nó bài rồi ông cháu ơi
