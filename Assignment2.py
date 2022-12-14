    # -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 19:37:21 2022

@author: ds22abr
"""

"""
FUNCTION PART
"""

rows=[]
with open("Forest_Area.csv", 'r') as file:
          print(file)
          
          file =file
          


"""
BAR GRAPH
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# In[]

frost_area = pd.read_csv("Forest_Area.csv")
print(frost_area)

drp_frost_column = frost_area.drop(['Country Code', 'Indicator Name', 'Indicator Code', '2008'], axis=1)
print(drp_frost_column)

new_frost_area = drp_frost_column.iloc[[2,4,5,8,10,11,20],:]
print(new_frost_area)

drp_frost_null = new_frost_area.dropna()
print(drp_frost_null)

frost_index = drp_frost_null.set_index('Country Name')
print(frost_index)

frost_sel_cols = (new_frost_area["Country Name"])

x = np.arange(len(frost_sel_cols))

frost_one = (new_frost_area["2010"])
frost_two = (new_frost_area["2012"])
frost_three = (new_frost_area["2014"])
frost_four = (new_frost_area["2016"])
frost_five = (new_frost_area["2018"])
frost_six = (new_frost_area["2020"])

plt.figure(figsize=(10,8))


plt.bar(x-0.3,frost_one, width=0.1, label="2010", edgecolor="black")
plt.bar(x-0.2,frost_two, width=0.1, label="2012", edgecolor="black")
plt.bar(x-0.1,frost_three, width=0.1, label="2014", edgecolor="black")
plt.bar(x+0.1,frost_four, width=0.1, label="2016", edgecolor="black")
plt.bar(x+0.2,frost_five, width=0.1, label="2018", edgecolor="black")
plt.bar(x+0.3,frost_six, width=0.1, label="2020", edgecolor="black")

plt.xticks(x, frost_sel_cols, rotation = 45)
plt.xlabel("Countries")
plt.ylabel("Forest Area")
plt.legend()
plt.show()






# In[]
"""
BAR GRAPH
"""
# In[]

Pop_total = pd.read_csv("Population_Total.csv")
print(Pop_total)

drp_Pop_column = Pop_total.drop(['Country Code', 'Indicator Name', 'Indicator Code', '1989'], axis=1)
print(drp_Pop_column)

new_Pop_total = drp_Pop_column.iloc[[13,119,154,178,186,263],:]
print(new_Pop_total)

drp_Pop_null = new_Pop_total.dropna()
print(drp_Pop_null)

Pop_index = drp_Pop_null.set_index('Country Name')
print(Pop_index)

Pop_sel_cols = (new_Pop_total["Country Name"])

x = np.arange(len(Pop_sel_cols))

Pop_one = (new_Pop_total["2010"])
Pop_two = (new_Pop_total["2012"])
Pop_three = (new_Pop_total["2014"])
Pop_four = (new_Pop_total["2016"])
Pop_five = (new_Pop_total["2018"])
Pop_six = (new_Pop_total["2020"])

plt.figure(figsize=(10,8))


plt.bar(x-0.3,Pop_one, width=0.1, label="2010", edgecolor="black")
plt.bar(x-0.2,Pop_two, width=0.1, label="2012", edgecolor="black")
plt.bar(x-0.1,Pop_three, width=0.1, label="2014", edgecolor="black")
plt.bar(x+0.1,Pop_four, width=0.1, label="2016", edgecolor="black")
plt.bar(x+0.2,Pop_five, width=0.1, label="2018", edgecolor="black")
plt.bar(x+0.3,Pop_six, width=0.1, label="2020", edgecolor="black")

plt.xticks(x, Pop_sel_cols, rotation = 45)
plt.xlabel("Countries")
plt.ylabel("Population Total")
plt.legend()
plt.show()



# In[]


"""
LINE GRAPH
"""

# Read Excel file and have a look

hfc = pd.read_csv("ghg-emissions.csv")
print("\nhfc: \n", hfc)

hfc = hfc.drop(['unit'], axis=1)
print("\ndrop hfc: \n", hfc)

# transpose it

# In[ ]:


hfc = pd.DataFrame.transpose(hfc)
print("\n transpose hfc: \n", hfc)

