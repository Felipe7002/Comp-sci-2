#Author: Felipe Miguens
#Date: 3/30/24
#Discription: This code gives you the option to graph two shakespeare plays. After chosing which play you want to graph it will give you the ten most used words in the play.
#Bugs: no bugs

import plotly.graph_objects as go
#the two shakespeare plays
play1_path = r"C:\Users\FMiguens26\Downloads\playwithboys1.txt"  
play2_path = r"C:\Users\FMiguens26\Downloads\playwithboys2.txt"
#the non descriptive words that should be removed from the play when graphing the top ten words
non_descriptive = ["he", "to", "and", "for", "and", "nor", "thee", "thy", "but", "when", "from", "more", "enter", "am", "my", "in", "macb.", "his", "our", "haue", "he", "be", "the", "of", "i", "a", "that", "is", "you", "with", "not", "all", "thou", "they", "it", "your", "have", "this", "what", "as", "we", "which", "me", "so", "do", "on", "no", "[enter", "him", "at", "by", "will", "th", "if", "yet", "shall", "upon", "her", "are", "hath", "their", "first", "was", "would", "good", "should", "like", "us", "th'", "did", "make", "or", "must", "i'll", "'tis", "let", "who", "where", "now", "how", "had", "an", "come", "them", "great", "know", "say", "may", "than", "scene", "=======", "second", "[they", "exit.]", "see", "were", "o", "she", "o,", "then", "here"]
shakespeare_play = input('Which play do you want to graph?')
if shakespeare_play == "1":
    file = open(play1_path)
if shakespeare_play == "2":
    file = open(play2_path)
counts = {}
#turns words to lowercase and breaks up the words by a space. Then the words get added to a dictionary along with a count for how many times they are said
for line in file:
    words = line.split()
    for word in words:
        word = word.lower()
        if word in non_descriptive: continue
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
#sorts the words from lowest count to highest count then reverses it
final_play1 = sorted(counts.items(), key=lambda x:x[1], reverse = True)
print(counts) 
#takes top ten words
final_play1 = final_play1[:10]
final_play1 = dict(final_play1)
top_values = final_play1.values()
top_labels = final_play1.keys()


labels = []
values = [30, 40, 20, 10]

#creats the pie charts in plotly and titals the pie chart shakespeare word count
fig = go.Figure(data=[go.Pie(labels=list(top_labels), values=list(top_values))])
fig.update_layout(title='Shakespeare word count')
fig.show()

