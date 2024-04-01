

play1_path = r"C:\Users\FMiguens26\Downloads\playwithboys1.txt"  
play2_path = r"C:\Users\FMiguens26\Downloads\playwithboys2.txt"
non_descriptive= ["a", "the", "of", "I", "or", "and", "to"]
shakespeare_play = input('Which play do you want to graph?')
if shakespeare_play == "1":
    file = open(play1_path)
if shakespeare_play == "2":
    file = open(play2_path)
counts = {}
for line in file:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)

labels = []
values = [30, 40, 20, 10]

import plotly.graph_objects as go
fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.update_layout(title='Shakespeare word count')
fig.show()

