import streamlit as st
import requests
import json

sts = st.session_state

if 'ls' not in sts:
	sts.craftRecipies = {'thing1': ['thing1', 'thing2', 'thing3'], 'thing2': ['thing1', 'thing2', 'thing3', 'thing4']}
	sts.refineRecipies = {}
	sts.cityCaftBonus = {}
	sts.cityRefineBonus = {}
	sts.cities = ['Bridgewatch', 'Caerleon', 'Fort Sterling', 'Lymhurst', 'Thetford']
	sts.savedCraft = {}
	sts.savedRefine = {}
	sts.craftItems = list(sts.craftRecipies.keys())
	sts.refineItems = list(sts.refineRecipies.keys())

selected_city = st.selectbox("Select A City", sts.cities)
selected_item = st.selectbox('Select An Item To Craft', sts.craftItems)
with st.form(key='columns_in_form'):
    cols = st.columns(len(sts.craftRecipies[selected_item]))
    num_of_inps = 0
    for i, col in enumerate(cols):
        col.number_input(f"Enter price of {sts.craftRecipies[selected_item][i]}", key=f"craft_inp_{i}")
        num_of_inps += 1
    submittedCraft = st.form_submit_button('Submit')

if submittedCraft:
	running = 0
	for i in range(num_of_inps):	
		running += int(getattr(sts, f"craft_inp_{i}"))

	st.write(running)
selected_item = st.selectbox('Select An Item To Refine', sts.refineItems)
