import streamlit as st
from chatbot_functies import chatbot_response
import json

st.title("🌐 Universal Translator 🤖")
st.markdown("Vertaal tekst met behulp van AI")

# Create tabs
tab1, tab2, tab3 = st.tabs(["Tekst", "Bestand Uploaden", "JSON Uploaden"])

# Tab 1: Text input
with tab1:
    st.header("Tekstinvoer")
    # Create a form for text input
    text_form = st.form(key="text_translation_form")
    with text_form:
        # Text input area
        input_text = st.text_area(
            "Voer de tekst in die je wilt vertalen:", 
            placeholder="Typ hier je tekst...", 
            height=200
        )
        # Language selection
        dest_lang = st.selectbox(
            "Selecteer doeltaal:", 
            ["Nederlands", "Engels", "Frans", "Duits", "Spaans"]
        )
        # Translation button
        translate_text_button = text_form.form_submit_button("Vertaal")

    # Perform translation for text input
    if translate_text_button:
        if not input_text:
            st.warning("Voer eerst tekst in om te vertalen!")
        else:
            # Create a prompt for the chatbot
            PROMPT = f"Vertaal de volgende tekst naar het {dest_lang}:\n{input_text}\nGeef alleen de vertaalde tekst terug, zonder extra uitleg of commentaar."
            
            # Show spinner and translate
            with st.spinner("Aan het vertalen..."):
                response = chatbot_response(PROMPT)
            
            # Display results
            st.subheader(f"Vertaald naar {dest_lang}:")
            st.write(response)

# Tab 2: File upload
with tab2:
    st.header("Bestand Uploaden")
    # File upload area
    uploaded_file = st.file_uploader(
        "Upload een tekstbestand", 
        type=['txt']
    )
    if uploaded_file is not None:
        try:
            # Read and decode uploaded file
            input_text = uploaded_file.getvalue().decode("utf-8")
            st.success("Bestand succesvol geüpload!")
            
            # Translation options
            dest_lang = st.selectbox(
                "Selecteer doeltaal voor het bestand:", 
                ["Nederlands", "Engels", "Frans", "Duits", "Spaans"]
            )
            if st.button("Vertaal Bestand"):
                PROMPT = f"Vertaal de volgende tekst naar het {dest_lang}:\n{input_text}\nGeef alleen de vertaalde tekst terug, zonder extra uitleg of commentaar."
                
                # Show spinner and translate
                with st.spinner("Aan het vertalen..."):
                    response = chatbot_response(PROMPT)
                
                # Display results
                st.subheader(f"Vertaald naar {dest_lang}:")
                st.text(response)

                # Download button for translated text
                st.download_button(
                    label="Download vertaalde tekst",
                    data=response,
                    file_name=f"vertaling_{dest_lang}.txt",
                    mime="text/plain"
                )
        except Exception as e:
            st.error(f"Fout bij het lezen van het bestand: {e}")

# Tab 3: JSON upload
with tab3:
    st.header("JSON Uploaden")
    # File upload area
    json_file = st.file_uploader(
        "Upload een JSON-bestand", 
        type=['json']
    )

    if json_file is not None: 
        try:
            #Read json file
            json_data = json.load(json_file)
            st.success("JSON bestand succesvol geüpload!")
            st.json(json_data)

            dest_lang = st.selectbox(
                "Selecteer doeltaal voor de JSON waarden:", 
                ["Nederlands", "Engels", "Frans", "Duits", "Spaans"]
            )

            if st.button("Vertaal Bestand"):
                PROMPT = f"Vertaal de volgende JSON tekst naar het {dest_lang}:\n{input_text}\nGeef alleen de vertaalde tekst terug, zonder extra uitleg of commentaar."
                
                # Show spinner and translate
                with st.spinner("Aan het vertalen..."):
                    response = chatbot_response(PROMPT)

                     # Display results
                st.subheader(f"Vertaald naar {dest_lang}:")
                st.text(response)

                # Download button for translated text
                st.download_button(
                    label="Download vertaalde tekst",
                    data=response,
                    file_name=f"vertaling_{dest_lang}.json",
                    mime="text/plain"
                )


        except Exception as e:
            st.error(f"Fout bij het lezen van het bestand: {e}")