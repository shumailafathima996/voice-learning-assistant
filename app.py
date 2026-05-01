import streamlit as st
import pyttsx3

st.title("Voice Learning Assistant")
st.write("Hello, I am your voice assistant!")

engine = pyttsx3.init()
if st.button("Speak"):
    engine.say("Hello, I am your voice assistant")
    engine.runAndWait()
 
