def SLIDE_GEN():
    root=os.getcwd()
    subdir=root+"/"+"SLIDE_GEN"
    os.chdir(subdir)
    f=open("SLIDE.tex","w")
    sss=r'''\documentclass[14pt,aspectratio=169]{beamer}
\usepackage{beamerthemesplit}
\usepackage{graphicx}
%\usepackage[3D]{movie15}
\usepackage{multimedia} %%% This is require pdfpc to show video
\begin{document}
'''
    f.write(sss)

    arr=['S0TITLE']
    for dirs in arr:
        filename=os.path.join(subdir,dirs)+"/"+dirs+".py"
        if (os.path.isfile(filename)):
           exec(open(filename).read(),globals())
           exec('MYINPUT(f,0)')

    arr=[ff for ff in os.listdir(subdir) if os.path.isdir(subdir+"/"+ff)]
    arr=sorted(arr)
    sss=r'''\begin{frame}
\frametitle{Outline}
\begin{itemize}
''' 
    f.write(sss)
    for dirs in arr:
        filename=os.path.join(subdir,dirs)+"/"+dirs+".py"
        if (os.path.isfile(filename)):
           exec(open(filename).read(),globals())
           if dirs!='S0TITLE':
              exec('MYINPUT(f,0)')
    sss=r'''
\end{itemize}
\end{frame}'''
    f.write(sss)

    for dirs in arr:
        filename=os.path.join(subdir,dirs)+"/"+dirs+".py"
        if (os.path.isfile(filename)):
           exec(open(filename).read(),globals())
           if dirs!='S0TITLE':
              exec('MYINPUT(f,1)')

    sss=r'\end{document}'
    f.write(sss)
    f.close()
    os.system("pdflatex SLIDE.tex")
    os.system("open SLIDE.pdf")
    os.chdir(root)
   
GUI_TYPE="Button"
GUI_TEXT="SLIDE-GEN"
GUI_COMMAND="SLIDE_GEN"
