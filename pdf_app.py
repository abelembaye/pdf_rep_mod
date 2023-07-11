# Econ 3133 News Analysis HW01
import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
from streamlit.components.v1 import iframe

st.set_page_config(layout="centered", page_icon="🎓", page_title="Econ 3133 Assignment 01")
st.title("Econ 3133 Assignment 01")

st.write(
    "This app converts your answers in the space provided to a pdf template that is convenient to grade in gradescope. "
    "So please fill the form carefully and make sure that you are able to download a pdf file at the end of your work "
    "by clicking the the 'generate PDF button' and then 'download button.' "
)

#left, right = st.columns(2)
#right.write("Here's the template we'll be using:")
#st.write("Here's the template we'll be using:")
#right.image("template.png", width=300)
# st.image("template.pdf", width=300)
# env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
# template = env.get_template("template.html")

#left.write("Fill in the data:")
#st.write("Fill in the data:")
#form = left.form("template_form")
form= st.form("template_form")

student = form.text_input(label="Student name",max_chars= 50)
Q01 = form.text_input("Question #1")
disc01 = form.text_area(label="Discussion of Question #1", height=100, max_chars=500)
st.file_uploader(label="upload png file of your graph", type="PNG")
# course = form.selectbox(
#     "Choose course",
#     ["Report Generation in Streamlit", "Advanced Cryptography"],
#     index=0,
# )
grade = form.slider("Guess Joe Biden's weight in lbs", 1, 300, 150)

submit = form.form_submit_button("Generate PDF")

if submit:
    html = template.render(
        student=student,
        course=course,
        grade=f"{grade}/100",
        date=date.today().strftime("%B %d, %Y"),
    )

    pdf = pdfkit.from_string(html, False)
    #st.balloons()

    #right.success("Your template successfully generated!")
    st.success("Your template successfully generated!")
    # st.write(html, unsafe_allow_html=True)
    # st.write("")
    #right.download_button(
    st.download_button(
        "⬇️ Download PDF",
        data=pdf,
        #file_name="diploma.pdf",
        file_name="your_name.pdf",
        mime="application/octet-stream",
    )
#This file uses the virt env at
#.\venv4pdfgen\Scripts\activate.ps1