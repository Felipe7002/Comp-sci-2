
play1_path = r"C:\Users\FMiguens26\Downloads\playwithboys1.txt"  
play2_path = r"C:\Users\FMiguens26\Downloads\playwithboys2.txt"
non_descriptive= ["a", "the", "of", "I", "or", "and", "to"]
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
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
fig.update_layout(title='Fruit Distribution')
fig.show()
