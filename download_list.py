import os, time
from ghapi.all import GhApi
api = GhApi()

for page in range(0,40):
    res = api.search.repos(q="compiler",sort="stars",order="desc",page=str(page))
    time.sleep(1)
    for item in res["items"]:
        name = item["name"]
        url = item["homepage"]
        html_url = item["html_url"]
        stars = item["stargazers_count"]
        topics = item["topics"]
        filename = "master_list/" + name.lower().replace(" ","_") + ".yaml"
        fp = open(filename,"w")
        fp.write("---\n")
        fp.write("name: " + name + "\n")
        if url:
            fp.write("website: " + url + "\n")
        fp.write("project: " + html_url + "\n")
        fp.write("tags:\n")
        for tag in topics:
            fp.write("- " + tag + "\n")
