import streamlit as st
import requests
import json
import os
from io import StringIO
from main import process_file, translate_file, summarize_file, generate_pdf


st.header('Home Remedies for :blue[diseases] :relieved:', divider='rainbow')
# st.header('_Streamlit_ is :blue[cool] :sunglasses:')


BASE_PATH = "/Users/debstutidas/Documents/MLProjects/transumate/src"
DOCUMENT_PATH = 'Document'
print(DOCUMENT_PATH)

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    filename = uploaded_file.name

    st.write(filename)
    # st.write(bytes_data)
    
    file_path = os.path.join(BASE_PATH, DOCUMENT_PATH, filename)
    st.write(file_path)
    with open(file_path, 'wb') as f:
        f.write(bytes_data)
        f.close()

source_language = st.selectbox('Select Original Document Language', ('English', 'Hindi', 'Bengali'))
st.write('You selected:', source_language)

process = st.button('Process File')

with st.spinner('Processing..'):

    result = None

    if process:
        process_file(file_name=filename, source_language=source_language)


target_language = st.selectbox('Select Target Document Language', ('English', 'Hindi', 'Bengali'))
translate = st.button('Translate File')

st.write('You selected:', target_language)

with st.spinner('Translating..'):

    result = None

    if translate:
        translate_file(file_name=filename, source_language=source_language, dest_language=target_language)
        translate_output_path = os.path.join(BASE_PATH, 'Destination', target_language, filename)
        generate_pdf(translate_output_path, filename, 'translation')




summarize = st.button('Summarize File')

st.write('You selected:', target_language)

with st.spinner('Summarizing..'):

    result = None

    if summarize:
        # summarize_file(file_name=filename, source_language=source_language)
        summary_path = os.path.join(BASE_PATH, 'Summary', source_language, filename)
        generate_pdf(summary_path, filename, 'summary')

        summary_op_path = os.path.join(BASE_PATH, 'SummaryOutputs', filename)
        with open(summary_op_path, 'rb') as f:
           st.download_button('Download Summary', f, file_name='summary.pdf')


#
# sidebar = st.sidebar
#
# sidebar.subheader('Choose which part of your body is not happy :unamused:')
#
# # Add a selectbox to the sidebar:
# disease_type = sidebar.selectbox(
#     '',
#     ('Digestive System', 'Blood Circulation System', 'Respiratory System')
# )
#
# sidebar.image("images/food.png", width=320)
# sidebar.image("images/food.png", width=320)
#
#
# st.image("images/systems.jpeg")
#
# left_column, right_column = st.columns(2)
# # You can use a column just like st.sidebar:
# left_column.subheader('	:point_left: Choose disease type')
# left_column.subheader('Choose your disease 	:point_right:')
#
# # Or even better, call Streamlit functions inside a "with" block:
# with right_column:
#     disease_name = st.radio(
#         '',
#         disease_map.get(disease_type))
#     # st.write(f"You are having {disease_name}!")
#
# st.text('Not in the list? Type the name here')
#
# other = st.text_input('disease_name')
# if other:
#     disease_name = other
#     add_disease_name(disease_name, disease_type)
#
# find = st.button('Find Details')
# with st.spinner('Finding'):
#
#     result = None
#
#     if find:
#         data = json.dumps({"disease_name": disease_name.lower(), "disease_type": disease_type})
#         try:
#             print('requesting with data'+data)
#             # result = requests.get("http://3.111.38.153/query", data=data)
#             result = requests.get("http://127.0.0.1:5000/query", data=data)
#         except Exception as e:
#             print(f'Error connecting to web server: {str(e)}')
#
#
#     if result:
#
#         result = result.json()
#         tab1, tab2, tab3, tab4, tab5 = st.tabs(["Causes", "Symptoms", "Remedies", "Harmful foods", "Beneficiary foods"])
#
#         with tab1:
#             st.header("Causes")
#             left_column, right_column = st.columns(2)
#             right_column.image("images/unhealthy.png", width=400)
#             left_column.write(result.get("causes"))
#
#         with tab2:
#             st.header("Symptoms")
#             left_column, right_column = st.columns(2)
#
#             right_column.image("images/symptoms.png", width=400)
#             left_column.write(result.get("symptoms"))
#
#         with tab3:
#             st.header("Remedies")
#             left_column, right_column = st.columns(2)
#
#             right_column.image("images/remedies.png", width=400)
#             left_column.write(result.get("remedies"))
#
#         with tab4:
#             st.header("Harmful Foods")
#             left_column, right_column = st.columns(2)
#
#             right_column.image("images/lifestyle.png", width=400)
#             left_column.write(result.get("harmful_foods"))
#
#         with tab5:
#             st.header("Beneficiary Foods")
#             left_column, right_column = st.columns(2)
#
#             right_column.image("images/healthy.png", width=400)
#             left_column.write(result.get("beneficial_foods"))