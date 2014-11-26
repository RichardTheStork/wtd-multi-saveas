# Copyright (c) 2013 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

import sgtk
import os
import sys
import threading
import maya.cmds as cmds

# by importing QT from sgtk rather than directly, we ensure that
# the code will be compatible with both PySide and PyQt.
from sgtk.platform.qt import QtCore, QtGui
from .ui.SaveAsResolution import Ui_SaveAsResolution


def show_dialog(app_instance):
	"""
	Shows the main dialog window.
	"""
	# in order to handle UIs seamlessly, each toolkit engine has methods for launching
	# different types of windows. By using these methods, your windows will be correctly
	# decorated and handled in a consistent fashion by the system. 
	
	# we pass the dialog class to this method and leave the actual construction
	# to be carried out by toolkit.
	resolution = app_instance.get_setting("target_resolution")
	print resolution
	app_instance.engine.show_dialog("Save as %s" %resolution, app_instance, AppDialog)
	

class AppDialog(QtGui.QWidget):
	"""
	Main application dialog window
	"""
	
	def __init__(self):
		"""
		Constructor
		"""
		# first, call the base class and let it do its thing.
		QtGui.QWidget.__init__(self)
		
		# now load in the UI that was created in the UI designer
		self.ui = Ui_SaveAsResolution() 
		self.ui.setupUi(self)
		
		# most of the useful accessors are available through the Application class instance
		# it is often handy to keep a reference to this. You can get it via the following method:
		self._app = sgtk.platform.current_bundle()
		
		# via the self._app handle we can for example access:
		# - The engine, via self._app.engine
		# - A Shotgun API instance, via self._app.shotgun
		# - A tk API instance, via self._app.tk 
		
		# lastly, set up our very basic UI
		self.ui.label_workArea.setText("WorkArea: %s" % self._app.context)
		
		self.resolution = self._app.get_setting("target_resolution")
		self.resolutionShort = self._app.get_setting("target_resolution_shortname")
		self.ui.groupBox_SaveAs.setTitle("Save as %s" % self.resolution)
		
		"""TODO thomas"""
		NewFileName = self.NewFileName()
		self.filename = str(os.path.basename(NewFileName))
		self.filepath = str(os.path.dirname(NewFileName))
		self.ui.label_fileName.setText("Filename: %s" % self.filename)
		self.ui.label_filePath.setText("Filepath: %s" % self.filepath)
		
		QtCore.QObject.connect(self.ui.pushButton_save, QtCore.SIGNAL('clicked()'), self.save_click)
		QtCore.QObject.connect(self.ui.pushButton_changeArea, QtCore.SIGNAL('clicked()'), self.change_workarea_click)
		QtCore.QObject.connect(self.ui.pushButton_cancel, QtCore.SIGNAL('clicked()'), self.cancel_click)
		self.ui.pushButton_changeArea.hide()
		
	def NewFileName(self):

		scenePath = cmds.file(q=True,sceneName=True)
		
		if scenePath:
			tk = sgtk.sgtk_from_path(scenePath)
			tk = self._app.sgtk
			scene_template = tk.template_from_path(scenePath)
			flds = scene_template.get_fields(scenePath)

			
			print "Click save"
			currCTXT = self._app.context
			newTemplateName = str(scene_template.name).replace("publish","work")
			newTemplate = self._app.get_template_by_name(newTemplateName)
			
			if not newTemplate:
				print "ERROR : %s is not existing template!" %newTemplateName
				return None
				
			flds['Step'] = currCTXT.as_template_fields(newTemplate)["Step"]
			
			pathCTXT = tk.context_from_path(scenePath)
			
			flds['Resolution'] = self.resolutionShort
			Newfile_path = newTemplate.apply_fields(flds)
			
			print "*"*20
			print scene_template
			print flds
			print "Scenepath = %s" %scenePath
			print "New file  = %s" %Newfile_path
			print "*"*20
			
			if currCTXT != pathCTXT:
				print currCTXT
				print pathCTXT
				print "ctxts differents"
				
			else:
				print "same ctxt"
			
			print "*"*20
			
			if Newfile_path:
				flds['version']+=1
				Newfile_path = newTemplate.apply_fields(flds)
				return Newfile_path
			else:
				print Newfile_path
				return Newfile_path
			# cmds.file(rename=Newfile_path)		
		else:
			flds ={}
			print 'pas de nom'
			currCTXT = self._app.context
			# test= self._app.get_setting("sg_entity_types", [])
			# print test
			print currCTXT
			tk = self._app.sgtk
			maya_asset_work_template = tk.templates["maya_asset_work"]
			print maya_asset_work_template
			newTemplate = self._app.get_template_by_name(maya_asset_work_template.name)
			flds["Asset"] = currCTXT.as_template_fields(newTemplate)["Asset"]
			flds["sg_asset_type"] = currCTXT.as_template_fields(newTemplate)["sg_asset_type"]
			# print test2
			flds['Step'] = currCTXT.as_template_fields(newTemplate)['Step']
			flds['version'] = 001
			flds['Resolution'] = self.resolutionShort
			print flds
			Newfile_path = newTemplate.apply_fields(flds)
			if Newfile_path:
				flds['version']= currCTXT.as_template_fields(newTemplate)["Asset"]
				flds['version']+=1
				Newfile_path = newTemplate.apply_fields(flds)
				return Newfile_path
			else:
				print Newfile_path
				return Newfile_path
			# return Newfile_path
			
			
	def reset_workarea(self):
		print 'todo'
		
	def save_click(self):

		NewName = self.NewFileName()
		cmds.file(rename=NewName)
		cmds.file(save=True)
		self.destroy_app()
				
	def change_workarea_click(self):
		print "Click change"
		# print self._app.engine._Engine__applications["tk-multi-workfiles"].init_app()
		# print dir(self._app.engine._Engine__applications["tk-multi-workfiles"])
		# print sgtk.engine.apps["tk-multi-workfiles"]
		
		print dir(sgtk)
		print dir(self)
		print dir(self._app)
		"""print dir(self)
		print dir(self._app)
		# print dir(self._app.engine)
		print dir(self._app.engine._Engine__applications)
		print self._app.engine._Engine__applications
		# print self._app.engine.apps
		print self._app.engine._Engine__applications["tk-maya-breakdown"]
		# print dir(self._app.engine._Engine__applications["tk-multi-workfiles"])
		# print self._app.engine.apps["tk-multi-about"]
		print 'OK...'"""
		
	def cancel_click(self):
		self.destroy_app()
		
	def destroy_app(self):
		# self.parent.log_debug("Destroying Save as...")
		print self.close()
