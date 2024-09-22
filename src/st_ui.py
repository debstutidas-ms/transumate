import os
import streamlit as st
from main import process_file, translate_file, summarize_file, generate_pdf


BASE_PATH = "/Users/debstutidas/Documents/MLProjects/transumate/src"
DOCUMENT_PATH = 'Document'

sidebar = st.sidebar

sidebar.title("Transumate AI")


# Another way to create a heading using markdown
st.subheader("Where Every Document Speaks Your Language")



sidebar.image('/Users/debstutidas/Documents/MLProjects/transumate/src/images/sidebar.png')


# Tabs
tab1, tab2, tab3 = st.tabs(["Upload Document", "Translate", "Summarize"])

with tab1:
    st.subheader("Upload Document")

    uploaded_file = st.file_uploader("Choose a File")
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        filename = uploaded_file.name


        source_language = st.selectbox('Select Original Document Language', ('English', 'Hindi', 'Kannada', 'Bengali',
                                                                             'French', 'German', 'Spanish', 'Chinese',
                                                                             'Japanese'))
        st.write('Original Document is in language:', source_language)

        updated_file_name = filename[:-4]+'_'+source_language+'.pdf'
        file_path = os.path.join(BASE_PATH, DOCUMENT_PATH, updated_file_name)

        with open(file_path, 'wb') as f:
            f.write(bytes_data)
            f.close()

    process = st.button('Process File')

    with st.spinner('Processing..'):

        result = None

        if process:
            process_file(file_name=updated_file_name, source_language=source_language)

with tab2:

    col1, col2 = st.columns([3, 1])

    with col1:
        st.subheader("Translate")
        target_language = st.selectbox('Select Target Document Language', ('English', 'Hindi', 'Kannada', 'Bengali',
                                                                             'French', 'German', 'Spanish', 'Chinese',
                                                                             'Japanese'))
        translate = st.button('Translate File')

        st.write('You selected:', target_language)

        translated = False

        with st.spinner('Translating..'):
            result = None

            if translate:
                translated_text_path = translate_file(file_name=updated_file_name, source_language=source_language, dest_language=target_language)
                output_pdf_path, file_name = generate_pdf(translated_text_path, target_language, 'translation')
                translated = True

        if translated:
            with open(output_pdf_path, "rb") as f:
                st.download_button("Download pdf", f, file_name)

    with col2:
        st.image('/Users/debstutidas/Documents/MLProjects/transumate/src/images/translation.png')

with tab3:

    col1, col2 = st.columns([3, 1])
    with col1:
        st.subheader("Summarize")
        summary_language = st.selectbox('Select Summary Language', ('English', 'Hindi', 'Kannada', 'Bengali',
                                                                           'French', 'German', 'Spanish', 'Chinese',
                                                                           'Japanese'))

        summarize = st.button('Summarize File')
        with st.spinner('Summarizing..'):
            result = None

            if summarize:
                output_pdf_path, file_name = summarize_file(file_name=filename, summary_language=summary_language)

                with open(output_pdf_path, 'rb') as f:
                    st.download_button('Download Summary', f, file_name=file_name)

    with col2:
        st.image('/Users/debstutidas/Documents/MLProjects/transumate/src/images/summary.png')

