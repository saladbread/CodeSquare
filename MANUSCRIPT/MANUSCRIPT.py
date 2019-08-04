def MANUSCRIPT():
    root=os.getcwd()
    subdir=root+"/"+"MANUSCRIPT"
    os.chdir(subdir)
    f=open("A20190731.tex","w")
    sss=r'''\documentclass[14pt,aspectratio=169]{article}
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

    sss=r'''
\begin{document}
\maketitle
''' 
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
    os.system("pdflatex A20190731.tex")
    os.system("open A20190731.pdf")
    os.chdir(root)
   
GUI_TYPE="Button"
GUI_TEXT="MANUSCRIPT"
GUI_COMMAND="MANUSCRIPT"
