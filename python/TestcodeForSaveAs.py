from sys import platform as _platform
import sgtk


if _platform == "win32":
	ProjectPath= "W:\WG\Shotgun_Configs\RTS_Master"
   
elif _platform == "linux" or _platform == "linux2":
	ProjectPath="/srv/projects/rts/WG/Shotgun_Configs/RTS_Master"
   
else:
	ProjectPath= "W:\WG\Shotgun_Configs\RTS_Master"

tk = sgtk.sgtk_from_path(ProjectPath)

scenePath = cmds.file(q=True,sceneName=True)
scene_template = tk.template_from_path(scenePath)
flds = scene_template.get_fields(scenePath)

def defaultSavePush(*args):
	print 'Button save was pushed.'

def defaultCancelPush(*args):
	print 'Button Cancel was pushed.'
   
def defaultTestPush(*args):
	res = flds['Resolution']
	rb0 = cmds.radioButton(btn01, q = True, sl = True)
	rb1 = cmds.radioButton(btn02,q = True, sl = True)
	rb2 = cmds.radioButton(btn03,q = True, sl = True)
	if (rb0 == True):
		flds['Resolution'] = "hir"
		Newfile_path= scene_template.apply_fields(flds)
	if (rb1 == True):
		flds['Resolution'] = "low"
		Newfile_path= scene_template.apply_fields(flds)
	if (rb2 == True):
		flds['Resolution'] = "lay"
		Newfile_path= scene_template.apply_fields(flds)
	print flds['Resolution']
	print Newfile_path

   
windowName = "SaveAsResolution"

if cmds.window(windowName, q=True, exists=True ):
	cmds.deleteUI(windowName)
   
myWindow = cmds.window(windowName, title="SaveAndChooseResolution")



cmds.columnLayout( adjustableColumn=True )
label01 = cmds.text( label= flds['Resolution'])
collection = cmds.radioCollection('res')
btn01 = cmds.radioButton( label='high' )
btn02 = cmds.radioButton( label='low' )
btn03 = cmds.radioButton( label='lay' )
cmds.showWindow(myWindow)
res = flds['Resolution']

cmds.button(label="SAVE", width=100, command=defaultSavePush)
cmds.button(label="Cancel", width=100, command=defaultCancelPush)
cmds.button(label="TEST", width=100, command=defaultTestPush)

#----------------------------------------------------------------------

flds['Resolution'] = res
Newfile_path= scene_template.apply_fields(flds)
print Newfile_path