

import plotly.graph_objects as go
play1_path = r"C:\Users\FMiguens26\Downloads\playwithboys1.txt"  
play2_path = r"C:\Users\FMiguens26\Downloads\playwithboys2.txt"
non_descriptive = ["he", "to", "and", "for", "and", "nor", "thee", "thy", "but", "when", "from", "more", "enter", "am", "my", "in", "macb.", "his", "our", "haue", "he", "be", "the", "of", "i", "a", "that", "is", "you", "with", "not", "all", "thou", "they", "it", "your", "have", "this", "what", "as", "we", "which", "me", "so", "do", "on", "no", "[enter", "him", "at", "by", "will", "th", "if", "yet", "shall", "upon", "her", "are", "hath", "their", "first", "was", "would", "good", "should", "like", "us", "th'", "did", "make", "or", "must", "i'll", "'tis", "let", "who", "where", "now", "how", "had", "an", "come", "them", "great", "know", "say", "may", "than", "scene", "=======", "second", "[they", "exit.]", "see", "were", "o", "she", "o,", "then", "here"]
shakespeare_play = input('Which play do you want to graph?')
if shakespeare_play == "1":
    file = open(play1_path)
if shakespeare_play == "2":
    file = open(play2_path)
counts = {}
for line in file:
    words = line.split()
    for word in words:
        word = word.lower()
        if word in non_descriptive: continue
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
final_play1 = sorted(counts.items(), key=lambda x:x[1], reverse = True)
print(counts) 

final_play1 = final_play1[:10]
final_play1 = dict(final_play1)
top_values = final_play1.values()
top_labels = final_play1.keys()


labels = []
values = [30, 40, 20, 10]


fig = go.Figure(data=[go.Pie(labels=list(top_labels), values=list(top_values))])
fig.update_layout(title='Shakespeare word count')
fig.show()
