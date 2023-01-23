import os
import yaml

indices = {}

for filename in os.listdir("master_list"):
    if not filename.endswith(".yaml"):
        continue
    o = yaml.load(open("master_list/"+filename).read())
    name = o["name"]
    if "project" in o:
        url = o["project"]
    elif "website" in o:
        url = o["website"]
    else:
        continue
    if not o["tags"]:
        continue
    for t in o["tags"]:
        if t not in indices:
            indices[t] = []
        indices[t].append((name, url))

for key in indices:
    skey = str(key)
    if not os.path.exists("index/" + skey):
        os.mkdir("index/" + skey)
    f = open("index/" + skey + "/README.md", "w")
    f.write("# " + skey + "\n\n")
    for (name,url) in indices[key]:
        f.write("[" + name + "](" + url + ")\n")

home = open("README.md","w")
home.write("# Compilers Index\n")
home.write("A manually curated list of Open Source compilers and infrastructure components. ")
home.write("This project is an evolution of my personal star/list usage patterns on Github.\n\n")

for key in indices:
    skey = str(key)
    home.write("[" + skey + "](https://github.com/andrew-johnson-4/CompilersIndex/tree/main/index/" + skey + "#readme)\n")
