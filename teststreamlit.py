import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use("ggplot")
pd.options.display.max_columns = 200 
pd.options.display.float_format = '{:.3f}'.format

#IMPORT DF
link = 'https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv'

df = pd.read_csv(link)

#MY GRAPHS
mypiv = df.pivot_table(index='year', columns='continent', values=['weightlbs','time-to-60'], aggfunc='mean' )

#FIG OF ALL DB PAGE
fig1, axes = plt.subplots(2, 2, figsize=(20, 11))

ax = sns.heatmap(df.iloc[:,:-1].corr(),
                 center=True,
                 cmap="YlGnBu",
                 ax= axes [0,0])
ax.set_title("HEATMAP of correlations ", fontdict = {'family':'serif','color':'black','size':18})

ax = sns.boxplot(df,
             y = 'time-to-60',
             x = 'year',
             color = 'orange',
             showfliers = False,
             showmeans = True,
             meanprops = {"marker":"s","markerfacecolor":"white", "markeredgecolor":"blue"},
             ax = axes [1,0])
ax.set_title("Time-to-60 over years distribution", fontdict = {'family':'serif','color':'black','size':18})

ax = sns.scatterplot(df,
                y = 'time-to-60',
                x = 'weightlbs',
                hue = 'continent',
                palette = ['red', 'green', 'blue'],
                ax= axes [0,1])
ax.set_title("Correlations between time-to-60 and weights of cars, depending of regions", fontdict = {'family':'serif','color':'black','size':18})

ax = sns.histplot(df,
             x = 'mpg',
             hue = 'continent',
             palette = ['red', 'green', 'blue'],
             multiple = 'stack',
             ax = axes [1,1]
             )
ax.set_title("Miles Per Gallon histogram", fontdict = {'family':'serif','color':'black','size':18})

#FIG OF EUROPE PAGE

fig2, axes = plt.subplots(1, 2, figsize=(15, 11))

plt.subplot(1, 2, 1)
ax = sns.lineplot(mypiv,
             x = 'year',
             y = ('time-to-60', ' Europe.'),
             color= 'green')
ax.set_title("means of cars time-to-60 in Europe over years", fontdict = {'family':'serif','color':'black','size':18})

plt.subplot(1, 2, 2)
ax = sns.lineplot(mypiv,
             x = 'year',
             y = ('weightlbs', ' Europe.'),
             color= 'green')
ax.set_title("means of cars weight(lbs) in Europe over years", fontdict = {'family':'serif','color':'black','size':18})

#FIG OF JAPAN PAGE

fig3, axes = plt.subplots(1, 2, figsize=(15, 11))

plt.subplot(1, 2, 1)
ax = sns.lineplot(mypiv,
             x = 'year',
             y = ('time-to-60', ' Japan.'),
             color= 'blue')
ax.set_title("means of cars time-to-60 in Japan over years", fontdict = {'family':'serif','color':'black','size':18})

plt.subplot(1, 2, 2)
ax = sns.lineplot(mypiv,
             x = 'year',
             y = ('weightlbs', ' Japan.'),
             color= 'blue')
ax.set_title("means of cars weight(lbs) in Japan over years", fontdict = {'family':'serif','color':'black','size':18})

#FIG OF US PAGE

fig4, axes = plt.subplots(1, 2, figsize=(15, 11))

plt.subplot(1, 2, 1)
ax = sns.lineplot(mypiv,
             x = 'year',
             y = ('time-to-60', ' US.'),
             color= 'red')
ax.set_title("means of cars time-to-60 in US over years", fontdict = {'family':'serif','color':'black','size':18})

plt.subplot(1, 2, 2)
ax = sns.lineplot(mypiv,
             x = 'year',
             y = ('weightlbs', ' US.'),
             color= 'red')
ax.set_title("means of cars weight(lbs) in US over years", fontdict = {'family':'serif','color':'black','size':18})

#MY API

st.title("CARS ANALYSIS")

options = st.selectbox(
    'Which analysis would you see ?',
    ('ALL DB', 'Europe', 'Japan', 'US'),
    index=None
)
st.write('You selected:', options, 'analysis')

if options == 'ALL DB':
    st.pyplot(fig1.figure)
    st.write('Very beautiful, isnt it ?')
elif options == 'Europe' :
    st.pyplot(fig2.figure)
elif options == 'Japan' : 
    st.pyplot(fig3.figure)
elif options == 'US' :
    st.pyplot(fig4.figure)