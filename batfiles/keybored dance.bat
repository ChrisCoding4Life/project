Set wshell = wscript.creatObject("WScript.shell")
do
wshcript.sleep 100
wshell.sendkeys "{CAPSLOCK}"
wshell.sendkeys "{NUMLOCK}"
wshell.sendkeys "{STROLLLOCK}"
loop