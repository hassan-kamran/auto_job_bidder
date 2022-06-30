import requests as r
import selenium as s

url = 'https://www.freelancer.pk/search/projects?projectSort=latest&projectLanguages=en'

cred = {}
with open('./credentials.txt', 'r') as f:
    for lines in f:
        cred[lines.split(':')[0]] = lines.split(':')[1].strip()
print(cred)
