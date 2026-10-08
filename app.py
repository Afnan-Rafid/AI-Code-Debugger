import streamlit as st
from PIL import Image
from api_call import debugger

st.title("AI Code Debugger App")
st.divider()

with st.container(border=True):
    images = st.file_uploader(
        "Upload Your Code Screenshot",
        type=['jpg','jpeg','png'],
        accept_multiple_files=True
    )

    if images:
        if len(images)>3:
            st.error("Maximum Upload Reached")
        else :
            col = st.columns(len(images))
            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)

            pil_images = []

            for img in images:
                pil_img = Image.open(img)
                pil_images.append(pil_img)

    option = st.selectbox(
        "Choose an option",
        ("Hints","Solution with Code"),
        index=None
    )

    btn = st.button("Debug",type="primary")
if btn:
    if not images:
        st.error("Please upload atleast one image")
    if not option:
         st.error("Please Select an Option")

    if images and option:
        with st.container(border=True):
            with st.spinner("Debugging..."):
                answer = debugger(pil_images,option)
                st.markdown(answer)





