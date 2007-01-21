"""
K7Z: Basic Archiver
Designed by Chris Giles

File:		Profile.py
Purpose:	Profile handler
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

# Load profile
def slProLoad( sProName ) :

	sProPath = QtCore.QString( Settings.sHomeK7Z + "/Profiles/" )

	# Open profile
	if sProName != "" :
		sProPath += sProName + ".txt"
	else :
		sProPath = QtGui.QFileDialog.getOpenFileName( None , "" , sProPath , "Profiles (*.txt)" )

	# Read profile
	fPro = QtCore.QFile( sProPath )

	if not fPro.open( QtCore.QIODevice.ReadOnly | QtCore.QIODevice.Text ) :
		Main.slError( "Error: Could not load the desired profile." )
	else :

		# Prepare text stream
		tsPro = QtCore.QTextStream( fPro )
		sLine = QtCore.QString( "" )

		while not tsPro.atEnd() :

			sLine = tsPro.readLine()

			# Recognised options

			# Type
			if sLine.startsWith( "Archive_Format " ) :
				Main.uiMain.cbAlgorithm.setCurrentIndex( Main.uiMain.cbAlgorithm.findText( sLine.section( ' ', 2 ) ) )
			elif sLine.startsWith( "Creation_Method " ) :
				Main.uiMain.cbMethod.setCurrentIndex( Main.uiMain.cbMethod.findText( sLine.section( ' ', 2 ) ) )
			elif sLine.startsWith( "Compression_Level " ) :
				Main.uiMain.cbComp.setCurrentIndex( Main.uiMain.cbComp.findText( sLine.section( ' ', 2 ) ) )
			elif sLine.startsWith( "Volume_Size " ) :
				Main.uiMain.cbVolume.setCurrentIndex( Main.uiMain.cbVolume.findText( sLine.section( ' ', 2 ) ) )
			elif sLine.startsWith( "SFX " ) :
				if sLine.section( ' ', 2 ) == "No" :
					Main.uiMain.cbSFX.setCheckState( QtCore.Qt.Unchecked )
				elif sLine.section( ' ', 2 ) == "Yes" :
					Main.uiMain.cbSFX.setCheckState( QtCore.Qt.Checked )
			elif sLine.startsWith( "Solid " ) :
				if sLine.section( ' ', 2 ) == "No" :
					Main.uiMain.cbSolid.setCheckState( QtCore.Qt.Unchecked )
				elif sLine.section( ' ', 2 ) == "Yes" :
					Main.uiMain.cbSolid.setCheckState( QtCore.Qt.Checked )
			elif sLine.startsWith( "Tarball " ) :
				if sLine.section( ' ', 2 ) == "No" :
					Main.uiMain.cbTarball.setCheckState( QtCore.Qt.Unchecked )
				elif sLine.section( ' ', 2 ) == "Yes" :
					Main.uiMain.cbTarball.setCheckState( QtCore.Qt.Checked )
			# Security
			elif sLine.startsWith( "Scramble " ) :
				if sLine.section( ' ', 2 ) == "No" :
					Main.uiMain.cbScramble.setCheckState( QtCore.Qt.Unchecked )
				elif sLine.section( ' ', 2 ) == "Yes" :
					Main.uiMain.cbScramble.setCheckState( QtCore.Qt.Checked )
			elif sLine.startsWith( "Password " ) :
				if sLine.section( ' ', 2 ) == "No" :
					Main.uiMain.cbCPassword.setCheckState( QtCore.Qt.Unchecked )
				elif sLine.section( ' ', 2 ) == "Yes" :
					Main.uiMain.cbCPassword.setCheckState( QtCore.Qt.Checked )
			# Destination
			elif sLine.startsWith( "Destination " ) :
				if sLine.section( ' ', 2 ) == "No" :
					Main.uiMain.gbCDestination.setChecked( False )
				elif sLine.section( ' ', 2 ) == "Yes" :
					Main.uiMain.gbCDestination.setChecked( True )
			elif sLine.startsWith( "Structured " ) :
				if sLine.section( ' ', 2 ) == "No" :
					Main.uiMain.cbStructured.setCheckState( QtCore.Qt.Unchecked )
				elif sLine.section( ' ', 2 ) == "Yes" :
					Main.uiMain.cbStructured.setCheckState( QtCore.Qt.Checked )
			elif sLine.startsWith( "Destination_Dir " ) :
				Main.uiMain.leCDDir.setText( sLine.section( ' ', 2 ) )
			elif sLine.startsWith( "Archive_Name " ) :
				if sLine.section( ' ', 2 ) == "No" :
					Main.uiMain.cbCName.setCheckState( QtCore.Qt.Unchecked )
				elif sLine.section( ' ', 2 ) == "Yes" :
					Main.uiMain.cbCName.setCheckState( QtCore.Qt.Checked )

			Main.uiMain.statusbar.showMessage( "Loaded '" + sProName + "' profile" )

		fPro.close()

# Load 'Other' profile
def slProLOther() :
	slProLoad( "" )

# Load 'Default' profile
def slProLDefault() :
	slProLoad( "Default" )

# Load 'Secure' profile
def slProLSecure() :
	slProLoad( "Secure" )

# Load 'Storage' profile
def slProLStorage() :
	slProLoad( "Storage" )


# Save profile
def slProSave( sProName ) :

	sProPath = QtCore.QString( Settings.sHomeK7Z + "/Profiles/" )

	# Open profile
	if sProName != "" :
		sProPath += sProName + ".txt"
	else :
		sProPath = QtGui.QFileDialog.getSaveFileName( None , "" , sProPath ,
			"Profiles (*.txt)" , "" , QtGui.QFileDialog.DontConfirmOverwrite )

	# Write profile
	fPro = QtCore.QFile( sProPath )

	if not fPro.open( QtCore.QIODevice.WriteOnly | QtCore.QIODevice.Text ) :
		Main.slError( "Error: Could not save the desired profile." )
	else :

		# Prepare text stream
		tsPro = QtCore.QTextStream( fPro )

		# Header
		tsPro << "### " + Settings.sAppName + " " + Settings.sAppVer + ": Profile\n"

		# Recognised options

		# Type
		tsPro << "\n# Type\n"
		tsPro << "Archive_Format = " + Main.uiMain.cbAlgorithm.currentText() + "\n"
		tsPro << "Creation_Method = " + Main.uiMain.cbMethod.currentText() + "\n"
		tsPro << "Compression_Level = " + Main.uiMain.cbComp.currentText() + "\n"
		tsPro << "Volume_Size = " + Main.uiMain.cbVolume.currentText() + "\n"
		if not Main.uiMain.cbSFX.isChecked() :
			tsPro << "SFX = No\n"
		else :
			tsPro << "SFX = Yes\n"
		if not Main.uiMain.cbSolid.isChecked() :
			tsPro << "Solid = No\n"
		else :
			tsPro << "Solid = Yes\n"
		if not Main.uiMain.cbTarball.isChecked() :
			tsPro << "Tarball = No\n"
		else :
			tsPro << "Tarball = Yes\n"

		# Security
		tsPro << "\n# Security\n"
		if not Main.uiMain.cbScramble.isChecked() :
			tsPro << "Scramble = No\n"
		else :
			tsPro << "Scramble = Yes\n"
		if not Main.uiMain.cbCPassword.isChecked() :
			tsPro << "Password = No\n"
		else :
			tsPro << "Password = Yes\n"

		# Destination
		tsPro << "\n# Destination\n"
		if not Main.uiMain.gbCDestination.isChecked() :
			tsPro << "Destination = No\n"
		else :
			tsPro << "Destination = Yes\n"
		if not Main.uiMain.cbStructured.isChecked() :
			tsPro << "Structured = No\n"
		else :
			tsPro << "Structured = Yes\n"
		tsPro << "Destination_Dir = " + Main.uiMain.leCDDir.displayText() + "\n"
		if not Main.uiMain.cbCName.isChecked() :
			tsPro << "Archive_Name = No\n"
		else :
			tsPro << "Archive_Name = Yes\n"

		Main.uiMain.statusbar.showMessage( "Saved '" + sProName + "' profile" )

		fPro.close()


# Save 'Other' profile
def slProSOther() :
	slProSave( "" )

# Save 'Default' profile
def slProSDefault() :
	slProSave( "Default" )

# Save 'Secure' profile
def slProSSecure() :
	slProSave( "Secure" )

# Save 'Storage' profile
def slProSStorage() :
	slProSave( "Storage" )


# Reset profile
def slProReset( sProName ) :

	sBackupPath = Settings.sInstK7Z + "/Desktop/Profiles/"
	sBackupPath += sProName + ".txt"
	sProPath = QtCore.QString( Settings.sHomeK7Z + "/Profiles/" + sProName + ".txt" )

	# Remove current
	QtCore.QFile.remove( sProPath )

	# Copy original
	QtCore.QFile.copy( sBackupPath , sProPath )

	Main.uiMain.statusbar.showMessage( "Reset '" + sProName + "' profile" )


# Reset 'Default' profile
def slProRDefault() :
	slProReset( "Default" )

# Reset 'Secure' profile
def slProRSecure() :
	slProReset( "Secure" )

# Reset 'Storage' profile
def slProRStorage() :
	slProReset( "Storage" )

# Test profile directory
def slProDirTest() :

	sProPath = QtCore.QString( Settings.sHomeK7Z + "/Profiles/" )
	dProPath = QtCore.QDir( sProPath )

	# Create profile directory
	if not dProPath.exists() :
		dProPath.mkpath( sProPath )


# Test profile
def slProTest( sProName ) :

	sProPath = QtCore.QString( Settings.sHomeK7Z + "/Profiles/" + sProName + ".txt" )

	if not QtCore.QFile.exists( sProPath ) :
		slProReset( sProName )
