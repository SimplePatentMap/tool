from io import BytesIO
import pandas as pd
import streamlit as st
from Tspm import SimplePatentMap

st.subheader('SimplePatentMap')

with st.sidebar:
    st.markdown("[データセット](https://github.com/SimplePatentMap/dataset)")
    st.markdown("[J-PlatPat](https://www.j-platpat.inpit.go.jp/)")
#    st.markdown("[使い方](https://www.j-platpat.inpit.go.jp/)")

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
df = pd.DataFrame()
for uploaded_file in uploaded_files:
    df = pd.concat([df, pd.read_csv(uploaded_file)])

if len(df) > 1:
    spm = SimplePatentMap()
    formatted_df = spm.format(df)

    st.write(formatted_df)


    #Downloadボタンの追加
    formatted_df.to_excel(buf := BytesIO(), index=False)
    st.download_button(
        "Download",
        buf.getvalue(),
        "sample.xlsx",
    )


