import plotly.express as px
import pandas as pd
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins

# Load the Palmer Penguins dataset
penguins_df = palmerpenguins.load_penguins()

# Define data table using Pandas DataFrame
penguins_df.head(2)  # Display only the first two rows

# slider range 
ui.input_slider("slider", "Slider", min=0, max=100, value=[20, 40])  

# Define UI layout
ui.page_opts(title="Penguin data Tesfamariam", fillable=True)

with ui.layout_columns():
    # Define charts
    @render_plotly
    def plot1():
        return px.histogram(penguins_df, y="bill_length_mm", title="Bill Length Distribution")

    @render_plotly
    def plot2():
        return px.histogram(penguins_df, y="body_mass_g", title="Body Mass Distribution")
