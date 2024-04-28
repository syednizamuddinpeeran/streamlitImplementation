import streamlit as st
import time


from dataElements import dataElements
from layouts import layouts, sidebar
from setup import setup
from textElements import textElements

st.title("Welcome to the streamlit demo + helper")
setup()
sidebar()
TextElements,DataElements,MultimediaElements,ChatSpecific,StructuralElements = st.tabs(["Text Elements","Data elements","multimedia elements","Chat specific","Structural Elements"])

            
with TextElements:    
    textElements()
with StructuralElements:
    layouts()
with DataElements:
    dataElements()
