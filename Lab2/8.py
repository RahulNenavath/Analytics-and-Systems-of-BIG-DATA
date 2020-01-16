# 8th Question:

# $ pip install plotly==4.4.1
import plotly.express as px
import matplotlib.pyplot as plt

steps = ['Requirement Elicitation','Requirement Analysis','Software Development','Debugging & Testing','Others']
TimeSpend = [50,110,250,180,70]

data = {'Product Development steps': steps, 'Time spent':TimeSpend}

fig = px.funnel(data, x='Time spent', y='Product Development steps')
fig.show()

plt.show()
