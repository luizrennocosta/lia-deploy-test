import streamlit as st

from multiapp import FirstPage
from pages import about_us, lia

app = FirstPage()
app.add_app("Início", lia.app)
app.add_app("Sobre LIA", about_us.app)
app.run()
