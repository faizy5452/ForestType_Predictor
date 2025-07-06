import streamlit as st
import numpy as np
import pickle
from PIL import Image



rfc=pickle.load(open('rfc.pkl','rb'))


#Creating we app

st.title('Forest Cover Type Prediction')
image=Image.open('image.png')
st.image(image, use_container_width=True)
user_input=st.text_input('Input Features')

if user_input:
    user_input=user_input.split(',')
    features = np.array(user_input, dtype='float32').reshape(1, -1)
    output=rfc.predict(features).reshape(1,-1)


    cover_type_dict = {
            1: {"name": "Spruce/Fir", "image": "1.jpg"},
            2: {"name": "Lodgepole Pine", "image": "2.png"},
            3: {"name": "Ponderosa Pine", "image": "3.png"},
            4: {"name": "Cottonwood/Willow", "image": "4.jpg"},
            5: {"name": "Aspen", "image": "5.jpg"},
            6: {"name": "Douglas-fir", "image": "6.png"},
            7: {"name": "Krummholz", "image": "7.png"}
        }


    predicted_cover_type=int(output[0][0])
    predicted_cover_info=cover_type_dict[predicted_cover_type]


    if predicted_cover_info is not None:
            cover_type_name=predicted_cover_info['name']
            cover_type_image=predicted_cover_info['image']

            col1,col2=st.columns([2,3])

            with col1:
             st.write("Predicted Cover Type:")
             st.write(f"<h1 style='font-size:40px;font-weight:bold'>{cover_type_name}</h1>",unsafe_allow_html=True)

            with col2:
             cover_type_image_path=Image.open(cover_type_image)
             st.image(cover_type_image_path,use_container_width=True)

    else:
            st.write("unable to Make Prediction!")
