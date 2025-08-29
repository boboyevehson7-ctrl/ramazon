import streamlit as st
import random

# -----------------------------
# 50 ta noto‘g‘ri fe’l (Present, Past, PP, Uzbekcha)
# -----------------------------
VERBS = [
    {"base": "be", "past": "was/were", "pp": "been", "uz": "bo‘l-"},
    {"base": "become", "past": "became", "pp": "become", "uz": "bo‘lib qolmoq"},
    {"base": "begin", "past": "began", "pp": "begun", "uz": "boshlamoq"},
    {"base": "break", "past": "broke", "pp": "broken", "uz": "sindirmoq"},
    {"base": "bring", "past": "brought", "pp": "brought", "uz": "olib kelmoq"},
    {"base": "build", "past": "built", "pp": "built", "uz": "qurmoq"},
    {"base": "buy", "past": "bought", "pp": "bought", "uz": "sotib olmoq"},
    {"base": "choose", "past": "chose", "pp": "chosen", "uz": "tanlamoq"},
    {"base": "come", "past": "came", "pp": "come", "uz": "kelmoq"},
    {"base": "do", "past": "did", "pp": "done", "uz": "qilmoq"},
    {"base": "drink", "past": "drank", "pp": "drunk", "uz": "ichmoq"},
    {"base": "drive", "past": "drove", "pp": "driven", "uz": "haydamoq"},
    {"base": "eat", "past": "ate", "pp": "eaten", "uz": "yemoq"},
    {"base": "fall", "past": "fell", "pp": "fallen", "uz": "yiqilmoq"},
    {"base": "feel", "past": "felt", "pp": "felt", "uz": "his qilmoq"},
    {"base": "find", "past": "found", "pp": "found", "uz": "topmoq"},
    {"base": "get", "past": "got", "pp": "gotten", "uz": "olmoq"},
    {"base": "give", "past": "gave", "pp": "given", "uz": "bermoq"},
    {"base": "go", "past": "went", "pp": "gone", "uz": "bor-"},
    {"base": "have", "past": "had", "pp": "had", "uz": "ega bo‘lmoq"},
    {"base": "hear", "past": "heard", "pp": "heard", "uz": "eshitmoq"},
    {"base": "keep", "past": "kept", "pp": "kept", "uz": "saqlamoq"},
    {"base": "know", "past": "knew", "pp": "known", "uz": "bilmoq"},
    {"base": "leave", "past": "left", "pp": "left", "uz": "tark etmoq"},
    {"base": "lose", "past": "lost", "pp": "lost", "uz": "yo‘qotmoq"},
    {"base": "make", "past": "made", "pp": "made", "uz": "tayyorlamoq"},
    {"base": "meet", "past": "met", "pp": "met", "uz": "uchrashmoq"},
    {"base": "pay", "past": "paid", "pp": "paid", "uz": "to‘lamoq"},
    {"base": "put", "past": "put", "pp": "put", "uz": "qo‘ymoq"},
    {"base": "read", "past": "read", "pp": "read", "uz": "o‘qimoq"},
    {"base": "run", "past": "ran", "pp": "run", "uz": "yugurmoq"},
    {"base": "say", "past": "said", "pp": "said", "uz": "aytmoq"},
    {"base": "see", "past": "saw", "pp": "seen", "uz": "ko‘rmoq"},
    {"base": "sell", "past": "sold", "pp": "sold", "uz": "sotmoq"},
    {"base": "send", "past": "sent", "pp": "sent", "uz": "jo‘natmoq"},
    {"base": "sit", "past": "sat", "pp": "sat", "uz": "o‘tirmoq"},
    {"base": "speak", "past": "spoke", "pp": "spoken", "uz": "gapirmoq"},
    {"base": "spend", "past": "spent", "pp": "spent", "uz": "sarflamoq"},
    {"base": "stand", "past": "stood", "pp": "stood", "uz": "turmoq"},
    {"base": "take", "past": "took", "pp": "taken", "uz": "olmoq"},
    {"base": "teach", "past": "taught", "pp": "taught", "uz": "o‘rgatmoq"},
    {"base": "tell", "past": "told", "pp": "told", "uz": "aytib bermoq"},
    {"base": "think", "past": "thought", "pp": "thought", "uz": "o‘ylamoq"},
    {"base": "understand", "past": "understood", "pp": "understood", "uz": "tushunmoq"},
    {"base": "wear", "past": "wore", "pp": "worn", "uz": "kiymoq"},
    {"base": "win", "past": "won", "pp": "won", "uz": "yutmoq"},
    {"base": "write", "past": "wrote", "pp": "written", "uz": "yozmoq"},
    {"base": "swim", "past": "swam", "pp": "swum", "uz": "suzmoq"},
    {"base": "cut", "past": "cut", "pp": "cut", "uz": "kesmoq"},
    {"base": "let", "past": "let", "pp": "let", "uz": "ruxsat bermoq"},
]

