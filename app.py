import streamlit as st

from pages import about_us, lia
from multiapp import FirstPage

app = FirstPage()
app.add_app("Home", lia.app)
app.add_app("Sobre LIA", about_us.app)
app.run()