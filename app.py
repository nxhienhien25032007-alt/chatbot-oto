import streamlit as st

# --- CẤU HÌNH TRANG WEB ---
st.set_page_config(page_title="Trợ lý An toàn AutoShop", page_icon="🛡️", layout="wide")

# --- MENU BÊN TRÁI ---
with st.sidebar:
    st.header("🔍 Hướng dẫn tra cứu")
    st.markdown("Nhập từ khóa như:")
    st.code("xe nâng")
    st.code("bảo hộ")
    st.code("sạc bình")
    st.divider()
    st.info("💡 Mẹo: Nhập câu hỏi ngắn gọn để bot trả lời chính xác nhất.")

# --- GIAO DIỆN CHÍNH ---
st.title("🛡️ TRỢ LÝ AN TOÀN XƯỞNG DỊCH VỤ")
st.write("---") 

# --- KHỞI TẠO LỊCH SỬ CHAT ---
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Chào bạn! Tôi có thể giúp gì về quy trình an toàn hôm nay?"}]

# --- HIỂN THỊ LỊCH SỬ ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- HÀM XỬ LÝ TRẢ LỜI ---
def get_detailed_response(user_input):
    text = user_input.lower()
    
    # 1. XE NÂNG
    if any(word in text for word in ["xe nâng", "nâng hàng", "lái xe", "vận hành"]):
        return """
### 🚜 QUY TRÌNH VẬN HÀNH XE NÂNG AN TOÀN

**1. Trước khi vận hành:**
* ✅ Kiểm tra: Phanh, lốp, càng nâng, hệ thống thủy lực.
* ✅ Kiểm tra nhiên liệu: Mức dầu hoặc mức dung dịch ắc quy.

**2. Khi nâng/hạ hàng:**
* ⚠️ **Tải trọng:** Đảm bảo < tải trọng cho phép.
* ⚠️ **Di chuyển:** Hạ càng thấp nhất có thể, giữ trọng tâm thấp.
* ⛔ **Tuyệt đối:** KHÔNG phanh gấp, KHÔNG cua gấp.
* 🚶 **An toàn:** Giữ khoảng cách an toàn với người đi bộ.

**3. Sau khi sử dụng:**
* Đỗ xe đúng nơi quy định ➡️ Tắt máy ➡️ Hạ càng xuống sát đất ➡️ Vệ sinh xe.
        """

    # 2. BẢO HỘ LAO ĐỘNG (PPE)
    elif any(word in text for word in ["ppe", "bảo hộ", "mũ", "giày", "găng", "kính", "mặc"]):
        return """
### 🛡️ TRANG BỊ BẢO HỘ CÁ NHÂN (PPE) BẮT BUỘC

Để đảm bảo an toàn, bạn cần trang bị đủ:

* **👷 Mũ bảo hộ:** Bảo vệ đầu khỏi vật rơi.
* **🥾 Giày bảo hộ:** Đế chống trượt & mũi sắt (chống dập ngón).
* **👓 Kính bảo hộ:** Chống bụi & hóa chất văng vào mắt.
* **🧤 Găng tay:**
    * *Găng chống hóa chất:* Khi làm việc với ắc quy/dầu nhớt.
    * *Găng chống cắt:* Khi làm việc cơ khí.
* **💺 Đai an toàn (Xe nâng):** Bắt buộc thắt để tránh văng khỏi xe khi sự cố.
        """

    # 3. ĐIỆN & ẮC QUY
    elif any(word in text for word in ["điện", "sạc", "ắc quy", "bình", "axit", "nước cất"]):
        return """
### ⚡ AN TOÀN ĐIỆN & BẢO DƯỠNG ẮC QUY

**🔋 Quy trình Sạc ắc quy:**
* 📍 **Vị trí:** Nơi thoáng khí, xa nguồn lửa.
* 🌡️ **Nhiệt độ:** Không sạc khi bình nóng > 50°C.
* 💨 **Lưu ý:** Phải mở nắp hộc bình để thoát khí (tránh nổ).

**🛠️ Bảo dưỡng:**
* 💧 **Châm nước:** Chỉ dùng **NƯỚC CẤT**, không châm quá vạch phao trắng.
* 🧪 **Kiểm tra:** Tỷ trọng dung dịch (Axit H₂SO₄ loãng).
* 🧼 **Vệ sinh:** Lau sạch bình sau khi sạc.

**🔌 An toàn chung:**
* 🚫 Không chạm vào điện khi tay ướt.
* ⚠️ Giữ khoảng cách với dây điện cao thế.
        """

    # 4. NỘI QUY XƯỞNG
    elif any(word in text for word in ["nội quy", "quy định", "vệ sinh", "cấm", "5s"]):
        return """
### 📋 TÓM TẮT NỘI QUY XƯỞNG

* **1. Tuân thủ:** Luôn mặc đủ PPE và làm đúng quy trình.
* **2. Vệ sinh (5S):** Sàng lọc - Sắp xếp - Sạch sẽ - Săn sóc - Sẵn sàng.
* **3. Báo cáo:** Báo ngay quản lý nếu thấy máy hỏng/nguy hiểm.
* **4. Cấm:** ⛔ KHÔNG mang đồ ăn, vật dụng cá nhân vào nơi sửa chữa.
        """
    
    # 5. CHÀO HỎI / KHÔNG HIỂU
    elif "chào" in text or "hi" in text:
        return "👋 Xin chào! Bạn cần tra cứu về: **Xe nâng**, **Đồ bảo hộ**, **Ắc quy** hay **Nội quy**?"
    
    else:
        return """
        Xin lỗi, tôi chưa hiểu rõ. Bạn hãy thử gõ các từ khóa chính như:
        * *Xe nâng*
        * *Sạc bình*
        * *Đồ bảo hộ*
        """

# --- XỬ LÝ DỮ LIỆU ---
if prompt := st.chat_input("Nhập câu hỏi..."):
    # Hiện câu hỏi người dùng
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Hiện câu trả lời của Bot (Hiện ngay lập tức, không chạy chữ)
    with st.chat_message("assistant"):
        full_response = get_detailed_response(prompt)
        st.markdown(full_response)
        
    # Lưu vào lịch sử
    st.session_state.messages.append({"role": "assistant", "content": full_response})