# -----------------------------
# Yordamchi: javobni tekshirish (masalan "was/were" uchun)
# -----------------------------
def normalize_set(ans: str):
    # "was/were" -> {"was", "were", "was/were"}
    parts = [p.strip().lower() for p in ans.replace(",", "/").split("/") if p.strip()]
    s = set(parts)
    s.add(ans.strip().lower())
    return s

def is_correct(user_inp: str, correct_ans: str):
    return user_inp.strip().lower() in normalize_set(correct_ans)

# -----------------------------
# Streamlit sahifa sozlamalari
# -----------------------------
st.set_page_config(page_title="Noto‘g‘ri fe’llar", page_icon="📚", layout="centered")
st.title("📚 Noto‘g‘ri fe’llar — o‘rganish va test")

menu = st.sidebar.radio("Bo‘limni tanlang:", ["📖 Jadval", "🎯 Test"])

# -----------------------------
# 📖 1-bo‘lim: Jadval
# -----------------------------
if menu == "📖 Jadval":
    st.subheader("50 ta asosiy noto‘g‘ri fe’l (3 shakl + tarjima)")
    st.dataframe(
        [{"Present": v["base"], "Past": v["past"], "Past Participle": v["pp"], "Tarjima (UZ)": v["uz"]} for v in VERBS],
        use_container_width=True
    )
    st.info("Maslahat: Avval jadvalni ko‘zdan kechir, keyin testga o‘t 😉")

# -----------------------------
# 🎯 2-bo‘lim: Test
# -----------------------------
else:
    st.subheader("Irregular Verbs — Test")

    # Boshlashdan oldingi sozlamalar
    if "quiz_active" not in st.session_state:
        st.session_state.quiz_active = False
        st.session_state.q_total = 0
        st.session_state.q_index = 0
        st.session_state.score = 0
        st.session_state.ask_form = "Aralash"
        st.session_state.queue = []

    if not st.session_state.quiz_active:
        col1, col2 = st.columns(2)
        with col1:
            q_total = st.selectbox("Savollar soni:", [5, 10, 15, 20], index=1)
        with col2:
            ask_form = st.selectbox("Qaysi shakl?", ["2-shakl", "3-shakl", "Aralash"], index=2)

        if st.button("🚀 Testni boshlash"):
            st.session_state.quiz_active = True
            st.session_state.q_total = q_total
            st.session_state.q_index = 0
            st.session_state.score = 0
            st.session_state.ask_form = ask_form

            # savollar navbati: tasodifiy tanlaymiz
            st.session_state.queue = [random.choice(VERBS) for _ in range(q_total)]

    else:
        # Hozirgi savol
        verb = st.session_state.queue[st.session_state.q_index]

        # Qaysi shakl so‘raladi
        if st.session_state.ask_form == "Aralash":
            form_key = random.choice(["past", "pp"])
        elif st.session_state.ask_form == "2-shakl":
            form_key = "past"
        else:
            form_key = "pp"

        # Savol matni
        st.write(f"### ❓ Fe’l: **{verb['base']}**  _(UZ: {verb['uz']})_")
        st.write(f"**Shu fe’lning {'Past (2-shakl)' if form_key=='past' else 'Past Participle (3-shakl)'} shaklini yozing.**")

        # Javob kiritish
        answer = st.text_input("Javobingiz:", key=f"ans_{st.session_state.q_index}")

        # Pastdagi ko‘rsatkichlar
        left = st.session_state.q_total - st.session_state.q_index
        st.write(f"📊 Ball: **{st.session_state.score}** | 🔢 Qolgan savollar: **{left}**")

        # Tekshirish
        if st.button("✅ Tekshirish", key=f"chk_{st.session_state.q_index}"):
            correct = verb[form_key]
            if is_correct(answer, correct):
                st.success("To‘g‘ri! ✅")
                st.session_state.score += 1
            else:
                st.error(f"Noto‘g‘ri. To‘g‘ri javob: **{correct}**")

            st.session_state.q_index += 1

            # Tugadimi?
            if st.session_state.q_index >= st.session_state.q_total:
                st.session_state.quiz_active = False
                # Natija
                score = st.session_state.score
                total = st.session_state.q_total
                percent = int(round(score * 100 / total))

                st.markdown("---")
                st.subheader("🏁 Yakuniy natija")
                st.write(f"Ball: **{score}/{total}**  —  Foiz: **{percent}%**")

                if percent >= 60:
                    st.success(
                        "Biz sizni tabriklaymiz! Siz yaxshi ishladingiz, shunday davom eting. "
                        "Hurmat bilan — **Nurmahmadov Ramazon**."
                    )
                else:
                    st.info("Harakatda davom et! Keyingi safar albatta ko‘tarilasiz 💪")

                if st.button("🔄 Yana test ishlash"):
                    # Reset
                    st.session_state.quiz_active = False
                    st.session_state.q_total = 0
                    st.session_state.q_index = 0
                    st.session_state.score = 0
                    st.session_state.queue = []
            else:
                st.rerun()

