import streamlit as st
import requests
import json

sts = st.session_state

if 'init' not in sts:
	sts.craftRecipies = {'thing1': [['thing1', 25], ['thing2', 50]],'thing2': [['thing1', 25]]}
	sts.refineRecipies = {}
	sts.cityCaftBonus = {}
	sts.cityRefineBonus = {}
	sts.cities = ['Bridgewatch', 'Caerleon', 'Fort Sterling', 'Lymhurst', 'Thetford']
	sts.savedCraft = {}
	sts.savedRefine = {}
	sts.savedItems = {}
	sts.craftItems = list(sts.craftRecipies.keys())
	sts.refineItems = list(sts.refineRecipies.keys())
	sts.init = 'init'

selected_city = st.selectbox("Select A City", sts.cities)
selected_item = st.selectbox('Select An Item To Craft', sts.craftItems)
with st.form(key='columns_in_form'):
    cols = st.columns(len(sts.craftRecipies[selected_item]))
    num_of_inps = 0
    for i, col in enumerate(cols):
        try:col.number_input(f"Enter price of {sts.craftRecipies[selected_item][i][0]}", key=sts.craftRecipies[selected_item][i][0], step=1, value=sts.savedItems[sts.craftRecipies[selected_item][i][0]])
        except: col.number_input(f"Enter price of {sts.craftRecipies[selected_item][i][0]}", key=sts.craftRecipies[selected_item][i][0], step=1)
        num_of_inps += 1
    submittedCraft = st.form_submit_button('Submit')

craftSellPrice = st.number_input(f'Enter the sell price of {selected_item}')

if submittedCraft:
	running = 0
	for i in (sts.craftRecipies[selected_item]):
		sts.savedItems[i[0]] = int(getattr(sts, i[0]))
		running += int(getattr(sts, i[0]))
try: 
	sts.savedCraft[selectedItem] = running
	st.write(sts.savedCraft)
except: st.write('aaaa')

st.table(sts.savedCraft)

selected_item = st.selectbox('Select An Item To Refine', sts.refineItems)
