"""
K7Z: Basic Archiver
Designed by Chris Giles

File:		Help.py
Purpose:	Help menu handler
"""


### Imports

# K7Z 1
import	Import

# PyQt4
try :
	from	PyQt4	import QtCore, QtGui
except :
	Import.slException( "PyQt4" )

# K7Z 2
import	Main, Settings


### Slots

# About Qt4
def slAboutQt4() :
	QtGui.QApplication.aboutQt()


# About K7Z
def slAboutK7Z() :
	QtGui.QMessageBox.about( Main.uiMain.centralwidget, "About " + Settings.sAppName,
		"<b>" + Settings.sAppName + "</b> " + Settings.sAppVer + ": Basic Archiver<br>"
		"Designed by " + Settings.sAuthorName + "<br><br>"
		"Use " + Settings.sAppName + " if you want to:<br>"
		"* Backup a folder to a storage location<br>"
		"* Create or extract a password-protected archive<br>"
		"* Update an existing archive quickly<br><br>"
		"Seek further information or send feedback via the 'Help' menu.<br><br>" )


# Open URL
def slUOpen( uURL ) :

	Main.uiMain.statusbar.showMessage( "Launching external application ..." )

	QtGui.QDesktopServices.openUrl( uURL )


# Feedback: Bad
def slFBBad() :

	# Set URL
	uURL = QtCore.QUrl( "mailto:" + Settings.sAuthorEmailUser + Settings.sAuthorEmailDomain + "?subject=" + Settings.sAppName + " " + Settings.sAppVer + ": Feedback: Bad" )

	slUOpen( uURL )

# Feedback: Good
def slFBGood() :

	# Set URL
	uURL = QtCore.QUrl( "mailto:" + Settings.sAuthorEmailUser + Settings.sAuthorEmailDomain + "?subject=" + Settings.sAppName + " " + Settings.sAppVer + ": Feedback: Good" )

	slUOpen( uURL )


# URL: K7Z
def slUK7Z() :

	# Set URL
	uURL = QtCore.QUrl( "http://k7z.sourceforge.net/" )

	slUOpen( uURL )

# URL: Qt4
def slUQt4() :

	# Set URL
	uURL = QtCore.QUrl( "http://www.trolltech.com/products/qt" )

	slUOpen( uURL )

# URL: PyQt4
def slUPyQt4() :

	# Set URL
	uURL = QtCore.QUrl( "http://www.riverbankcomputing.co.uk/pyqt/" )

	slUOpen( uURL )

# URL: Python
def slUPython() :

	# Set URL
	uURL = QtCore.QUrl( "http://www.python.org/" )

	slUOpen( uURL )

# URL: 7-Zip
def slU7_Zip() :

	# Set URL
	uURL = QtCore.QUrl( "http://www.7-zip.org/" )

	slUOpen( uURL )

# URL: P7Zip
def slUP7Zip() :

	# Set URL
	uURL = QtCore.QUrl( "http://p7zip.sourceforge.net/" )

	slUOpen( uURL )

# URL: MinGW
def slUMinGW() :

	# Set URL
	uURL = QtCore.QUrl( "http://www.mingw.org/" )

	slUOpen( uURL )

# URL: Tar
def slUTar() :

	# Set URL
	uURL = QtCore.QUrl( "http://www.gnu.org/software/tar/" )

	slUOpen( uURL )

# URL: Make
def slUMake() :

	# Set URL
	uURL = QtCore.QUrl( "http://www.gnu.org/software/make/" )

	slUOpen( uURL )

# URL: CheckInstall
def slUCheckInstall() :

	# Set URL
	uURL = QtCore.QUrl( "http://asic-linux.com.mx/~izto/checkinstall/" )

	slUOpen( uURL )

# URL: FileMenu Tools
def slUFileMenu_Tools() :

	# Set URL
	uURL = QtCore.QUrl( "http://www.lopesoft.com/en/fmtools/info.html" )

	slUOpen( uURL )


# Doc: Authors
def slDocAuthors() :

	# Set URL
	uURL = QtCore.QUrl( "file:" + Settings.sInstK7Z + Settings.sPathSep + "Doc" + Settings.sPathSep + "AUTHORS.txt" )

	slUOpen( uURL )

# Doc: Changes
def slDocChanges() :

	# Set URL
	uURL = QtCore.QUrl( "file:" + Settings.sInstK7Z + Settings.sPathSep + "Doc" + Settings.sPathSep + "ChangeLog.txt" )

	slUOpen( uURL )

# Doc: Copying
def slDocCopying() :

	# Set URL
	uURL = QtCore.QUrl( "file:" + Settings.sInstK7Z + Settings.sPathSep + "Doc" + Settings.sPathSep + "COPYING.txt" )

	slUOpen( uURL )

# Doc: Install
def slDocInstall() :

	# Set URL
	uURL = QtCore.QUrl( "file:" + Settings.sInstK7Z + Settings.sPathSep + "Doc" + Settings.sPathSep + "INSTALL.txt" )

	slUOpen( uURL )

# Doc: Issues
def slDocIssues() :

	# Set URL
	uURL = QtCore.QUrl( "file:" + Settings.sInstK7Z + Settings.sPathSep + "Doc" + Settings.sPathSep + "ISSUES.txt" )

	slUOpen( uURL )

# Doc: Licence
def slDocLicence() :

	# Set URL
	uURL = QtCore.QUrl( "file:" + Settings.sInstK7Z + Settings.sPathSep + "Doc" + Settings.sPathSep + "LICENCE.txt" )

	slUOpen( uURL )

# Doc: News
def slDocNews() :

	# Set URL
	uURL = QtCore.QUrl( "file:" + Settings.sInstK7Z + Settings.sPathSep + "Doc" + Settings.sPathSep + "NEWS.txt" )

	slUOpen( uURL )

# Doc: Introduction
def slDocIntroduction() :

	# Set URL
	uURL = QtCore.QUrl( "file:" + Settings.sInstK7Z + Settings.sPathSep + "Doc" + Settings.sPathSep + "README.txt" )

	slUOpen( uURL )

# Doc: Requests
def slDocRequests() :

	# Set URL
	uURL = QtCore.QUrl( "file:" + Settings.sInstK7Z + Settings.sPathSep + "Doc" + Settings.sPathSep + "TODO.txt" )

	slUOpen( uURL )
