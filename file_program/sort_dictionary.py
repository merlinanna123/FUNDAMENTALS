placements={"django":28,"stack":45,"asp.net":36,"c++":25}
def get_value(key):
    return placements.get(key)
srt=sorted(placements,key=get_value,reverse=True)
print(srt)