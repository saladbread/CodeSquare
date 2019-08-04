csq_import=["datetime"]
for ccy in csq_import:
    exec("import "+ccy)

def cmdCLOCK():
    GUI_TYPE="Label"
    GUI_TEXT="CLOCK"
    GUI_COMMAND="cmdCLOCK"
    var="global "+GUI_TYPE+GUI_TEXT
    exec(var)
    string='Time : '+datetime.datetime.now().strftime('%H:%M')
    cmd=GUI_TYPE+GUI_TEXT+".config(text=string)"
    exec(cmd)
    cmd=GUI_TYPE+GUI_TEXT+".after(1000,cmdCLOCK)"
    exec(cmd)

GUI_TYPE="Label"
GUI_TEXT="CLOCK"
GUI_COMMAND="cmdCLOCK"
