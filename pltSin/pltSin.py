def cmdPltSin():
    import numpy as np
    import matplotlib.pyplot as plt

    x=np.arange(0,4*np.pi,0.1)
    y=np.sin(x)
    plt.plot(x,y)
    plt.show()
    

GUI_TYPE="Button"
GUI_TEXT="Sin(x)"
GUI_COMMAND="cmdPltSin"
