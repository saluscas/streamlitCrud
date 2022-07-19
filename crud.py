import streamlit as st;

with st.form(key="includ_cliente"):
    input_name = st.text_input(label="insira o seu nome")
    input_age = st.number_input(label="insira sua idade", format="%d", step=1)
    input_occupation = st.selectbox("selecione sua profissão", ["Desenvolvedor", "Designer", "Outro"])
    input_button_submit = st.form_submit_button("Enviar")