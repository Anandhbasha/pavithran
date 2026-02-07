# pip install ipywidgets
#%%
import ipywidgets as wid
from IPython.display import display

# Slider = wid.IntSlider(
#     value=300,
#     min=200,
#     max=10000,
#     step=50,
#     description="Amount"
# )

# display(Slider)

toggle = wid.ToggleButton(value=False,description="ON/OFF")

display(toggle)

data = wid.DatePicker(
    description = "DOB"
)
display(data)
# print(Slider)
# %%
