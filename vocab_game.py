import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")

# -----------------------------
# ตั้งค่าเริ่มต้น Session State
# -----------------------------
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""

if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""

if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""

if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""

if "is_ended" not in st.session_state:
    st.session_state.is_ended = False


# -----------------------------
# ฟังก์ชันเริ่มเกมใหม่
# -----------------------------
def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""

    st.session_state.start = time.time()
    st.session_state.is_ended = False


# -----------------------------
# แสดงผลคะแนน
# -----------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4):

    st.balloons()

    score = 0

    # แปลงคำตอบให้เป็นตัวพิมพ์เล็ก
    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()

    # ข้อ 1
    if u_ans1 == "apple":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

    # ข้อ 2
    if u_ans2 == "fish":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

    # ข้อ 3
    if u_ans3 == "school":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")

    # ข้อ 4
    if u_ans4 == "garden":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")

    # คะแนนรวม
    st.info(f"🏆 ได้คะแนนรวม: {score} / 4 คะแนน")

    if score == 4:
        st.success("🎉 You win!")
    else:
        st.error("💀 You lose!")


# -----------------------------
# ปุ่มเริ่มเกม
# -----------------------------
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)


# -----------------------------
# ระบบจับเวลา
# -----------------------------
if "start" in st.session_state and not st.session_state.is_ended:

    elapsed_time = time.time() - st.session_state.start
    time_left = max(0, int(30 - elapsed_time))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()


st.divider()


# -----------------------------
# ช่องกรอกคำตอบ
# -----------------------------
ans1 = st.text_input(
    "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎",
    key="ans1_val"
)

ans2 = st.text_input(
    "ข้อ 2: Cats love to eat `f _ s h`. 🐟",
    key="ans2_val"
)

ans3 = st.text_input(
    "ข้อ 3: I go to `_ c _ o o _` on weekdays. 🏫",
    key="ans3_val"
)

ans4 = st.text_input(
    "ข้อ 4: The flowers are in the `g _ r d e _`. 🌼",
    key="ans4_val"
)


# -----------------------------
# ปุ่มส่งคำตอบ
# -----------------------------
if "start" in st.session_state and not st.session_state.is_ended:

    if st.button("📥 ส่งคำตอบ"):

        st.session_state.is_ended = True
        st.rerun()

    # อัปเดตหน้าจอทุก 1 วินาที
    time.sleep(1)
    st.rerun()


# -----------------------------
# แสดง Dialog ผลลัพธ์
# -----------------------------
if st.session_state.is_ended and "start" in st.session_state:

    show_result_dialog(
        st.session_state.ans1_val,
        st.session_state.ans2_val,
        st.session_state.ans3_val,
        st.session_state.ans4_val
    )


st.divider()

st.write("นางสาวสุมณกัญญา ชวดต่าย เลขที่ 25 ม.4/3")