# Create the header

# In[ ]:

header_1 = hfc.iloc[0].values.tolist()
hfc.columns = header_1
print("\nheader hfc",hfc)

# Two ways to remove the first two lines

# In[ ]:

hfc = hfc.iloc[2:]
print("\nremove lines hfc: \n",hfc)
# Remove NaN entries for Germany and India. 

# In[ ]:

print(len(hfc))

# hfc = hfc[hfc["United States"].notna()]

hfc = hfc[hfc["Russia"].notna()]
hfc = hfc[hfc["India"].notna()]
hfc = hfc[hfc["Indonesia"].notna()]
hfc = hfc[hfc["Brazil"].notna()]
hfc = hfc[hfc["Japan"].notna()]
hfc = hfc[hfc["Iran"].notna()]
hfc = hfc[hfc["Canada"].notna()]
hfc = hfc[hfc["Italy"].notna()]
hfc = hfc[hfc["Germany"].notna()]


# And the plot

# In[ ]:


hfc.index = hfc.index.astype(int)

plt.figure(figsize=(10,8))


plt.plot(hfc.index, hfc["Russia"], label="Russia", linestyle='dashed')
plt.plot(hfc.index, hfc["Brazil"], label="Brazil", linestyle='dashed')
plt.plot(hfc.index, hfc["India"], label="India", linestyle='dashed')
plt.plot(hfc.index, hfc["Indonesia"], label="Indonesia", linestyle='dashed')
plt.plot(hfc.index, hfc["Japan"], label="Japan", linestyle='dashed')
plt.plot(hfc.index, hfc["Iran"], label="Iran", linestyle='dashed')
plt.plot(hfc.index, hfc["Canada"], label="Canada", linestyle='dashed')
plt.plot(hfc.index, hfc["Italy"], label="Italy", linestyle='dashed')
plt.plot(hfc.index, hfc["Germany"], label="Germany", linestyle='dashed')

plt.xlabel("year")
plt.ylabel("GHG Emmissions")
plt.legend()
plt.show()




"""
LINE GRAPH (2)
"""

# Read Excel file and have a look

pop = pd.read_csv("Population_Total.csv")
print("\npop: \n", pop)

pop = pop.drop(['Indicator Name','Indicator Code'], axis=1)
print("\ndrop pop: \n", pop)

# transpose it

# In[ ]:


pop = pd.DataFrame.transpose(pop)
print("\n transpose pop: \n", pop)

# Create the header

# In[ ]:

header_2 = pop.iloc[0].values.tolist()
pop.columns = header_2
print("\nheader pop",pop)

# Two ways to remove the first two lines

# In[ ]:

pop = pop.iloc[2:]
print("\nremove lines pop: \n",pop)
# Remove NaN entries for Brazil and Russia. 

# In[ ]:

print(len(pop))

pop = pop[pop["Russia"].notna()]
pop = pop[pop["Brazil"].notna()]
pop = pop[pop["Indonesia"].notna()]
pop = pop[pop["Japan"].notna()]
pop = pop[pop["Iran"].notna()]
pop = pop[pop["Canada"].notna()]
pop = pop[pop["Italy"].notna()]
pop = pop[pop["Germany"].notna()]


# And the plot

# In[ ]:


pop.index = pop.index.astype(int)

plt.figure(figsize=(10,8))

plt.plot(pop.index, pop["Russia"], label="Russia", linestyle='dashed')
plt.plot(pop.index, pop["Brazil"], label="Brazil", linestyle='dashed')
plt.plot(pop.index, pop["Indonesia"], label="Indonesia", linestyle='dashed')
plt.plot(pop.index, pop["Japan"], label="Japan", linestyle='dashed')
plt.plot(pop.index, pop["Iran"], label="Iran", linestyle='dashed')
plt.plot(pop.index, pop["Canada"], label="Canada", linestyle='dashed')
plt.plot(pop.index, pop["Italy"], label="Italy", linestyle='dashed')
plt.plot(pop.index, pop["Germany"], label="Germany", linestyle='dashed')

plt.xlabel("year")
plt.ylabel("Population")
plt.legend()
plt.show()











