import pandas as pd
import matplotlib.pyplot as plt
import re

# Read in the data from the csv file and stored it as a pandas dataframe
df = pd.read_csv('survey.csv')

#Bar Chart --------------------------------------------------------------------------------------------------------------------

#Stores the column names and the title of the bar chart in a dictionary
barChartCols = {  
                    'Age': 'Age', 
                    'What area of study are you in?': 'What area of study are you in?', 
                }

#Adjust the spacing of the bar chart to fit the chart 
plt.subplots_adjust(left=0.15, bottom=0.25)

#loop through the dictionary and create a bar chart for each column present in the barChartCols dictionary
for i,j in barChartCols.items():
    #creates a new column with the values of the column sorted (this is so that columns are sorted in the bar chart)
    temp1 = df[i].value_counts().sort_index()
    #plots the bar chart while settings its title, x and y labels, color  
    temp1.plot(kind='bar', color='black', legend=None, title=i, xlabel="", ylabel="count")
    #Since the columns name may contain special characters, this will reromve themn and replace them with an nothing 
    filename = re.sub('[^\w\-_\. ]', '', j)
    #Saves the chart as a .png in the folder output
    plt.savefig(f"output/{filename}.png")
    #This is to ensure that the chart is cleard before each iteration of the loop
    plt.clf()

#Multiple choice Bar Charts ---------------------------------------------------------------------------------------------------

#Stores the column names and the title of the bar chart in a List
multiBarChartCols = ['What do you do when you do not understand a topic and need a better explanation?', 'What do you use ChatGPT for?']  

#Adjust the spacing of the bar chart to fit the chart 
plt.subplots_adjust(left=0.27, bottom=0.2, right=0.73, top=0.8)

#loop through the list and create a bar chart for each column present in the multiBarChartCols list
for i in multiBarChartCols:
    #Since this is a multiple choice question, the values are seperated by a semi-colon. So we need to split the values 
    df[i + '_'] = df[i].str.split(';')
    #Explodes the column so that each value is on its own row (Since we split the values)
    exploded = df.explode(i + '_')[i + '_'].value_counts().sort_index()

    #Plots the horizontal bar chart while settings its title, x and y labels, color, font size and font weight
    plt.barh(exploded.index, exploded.values, color='black')
    plt.xlabel('',)
    plt.ylabel('count', fontsize=16, fontweight='bold')

    #A condition to replace the long title with a shorter one in the list
    if i == 'What do you do when you do not understand a topic and need a better explanation?':
        plt.title('What recources do you use learn a new topic?')
    else:
        plt.title(i)

    #Since the columns name may contain special characters, this will remove themn and replace them with an nothing 
    filename = re.sub('[^\w\-_\. ]', '', i)

    #Adjust the spacing of the bar chart to fit the chart
    fig = plt.gcf()
    fig.set_size_inches(12, 8)

    #Saves the chart as a .png in the folder output
    plt.savefig(f"output/{filename}.png")

    plt.clf()

#Pie Charts -------------------------------------------------------------------------------------------------------------------

#Stores the column names and the title of the pie chart in a List
pieChart = ['Gender', 'What is your ethnicity?', 'Did either of your parents/legal guardian attend college/university?', 'What area of study are you in?','Have you used ChatGPT before?','Do you believe that ChatGPT is beneficial to students? ','Do you think ChatGPT is plagiarism in and of itself?', 'Would the use of AI tools such as ChatGPT inhibit education?']

#iterates through the list and creates a pie chart for each column present in the pieChart list
for i in pieChart:
    #Assign the values of the column to a variable 'entry'
    entry = df[i].value_counts()

    #Creates a pie chart with the values of the column, sets the colors, font size and font weight
    fig, ax = plt.subplots()
    wedges, texts, autotexts = ax.pie(entry, autopct="%1.1f%%", startangle=90, colors=['#232133', '#4a2f51', '#7c3962', '#b04363', '#dc5656', '#000000'] , textprops={"color": "white", "fontsize": 16})
    
    #Settings the aspect ratio of the pie chart to be equal
    ax.axis("equal")  
    
    #Adding legend to the pie chart while adding 'entry' from the column
    legend = ax.legend(wedges, entry.index, bbox_to_anchor=(.18, 0.1), loc="lower right", ncol=1, fontsize=12)

    #Sets the title of the pie chart
    plt.title(i, y=1.05, fontdict={'fontsize': 18, 'fontweight': 'bold'})

    #Adjust the spacing of the bar chart to fit the chart
    fig = plt.gcf()
    fig.set_size_inches(12, 11)

    #Since the columns name may contain special characters, this will remove themn and replace them with     
    filename = re.sub('[^\w\-_\. ]', '', i)
    plt.savefig(f"output/{filename}.png")


    