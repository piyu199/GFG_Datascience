import streamlit as st
import pandas as pd

st.subheader("Loading the CSV Files")

df=st.file_uploader("upload the csv file :-",type=['csv','xlsx'])
# st.dataframe(df)


df1=pd.read_csv(r'D:\\DataScience_GeeksForGeeks\\Libraries_for_DataAnalysis\\Football.csv')
if df1 is not None:
    st.table(df1.head())


st.subheader("Dealing with Images")

st.image(r"C:\\Users\\Admin\\OneDrive\\Desktop\\GreatKart Images\\cover.jpg")

image_file= st.file_uploader("Upload the image of your choice :- ",type=["png","jpg"])
if image_file is not None:
    st.image(image_file)



st.subheader("Working with Videos")
video_file = st.file_uploader("Upload the video file",type=["mkv","mp4"])
if video_file is not None:
    st.video(video_file)


st.subheader("Working with Audio")
audio_file = st.file_uploader("Upload the audio file",type=['mp3','wav'])
if audio_file is not None:
    st.audio(audio_file.read())

