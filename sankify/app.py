from io import StringIO

import streamlit as st
import pandas as pd
from sankify.sankey import plot_sankey

if __name__ == '__main__':
    st.header("Sankify")
    st.subheader("Load a csv from the web or upload from your drive")
    csv_url = st.text_input("Provide csv URL ", value='https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv')
    if st.checkbox("Use CSV Url"):
        data = pd.read_csv(csv_url)
    else:
        data = st.file_uploader("Upload a csv file")
        if data is not None:
            stringio = StringIO(data.getvalue().decode("utf-8"))
            data = pd.read_csv(stringio)

    if data is not None:
        st.dataframe(data.head(5))
        id_col = st.selectbox("Id column:", options=["index"] + data.columns.to_list())
        sankey_col_options = [col for col in data.columns if not col == id_col]
        sankey_columns = st.multiselect("Columns for sankey:", options=data.columns)
        # todo have options for selecting which labels are relevant and all other go into "other" category

        if id_col and len(sankey_columns) >= 2:
            chart = plot_sankey(data, id_col, sankey_columns)
            st.plotly_chart(chart)
        else:
            st.write("Choose an id col and at least two sankey columns!")
