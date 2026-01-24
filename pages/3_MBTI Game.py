import streamlit as st
import random

# --- 1. MBTI 데이터 및 질문 ---
MBTI_QUESTIONS = [
    # 라운드 1: E/I (외향성/내향성) - 10개 질문
    [
        {"question": "주말에 무엇을 하고 싶은가?", "E": "친구들과 활동적으로 시간을 보내기", "I": "혼자 조용히 휴식 취하기"},
        {"question": "새로운 사람을 만날 때 기분은?", "E": "설렘과 흥미로움", "I": "긴장하고 신중함"},
        {"question": "에너지를 어디서 얻는가?", "E": "사람과의 상호작용에서", "I": "혼자 있을 때"},
        {"question": "파티에서의 당신은?", "E": "많은 사람과 얘기하며 돌아다님", "I": "한두 사람과 깊은 대화"},
        {"question": "스트레스 해소 방법은?", "E": "외출해서 활동하기", "I": "집에서 휴식하기"},
        {"question": "휴일에 주로 무엇을 하는가?", "E": "외출해서 사람을 만남", "I": "집에서 여유 있게 지냄"},
        {"question": "그룹 활동에서 당신은?", "E": "주도적으로 나서서 리드함", "I": "필요할 때만 참여함"},
        {"question": "전화 통화를 좋아하는가?", "E": "다양한 사람들과 자주 통화함", "I": "필요한 경우에만 함"},
        {"question": "새로운 취미를 시작할 때는?", "E": "단체 활동으로 배우고 싶음", "I": "혼자 천천히 배우고 싶음"},
        {"question": "회사 행사에서의 당신은?", "E": "여러 사람과 네트워킹함", "I": "편한 사람들과만 어울림"}
    ],
    # 라운드 2: S/N (감각/직관) - 10개 질문
    [
        {"question": "결정할 때 중요한 것은?", "S": "구체적인 사실과 경험", "N": "가능성과 미래 비전"},
        {"question": "선호하는 일의 방식은?", "S": "검증된 방법으로 차근차근", "N": "창의적이고 새로운 방법으로"},
        {"question": "일을 배울 때 선호하는 방식은?", "S": "실무적이고 체계적으로", "N": "큰 그림을 먼저 이해하기"},
        {"question": "당신의 강점은?", "S": "세부사항 포착 및 실행력", "N": "패턴 인식 및 창의력"},
        {"question": "미래를 생각할 때는?", "S": "현실 기반으로", "N": "가능성 기반으로"},
        {"question": "새로운 프로젝트를 시작할 때는?", "S": "명확한 계획과 절차부터", "N": "전체적인 비전부터"},
        {"question": "문제 해결 방식은?", "S": "과거 경험과 사례로", "N": "새로운 이론과 가설로"},
        {"question": "독서할 때 선호하는 책은?", "S": "실용적이고 구체적인 책", "N": "철학적이고 추상적인 책"},
        {"question": "일상적인 작은 것들에 대해?", "S": "중요하고 주목할 가치 있음", "N": "흥미롭지만 큰 그림의 일부일 뿐"},
        {"question": "변화에 대한 태도는?", "S": "현재 상황을 개선하고 싶음", "N": "완전히 새로운 것을 시도하고 싶음"}
    ],
    # 라운드 3: T/F (사고/감정) - 10개 질문
    [
        {"question": "결정할 때 중시하는 것은?", "T": "논리와 객관적 분석", "F": "개인의 감정과 가치관"},
        {"question": "갈등 상황에서는?", "T": "문제를 논리적으로 해결", "F": "관계와 감정을 우선 고려"},
        {"question": "타인의 실수에 대해?", "T": "객관적으로 지적하고 개선", "F": "상황을 이해하고 위로"},
        {"question": "당신의 강점은?", "T": "분석력과 객관적 판단", "F": "공감능력과 따뜻함"},
        {"question": "중요한 것은?", "T": "효율성과 성과", "F": "조화와 사람과의 관계"},
        {"question": "비판을 받을 때는?", "T": "내용의 타당성을 검토함", "F": "상대의 의도를 고민함"},
        {"question": "업무에서 우선순위는?", "T": "결과와 성과", "F": "팀의 화합과 만족도"},
        {"question": "남의 고민을 들을 때는?", "T": "해결책을 제시하고 싶음", "F": "공감하고 위로하고 싶음"},
        {"question": "칭찬받을 때 기분은?", "T": "능력을 인정받아 뿌듯함", "F": "소중한 사람이 되어 감동함"},
        {"question": "직장에서 중요한 것은?", "T": "공정하고 명확한 규칙", "F": "따뜻한 인간관계"}
    ],
    # 라운드 4: J/P (판단/인식) - 10개 질문
    [
        {"question": "계획을 세울 때 당신은?", "J": "상세하게 미리 계획함", "P": "자유롭게 유동적으로"},
        {"question": "마감일이 있을 때는?", "J": "미리 완료하려 함", "P": "마지막에 빨리 하는 편"},
        {"question": "삶의 방식은?", "J": "구조화되고 조직적", "P": "자유롭고 개방적"},
        {"question": "선호하는 환경은?", "J": "명확한 목표와 규칙", "P": "선택의 폭과 유연성"},
        {"question": "당신의 강점은?", "J": "계획성과 책임감", "P": "적응력과 유연성"},
        {"question": "변경 사항이 생기면?", "J": "불안감을 느낌", "P": "새로운 기회로 봄"},
        {"question": "집 정리 상태는?", "J": "깔끔하고 체계적임", "P": "편하면 되는 스타일"},
        {"question": "업무 스타일은?", "J": "일정에 맞춰 진행", "P": "상황에 따라 유동적"},
        {"question": "결정을 내릴 때는?", "J": "신중하게 결정 후 실행", "P": "여러 옵션을 두고 유지"},
        {"question": "시간 약속에 대해?", "J": "정확히 지키려고 함", "P": "약간의 여유를 봄"}
    ]
]

