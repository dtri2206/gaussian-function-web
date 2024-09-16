import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from math import *
col1, col2 = st.columns(2)
with col1:
  μ = st.slider('μ',-10.0,10.0)
with col2:
  σ = st.slider('σ',0.1,10.0)
def y(x,μ,σ):
  return (1/(np.sqrt(σ*2*3.14)))*np.exp(-((x-μ)**2)/(2*σ))
def xy(a):
  return 0*a

x = np.linspace(-10,10)

fig, ax = plt.subplots()
ax.plot(x, y(x,μ,σ))
ax.plot(x, xy(x), color = 'red')
ax.plot(xy(x) ,y(x,μ,σ), color = 'red')
plt.title('GAUSS MASS FUNCTION')
plt.xlabel('x')
plt.ylabel('p(x)')
st.pyplot(fig)
