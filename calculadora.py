import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

# This is header
st.header('Numerical Base Conversion Calculator :computer:')
# This subheader
st.markdown('A number base calculator is a tool designed to perform mathematical calculations involving numbers in different number systems, such as the decimal, binary, octal, or hexadecimal system.')

bases = ['Binary', 'Octal', 'Decimal', 'Hexadecimal']

# Selection
entrada_base = st.selectbox('Select input base:', bases)
entrada_valor = st.text_input(
    'Select input value:', value='', max_chars=None, key=None)

saida_base = st.selectbox('Select outpat basis', bases)


def is_valid_digited(digited, base):
    valid_digits = {
        'Binary': ['0', '1'],
        'Octal': ['0', '1', '2', '3', '4', '5', '6', '7'],
        'Decimal': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
        'Hexadecimal': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    }
    return digited.upper() in valid_digits[base]


if st.button('Convert'):
    if is_valid_digited(entrada_valor, entrada_base):
        try:
            # Convert input to decimal
            if entrada_base == 'Binary':
                valor_decimal = int(str(entrada_valor), 2)

            elif entrada_base == 'Octal':
                valor_decimal = int(str(entrada_valor), 8)

            elif entrada_base == 'Decimal':
                valor_decimal = int(str(entrada_valor))

            elif entrada_base == 'Hexadecimal':
                valor_decimal = int(str(entrada_valor), 16)

            # Convert decimal to output
            if saida_base == 'Binary':
                valor_saida = bin(valor_decimal)[2:]

            elif saida_base == 'Octal':
                valor_saida = oct(valor_decimal)[2:]

            elif saida_base == 'Decimal':
                valor_saida = str(valor_decimal)

            elif saida_base == 'Hexadecimal':
                valor_saida = hex(valor_decimal)[2:]

            # Show result
            st.success(
                f'The value {entrada_valor} at the base {entrada_base} is the same as {valor_saida}  at the base {saida_base}')

        except ValueError:
            st.markdown('Input value is invalid for selected base!')

# title table equivalence
st.subheader('Equivalence Table')

# table equivalence
decimals = list(range(17))
octals = [oct(i)[2:] for i in decimals]
binaries = [bin(i)[2:].zfill(5) for i in decimals]
hexadecimals = [hex(i)[2:].upper() for i in decimals]
data = {'Decimal': decimals, 'Octal': octals,
        'Binary': binaries, 'Hexadecimal': hexadecimals}
df = pd.DataFrame(data)

st.table(df)
