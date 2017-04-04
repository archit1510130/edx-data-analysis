import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
from wordcloud import WordCloud,STOPWORDS


df=pd.read_csv('/home/archit/edx.csv',parse_dates=['Launch Date'])
df['year'] = df['Launch Date'].dt.year
#print(df.head())

#no_of_participents = df[['Institution',"Participants (Course Content Accessed)"]].groupby('Institution').sum()
#no_of_participents = no_of_participents.reset_index()
#sns.factorplot(x='Institution',y='Participants (Course Content Accessed)',kind='bar',data=no_of_participents)







#  no of participants  year based in per institution

'''no_of_participents=df[['Participants (Course Content Accessed)','Institution','year']].groupby(['Institution','year']).sum()
no_of_participents=no_of_participents.reset_index()
#data to plot
n_groups=5
harvard=no_of_participents['Participants (Course Content Accessed)'][:5]
mit=no_of_participents['Participants (Course Content Accessed)'][5:10]
#create plot
fig,ax=plt.subplots()
index=[1,2,3,4,5]
index2=[1.35,2.35,3.35,4.35,5.35]
bar_width=0.35
opacity=0.8

rec1=plt.bar(index,harvard,bar_width,alpha=opacity,color='b',label="harvard")
rec2=plt.bar(index2,mit,bar_width,alpha=opacity,color='g',label='mit')
plt.xlabel('year')
plt.ylabel('participents')
plt.xticks(index2,('2012','2013','2014','2015','2016'))
plt.legend(loc='upper left')
plt.show()
'''








#Comparison - Total number of Participants, Total number of Participants > 50% Course Content Accessed and Certified
no_of_participents = df[['Institution',"Participants (Course Content Accessed)","Audited (> 50% Course Content Accessed)","Certified",'year']].groupby(['Institution','year']).sum()
print(no_of_participents)
no_of_participents=no_of_participents.reset_index()
n_groups=5
harvard1=no_of_participents['Participants (Course Content Accessed)'][:5]
harvard2=no_of_participents['Audited (> 50% Course Content Accessed)'][:5]
harvard3=no_of_participents['Certified'][:5]
#create plot


fig,ax=plt.subplots()
index = np.arange(n_groups)

bar_width=.35
opacity=0.8
rec1=plt.bar(index,harvard1,bar_width,alpha=opacity,color='b',label='p')
rec2=plt.bar(index+bar_width,harvard2,bar_width,alpha=opacity,color='r',label='a')
rec3=plt.bar(index+bar_width+bar_width,harvard3,bar_width,alpha=opacity,color='k',label='c')

plt.xlabel('year')
plt.ylabel('comparison')
plt.xticks(index+bar_width,('2012','2013','2014','2015','2016'))
plt.legend(loc='upper left')
plt.title("harvard data")
plt.show()
#done

















# trying to put matplotlib bar plots
'''no_of_participents = df[['Institution',"Participants (Course Content Accessed)"]].groupby('Institution').sum()
no_of_participents = no_of_participents.reset_index()
print(no_of_participents)
#plt.bar(x=no_of_participents["Institution"],y=no_of_participents["Participants (Course Content Accessed)"])
x=[1,2]
y=no_of_participents['Participants (Course Content Accessed)']
lable=['harvard','mit']
plt.bar(x,y,align='center')
plt.xticks(x,lable)
plt.show()
'''
#done







#Most frequent course title with d help of matplotlib
'''#print(df['Course Title'])
course_title = df[['Course Title']].groupby('Course Title').size() #this give the size of each member of dat dataframe
wordcloud=WordCloud(stopwords=STOPWORDS,
                    background_color='white',
                    width=1200,
                    height=1000
                    ).generate(" ".join(df['Course Title']))# here a word string required like a whole para datsy we used joined

plt.imshow(wordcloud)
plt.show()'''
#done




#Number of course by Institution using matplotlib
'''
print(df.columns)
df1=df[['Institution','Course Number']].groupby('Institution').sum()
counts = df[['Institution','Course Number']].groupby(['Institution']).agg(len)
counts=counts.reset_index()
print(counts)
x=[1,2]
y=counts['Course Number']
label=['Harvard','MIT']
plt.bar(x,y,align='center')
plt.xticks(x,label)
plt.show()
'''
#done









