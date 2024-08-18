import streamlit as st
from streamlit_option_menu import option_menu


data_dashboard = st.Page(
    "views/data_dashboard.py",
    title="Data Dashboard",
    icon=":material/smart_toy:",
)

# 5. Add on_change callback
def on_change(key):
    selection = st.session_state[key]
    
with st.sidebar:
    selected = option_menu("Main Menu", ["Home", "Upload", "Tasks", 'Settings'],
                            icons=['house', 'cloud-upload', "list-task", 'gear'],menu_icon="cast", default_index=0,
                            on_change=on_change, key='menu',styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "15px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"},
    })
    selected

if selected=="Home":
    st.write("Hi")
    pg=st.navigation({
        "Personal Projects": [data_dashboard],
    })
    
pg.run()
