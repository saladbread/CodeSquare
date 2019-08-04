def MYINPUT(f,iflag):
    stitle='Introduction'
    if iflag==0:
       sss=r'''\item '''+stitle
       f.write(sss)

    if iflag==1:
       sss=r'''
\begin{frame}
\frametitle{'''+stitle+r'''}
\begin{itemize}'''
       f.write(sss)
       root=os.getcwd()
       subdir=root+"/"+"S4TOPIC"
       arr=[ff for ff in os.listdir(subdir) if os.path.isdir(subdir+"/"+ff)]
       arr=sorted(arr)
       for dirs in arr:
           filename=os.path.join(subdir,dirs)+"/"+dirs+".py"
           exec(open(filename).read(),globals())
           exec('MYINPUT2(f,0)')
       sss=r'''
\end{itemize}
\end{frame}
'''
       f.write(sss)

       for dirs in arr:
           filename=os.path.join(subdir,dirs)+"/"+dirs+".py"
           exec(open(filename).read(),globals())
           exec('MYINPUT2(f,1)')
