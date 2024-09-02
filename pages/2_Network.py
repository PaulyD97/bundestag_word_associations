import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from pyvis.network import Network
from build_network_with_word import build_network_with_word

#import the data for building a list for the options of words for the user
coo_matrix = pd.read_hdf('data/coo_matrix.h5', key='df')

#user can choose a word from the list
selected_word = st.selectbox('Auswahl Wort', coo_matrix.columns)

# builds the graph with the chosen word
G = build_network_with_word(selected_word)

# This creates the settings for the HTML file which will later contain the graph
graph_ch = Network(height='550px', width='100%', notebook=True, bgcolor="black", font_color="white")

# Configure the graph. Play around with the values to see what the settings change
graph_ch.set_options("""
{
  "nodes": {
    "color": {
         "inherit": true
       },
    "size": 1000
  },
  "edges": {
    "width": 1000,
     "color": {
      "inherit": true
    },
    "selfReferenceSize": null,
    "selfReference": {
      "angle": 0.7853981633974483
    },
    "smooth": false
  },
  "physics": {
    "enabled": true,
    "barnesHut": {
      "gravitationalConstant": -8000
    },
    "minVelocity": 0.075,
    "maxVelocity": 2
  }
}""")

# This creates a pyvis graph from the networkx graph (we do this because a pyvis graph is easily stored as an HTML file which we can load into streamlit)
graph_ch.from_nx(G)

# The pyvis graph is saved in a html file
graph_ch.save_graph("data/graph_40.html")
print("saved")

# This opens the HTML file
print("preopen")
HtmlFile = open("data/graph_40.html", 'r', encoding='utf-8')
source_code = HtmlFile.read()

# This embeds the HTML file in the streamlit webpage
print("preshow")
components.html(source_code, height=560, width=900, scrolling=True)