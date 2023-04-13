import streamlit as st
import time

st.title('Add title of your app here')

with st.sidebar:
    image = st.file_uploader(label='Upload image')
    st.write('Or...')
    image = st.camera_input(label='Make a photo')
if image:

    print('Thanks! Processing')
    # import your model

    # process image with your model

    # add post-processing steps

    # Print out the results

    with st.spinner('Wait for it...'):
        time.sleep(5)

    st.image(image)
    st.success('Done!')
