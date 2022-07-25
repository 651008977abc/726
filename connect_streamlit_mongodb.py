# streamlit_app.py

import streamlit as st
import pymongo
import pandas as pd
# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return pymongo.MongoClient(**st.secrets["mongo"])

client = init_connection()

# Pull data from the collection.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def get_data():
    db = client['IRCdatabase']
    items = db['IRB1210axis2_03_endurance'].find().limit(10)
    items = pd.DataFrame(list(items),columns=('Time','GB_IRB1210_ax2__speed__1'))  # make hashable for st.experimental_memo
    return items

itemf = get_data()
# st.table(itemf)
st.write(itemf)
# Print results.
# for item in items:
#     st.write(item)