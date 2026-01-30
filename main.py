import streamlit as st

#--------------------------------
# 1) Title & Display Component
#----------------------------------

st.title("Hi! I am Streamlit web app")
st.subheader("Hi! I am your subheader")
st.header("I am header")
st.text("Hi I am text function and programmers uses me inplace of paragraph")
st.markdown("**Bold** *Italic*") #**-bold *-italic
st.markdown(" # Heading 1")
st.markdown(" > blockquote")
st.markdown("---")
st.markdown("[Link](https://google.com)")
st.caption("Hi! I am  a Caption")
st.latex("r'y=u+b")
st.latex(r"\begin{pmatrix}a & b \\ c & d\end{pmatrix}") #matrix
json={"a":"1,2,3","b":"4,5,6"}
st.json(json)
code="""
print("Hello World)
def func():
    return 0;"""
st.code(code, language="Python")
st.write("## writefun")

#------------------------------------------------------------------------------------------

st.metric(label="Wind Speed", value="120\^-1") #used to display equation or matrix --> metric()
#--------------------------------------------------------------------------------------
# 2) Input Components(User interaction)
#------------------------------------------------------------------------------------

name=st.text_input("Enter your name: ") #takes user input 1)text_input
st.write("Name:",name)
age=st.number_input("Enter age: ", min_value=0) #takes numerical input 2)number_input
st.write(age)
feedback=st.text_area("Enter feedback") #multiline input 3)text_area
pwd=st.text_input("Password", type="password")#hiddeninput 4)use type=password to hide
agree=st.checkbox("I agree") #chechkbox returns true or false 5)chechbox()
st.write(agree) 
choice=st.radio("Select gender", ["Male","Female"])#select 1 option 6)radio options radio()
st.write(choice)
lang=st.selectbox("Choose Languages", ["Python", "Java", "C"])#dropdown selection 7)selectbox()
st.write(lang)
skills=st.multiselect("Select skills: ", ["AI", "ML","Web","Cloud"]) #multiple selections 8)multi_select()
st.write(skills)
score=st.slider("Score: ",0,100)#slider input 9)slider()
st.write(score)
file=st.file_uploader("Upload a file")#upload a file 10)file_uploader()
date=st.date_input("Select date")#select a date 11)date_input()
time=st.time_input("Select time")#select time 12)time_input()

#-----------------------------------------------------------------------------------------
# 3) Button & action components
#---------------------------------------------------------------------------------

if st.button("Click Me"): #triggers action 1)butto()
    st.success("Button clicked")
st.download_button("Download","Hello World", file_name="file.txt")#download files 2)download_button
with st.form("my_form"): #group inputs together
    name=st.text_input("Name")
    submit=st.form_submit_button("Submit")
    if submit:
        st.success("Submitted succesfully")

#---------------------------------------------------------------------------------------
# 4) Media Components
#--------------------------------------------------------------------------------------

#st.image("image.jpg",caption="Sample Image") #1) display image-->image()
#st.audio("audio.mp3") #2)play audio --> audio()
#st.video("video.mp4") #3)play video --> video()

#-----------------------------------------------------------------------------------
# 5) Data Display Component
#-----------------------------------------------------------------------------------

st.write("Hello",123,{"a":1}) #universaldisplay function
import pandas as pd
df=pd.DataFrame({"A":[1,2], "B":[3,4]}) 
st.table(df) #statictable

st.dataframe(df)#tabular data structure,created using pandas 

st.json({"Name":"AI","Year":2025})#JavascriptobjectNotation   key-value data format
st.latex("120 \, ms^{-1}")  #KPI with LaTex
st.metric("Accuracy", "92", "+2%")

#--------------------------------------------------------------------------------------
#6)Chart Component
#------------------------------------------------------------------------------------------

st.line_chart([1,2,3,4])
st.bar_chart([10,20,30])
st.area_chart([3,6,9])