# MBTI별 어울리는 MBTI와 연예인 (성별 구분)
MBTI_INFO = {
    "ISTJ": {"compatible": "ISFP, INFP", "male_celebrities": "박보검, 이준호", "female_celebrities": "아이유, 박신혜"},
    "ISFJ": {"compatible": "ISFP, INFP", "male_celebrities": "박신혜, 정해인", "female_celebrities": "설현, 박민영"},
    "INFJ": {"compatible": "ENFP, ENFJ", "male_celebrities": "정해인, 이준호", "female_celebrities": "문근영, 전지현"},
    "INTJ": {"compatible": "ENFP, INTP", "male_celebrities": "차승원, 박형식", "female_celebrities": "수지, 전소미"},
    "ISTP": {"compatible": "ESFJ, ISFJ", "male_celebrities": "공유, 손흥민", "female_celebrities": "유연석, 윤승아"},
    "ISFP": {"compatible": "ISTJ, ISFJ", "male_celebrities": "뷔, 진", "female_celebrities": "아이유, 제니"},
    "INFP": {"compatible": "ENTJ, ENFJ", "male_celebrities": "박서준, 윤석열", "female_celebrities": "전지현, 박예진"},
    "INTP": {"compatible": "ENFP, ENTJ", "male_celebrities": "이준호, 박형식", "female_celebrities": "보아, 이지은"},
    "ESTP": {"compatible": "ISFJ, ISTJ", "male_celebrities": "손흥민, 지드래곤", "female_celebrities": "수현, 이하나"},
    "ESFP": {"compatible": "ISFJ, ISTJ", "male_celebrities": "싸이, 제이홉", "female_celebrities": "제니, 현아"},
    "ENFP": {"compatible": "INTJ, INFJ", "male_celebrities": "카이, 태양", "female_celebrities": "러셀, 가희"},
    "ENTP": {"compatible": "INFJ, INTJ", "male_celebrities": "리딩만, 더피", "female_celebrities": "보아, 설리"},
    "ESTJ": {"compatible": "ISFP, ISTP", "male_celebrities": "RM, 이순신", "female_celebrities": "정소민, 은혜"},
    "ESFJ": {"compatible": "ISFP, ISTP", "male_celebrities": "빅토르", "female_celebrities": "선미, 박민영"},
    "ENFJ": {"compatible": "INFP, ISFP", "male_celebrities": "이준호, 박해일", "female_celebrities": "한효주, 한지민"},
    "ENTJ": {"compatible": "ISFP, INFP", "male_celebrities": "이영건, 강소라", "female_celebrities": "전소미, 고윤정"}
}

# --- 2. 게임 초기화 및 상태 관리 ---
if 'gender' not in st.session_state:
    st.session_state.gender = None
    st.session_state.round_index = 0
    st.session_state.question_index = 0
    st.session_state.mbti_scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
    st.session_state.result_mbti = None
    st.session_state.game_over = False

# --- 3. 게임 로직 함수 ---
def calculate_mbti():
    E_I = "E" if st.session_state.mbti_scores["E"] > st.session_state.mbti_scores["I"] else "I"
    S_N = "S" if st.session_state.mbti_scores["S"] > st.session_state.mbti_scores["N"] else "N"
    T_F = "T" if st.session_state.mbti_scores["T"] > st.session_state.mbti_scores["F"] else "F"
    J_P = "J" if st.session_state.mbti_scores["J"] > st.session_state.mbti_scores["P"] else "P"
    
    st.session_state.result_mbti = E_I + S_N + T_F + J_P
    st.session_state.game_over = True

def select_answer(mbti_type):
    if mbti_type == "E":
        st.session_state.mbti_scores["E"] += 1
    elif mbti_type == "I":
        st.session_state.mbti_scores["I"] += 1
    elif mbti_type == "S":
        st.session_state.mbti_scores["S"] += 1
    elif mbti_type == "N":
        st.session_state.mbti_scores["N"] += 1
    elif mbti_type == "T":
        st.session_state.mbti_scores["T"] += 1
    elif mbti_type == "F":
        st.session_state.mbti_scores["F"] += 1
    elif mbti_type == "J":
        st.session_state.mbti_scores["J"] += 1
    elif mbti_type == "P":
        st.session_state.mbti_scores["P"] += 1
    
    st.session_state.question_index += 1
    
    if st.session_state.question_index >= 5:
        st.session_state.question_index = 0
        st.session_state.round_index += 1
        
        if st.session_state.round_index >= 4:
            calculate_mbti()
    
    st.rerun()

