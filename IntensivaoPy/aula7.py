c=["magali", 55, 1500, 84, "T", "vhs", "br", "pt"]
itC=iter(c)

while itC:
    try:
        print(next(itC))
    except StopIteration:
        print("fim")
        break