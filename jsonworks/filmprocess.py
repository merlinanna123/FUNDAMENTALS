from json import load

f=open("C:\\Users\\HELEN VIJU\\OneDrive\\Documents\\OneDrive\\Documents\\PYTHON\\FUNDAMENTALS\\jsonworks\\film.json")

films =load(f)

for f in films:
    print(f.get("title"))