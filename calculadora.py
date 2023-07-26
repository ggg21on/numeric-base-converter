import pandas as pd
import streamlit as st

# This is header
st.header('Numerical Base Conversion Calculator :computer:')
# This subheader
st.markdown(
    'A number base calculator is a tool designed to perform mathematical calculations involving numbers in different number systems, such as the decimal, binary, octal, or hexadecimal system.'
)

bases = {'Binary': 2, 'Octal': 8, 'Decimal': 10, 'Hexadecimal': 16}

# Function to convert a number from any base to decimal
def base_to_decimal(number, base):
    digits = '0123456789ABCDEF'
    decimal_value = 0
    power = len(number) - 1

    for digit in number:
        if digit.upper() not in digits[:base]:
            return None  # Invalid digit for the selected base
        decimal_value += digits.index(digit.upper()) * (base ** power)
        power -= 1

    return decimal_value

# Function to convert a decimal number to any base
def decimal_to_base(decimal_value, base):
    if decimal_value == 0:
        return '0'  # Special case for decimal value zero

    digits = '0123456789ABCDEF'
    result = ''

    while decimal_value > 0:
        remainder = decimal_value % base
        result = digits[remainder] + result
        decimal_value //= base

    return result

# Selection
entrada_base = st.selectbox('Select input base:', bases)
entrada_valor = st.text_input('Select input value:', max_chars=None, key=None)
saida_base = st.selectbox('Select output base:', bases)

# Input
if st.button('Convert'):
    if entrada_valor.strip() == '':
        st.markdown('Please enter a valid input value!')
    else:
        valor_decimal = base_to_decimal(entrada_valor, bases[entrada_base])
        if valor_decimal is not None:
            valor_saida = decimal_to_base(valor_decimal, bases[saida_base])
            st.success(
                f'The value {entrada_valor} at the base {entrada_base} is the same as {valor_saida} at the base {saida_base}'
            )
        else:
            st.markdown('Input value is invalid for selected base!')

# title table equivalence
st.subheader('Equivalence Table')

# table equivalence
decimals = list(range(17))
octals = [decimal_to_base(i, 8) for i in decimals]
binaries = [decimal_to_base(i, 2) for i in decimals]
hexadecimals = [decimal_to_base(i, 16) for i in decimals]

data = {'Decimal': decimals, 'Octal': octals, 'Binary': binaries, 'Hexadecimal': hexadecimals}
df = pd.DataFrame(data)

st.table(df)

footer = """
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
    img {
        max-width: 100%;
    }

    .footer {
        position: static;
        left: 0;
        bottom: 0;
        width: 100%;
        height: auto;
        text-align: center;
    }

    .footer img {
        filter: invert(1);
    }

    a[href="https://github.com/ggg21on/numeric-base-converter"] img {
        filter: invert(32%) sepia(99%) saturate(465%) hue-rotate(194deg) brightness(102%) contrast(101%);
    }
</style>
<div class="footer">
    <br><br><br><br>
    <p><b>Get In Touch With Me</b></p>
    <a href="https://github.com/ggg21on/numeric-base-converter"><img
            src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="github icon" width="50" height="50"></a>
    <a href="https://www.linkedin.com/in/gabriel-gomes-574287258/?locale=en_US"><img
            src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="linkedin icon" width="50" height="50"></a>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
