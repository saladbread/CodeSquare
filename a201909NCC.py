csq_import=["os","sys","tkinter"]
for ccy in csq_import:
    exec("import "+ccy)

root=os.getcwd()
arr=[ccy for ccy in os.listdir(root) if os.path.isdir(root+"/"+ccy)]
arr=sorted(arr)

win=tkinter.Tk()
win.geometry('300x400')
nnn=0
NRC=3
for dirs in arr:
    filename=os.path.join(os.getcwd(),dirs)+"/"+dirs+".py"
    if (os.path.isfile(filename)):
       try:
           os.chdir(os.path.join(os.getcwd(),dirs))
           exec(open(filename).read(),globals())
           if GUI_TYPE=="Button":
              cmd="w=tkinter."+GUI_TYPE+"(win,text='"+GUI_TEXT+"',width=10,command="+GUI_COMMAND+")"
              exec(cmd)
              ''' exec("w.pack(side=tkinter.LEFT)") '''
              exec("w.grid(row=nnn//NRC,column=nnn%NRC)")
              nnn=nnn+1
           if GUI_TYPE=="Label":
              exec(GUI_TYPE+GUI_TEXT+"=tkinter."+GUI_TYPE+"(win,width=10)")
              ''' exec(GUI_TYPE+GUI_TEXT+".pack(side=tkinter.LEFT)") '''
              exec(GUI_TYPE+GUI_TEXT+".grid(row=nnn//NRC,column=nnn%NRC)")
              nnn=nnn+1
              if len(GUI_COMMAND)>0:
                 exec(GUI_COMMAND+"()")
           os.chdir("..")
       except:
           print("An exception occurred in "+os.getcwd())
    else:
       print("There is no "+filename)

win.mainloop()
