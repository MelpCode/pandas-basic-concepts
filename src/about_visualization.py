
from tkinter import *
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
plt.style.use('ggplot')

#Import CSV files
df1 = pd.read_csv('src/df1.csv',index_col=0)  # Se importa un archivo CSV de prueba y se asigna la primera columna como indice
df2 = pd.read_csv('src/df2.csv')

class Graphics:
    def __init__(self,master):
        self.master = master
        self.master.title('Pandas Visualization')
        self.master.geometry("600x500+120+120")

        frm = Frame(self.master, padx=10, pady=10)
        frm.pack()

        fig = Figure()
        ax = fig.add_subplot(111)
        graph = FigureCanvasTkAgg(fig, master=frm)
        graph.draw()
        graph.get_tk_widget().pack()

        # TYPES OF PLOT
        # AREA
        #df2.plot.area(ax=ax)

        # BAR
        #df2.plot.bar(ax=ax)
        #Stacked Bar
        #df2.plot.bar(ax=ax,stacked=True)

        # SCATTER
        #df1.plot.scatter(x='A',y='B',ax=ax)
        #df1.plot.scatter(ax=ax,x='A', y='B', c='C', cmap='coolwarm')

        #HISTOGRAM
        #print(df1['A'].plot.hist(ax=ax,bins=60))

        #LINE
        #df1.plot.line(ax=ax,y='A',figsize=(15,7), lw=2, color='blue')

        #HEXAGONAL BIN PLOT
        #df = pd.DataFrame(np.random.randn(1000, 2), columns=['a', 'b'])
        #df.plot.hexbin(ax=ax, x='a',y='b',gridsize=25,cmap='Oranges')

        #KERNEL DENSITY OBSERVATION
        #df2['a'].plot.kde(ax=ax)
        #df2.plot.density(ax=ax)

root = Tk()
app = Graphics(root)
root.mainloop()


