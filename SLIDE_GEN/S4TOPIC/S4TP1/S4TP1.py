def MYINPUT2(f,iflag):
    stitle='Input Topic Here'
    if iflag==0:
       sss=r'''\item '''+stitle
       f.write(sss)

    if iflag==1:
       sss=r'''
\begin{frame}
\frametitle{'''+stitle+r'''}
Input Content Here.
\end{frame}
'''
       f.write(sss)
