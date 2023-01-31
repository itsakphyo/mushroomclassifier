
import numpy as np

import pandas as pd

import pickle

import streamlit as st

import base64

from sklearn.preprocessing import StandardScaler

st.markdown(
    """
<style>
.sidebar .sidebar-content {
    background-image: linear-gradient(#FFB6C1,#FFB6C1);
    color: white;
}
</style>
""",
    unsafe_allow_html=True,
)

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

add_bg_from_local('./img/bbb.jpg')   

header = st.container()
notic = st.container()
image = st.container()
model = st.container()


with header:
    st.title('Welcome to my Mushroom Classiffier Web App')
    st.markdown('Mushrooms are fungi (plant-like form) . They belong in a kingdom of their own, separate from plants and animals. Fungi differ from plants and animals in the way they obtain their nutrients.The nutritional value of edible mushrooms is due to their high protein, fiber, vitamin and mineral contents, and low-fat levels.')

with notic:
    st.markdown('**Before assuming that any wild mushroom is edible, it should be identified first.** ')

st.sidebar.markdown('**Parts of Mushrom**')
st.sidebar.image('./img/Mushroom.jpg')


with model:
    st.subheader('Classifier Model')



cap_shape={'bell': 0, 'conical': 1, 'flat': 2, 'knobbed': 3, 'sunken': 4, 'convex': 5}
cap_surface={'fibrous': 0, 'grooves': 1, 'smooth': 2, 'scaly': 3}
cap_color={'buff': 0,'cinnamon': 1,'red': 2,'gray': 3,'brown': 4,'pink': 5,'green': 6,'purple': 7,'white': 8,'yellow': 9}
bruises= {'no': 0, 'yes': 1}
odor={'almond': 0, 'creosote': 1, 'foul': 2, 'anise': 3, 'musty': 4, 'none': 5, 'pungent': 6, 'spicy': 7, 'fishy': 8}
gill_attachment= {'attached': 0, 'free': 1}
gill_spacing= {'close': 0, 'crowded': 1}
gill_size={'broad': 0, 'narrow': 1}
gill_color={'buff': 0,'red': 1,'gray': 2,'chocolate': 3,'black': 4,'brown': 5,'orange': 6,'pink': 7,'green': 8,'purple': 9,'white': 10,'yellow': 11}
stalk_shape={'enlarging': 0, 'tapering': 1}
stalk_root= {'missing': 0, 'bulbous': 1, 'club': 2, 'equal': 3, 'rooted': 4}
stalk_surface_above_ring={'fibrous': 0, 'silky': 1, 'smooth': 2, 'scaly': 3}
stalk_surface_below_ring={'fibrous': 0, 'silky': 1, 'smooth': 2, 'scaly': 3}
stalk_color_above_ring= {'buff': 0, 'cinnamon': 1, 'red': 2, 'gray': 3, 'brown': 4, 'orange': 5, 'pink': 6, 'white': 7, 'yellow': 8}
stalk_color_below_ring= {'buff': 0, 'cinnamon': 1, 'red': 2, 'gray': 3, 'brown': 4, 'orange': 5, 'pink': 6, 'white': 7, 'yellow': 8}
veil_type= {'partial': 0, 'universal': 1 }
veil_color={'brown': 0, 'orange': 1, 'white': 2, 'yellow': 3}
ringnumber={'none': 0, 'one': 1, 'two': 2}
ringtype={'evanescent': 0, 'flaring': 1, 'large': 2, 'none': 3, 'pendant': 4}
spore_print_color={'buff': 0, 'chocolate': 1, 'black': 2, 'brown': 3, 'orange': 4, 'green': 5, 'purple': 6, 'white': 7, 'yellow': 8}
population={'abundant': 0, 'clustered': 1, 'numerous': 2, 'scattered': 3, 'several': 4, 'solitary': 5}
habitat={'woods': 0, 'grasses': 1, 'leaves': 2, 'meadows': 3, 'paths': 4, 'urban': 5, 'waste': 6}

st.markdown('**Cap\'s Appearance**')
col1, col2, col3 = st.columns(3)
with col1:
    cap_shape_choice= st.selectbox('Cap Shape',cap_shape,key=cap_shape)
with col2:
    cap_surface_choice = st.selectbox('Cap Surface',cap_surface,key=cap_surface)
with col3:
    cap_color_choice =st.selectbox('Cap Color',cap_color,key=cap_color)

