import urllib.request
import urllib.error
import re
import json

# "title"Jason Leinster - IMDb"url"7https://www.imdb.com/name/nm0500493/?ref_=ttfc_fc_cr550"

pattern = "\".title\".*IMDb\"\Surl\"..*\""
filename = '039885.log'
returnList = []
with open(filename, 'r', encoding='iso-8859-1') as readfile:
    for line in readfile:
        match1 = re.findall(pattern, line, re.IGNORECASE | re.DOTALL)
        if match1:
            returnList.append(match1)

for match in returnList:
    patternname = "title\".*IMDB\""
    name = str(re.findall(patternname, str(match), re.IGNORECASE | re.DOTALL))[13:-10]

    patternurl = "url\"..*\""
    url = str(re.findall(patternurl, str(match), re.IGNORECASE |
                     re.DOTALL))[15:-19]

    print(name)
    print(url)

linkedinurl = 'https://api.linkedin.com/v1/people/{}?format=json'

jsonlist = []
with open("outputnames.txt", "r") as output:
    for names in output:
        newurl = linkedinurl.format("+".join(names.split()))
        print(newurl)
        with urllib.request.urlopen(newurl) as url_file:
            json = url_file.read().json()
            jsonlist.append(json)

    print(jsonlist)


