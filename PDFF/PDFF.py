def cmdOpen(a):
    from PyPDF2 import PdfFileReader
    pdf_toread=PdfFileReader(open(a,"rb"))
    pdf_info=pdf_toread.getDocumentInfo()
    print(str(pdf_info))
    os.system("open "+a)

def cmdPDFF():
    thisdir=os.getcwd()
    numPDF=0
    for r,d,f in os.walk(thisdir):
        for file in f:
            if ".pdf" in file:
               numPDF=numPDF+1
    if numPDF>0:
       win2=tkinter.Toplevel()
       for r,d,f in os.walk(thisdir):
           for file in f:
               if ".pdf" in file:
                    w=tkinter.Button(win2,text=file,command=lambda a=os.path.join(r,file):cmdOpen(a))
                    w.pack()
GUI_TYPE="Button"
GUI_TEXT="ALL-PDF"
GUI_COMMAND="cmdPDFF"