bruises_choice =st.selectbox('**Are there any Bruises?**',bruises,key=bruises)
odor_choice =st.selectbox('**Odor of the mushroom**',odor,key=odor)

st.markdown('**Gill\'s Nature**')

gc1,gc2,gc3,gc4=st.columns(4)
with gc1:
    gill_attachment_choice =st.selectbox('Gill Attachment',gill_attachment,key=gill_attachment)
with gc2:
    gill_spacing_choice =st.selectbox('Gill Spacing',gill_spacing,key=gill_spacing)
with gc3:
    gill_size_choice =st.selectbox('Gill Size',gill_size,key=gill_size)
with gc4:
    gill_color_choice =st.selectbox('Gill Color',gill_color,key=gill_color)

st.markdown('**Stalk\'s Nature**')
ss1,ss2=st.columns(2)
with ss1:
    stalk_shape_choice =st.selectbox('Stalk Shape',stalk_shape,key=stalk_shape)
with ss2:
    stalk_root_choice =st.selectbox('Stalk Root',stalk_root,key=stalk_root)


sb1,sb2,sb3,sb4=st.columns(4)
with sb1:
    stalk_surface_above_ring_choice =st.selectbox('Stalk Surface Above Ring',stalk_surface_above_ring,key=stalk_surface_above_ring)
with sb2:
    stalk_surface_below_ring_choice =st.selectbox('Stalk Surface below Ring',stalk_surface_below_ring,key=None)
with sb3:
    stalk_color_above_ring_choice =st.selectbox('Stalk Color Above Ring',stalk_color_above_ring,key=stalk_color_above_ring)
with sb4:
    stalk_color_below_ring_choice =st.selectbox('Stalk Color Below Ring',stalk_color_below_ring)

st.markdown('**Veil\' Nature**')
ve2=st.container()
with ve2:
    veil_color_choice =st.selectbox('Veil Color',veil_color,key=veil_color)

st.markdown('**Ring\'s Nature**')
r1,r2=st.columns(2)
with r1:
    ringnumber_choice =st.selectbox('Ring Number',ringnumber,key=ringnumber)
with r2:
    ringtype_choice =st.selectbox('Ring Type',ringtype,key=ringtype)


spore_print_color_choice =st.selectbox('**The Color of Spore Print**',spore_print_color,key=spore_print_color)
population_choice =st.selectbox('**Population**',population,key=population)
habitat_choice =st.selectbox('**Habitat**',habitat,key=habitat)



predit_X=[ cap_shape[cap_shape_choice],cap_surface[cap_surface_choice],cap_color[cap_color_choice],bruises[bruises_choice],odor[odor_choice],gill_attachment[gill_attachment_choice],gill_spacing[gill_spacing_choice],gill_size[gill_size_choice],gill_color[gill_color_choice],stalk_shape[stalk_shape_choice],stalk_root[stalk_root_choice],stalk_surface_above_ring[stalk_surface_above_ring_choice],stalk_color_below_ring[stalk_color_below_ring_choice],stalk_color_above_ring[stalk_color_above_ring_choice],stalk_color_below_ring[stalk_color_below_ring_choice],veil_color[veil_color_choice],ringnumber[ringnumber_choice],ringtype[ringtype_choice],spore_print_color[spore_print_color_choice],population[population_choice],habitat[habitat_choice]]
repre_X=pd.DataFrame(np.reshape(predit_X, (1,21)))
scaler = StandardScaler()

loaded_model = pickle.load(open('./model/msclasifier_model', 'rb'))

prediction = st.container()
result=loaded_model.predict(np.array(repre_X) , check_input=True)
with prediction:
    st.markdown('**CLASSIFICATION** : ')
    #st.markdown(repre_X.shape)
    #st.markdown(repre_X)
    #st.markdown(result)

if result==1:
    st.markdown('**----------------------------------------------> This mushroom is POISINOUS!! <--------------------------------------------**')
else:
    st.markdown('**--------------------------------------------> This mushroom is NOT poisinous. <-------------------------------------------**')



dataset = st.container()
with dataset:
    st.subheader('About the dataset')
    st.markdown('Dataset from the UCI Machine Learning Repository which was donated in April 1987 by Jeff Schlimmer (Carnegie Mellon University) and originates from the Audubon Society Field Guide to North American Mushrooms (1981).')
    original_title = '<p style="font-family:Courier; color:Red; font-size: 20px;">This project is just for educational purposes.Always refer to reliable resources before eating wild mushrooms.</p>'
    st.markdown(original_title, unsafe_allow_html=True)



