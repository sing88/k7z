"""
K7Z: Basic Archiver
Designed by Chris Giles

File:		Thread.py
Purpose:	Thread handler
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


### Threads

# Create
class tCreate( QtCore.QThread ) :

	def create( self ) :

		# Declare process
		self.pArc = QtCore.QProcess()

		# Declare paths
		dSource = QtCore.QDir()
		dOutput = QtCore.QDir()

		self.oParams.bSuccess = False

		# Initialise command arguments
		slArcCmdArgs = QtCore.QStringList()
		slArcCmdArgs.clear()

		# Use the tarball?
		if not self.oParams.bUTarball :

			# Directory chosen manually
			if Settings.iNumInputArgs < 3 :
				self.oParams.slFiles.clear()
				self.oParams.slFiles.append( Main.uiMain.leSDir.displayText() )

			# Source
			dSource.setPath( self.oParams.slFiles.first() )

		else :

			self.oParams.slFiles.clear()
			self.oParams.slFiles.append( self.oParams.sArcPath )

			# Source
			dSource.setPath( self.oParams.sArcPath )

		# Archive name
		dSource.makeAbsolute()
		sArcName = QtCore.QString( dSource.dirName() )
		dSource.cdUp()

		# Command
		sCmd = Settings.sCmd7z

		# Algorithm
		if self.oParams.bCTarball or Main.uiMain.cbAlgorithm.currentText() == "Tar" :

			# Linux
			if Settings.sOS == "Linux" :

				# Command
				sCmd = Settings.sCmdTar

				# Working directory
				slArcCmdArgs.append( "-cC" )
				slArcCmdArgs.append( dSource.path() )

				# Use relative paths for tarball contents
				for iEntry in range(0,self.oParams.slFiles.count()) :
					self.oParams.slFiles.replace( iEntry , dSource.relativeFilePath( self.oParams.slFiles.__getitem__( iEntry ) ) )

				# Output file
				slArcCmdArgs.append( "-f" )

			else :

				# Format
				slArcCmdArgs.append( "-ttar" )

				# Method
				slArcCmdArgs.append( "u" )
				slArcCmdArgs.append( "-uq0" )

			fnExt = ".tar"

		else :

			# Format
			if Main.uiMain.cbAlgorithm.currentText() == "7-Zip" :
				slArcCmdArgs.append( "-t7z" )
				fnExt = ".7z"

				# Scrambled
				if not Main.uiMain.cbScramble.isChecked() :
					slArcCmdArgs.append( "-mhe=off" )
				else :
					slArcCmdArgs.append( "-mhe=on" )

				# Solid
				if not Main.uiMain.cbSolid.isChecked() :
					slArcCmdArgs.append( "-ms=off" )
				else :
					slArcCmdArgs.append( "-ms=on" )

				# Volumes
				if Main.uiMain.cbVolume.currentText() == "Floppy" :
					slArcCmdArgs.append( "-v1440k" )
				elif Main.uiMain.cbVolume.currentText() == "CD" :
					slArcCmdArgs.append( "-v720000k" )
				elif Main.uiMain.cbVolume.currentText() == "DVD" :
					slArcCmdArgs.append( "-v4700000000b" )

			elif Main.uiMain.cbAlgorithm.currentText() == "BZip2" :
				slArcCmdArgs.append( "-tbzip2" )
				fnExt = ".bz2"
			elif Main.uiMain.cbAlgorithm.currentText() == "Zip" :
				slArcCmdArgs.append( "-tzip" )
				fnExt = ".zip"
			elif Main.uiMain.cbAlgorithm.currentText() == "GZip" :
				slArcCmdArgs.append( "-tgzip" )
				fnExt = ".gz"

			# Compression level
			if Main.uiMain.cbComp.currentText() == "None" :
				slArcCmdArgs.append( "-mx0" )
			elif Main.uiMain.cbComp.currentText() == "Fastest" :
				slArcCmdArgs.append( "-mx1" )
			elif Main.uiMain.cbComp.currentText() == "Fast" :
				slArcCmdArgs.append( "-mx3" )
			elif Main.uiMain.cbComp.currentText() == "Normal" :
				slArcCmdArgs.append( "-mx5" )
			elif Main.uiMain.cbComp.currentText() == "Maximum" :
				slArcCmdArgs.append( "-mx7" )
			elif Main.uiMain.cbComp.currentText() == "Ultra" :
				slArcCmdArgs.append( "-mx9" )

			# Method
			if Main.uiMain.cbMethod.currentText() == "Update" :
				slArcCmdArgs.append( "u" )
			elif Main.uiMain.cbMethod.currentText() == "Sync" :
				slArcCmdArgs.append( "u" )
				slArcCmdArgs.append( "-uq0" )
			elif Main.uiMain.cbMethod.currentText() == "Add" :
				slArcCmdArgs.append( "a" )

			# Yes to all
			slArcCmdArgs.append( "-y" )

			# Password
			if Main.uiMain.cbCPassword.isChecked() and not Main.uiMain.leCPassword.displayText().isEmpty() :
				slArcCmdArgs.append( "-p" + Main.uiMain.leCPassword.displayText() )

			# SFX
			if Main.uiMain.cbSFX.isChecked() :
				slArcCmdArgs.append( "-sfx" )
				fnExt = ".exe"

		# Destination
		if not Main.uiMain.gbCDestination.isChecked() :
			if not self.oParams.slFiles.count() > 1 :
				self.oParams.sArcPath = dSource.path() + Settings.sPathSep + sArcName
			else :
				self.oParams.sArcPath = dSource.path() + "/K7Z"
		else :

			# Directory
			if not Main.uiMain.leCDDir.displayText().isEmpty() and not self.oParams.bUTarball :

				# Structured
				if Main.uiMain.cbStructured.isChecked() :

					# Remove colons
					sSource = dSource.path()
					sSource.remove( ":" )
					dOutput.setPath( Main.uiMain.leCDDir.displayText() + Settings.sPathSep + sSource )

				else :
					dOutput.setPath( Main.uiMain.leCDDir.displayText() + Settings.sPathSep )

			else :
				dOutput.setPath( dSource.path() )

			# Filename
			if not Main.uiMain.cbCName.isChecked() :
				if not self.oParams.slFiles.count() > 1 :
					self.oParams.sArcPath = dOutput.path() + Settings.sPathSep + sArcName
				else :
					self.oParams.sArcPath = dOutput.path() + "/K7Z"
			else :
				self.oParams.sArcPath = dOutput.path() + Settings.sPathSep + Main.uiMain.leCName.displayText()

		# Append archive and file(s)
		self.oParams.sArcPath += fnExt
		slArcCmdArgs.append( self.oParams.sArcPath )
		slArcCmdArgs << self.oParams.slFiles

		# Volumes
		if Main.uiMain.cbVolume.currentText() != "Unlimited" :
			self.oParams.sArcPath += ".001"

		# Verbose
		if Settings.bVerbose is True :
			print "Creating ..."
			print "Input = " + self.oParams.slFiles.first()
			print "Archive = " + self.oParams.sArcPath

			# Command Arguments
			print "Command = " + sCmd
			print "Arguments ="
			for iEntry in range(0,slArcCmdArgs.count()) :
				print "\t" + slArcCmdArgs.__getitem__( iEntry )

		# Execute process
		self.pArc.start( sCmd , slArcCmdArgs )

		if self.pArc.waitForStarted( 1000 ) :

			# Verbose
			if Settings.bVerbose is True :
				print "Create: Started"

			while not self.pArc.waitForFinished( 500 ) :
				pass
				# Search for percentage indicator
				#sArcData = QtCore.QString( self.pArc.readData(512) )

			# Analyse exit-code
			if self.pArc.exitCode() is not 0 :

				iPercent = 0
				self.emit( QtCore.SIGNAL( "error(QString)" ) , str(self.pArc.readAllStandardOutput()) )
				print "Create: Failure"
				print ""

			else :

				# Verbose
				if Settings.bVerbose is True :
					print "Create: Success"
					print ""

				iPercent = 100
				self.oParams.bSuccess = True

				# Adjust percentage
				if Main.uiMain.cbCTest.isChecked() :
					iPercent /= 2

				if self.oParams.bCTarball :
					iPercent /= 2

			self.emit( QtCore.SIGNAL( "done(int)" ) , iPercent )

		else :
			self.emit( QtCore.SIGNAL( "error(QString)" ) , "Error: Could not start 'P7Zip'; View the INSTALL file for more info." )

		return self.oParams


	def stop( self ) :

		# Stop archiving
		if self.pArc.state() == QtCore.QProcess.Running :
			self.pArc.terminate()
		else :
			tiExtract.stop()


	def run( self ) :

		# Parameter container
		self.oParams = QtCore.QObject()
		self.oParams.bUTarball = False
		self.oParams.sArcPath = ""

		# Copy files list
		self.oParams.slFiles = QtCore.QStringList()
		self.oParams.slFiles << Settings.slFiles

		# Create tarball first
		self.oParams.bCTarball = Main.uiMain.cbTarball.isChecked()

		if Main.uiMain.cbAlgorithm.currentText() == "BZip2" :
			self.oParams.bCTarball = True
		elif Main.uiMain.cbAlgorithm.currentText() == "GZip" :
			self.oParams.bCTarball = True

		# Execute archiver
		if Main.uiMain.leSDir.displayText() != "" :

			# Create Tarball and/or archive
			if self.oParams.bCTarball :

				self.create()
				fArcPath = QtCore.QFile( self.oParams.sArcPath )

				if self.oParams.bSuccess :

					self.oParams.bCTarball = False
					self.oParams.bUTarball = True
					self.create()
					fArcPath.remove()

			else :
				self.create()

			if self.oParams.bSuccess :

				# Test the archive
				if Main.uiMain.cbCTest.isChecked() :
					self.oParams.iSource = Settings.iOpCreate
					self.oParams.iOperation = Settings.iOpTest
					tiExtract.extract( self.oParams )

				# Start event loop
				self.exec_()

		else :
			self.emit( QtCore.SIGNAL( "error(QString)" ) , "" )


# Extract the archive
class tExtract( QtCore.QThread ) :

	def extract( self , oParams ) :

		# Declare process
		self.pArc = QtCore.QProcess()

		# Declare paths
		dSource = QtCore.QDir()
		dOutput = QtCore.QDir()

		# Initialise command arguments
		slArcCmdArgs = QtCore.QStringList()
		slArcCmdArgs.clear()

		# Command
		sCmd = Settings.sCmd7z

		# Archive chosen manually
		if Settings.iNumInputArgs < 3 :
			oParams.slFiles.clear()
			oParams.slFiles.append( Main.uiMain.leArchive.displayText() )

		# Archive recently created
		if oParams.iSource == Settings.iOpCreate :
			oParams.slFiles.clear()
			oParams.slFiles.append( oParams.sArcPath )

		# Beneath
		dSource.setPath( oParams.slFiles.first() )
		dSource.makeAbsolute()
		sBeneath = dSource.dirName()
		sBeneath.resize( sBeneath.lastIndexOf( '.' ) )
		dSource.cdUp()

		# Destination
		if not Main.uiMain.gbEDestination.isChecked() :
			dOutput.setPath( dSource.path() )
		else :

			# Directory
			if not Main.uiMain.leEDDir.displayText().isEmpty() :
				dOutput.setPath( Main.uiMain.leEDDir.displayText() )
			else :
				dOutput.setPath( dSource.path() )

			# Filename
			if Main.uiMain.cbEName.isChecked() :
				dOutput.setPath( dOutput.path() + Settings.sPathSep + Main.uiMain.leEName.displayText() )

			# Beneath
			if Main.uiMain.cbBeneath.isChecked() :
				dOutput.setPath( dOutput.path() + Settings.sPathSep + sBeneath )

		# Algorithm
		if Settings.sOS == "Linux" \
			and oParams.slFiles.first().endsWith( ".tar" ) \
			and oParams.iOperation == Settings.iOpExtract :

			# Command
			sCmd = Settings.sCmdTar

			# Extract
			slArcCmdArgs.append( "-xf" )

			# Archive
			slArcCmdArgs.append( oParams.slFiles.first() )

			# Output directory
			if not dOutput.exists() :
				dOutput.mkpath( dOutput.path() )

			slArcCmdArgs.append( "-C" )
			slArcCmdArgs.append( dOutput.path() + Settings.sPathSep )

		else :

			# Extract or test
			if oParams.iOperation == Settings.iOpExtract :
				slArcCmdArgs.append( "x" )
			else :
				slArcCmdArgs.append( "t" )

			# Answer 'yes' to all queries
			slArcCmdArgs.append( "-y" )

			# Output directory
			slArcCmdArgs.append( "-o" + dOutput.path() + Settings.sPathSep )

			# Password
			if oParams.iSource == Settings.iOpCreate :
				if Main.uiMain.cbCPassword.isChecked() and not Main.uiMain.leCPassword.displayText().isEmpty() :
					slArcCmdArgs.append( "-p" + Main.uiMain.leCPassword.displayText() )
				else :
					slArcCmdArgs.append( "-pNoPassword" )
			else :
				if Main.uiMain.cbEPassword.isChecked() and not Main.uiMain.leEPassword.displayText().isEmpty() :
					slArcCmdArgs.append( "-p" + Main.uiMain.leEPassword.displayText() )
				else :
					slArcCmdArgs.append( "-pNoPassword" )

			# Archive
			slArcCmdArgs.append( oParams.slFiles.first() )

		# Verbose
		if Settings.bVerbose is True :
			print "Extracting ..."
			print "Operation = " + str( oParams.iOperation )
			print "Archive = " + oParams.slFiles.first()
			print "Destination = " + dOutput.path() + Settings.sPathSep

			# Command Arguments
			print "Command = " + sCmd
			print "Arguments ="
			for iEntry in range(0,slArcCmdArgs.count()) :
				print "\t" + slArcCmdArgs.__getitem__( iEntry )

		# Execute process
		self.pArc.start( sCmd , slArcCmdArgs )

		if self.pArc.waitForStarted( 1000 ) :

			# Verbose
			if Settings.bVerbose is True :
				print "Extract/Test: Started"

			while not self.pArc.waitForFinished( 500 ) :
				pass
				"""
				# Get output
				sArcData = QtCore.QString( self.pArc.readData(512) )

				# Password?
				if sArcData.contains( "Enter password" ) :

					# Verbose
					if Settings.bVerbose is True :
						print "Password Requested"

					idPassword = QtGui.QInputDialog()
					Main.uiMain.leEPassword.setText( idPassword.getText( QtGui.QWidget, "K7Z: Enter Password" , "K7Z: Enter Password" ) )
				"""

			# Analyse exit-code
			if self.pArc.exitCode() is not 0 :

				iPercent = 0
				self.emit( QtCore.SIGNAL( "error(QString)" ) , str(self.pArc.readAllStandardOutput()) )
				print "Extract/Test: Failure"
				print ""

			else :

				iPercent = 100
				oParams.bSuccess = True

				# Verbose
				if Settings.bVerbose is True :
					print "Extract/Test: Success"
					print ""

			self.emit( QtCore.SIGNAL( "done(int)" ) , iPercent )

		else :
			self.emit( QtCore.SIGNAL( "error(QString)" ) , "Error: Could not start 'P7Zip'; View the INSTALL file for more info." )

		return oParams


	def stop( self ) :

		# Stop archiving
		self.pArc.terminate()


	def run( self ) :

		# Parameter container
		self.oParams = QtCore.QObject()
		self.oParams.iSource = Settings.iOpExtract
		self.oParams.sArcPath = ""

		# Copy files list
		self.oParams.slFiles = QtCore.QStringList()
		self.oParams.slFiles << Settings.slFiles

		# Extract or test
		if Main.uiMain.cbETest.isChecked() :
			self.oParams.iOperation = Settings.iOpTest
		else :
			self.oParams.iOperation = Settings.iOpExtract

		# Execute archiver
		if Main.uiMain.leArchive.displayText() != "" :

			# Extract/Test archive
			self.extract( self.oParams )

			# Start event loop
			self.exec_()

		else :
			self.emit( QtCore.SIGNAL( "error(QString)" ) , "" )


### Variables

tiCreate	= tCreate()
tiExtract	= tExtract()


### Slots

# Start the 'create' thread
def slCreate() :

	Main.uiMain.leArchive.setText( "" )
	Main.uiMain.statusbar.showMessage( "Creating archive ..." )
	Main.mwMain.setWindowTitle( Settings.sAppName + " - Creating ..." )

	# Disable GUI
	slDisableGUI()

	# Execute thread
	tiCreate.start()
	tiCreate.setPriority( QtCore.QThread.LowPriority )
	tiCreate.msleep( 50 )


# Start the 'extract' thread
def slExtract() :

	Main.uiMain.leSDir.setText( "" )
	Main.uiMain.statusbar.showMessage( "Extracting/testing archive ..." )
	Main.mwMain.setWindowTitle( Settings.sAppName + " - Extracting/Testing ..." )

	# Disable GUI
	slDisableGUI()

	# Execute thread
	tiExtract.start()
	tiExtract.setPriority( QtCore.QThread.LowPriority )
	tiExtract.msleep( 50 )


# Enable GUI
def slEnableGUI() :

	Main.uiMain.aStop.setEnabled( False )
	Main.uiMain.pbStop.setEnabled( False )
	Main.uiMain.pbComplete.setEnabled( False )
	Main.uiMain.twOperations.setEnabled( True )

	Main.mwMain.setWindowTitle( Settings.sAppName )
	Main.uiMain.statusbar.clearMessage()


# Disable GUI
def slDisableGUI() :

	# Reset or disable items
	Main.uiMain.twOperations.setEnabled( False )
	Main.uiMain.aStop.setEnabled( True )
	Main.uiMain.pbComplete.setEnabled( True )
	Main.uiMain.pbStop.setEnabled( True )
	Main.uiMain.pbComplete.setValue( 0 )


# Finished
def slArcDone( iRetVal ) :

	# Exit threads
	slArcExit()

	# Update info
	Main.uiMain.pbComplete.setValue( iRetVal )

	# Reset GUI
	if iRetVal == 100 :
		slEnableGUI()

	# Default and storage
	if iRetVal == 100 and Settings.iNumInputArgs >= 3 :
		if Settings.bAutoExit :
			Main.uiMain.pbExit.click()


# Error
def slError( sError ) :

	# Exit threads
	slArcExit()

	if sError != "" :
		QtGui.QErrorMessage.showMessage( QtGui.QErrorMessage.qtHandler() , sError )

	# Reset GUI
	slEnableGUI()


# Stop Archiving
def slArcStop() :

	# Terminate process
	if tiCreate.isRunning() :
		tiCreate.stop()
	if tiExtract.isRunning() :
		tiExtract.stop()

	# Exit threads
	slArcExit()

	# Reset GUI
	slEnableGUI()


# Exit threads
def slArcExit() :

	tiCreate.exit()
	tiExtract.exit()
