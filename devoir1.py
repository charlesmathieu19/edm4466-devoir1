# coding : utf-8

campus = []
for m in range(20000, 30151):
    url = 'https://montrealcampus.ca?p={}'.format(m)
    campus.append(url)
print(*campus, sep='\n')
print(type(campus), len(campus))
