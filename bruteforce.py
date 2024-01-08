import requests
r = requests.get("https://gvpt.sk/sk/", auth=("user", "pass"))
fw= open ("bordel.txt", "w", encoding="UTF-8")
page=r.text
zob=True
for i in page:
    if i =="<":
        zob=False
    elif i ==">":
        zob=True
    elif zob:
        if not i=="/n":
            fw.write()

