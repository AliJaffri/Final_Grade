import streamlit as st

# Page Layout
st.set_page_config(page_title='Principles of Economics Final Grade Calculator', layout='wide')

# Title
st.title(' Department of Economics Final Grade Calculator')

# Sidebar for user input
st.sidebar.header('User Input')

# Input for grades and weights
midterm_Highest_grade = st.sidebar.number_input('Midterm Highest Grade (%)', min_value=0, max_value=100, value=60)
midterm_Middle_grade = st.sidebar.number_input('Midterm Middle Grade (%)', min_value=0, max_value=100, value=95)
midterm_Lowest_grade = st.sidebar.number_input('Midterm Lowest Grade (%)', min_value=0, max_value=100, value=80)

homework_grade = st.sidebar.number_input('Homework Grade (%)', min_value=0, max_value=100, value=95)
quizzes_grade = st.sidebar.number_input('Quizzes Grade (%)', min_value=0, max_value=100, value=95)
final_exam_grade = st.sidebar.number_input('Final Exam Grade (%)', min_value=0, max_value=100, value=85)

# Weighting for each component
midterm_Highest_exam_weight = 0.25
midterm_Middle_exam_weight = 0.15
midterm_Lowest_exam_weight = 0.10

homework_weight = 0.15
quizzes_weight = 0.10
final_exam_weight = 0.2

# Calculate final grade
final_grade = (
    midterm_Highest_grade * midterm_Highest_exam_weight +
    midterm_Middle_grade * midterm_Middle_exam_weight +
    midterm_Lowest_grade * midterm_Lowest_exam_weight +
    homework_grade * homework_weight +
    quizzes_grade * quizzes_weight +
    final_exam_grade * final_exam_weight
)

# Determine the letter grade based on the grading scale
if final_grade >= 88:
    letter_grade = 'A'
elif final_grade >= 78:
    letter_grade = 'B'
elif final_grade >= 68:
    letter_grade = 'C'
elif final_grade >= 58:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# Display final grade and letter grade
st.subheader('Final Grade Calculation')
st.write(f'The calculated final grade is: {final_grade:.2f}%')
st.write(f'The corresponding letter grade is: {letter_grade}')
