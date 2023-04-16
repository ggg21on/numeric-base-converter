import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

# This is header
st.header('Numerical Base Conversion Calculator :computer:')
# This subheader
st.markdown('<h1 style="font-size:16px;">A number base calculator is a tool designed to perform mathematical calculations involving numbers in different number systems, such as the decimal, binary, octal, or hexadecimal system.</h1>', unsafe_allow_html=True)


bases = ['Binary', 'Octal', 'Decimal', 'Hexadecimal', 'Sexagesimal']


# Selection
entrada_base = st.selectbox('Select input base:', bases)
entrada_valor = st.number_input('Select input value:', step=1)

saida_base = st.selectbox('Select outpat basis', bases)

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
        if saida_base == 'Binary':
            valor_saida = bin(valor_decimal)[2:]

        elif saida_base == 'Octal':
            valor_saida = oct(valor_decimal)[2:]

        elif saida_base == 'Decimal':
            valor_saida = str(valor_decimal)

        elif saida_base == 'Hexadecimal':
            valor_saida = hex(valor_decimal)[2:]

        elif saida_base == 'Sexagesimal':
            valor_saida = divmod(valor_decimal)[2:]

        # Exibir resultado
        st.write(f'The value {entrada_valor} at the base {entrada_base} is the same as {valor_saida}  at the base {saida_base}')
        
    except ValueError:
        st.write('Input value is invalid for selected base!',
                 unsafe_allow_html=True)

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
