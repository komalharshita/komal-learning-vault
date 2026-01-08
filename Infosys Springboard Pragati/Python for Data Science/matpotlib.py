import random        
import pandas as pd
df = pd.read_csv('pokemon_alopez247.csv') 
 
           
from scipy.stats import itemfreq
# Retrieve a list of group types against the
# number of pokemon(s) belonging to that group
type_1 = itemfreq(df.iloc[:,2])
print(type_1)
# Total number of distinct groups
type_1_grps = len(type_1)
print(type_1_grps)
# Names of group
type_1_names = type_1[:,0]
print(type_1_names)
# Pokemon count particular to each group
type_1_count = type_1[:,1]
print(type_1_count)

           
type_1_grps = np.arange(type_1_grps)
bar_width = 0.5
plt.bar(type_1_grps, type_1_count, bar_width,
                 alpha = 0.5,   # tranparency factor
                 color = 'g',   # color factor
                 label='Pokemon count respective to their Type_1')
plt.legend(loc='best')
plt.xticks(type_1_grps + bar_width/2, type_1_names)
 
# Creating 18 random colors range (0 - 1)
clrs = np.linspace( 0, 1, 18 )
random.shuffle(clrs)
# Creating final list of 18 random colors
colors = []
for i in range(0, 72, 4):
    idx = np.arange( 0, 18, 1 )
    random.shuffle(idx)
    r = clrs[idx[0]]
    g = clrs[idx[1]]
    b = clrs[idx[2]]
    a = clrs[idx[3]]
    colors.append([r, g, b, a])


           
bar_graph = plt.bar(type_1_grps, type_1_count, bar_width,
                 alpha = 0.5,   # tranparency factor
                 color = colors)   # color factor

           
plt.legend(bar_graph, 
           type_1_names,                    # List of group names
           bbox_to_anchor=(1.128, 1.015))   # Position of legend
            
           
plt.xticks(type_1_grps + bar_width/2, type_1_names)
plt.xlabel('Type')
plt.ylabel('Pokemon count')
plt.title('Number of Pokemon per Type_1')
plt.grid()
plt.ylim(0,130)
 

           
df_pie = df[['Type_1', 'Attack', 'Defense', 'Speed', 'HP']].copy()
print(df_pie.head())
frequent_grp = itemfreq(df_pie.iloc[:,0])
frequent_grp = np.array(sorted(frequent_grp, key=lambda x: x[1]))[::-1][0:4,:]
print(frequent_grp)
           
df_pie = df_pie.loc[df_pie.loc[:,'Type_1'].str.contains(r'(Water|Normal|Grass|Bug)')]
print(df_pie)
 
           
# Names of the group
type_1_names = frequent_grp[:,0]
print(type_1_names)
# Mean of samples for each feature corresponding to all 4 group 
df_grp = df_pie.groupby('Type_1').mean()
print(df_grp)
 
           
names = df_grp.columns
colors = ['gold', 'lightcoral', 
              'yellowgreen', 'lightskyblue']
explode = (0, 0, 0, 0.1)  # takes out only the 4th slice 
fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(nrows=2, ncols=2)
ax = [ax1, ax2, ax3, ax4]
for i in range(0,4):
    percent = df_grp.iloc[i,:]
    ax[i].pie(percent, explode = explode,
            labels = names, colors = colors,
            autopct='%.2f%%',   # display value
            shadow=True,
            startangle=90)
    ax[i].set_aspect('equal')
    ax[i].set_title(type_1_names[i])
plt.suptitle('Comparing major features of 4 most frequent Pokemon Group',
             fontsize = 14,
             fontweight = 'bold')
              


df = pd.read_csv('pokemon_alopez247.csv')
tot_power = df.iloc[:,4]
print(tot_power.head(4))
catch_rate = df.iloc[:,21]
print(catch_rate.head(4))
fig, ax = plt.subplots()
p = ax.scatter(catch_rate, tot_power, c = 'g')
ax.grid()
ax.set_xlabel('Catch Rate')
ax.set_ylabel('Total Power')
ax.set_title('Pokemon Catch Rate vs their Power')
plt.legend([p],['Pokemons'])

           
catch_rate_45 = df[df.loc[:,'Catch_Rate'] == 45]
pow_330 = catch_rate_45[catch_rate_45.loc[:,'Total'] <= 330]
print("Number of such Pokemons:", len(pow_330))
# Top 10 adamant Pokets
print(pow_330.loc[:,'Name'].head(10))
 




