import pandas as pd
import matplotlib.pyplot as plt
import re

df = pd.read_csv('survey.csv')



#Bar Chart --------------------------------------------------------------------------------------------------------------------

barChartCols = {  
                    'Age': 'Age', 
                    'What area of study are you in?': 'What area of study are you in?', 
                }

plt.subplots_adjust(left=0.15, bottom=0.25)

for i,j in barChartCols.items():
    temp1 = df[i].value_counts().sort_index()

    temp1.plot(kind='bar', color='black', legend=None, title=i, xlabel="", ylabel="count")
    filename = re.sub('[^\w\-_\. ]', '', j)

    plt.savefig(f"output/{filename}.png")
    plt.clf()

#Multiple choice Bar Charts ---------------------------------------------------------------------------------------------------

multiBarChartCols = ['What do you do when you do not understand a topic and need a better explanation?', 'What do you use ChatGPT for?']  

plt.subplots_adjust(left=0.27, bottom=0.2, right=0.73, top=0.8)

for i in multiBarChartCols:
    df[i + '_'] = df[i].str.split(';')

    exploded = df.explode(i + '_')[i + '_'].value_counts().sort_index()

    plt.barh(exploded.index, exploded.values, color='black')
    plt.xlabel('',)
    plt.ylabel('count', fontsize=16, fontweight='bold')


    if i == 'What do you do when you do not understand a topic and need a better explanation?':
        plt.title('What recources do you use learn a new topic?')
    else:
        plt.title(i)

    filename = re.sub('[^\w\-_\. ]', '', i)

    fig = plt.gcf()
    fig.set_size_inches(12, 8)
    plt.savefig(f"output/{filename}.png")

    plt.clf()

#Pie Charts -------------------------------------------------------------------------------------------------------------------

pieChart = ['Gender', 'What is your ethnicity?', 'Did either of your parents/legal guardian attend college/university?', 'What area of study are you in?','Have you used ChatGPT before?','Do you believe that ChatGPT is beneficial to students? ','Do you think ChatGPT is plagiarism in and of itself?', 'Would the use of AI tools such as ChatGPT inhibit education?']

for i in pieChart:
    entry = df[i].value_counts()

    fig, ax = plt.subplots()
    wedges, texts, autotexts = ax.pie(entry, autopct="%1.1f%%", startangle=90, colors=['#232133', '#4a2f51', '#7c3962', '#b04363', '#dc5656', '#000000'] , textprops={"color": "white", "fontsize": 16})
    
    ax.axis("equal")  
    
    legend = ax.legend(wedges, entry.index, bbox_to_anchor=(.18, 0.1), loc="lower right", ncol=1, fontsize=12)
    # legend = ax.legend(wedges, entry.index, title=i, bbox_to_anchor=(.26, 0.1), loc="lower right", ncol=1)

    plt.title(i, y=1.05, fontdict={'fontsize': 18, 'fontweight': 'bold'})

    fig = plt.gcf()
    fig.set_size_inches(12, 11)
    
    filename = re.sub('[^\w\-_\. ]', '', i)
    plt.savefig(f"output/{filename}.png")


    