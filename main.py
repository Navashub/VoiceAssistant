import streamlit as st
import pyttsx3 as p
import speech_recognition as sr


engine = p.init()
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

st.title("Voice Assistant")
st.text("This app performs speech recognition and text-to-speech.")

# Text-to-speech
if st.button("Greet"):
    engine.say("Hello there, I am your voice assistant")
    engine.runAndWait()
    st.success("Greeting message played!")


uploaded_audio = st.file_uploader("Upload an audio file (WAV format)", type=["wav"])

if uploaded_audio is not None:
    st.audio(uploaded_audio, format='audio/wav')
    recognizer = sr.Recognizer()
    with sr.AudioFile(uploaded_audio) as source:
        recognizer.adjust_for_ambient_noise(source, duration=1.2)
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        st.write("Recognized Text:")
        st.write(text)
    except sr.UnknownValueError:
        st.error("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        st.error(f"Could not request results; {e}")
