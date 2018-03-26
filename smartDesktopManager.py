import os, shutil

def moveFile(src,dest,i,ext):
    try:
        myflag=True
        while os.path.isfile(dest):
            if myflag:
                tempName=dest.replace(ext,'')

                myflag=False
            else:
                tempName=dest.replace(ext,'')
                tempName=dest[:-3]

            dest=tempName+'('+str(i)+').pdf'
            i=i+1
        shutil.copy(src,dest)
    except FileExistsError:
        print('in except block')
        i=1+1
        moveFile(src,dest,i)

desktop='C:\\Users\\Anup\\Desktop'
pdfs='C:\\Users\\Anup\\Documents\\PDFs'
if os.path.exists('C:\\Users\\Anup\\Documents\\PDFs'):
    print('Folder found')
else:
    os.mkdir(pdfs)
    print('Folder Created!!')

print('-------------------------------------------------------------')
files=os.listdir(desktop)
for file in files:
    if '.pdf' in str(file):
        i=0
        fname=desktop+'\\'+str(file)
        target=pdfs+'\\'+str(file)
        moveFile(fname,target,i,'.pdf')
#    if '.pptx' or '.docx' in str(file):
#        print('PPTs and Word files found!!')


movedFiles=os.listdir(pdfs)
for pdf in movedFiles:
    print(str(pdf))
