
import google.generativeai as genai
import streamlit as st

f=open('keys/.key.txt')
KEY=f.read()
genai.configure(api_key=KEY)
model = genai.GenerativeModel('gemini-pro')
prompt=st.text_area("enter your code")
x='''
            as a obedient ai assistant given an input python code
            you must evaluate and list out the errors
            also provide the resolved code

            Return reponse in following format

            heading1 : Code Review

            heading2: Bug report

            list of bugs

            heading2: Correct Code

            Corrected code


            '''

if st.button('submit')==True:
    response = model.generate_content(x+'verify and print'+prompt)

    st.write(response.text)