f=open("C:\\Users\\HELEN VIJU\\OneDrive\\Documents\\OneDrive\\Documents\\PYTHON\\FUNDAMENTALS\\file_program\\news.txt","r")
# word_lst=[]
# for line in f:
#     words=line.strip("\n").split(" ")
#     for w in words :
#         word_lst.append(w)
#print(word_lst)



word_lst=[w for line in f for w in line.rstrip("\n").split(" ")]
wc={w:word_lst.count(w) for w in word_lst}
print(wc)


def get_value(key):
    return wc.get(key)
srt=sorted(wc,key=get_value,reverse=True)
print(srt)