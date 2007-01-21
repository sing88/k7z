"""
K7Z: Basic Archiver
Designed by Chris Giles

File:		Main.py
Purpose:	Controller
"""


### Imports

# K7Z 1
import	Import
import	Help, Input, Profile, Settings, Thread

# Python
try :
	import	sys
except :
	Import.slException( "Python" )

# PyQt4
try :
	from	PyQt4	import QtCore, QtGui
except :
	Import.slException( "PyQt4" )

# K7Z 2
try :
	from	Main_ui			import Ui_Main
	from	Main_rc			import *
	from	Settings_ui		import Ui_Settings
	from	Settings_rc		import *
except :
	Import.slException( Settings.sAppName )


### Variables

# Main
aMain			= QtGui.QApplication(sys.argv)
mwMain			= QtGui.QMainWindow()
uiMain			= Ui_Main()
uiMain.setupUi(mwMain)

# Settings
dSettings		= QtGui.QDialog()
uiSettings		= Ui_Settings()
uiSettings.setupUi(dSettings)


### Slots

# Choose the source creation directory
def slCGetSDir() :
	uiMain.leSDir.setText( QtGui.QFileDialog.getExistingDirectory( None , "" , uiMain.leSDir.displayText() ) )

# Choose the source extraction archive
def slEGetSArc() :
	dOutput = QtCore.QDir()
	dOutput.setPath( uiMain.leArchive.displayText() )
	uiMain.leArchive.setText( QtGui.QFileDialog.getOpenFileName( None , "" , dOutput.path() ,
		"Archives (*.exe *.7z *.bz2 *.zip *.rpm *.deb *.gz *.tar *.cab *.arj *.cpio *.rar *.chm *.iso *.lzh *.lha *.nsi *.z *.001)" ) )

# Choose the destination creation directory
def slCGetDDir() :
	uiMain.leCDDir.setText( QtGui.QFileDialog.getExistingDirectory( None , "" , uiMain.leCDDir.displayText() ) )

# Choose the destination extraction directory
def slEGetDDir() :
	uiMain.leEDDir.setText( QtGui.QFileDialog.getExistingDirectory( None , "" , uiMain.leEDDir.displayText() ) )


# Enable or disable items
def slToggles() :

	# Line Edits
	uiMain.leCName.setEnabled( uiMain.cbCName.isChecked() )
	uiMain.leCPassword.setEnabled( uiMain.cbCPassword.isChecked() )
	uiMain.leEName.setEnabled( uiMain.cbEName.isChecked() )
	uiMain.leEPassword.setEnabled( uiMain.cbEPassword.isChecked() )


### Signals

# Actions
uiMain.aSettings.connect( uiMain.aSettings, QtCore.SIGNAL( "triggered()" ), Settings.slSettingsL )
uiMain.aStop.connect( uiMain.aStop, QtCore.SIGNAL( "triggered()" ), Thread.slArcStop )

uiMain.aLOther.connect( uiMain.aLOther, QtCore.SIGNAL( "triggered()" ), Profile.slProLOther )
uiMain.aLDefault.connect( uiMain.aLDefault, QtCore.SIGNAL( "triggered()" ), Profile.slProLDefault )
uiMain.aLSecure.connect( uiMain.aLSecure, QtCore.SIGNAL( "triggered()" ), Profile.slProLSecure )
uiMain.aLStorage.connect( uiMain.aLStorage, QtCore.SIGNAL( "triggered()" ), Profile.slProLStorage )
uiMain.aSOther.connect( uiMain.aSOther, QtCore.SIGNAL( "triggered()" ), Profile.slProSOther )
uiMain.aSDefault.connect( uiMain.aSDefault, QtCore.SIGNAL( "triggered()" ), Profile.slProSDefault )
uiMain.aSSecure.connect( uiMain.aSSecure, QtCore.SIGNAL( "triggered()" ), Profile.slProSSecure )
uiMain.aSStorage.connect( uiMain.aSStorage, QtCore.SIGNAL( "triggered()" ), Profile.slProSStorage )
uiMain.aRDefault.connect( uiMain.aRDefault, QtCore.SIGNAL( "triggered()" ), Profile.slProRDefault )
uiMain.aRSecure.connect( uiMain.aRSecure, QtCore.SIGNAL( "triggered()" ), Profile.slProRSecure )
uiMain.aRStorage.connect( uiMain.aRStorage, QtCore.SIGNAL( "triggered()" ), Profile.slProRStorage )

uiMain.aAK7Z.connect( uiMain.aAK7Z, QtCore.SIGNAL( "triggered()" ), Help.slAboutK7Z )
uiMain.aAQt4.connect( uiMain.aAQt4, QtCore.SIGNAL( "triggered()" ), Help.slAboutQt4 )

