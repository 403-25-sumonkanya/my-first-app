import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")


# ----------------------------------------------------
# 1. กำหนดค่าเริ่มต้นใน session_state
# ----------------------------------------------------
if "ans1" not in st.session_state:
    st.session_state.ans1 = ""

if "ans2" not in st.session_state:
    st.session_state.ans2 = ""

if "ans3" not in st.session_state:
    st.session_state.ans3 = ""

if "ans4" not in st.session_state:
    st.session_state.ans4 = ""

if "start" not in st.session_state:
    st.session_state.start = None

if "is_ended" not in st.session_state:
    st.session_state.is_ended = False


# ----------------------------------------------------
# 2. ฟังก์ชันเริ่มเกมใหม่
# ----------------------------------------------------
def reset_game():
    st.session_state.ans1 = ""
    st.session_state.ans2 = ""
    st.session_state.ans3 = ""
    st.session_state.ans4 = ""

    st.session_state.start = time.time()
    st.session_state.is_ended = False


# ----------------------------------------------------
# 3. Dialog แสดงผล
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog():
    st.balloons()

    score = 0

    # ดึงคำตอบจาก session_state
    u_ans1 = st.session_state.ans1.strip().lower()
    u_ans2 = st.session_state.ans2.strip().lower()
    u_ans3 = st.session_state.ans3.strip().lower()
    u_ans4 = st.session_state.ans4.strip().lower()

    # ---------------- ข้อ 1 ----------------
    if u_ans1 == "apple":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(
            f"❌ ข้อ 1: ยังไม่ถูกต้อง "
            f"(คุณตอบ '{u_ans1}')"
        )

    # ---------------- ข้อ 2 ----------------
    if u_ans2 == "fish":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(
            f"❌ ข้อ 2: ยังไม่ถูกต้อง "
            f"(คุณตอบ '{u_ans2}')"
        )

    # ---------------- ข้อ 3 ----------------
    if u_ans3 == "school":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(
            f"❌ ข้อ 3: ยังไม่ถูกต้อง "
            f"(คุณตอบ '{u_ans3}')"
        )

    # ---------------- ข้อ 4 ----------------
    if u_ans4 == "garden":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(
            f"❌ ข้อ 4: ยังไม่ถูกต้อง "
            f"(คุณตอบ '{u_ans4}')"
        )

    # ---------------- คะแนนรวม ----------------
    st.info(f"🏆 ได้คะแนนรวม: {score} / 4 คะแนน")

    if score == 4:
        st.success("🎉 You win!")
    else:
        st.error("💀 You lose!")


# ----------------------------------------------------
# 4. ปุ่มเริ่มเกม
# ----------------------------------------------------
st.button(
    "🎮 เริ่มเล่นเกม",
    on_click=reset_game
)


# ----------------------------------------------------
# 5. แสดงเวลานับถอยหลัง
# ----------------------------------------------------
if (
    st.session_state.start is not None
    and not st.session_state.is_ended
):

    time_left = int(
        30 - (time.time() - st.session_state.start)
    )

    if time_left > 0:
        st.error(
            f"⏳ เหลือเวลา: {time_left} วินาที"
        )
    else:
        # หมดเวลา
        st.session_state.is_ended = True
        st.rerun()


st.divider()


# ----------------------------------------------------
# 6. ช่องกรอกคำตอบ
# ----------------------------------------------------
st.text_input(
    "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎",
    key="ans1"
)

st.text_input(
    "ข้อ 2: Cats love to eat `f _ s h`. 🐟",
    key="ans2"
)

st.text_input(
    "ข้อ 3: I go to `_ s c _ _ o _` on weekdays. 🏫",
    key="ans3"
)

st.text_input(
    "ข้อ 4: Flowers are in the `g _ r _ e n`. 🌼",
    key="ans4"
)


# ----------------------------------------------------
# 7. ปุ่มส่งคำตอบ
# ----------------------------------------------------
if (
    st.session_state.start is not None
    and not st.session_state.is_ended
):

    if st.button("📥 ส่งคำตอบ"):

        # จบเกม
        st.session_state.is_ended = True

        # แสดงผล
        st.rerun()


# ----------------------------------------------------
# 8. แสดง Dialog เมื่อเกมจบ
# ----------------------------------------------------
if st.session_state.is_ended:
    show_result_dialog()


# ----------------------------------------------------
# 9. ทำให้เวลานับถอยหลังทุก 1 วินาที
# ----------------------------------------------------
if (
    st.session_state.start is not None
    and not st.session_state.is_ended
):
    time.sleep(1)
    st.rerun()


st.divider()

st.write("นางสาวสุมณกัญญา ชวดต่าย เลขที่ 25 ม.4/3")