def reset_game():
    st.session_state.gender = None
    st.session_state.round_index = 0
    st.session_state.question_index = 0
    st.session_state.mbti_scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
    st.session_state.result_mbti = None
    st.session_state.game_over = False
    st.session_state.selected_questions = None
    st.rerun()

def initialize_selected_questions():
    """각 라운드별로 10개 중 5개 질문을 랜덤으로 선택"""
    if "selected_questions" not in st.session_state or st.session_state.selected_questions is None:
        st.session_state.selected_questions = []
        for round_idx in range(4):
            # 각 라운드의 10개 질문 중 5개를 랜덤 선택
            selected = random.sample(MBTI_QUESTIONS[round_idx], 5)
            st.session_state.selected_questions.append(selected)

# --- 4. 게임 화면 구성 ---
st.title("💫 MBTI 성격 유형 게임!")

# 성별 선택 화면
if st.session_state.gender is None:
    st.write("먼저 성별을 선택해주세요!")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("👨 남성", use_container_width=True, key="male"):
            st.session_state.gender = "male"
            st.rerun()
    
    with col2:
        if st.button("👩 여성", use_container_width=True, key="female"):
            st.session_state.gender = "female"
            st.rerun()

# 게임 진행 중
elif not st.session_state.game_over:
    # 선택된 질문 초기화
    initialize_selected_questions()
    
    # 진행도 표시
    current_question = st.session_state.question_index + 1
    current_round = st.session_state.round_index + 1
    st.progress((st.session_state.round_index * 5 + st.session_state.question_index) / 20)
    st.write(f"🎯 {current_round}번째 라운드 - {current_question}/5 질문")
    
    # 현재 질문 표시
    current_q = st.session_state.selected_questions[st.session_state.round_index][st.session_state.question_index]
    st.subheader(current_q["question"])
    
    # 라운드별 선택지 표시
    round_types = [["E", "I"], ["S", "N"], ["T", "F"], ["J", "P"]]
    type_a, type_b = round_types[st.session_state.round_index]

    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button(f"← {current_q[type_a]}", use_container_width=True, key="answer_a"):
            select_answer(type_a)
    
    with col2:
        if st.button(f"→ {current_q[type_b]}", use_container_width=True, key="answer_b"):
            select_answer(type_b)

# 결과 화면
else:
    st.balloons()
    mbti_result = st.session_state.result_mbti
    mbti_data = MBTI_INFO[mbti_result]
    
    st.success(f"당신의 MBTI는 **{mbti_result}** 입니다! 🎉")
    
    # 성별에 따라 다른 연예인 표시
    if st.session_state.gender == "male":
        celebrities = mbti_data['female_celebrities']
        celebrity_label = "👩 추천 여자 연예인"
    else:
        celebrities = mbti_data['male_celebrities']
        celebrity_label = "👨 추천 남자 연예인"
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info(f"💑 어울리는 MBTI\n{mbti_data['compatible']}")
    
    with col2:
        st.warning(f"⭐ {celebrity_label}\n{celebrities}")
    
    # MBTI 설명
    st.divider()
    st.write("### MBTI 유형 설명")
    
    type_descriptions = {
        "E": "외향적이고 활동적",
        "I": "내향적이고 신중함",
        "S": "현실적이고 구체적",
        "N": "직관적이고 창의적",
        "T": "논리적이고 객관적",
        "F": "감정적이고 따뜻함",
        "J": "계획적이고 조직적",
        "P": "유연하고 개방적"
    }
    
    desc_text = f"**{mbti_result[0]}**: {type_descriptions[mbti_result[0]]} | "
    desc_text += f"**{mbti_result[1]}**: {type_descriptions[mbti_result[1]]} | "
    desc_text += f"**{mbti_result[2]}**: {type_descriptions[mbti_result[2]]} | "
    desc_text += f"**{mbti_result[3]}**: {type_descriptions[mbti_result[3]]}"
    
    st.info(desc_text)
    
    if st.button("다시 하기", use_container_width=True):
        reset_game()

# --- 5. 배너 추가 ---
st.markdown("""
<div style='text-align: center; margin: 20px 0;'>
    <a href="https://link.coupang.com/a/dyGliT" target="_blank" referrerpolicy="unsafe-url"><img src="https://ads-partners.coupang.com/banners/803279?subId=&traceId=V0-301-879dd1202e5c73b2-I803279&w=728&h=90" alt=""></a>
</div>
""", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; font-size: 0.8em;'>※ 쿠팡 파트너스 활동을 통해 일정액의 수수료를 제공받을 수 있습니다.</p>", unsafe_allow_html=True)