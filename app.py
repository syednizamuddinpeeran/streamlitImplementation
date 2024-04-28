import streamlit as st
import time

st.title("This is a Demo title")
st.header("This is a header")
st.subheader("This is SubHeader")
st.text("This is a text")
st.write("This is a st.wrte command. we can pass fucntions that return stuff here")
def sampleStringreturn():
    return f"This string comes from function {time.localtime()}" 
st.write(sampleStringreturn())

st.write("This *text* is italised by enclosing it in astrics (*)")
st.write(st.write)
