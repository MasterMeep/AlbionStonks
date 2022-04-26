import streamlit as st
import requests
import json

sts = st.session_state

if 'ls' not in sts:
	sts.craftRecipies = {'thing1': ['thing1', 'thing2', 'thing3']}
	sts.refineRecipies = {}
	sts.cityCaftBonus = {}
	sts.cityRefineBonus = {}
	sts.cities = ['Bridgewatch', 'Caerleon', 'Fort Sterling', 'Lymhurst', 'Thetford']
	sts.saveCraft = {}
	sts.saveRefine = {}
	sts.craftItems = list(sts.craftRecipies.keys())
	sts.refineItems = list(sts.refineRecipies.keys())

selected_city = st.selectbox("Select A City", sts.cities)
selected_item = st.selectbox('Select An Item To Craft', sts.craftItems)
with st.form(key='columns_in_form'):
    cols = st.beta_columns(len(sts.craftRecipies[selected_item]))
    for i, col in enumerate(cols):
        col.number_input(f"Enter price of {sts.craftRecipies[selected_item][i]}", key=i)
    submitted = st.form_submit_button('Submit')


selected_item = st.selectbox('Select An Item To Refine', sts.refineItems)
