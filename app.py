import streamlit as st
import requests
import json

sts = st.session_state

if 'init' not in sts:
	sts.craftRecipes = {'thing1': [['thing1', 25], ['thing2', 50]],'thing2': [['thing1', 25]]}
	sts.refineRecipes = {'4': 3, '4.1': 3, '5': 3, '5.1': 3, '6': 4, '6.1': 4, '7': 5, '7.1': 5, '8': 5, '8.1': 5}
	sts.cityCaftBonus = {}
	sts.cityRefineBonus = {}
	sts.cities = ['Bridgewatch', 'Caerleon', 'Fort Sterling', 'Lymhurst', 'Thetford']
	sts.savedCraft = {'Craft Price': {}, 'Sell Price': {}, 'Profit Per Craft': {}, '% Profit': {}}
	sts.savedRefine = {'Craft Price': {}, 'Sell Price': {}, 'Profit Per Craft': {}, '% Profit': {}}
	sts.savedItems = {}
	sts.craftItems = list(sts.craftRecipes.keys())
	sts.refineItems = list(sts.refineRecipes.keys())
	sts.init = 'init'

selected_city = st.selectbox("Select A City", sts.cities)
selected_item = st.selectbox('Select An Item To Craft', sts.craftItems)
with st.form(key='columns_in_form'):
    cols = st.columns(len(sts.craftRecipes[selected_item]))
    num_of_inps = 0
    for i, col in enumerate(cols):
        try:col.number_input(f"Enter price of {sts.craftRecipes[selected_item][i][0]}", key=sts.craftRecipes[selected_item][i][0], step=1, value=sts.savedItems[sts.craftRecipes[selected_item][i][0]])
        except: col.number_input(f"Enter price of {sts.craftRecipes[selected_item][i][0]}", key=sts.craftRecipes[selected_item][i][0], step=1)
        num_of_inps += 1
    submittedCraft = st.form_submit_button('Submit')

craftSellPrice = st.number_input(f'Enter the sell price of {selected_item}', step=1)

if submittedCraft:
	running = 0
	for i in (sts.craftRecipes[selected_item]):
		sts.savedItems[i[0]] = int(getattr(sts, i[0]))
		running += int(getattr(sts, i[0]))*i[1]
	sts.savedCraft['Craft Price'][selected_item] = running
	sts.savedCraft['Sell Price'][selected_item] = craftSellPrice
	sts.savedCraft['Profit Per Craft'][selected_item] = craftSellPrice-running
	sts.savedCraft['% Profit'][selected_item] = str(round(round((craftSellPrice-running)/running, 4)*100, 2))+'%'
	
st.table(sts.savedCraft)


selected_refine = st.selectbox('Select An Item To Refine', sts.refineItems)

form = st.form("Refine Profits")
item1 = form.number_input('Enter the price of one log', step=1)
item2 = form.number_input('Enter the price of the plank', step=1) 
sell = form.number_input(f'Enter the sell price', step=1)

submitRefine = form.form_submit_button("Submit")

if submitRefine:
	sell = sell*1.4
	buy = (item1*sts.refineRecipes[selected_refine]+item2)
	sts.savedRefine['Craft Price'][selected_refine] = round(buy,2)
	sts.savedRefine['Sell Price'][selected_refine] = round(sell,2)
	sts.savedRefine['Profit Per Craft'][selected_refine] = round(sell-buy,2)
	sts.savedRefine['% Profit'][selected_refine] = str(round(round((sell-buy)/buy, 4)*100, 2))+'%'
	
st.table(sts.savedRefine)
	
