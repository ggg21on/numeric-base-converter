import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

github_icon = '<a href="https://github.com/ggg21on/numeric-base-converter" target="_blank"><img src="https://img.icons8.com/fluent/48/000000/github.png"/></a>'
github_text = '<a href="https://github.com/ggg21on/numeric-base-converter" target="_blank" style="font-size: 1.2em; margin-left: 0.5em;">Source Code</a>'
linkedin_icon = '<a href="https://www.linkedin.com/in/gabriel-gomes-574287258/" target="_blank"><img src="https://img.icons8.com/fluent/48/000000/linkedin.png"/></a>'
linkedin_text = '<a href="https://www.linkedin.com/in/gabriel-gomes-574287258/" target="_blank" style="font-size: 1.2em; margin-left: 0.5em;">LinkedIn</a>'

st.sidebar.markdown(linkedin_icon + linkedin_text)

github_link = f'<div style="display: flex; align-items: center;">{github_icon}{github_text}</div>'

st.sidebar.markdown(github_link)

options = ['Binary', 'Octal', 'Decimal', 'Hexadecimal']
# This is header
st.header('Numerical Base Conversion Calculator :computer:')
# This subheader
st.markdown('<h1 style="font-size:16px;">A number base calculator is a tool designed to perform mathematical calculations involving numbers in different number systems, such as the decimal, binary, octal, or hexadecimal system.</h1>', unsafe_allow_html=True)

bases = ['Binary', 'Octal', 'Decimal', 'Hexadecimal']

# Selection
entrada_base = st.selectbox('Select input base:', bases)
entrada_valor = st.number_input('Select input value:', step=1)

saida_base = st.selectbox('Selct outpat basis', bases)

# Entrada
if st.button('Convert'):
    try:
        # Converter entrada para decimal
        if entrada_base == 'Binary':
            valor_decimal = int(str(entrada_valor), 2)

        elif entrada_base == 'Octal':
            valor_decimal = int(str(entrada_valor), 8)

        elif entrada_base == 'Decimal':
            valor_decimal = int(str(entrada_valor))

        elif entrada_base == 'Hexadecimal':
            valor_decimal = int(str(entrada_valor), 16)

        # Converter decimal para saída
        if saida_base == 'Binário':
            valor_saida = bin(valor_decimal)[2:]

        elif saida_base == 'Octal':
            valor_saida = oct(valor_decimal)[2:]

        elif saida_base == 'Decimal':
            valor_saida = str(valor_decimal)

        elif saida_base == 'Hexadecimal':
            valor_saida = hex(valor_decimal)[2:]

        # Exibir resultado
        st.write(
            f'O valor {entrada_valor} na base {entrada_base} é igual a {valor_saida} na base {saida_base}')

    except ValueError:
        st.write('Input value is invalid for selected base!')

st.subheader('Equivalence Table')
# table
decimals = list(range(17))
octals = [oct(i)[2:] for i in decimals]
binaries = [bin(i)[2:].zfill(5) for i in decimals]
hexadecimals = [oct(i)[2:].upper() for i in decimals]

data = {'Decimal': decimals, 'Octal': octals,
        'Binary': binaries, 'Hexadecimal': hexadecimals}
df = pd.DataFrame(data)

st.table(df)
