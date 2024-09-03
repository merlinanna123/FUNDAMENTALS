f_read=open("C:\\Users\\HELEN VIJU\\OneDrive\\Documents\\OneDrive\\Documents\\PYTHON\\FUNDAMENTALS\\file_program\\years.txt","r")
f_century=open("C:\\Users\\HELEN VIJU\\OneDrive\\Documents\\OneDrive\\Documents\\PYTHON\\FUNDAMENTALS\\file_program\\century","w")
f_non_century=open("C:\\Users\\HELEN VIJU\\OneDrive\\Documents\\OneDrive\\Documents\\PYTHON\\FUNDAMENTALS\\file_program\\non_century","w")
for year in f_read:
    y=int(year.rstrip("\n"))
    if y%100==0:
        f_century.write(str(y)+"\n")
    else:
        f_non_century.write(str(y)+"\n")