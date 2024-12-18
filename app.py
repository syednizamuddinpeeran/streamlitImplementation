import streamlit as st
import time


from dataElements import dataElements
from layouts import layouts, sidebar
from setup import setup
from textElements import textElements
def app():
    st.title("Welcome to the Streamlit demo + helper")
    setup()
    sidebar()
    TextElements,DataElements,MultimediaElements,ChatSpecific,StructuralElements = st.tabs(["Text Elements","Data elements","multimedia elements","Chat specific","Structural Elements"])

                
    with TextElements:    
        textElements()
    with StructuralElements:
        layouts()
    with DataElements:
        dataElements()

if __name__ == '__main__' : 
    app()
    st.set_option('server.enableCORS',True)
