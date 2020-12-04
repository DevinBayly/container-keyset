import os
import yaml

all_files = []
for pth,sub,fls in os.walk("."):
    for fl in fls:
        if ".ks" in fl:
            all_files.append(f"{pth}/{fl}")
            all_files.append(f"{pth}/{fl.split('.')[0]}.yaml")

print(all_files)
## organize the list of files 
as_dict ={}

for f in all_files:
    ## belief is that the structure of all elements is ./{onealpha}/ {name} /{.ks} or {.yaml}
    _,alpha,name,fname = f.split("/")
    ## skip the 2 first chars of the f for appending in the weburl
    web_url = f"https://raw.githubusercontent.com/DevinBayly/container-keyset/main/{f[2:]}"
    as_dict.setdefault(name,[]).append(dict(name=name,relative_path=f,web_url=web_url))
print(yaml.dump(all_files))
print(yaml.dump(as_dict))

with open("manifest.yaml","w") as phile:
    phile.write(yaml.dump(as_dict))