uiMain.aUK7Z.connect( uiMain.aUK7Z, QtCore.SIGNAL( "triggered()" ), Help.slUK7Z )
uiMain.aUP7Zip.connect( uiMain.aUP7Zip, QtCore.SIGNAL( "triggered()" ), Help.slUP7Zip )
uiMain.aU7_Zip.connect( uiMain.aU7_Zip, QtCore.SIGNAL( "triggered()" ), Help.slU7_Zip )
uiMain.aUMake.connect( uiMain.aUMake, QtCore.SIGNAL( "triggered()" ), Help.slUMake )
uiMain.aUMinGW.connect( uiMain.aUMinGW, QtCore.SIGNAL( "triggered()" ), Help.slUMinGW )
uiMain.aUQt4.connect( uiMain.aUQt4, QtCore.SIGNAL( "triggered()" ), Help.slUQt4 )
uiMain.aUTar.connect( uiMain.aUTar, QtCore.SIGNAL( "triggered()" ), Help.slUTar )
uiMain.aUPyQt4.connect( uiMain.aUPyQt4, QtCore.SIGNAL( "triggered()" ), Help.slUPyQt4 )
uiMain.aUPython.connect( uiMain.aUPython, QtCore.SIGNAL( "triggered()" ), Help.slUPython )
uiMain.aUCheckInstall.connect( uiMain.aUCheckInstall, QtCore.SIGNAL( "triggered()" ), Help.slUCheckInstall )
uiMain.aUFileMenu_Tools.connect( uiMain.aUFileMenu_Tools, QtCore.SIGNAL( "triggered()" ), Help.slUFileMenu_Tools )

uiMain.aFBGood.connect( uiMain.aFBGood, QtCore.SIGNAL( "triggered()" ), Help.slFBGood )
uiMain.aFBBad.connect( uiMain.aFBBad, QtCore.SIGNAL( "triggered()" ), Help.slFBBad )

uiMain.aDAuthors.connect( uiMain.aDAuthors, QtCore.SIGNAL( "triggered()" ), Help.slDocAuthors )
uiMain.aDChanges.connect( uiMain.aDChanges, QtCore.SIGNAL( "triggered()" ), Help.slDocChanges )
uiMain.aDCopying.connect( uiMain.aDCopying, QtCore.SIGNAL( "triggered()" ), Help.slDocCopying )
uiMain.aDInstall.connect( uiMain.aDInstall, QtCore.SIGNAL( "triggered()" ), Help.slDocInstall )
uiMain.aDIssues.connect( uiMain.aDIssues, QtCore.SIGNAL( "triggered()" ), Help.slDocIssues )
uiMain.aDLicence.connect( uiMain.aDLicence, QtCore.SIGNAL( "triggered()" ), Help.slDocLicence )
uiMain.aDNews.connect( uiMain.aDNews, QtCore.SIGNAL( "triggered()" ), Help.slDocNews )
uiMain.aDIntroduction.connect( uiMain.aDIntroduction, QtCore.SIGNAL( "triggered()" ), Help.slDocIntroduction )
uiMain.aDRequests.connect( uiMain.aDRequests, QtCore.SIGNAL( "triggered()" ), Help.slDocRequests )

# Check Boxes
uiMain.cbCName.connect( uiMain.cbCName, QtCore.SIGNAL( "stateChanged(int)" ), slToggles )
uiMain.cbCPassword.connect( uiMain.cbCPassword, QtCore.SIGNAL( "stateChanged(int)" ), slToggles )
uiMain.cbEName.connect( uiMain.cbEName, QtCore.SIGNAL( "stateChanged(int)" ), slToggles )
uiMain.cbEPassword.connect( uiMain.cbEPassword, QtCore.SIGNAL( "stateChanged(int)" ), slToggles )

# Push Buttons
uiMain.pbCreate.connect( uiMain.pbCreate, QtCore.SIGNAL( "clicked()" ), Thread.slCreate )
uiMain.pbExtract.connect( uiMain.pbExtract, QtCore.SIGNAL( "clicked()" ), Thread.slExtract )
uiMain.pbStop.connect( uiMain.pbStop, QtCore.SIGNAL( "clicked()" ), Thread.slArcStop )

uiMain.pbSDir.connect( uiMain.pbSDir, QtCore.SIGNAL( "clicked()" ), slCGetSDir )
uiMain.pbSArc.connect( uiMain.pbSArc, QtCore.SIGNAL( "clicked()" ), slEGetSArc )
uiMain.pbCDDir.connect( uiMain.pbCDDir, QtCore.SIGNAL( "clicked()" ), slCGetDDir )
uiMain.pbEDDir.connect( uiMain.pbEDDir, QtCore.SIGNAL( "clicked()" ), slEGetDDir )

uiSettings.pbAccept.connect( uiSettings.pbAccept, QtCore.SIGNAL( "clicked()" ), Settings.slSettingsA )

# Processes
Thread.tiCreate.connect( Thread.tiCreate, QtCore.SIGNAL( "done(int)" ), Thread.slArcDone )
Thread.tiExtract.connect( Thread.tiExtract, QtCore.SIGNAL( "done(int)" ), Thread.slArcDone )
Thread.tiCreate.connect( Thread.tiCreate, QtCore.SIGNAL( "error(QString)" ), Thread.slError )
Thread.tiExtract.connect( Thread.tiExtract, QtCore.SIGNAL( "error(QString)" ), Thread.slError )


### Execution

# Test profiles
Profile.slProDirTest()
Profile.slProTest( "Default" )
Profile.slProTest( "Secure" )
Profile.slProTest( "Storage" )

# Input arguments
Input.slArgTest()

# Temp values

# Show the GUI?
if not Settings.bInvisible :

	# Show Main dialog
	mwMain.move( QtGui.QApplication.desktop().screen().rect().center() - mwMain.rect().center() )
	mwMain.show()
