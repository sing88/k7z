; NSIS for K7Z
; Designed by Chris Giles


;--------------------------------
; Include Modern UI

	!include 			"MUI.nsh"

	!include			"TextFunc.nsh"
	!include			"WordFunc.nsh"


	!insertmacro		LineFind
	!insertmacro		WordReplace


;--------------------------------
; General

	SetCompressor		lzma

	; Name and file
	Name 				"K7Z"
	OutFile 			"..\Package\K7Z-0.6-1.win32.exe"

	Icon				"..\Source\Images\apps\K7Z.ico"
	UninstallIcon		"..\Source\Images\apps\K7Z.ico"

	;AutoCloseWindow 	true

	;ShowInstDetails 	show
	;ShowUninstDetails 	show

	;XPStyle 			on

	;DirText "Please select the desired MicroStation root path.  The default is: C:\Program Files\Bentley\." "" "" \
	;		"Please select the desired MicroStation root path.  The default is: C:\Program Files\Bentley\."

	; Default installation folder
	InstallDir 			"$PROGRAMFILES\Archiving\K7Z\"


;--------------------------------
; Variables

	Var 	MUI_TEMP
	Var 	STARTMENU_FOLDER

	Var 	"AppName"
	Var		"AppFileName"
	Var		"AppVer"

	Var     "Dir_K7Z"
	Var		"Dir_K7Z_DB"
	Var		"PythonCmd"


;--------------------------------
; Interface Settings

	;!define MUI_ABORTWARNING


;--------------------------------
; Pages

	!insertmacro 	MUI_PAGE_LICENSE 		"..\Doc\LICENCE.txt"
	!insertmacro 	MUI_PAGE_COMPONENTS

	;!insertmacro 	MUI_PAGE_DIRECTORY

	PageEx 			directory
		;DirText 			"Please select the desired MicroStation v8.9 (XM) root path.  The default is: C:\Program Files\Bentley\." "" "" \
		;					"Please select the desired MicroStation v8.9 (XM) root path.  The default is: C:\Program Files\Bentley\."
		DirVar              $Dir_K7Z
		DirVerify           auto
		;PageCallbacks		autoPath-K7Z
	PageExEnd

	; Start Menu Folder Page Configuration
	!define 		MUI_STARTMENUPAGE_REGISTRY_ROOT 		"HKLM"
	!define 		MUI_STARTMENUPAGE_REGISTRY_KEY 			"Software\Archiving\$AppName"
	!define 		MUI_STARTMENUPAGE_REGISTRY_VALUENAME 	"Start Menu Folder"
	!define			MUI_STARTMENUPAGE_DEFAULTFOLDER			"Archiving\$AppName"

	!insertmacro 	MUI_PAGE_STARTMENU Application 			$STARTMENU_FOLDER

	!insertmacro 	MUI_PAGE_INSTFILES

	!insertmacro 	MUI_UNPAGE_COMPONENTS
	;!insertmacro 	MUI_UNPAGE_CONFIRM
	!insertmacro 	MUI_UNPAGE_INSTFILES


;--------------------------------
; Languages

	!insertmacro 	MUI_LANGUAGE 	"English"
	;!insertmacro 	MUI_LANGUAGE 	"German"
	;!insertmacro 	MUI_LANGUAGE 	"French"
	;!insertmacro 	MUI_LANGUAGE 	"Indonesian"
	;!insertmacro 	MUI_LANGUAGE 	"Spanish"


;--------------------------------
; Installer Sections

SectionGroup /e "Prerequisites"

	Section "Qt 4.2" Sec-I-Qt

		AddSize 215000

		; Launch website
		;ExecShell "open" "http://www.trolltech.com/products/qt"
		Exec "explorer http://www.trolltech.com/products/qt"

	SectionEnd

	Section "PyQt 4.1" Sec-I-PyQt

		AddSize 7000

		; Launch website
		;ExecShell "open" "http://www.riverbankcomputing.co.uk/pyqt/"
		Exec "explorer http://www.riverbankcomputing.co.uk/pyqt/"

	SectionEnd

	Section "7-Zip 4.30" Sec-I-7Zip

		AddSize 3000

		; Launch website
		;ExecShell "open" "http://www.7-zip.org/"
		Exec "explorer http://www.7-zip.org/"

	SectionEnd

	Section "MinGW 3.10" Sec-I-MinGW

		AddSize 60000

		; Launch website
		;ExecShell "open" "http://www.mingw.org/"
		Exec "explorer http://www.mingw.org/"

	SectionEnd

	Section "Python 2.5" Sec-I-Python

		AddSize 30000

		; Launch website
		;ExecShell "open" "http://www.python.org/"
		Exec "explorer http://www.python.org/"

	SectionEnd

	Section "FileMenu Tools 5.0" Sec-I-FileMenuTools

		AddSize 5000

		; Launch website
		;ExecShell "open" "http://www.python.org/"
		Exec "explorer http://www.lopesoft.com/en/fmtools/info.html"

	SectionEnd

SectionGroupEnd

SectionGroup /e "Program"

	Section "$AppName $AppVer" Sec-I-K7Z

		; Store installation folder
		WriteRegStr HKLM "Software\Archiving\$AppName" "Path" $Dir_K7Z

		SetOverwrite	on

		; Output Reqired Files
		SetOutPath "$Dir_K7Z"
		File /a /r "..\Build"
		File /a /r "..\Doc"
		File /a /r "..\Source"

		SetOverwrite	ifnewer

		File /a /r "..\Desktop"
		File /a /r "..\Desktop\Profiles"

		; Create uninstaller
		WriteUninstaller "$Dir_K7Z\$AppName-UnInstall.EXE"

		; Make
		StrCpy 	$OUTDIR	"$Dir_K7Z\Build\"
		ExecWait '"$Dir_K7Z\Build\MakeCmd.bat"'

	SectionEnd

SectionGroupEnd

SectionGroup /e "Windows"

	Section "-ShortCuts" Sec-I-ShortCuts

		!insertmacro MUI_STARTMENU_WRITE_BEGIN Application

			; Create shortcuts
			CreateDirectory 	"$SMPROGRAMS\$STARTMENU_FOLDER"
			CreateShortCut 		"$SMPROGRAMS\$STARTMENU_FOLDER\$AppName.LNK" "$Dir_K7Z\Source\$AppFileName" "" "$Dir_K7Z\Source\Images\apps\$AppName.ico"
			CreateShortCut 		"$SMPROGRAMS\$STARTMENU_FOLDER\UnInstall.LNK" "$Dir_K7Z\$AppName-UnInstall.EXE"

			CreateDirectory 	"$SMPROGRAMS\$STARTMENU_FOLDER\Doc\"
			CreateShortCut 		"$SMPROGRAMS\$STARTMENU_FOLDER\Doc\Authors.LNK" "$Dir_K7Z\Doc\AUTHORS.txt"
			CreateShortCut 		"$SMPROGRAMS\$STARTMENU_FOLDER\Doc\Changes.LNK" "$Dir_K7Z\Doc\ChangeLog.txt"
			CreateShortCut 		"$SMPROGRAMS\$STARTMENU_FOLDER\Doc\Copying.LNK" "$Dir_K7Z\Doc\COPYING.txt"
			CreateShortCut 		"$SMPROGRAMS\$STARTMENU_FOLDER\Doc\Install.LNK" "$Dir_K7Z\Doc\INSTALL.txt"
			CreateShortCut 		"$SMPROGRAMS\$STARTMENU_FOLDER\Doc\Issues.LNK" "$Dir_K7Z\Doc\ISSUES.txt"
			CreateShortCut 		"$SMPROGRAMS\$STARTMENU_FOLDER\Doc\Licence.LNK" "$Dir_K7Z\Doc\LICENCE.txt"
			CreateShortCut 		"$SMPROGRAMS\$STARTMENU_FOLDER\Doc\News.LNK" "$Dir_K7Z\Doc\NEWS.txt"
			CreateShortCut 		"$SMPROGRAMS\$STARTMENU_FOLDER\Doc\Introduction.LNK" "$Dir_K7Z\Doc\README.txt"
			CreateShortCut 		"$SMPROGRAMS\$STARTMENU_FOLDER\Doc\Requests.LNK" "$Dir_K7Z\Doc\TODO.txt"

			CreateShortCut 		"$SMPROGRAMS\$STARTMENU_FOLDER\Website.LNK" "http://k7z.SourceForge.net/" "" "%WINDIR%\system32\url.dll"

		!insertmacro MUI_STARTMENU_WRITE_END

	SectionEnd

	SectionGroup /e "Shell Menu"

		/*
		Section "Common" Sec-I-ShellMenu-Common

			WriteRegStr 	HKCR "Directory\shell" "" 'None'
			;WriteRegStr 	HKCR "Directory\shell\$AppName: Create: Default\command" "" '$PythonCmd "$Dir_K7Z\Source\$AppFileName" "-cd" "%1"'
			;WriteRegStr 	HKCR "Directory\shell\$AppName: Create: Storage\command" "" '$PythonCmd "$Dir_K7Z\Source\$AppFileName" "-cs" "%1"'
			WriteRegStr 	HKCR "Directory\shell\$AppName: Create ...\command" "" '$PythonCmd "$Dir_K7Z\Source\$AppFileName" "-c" "%1"'

			;WriteRegStr 	HKCR "*\shell\$AppName: Create: Default\command" "" '$PythonCmd "$Dir_K7Z\Source\$AppFileName" "-cd" "%1"'
			;WriteRegStr 	HKCR "*\shell\$AppName: Create: Storage\command" "" '$PythonCmd "$Dir_K7Z\Source\$AppFileName" "-cs" "%1"'
			WriteRegStr 	HKCR "*\shell\$AppName: Create ...\command" "" '$PythonCmd "$Dir_K7Z\Source\$AppFileName" "-c" "%1"'
			;WriteRegStr 	HKCR "*\shell\$AppName: Extract: Default\command" "" '$PythonCmd "$Dir_K7Z\Source\$AppFileName" "-ed" "%1"'
			WriteRegStr 	HKCR "*\shell\$AppName: Extract ...\command" "" '$PythonCmd "$Dir_K7Z\Source\$AppFileName" "-e" "%1"'

			;WriteRegStr 	HKCR "*\shell\$AppName: Test\command" "" '$PythonCmd "$Dir_K7Z\Source\$AppFileName" "-td" "%1"'

		SectionEnd
		*/

		Section "Neat" Sec-I-ShellMenu-Neat

			; Replace with correct path
			StrCpy $R0 0
			${LineFind} "$Dir_K7Z\Build\K7Z.reg" "" "1:-1" "ReplaceString"
			;IfErrors 0 +2
			;MessageBox MB_OK "Error" IDOK +2
			;MessageBox MB_OK "Changed lines=$R0"

			; Merge information into the Registry
			StrCpy 	$OUTDIR	"$Dir_K7Z\Build\"
			ExecShell "" "$Dir_K7Z\Build\K7Z.reg"

		SectionEnd

		Section /o "Messy" Sec-I-ShellMenu-Messy

			;WriteRegStr 	HKCR "$AppName.1\Shell" "" 'None'
			;WriteRegStr 	HKCR "$AppName.1\Shell\$AppName: Create: Default\command" "" '$PythonCmd "$Dir_K7Z\Source\$AppFileName" "-cd" "%1"'
			;WriteRegStr 	HKCR "$AppName.1\Shell\$AppName: Create: Storage\command" "" '$PythonCmd "$Dir_K7Z\Source\$AppFileName" "-cs" "%1"'
			;WriteRegStr 	HKCR "$AppName.1\Shell\$AppName: Create ...\command" "" '$PythonCmd "$Dir_K7Z\Source\$AppFileName" "-c" "%1"'

			WriteRegStr 	HKCR "Directory\shell" "" 'None'
			WriteRegStr 	HKCR "Directory\shell\$AppName: Create: Default\command" "" '$PythonCmd "$Dir_K7Z\Source\$AppFileName" "-cd" "%1"'
			WriteRegStr 	HKCR "Directory\shell\$AppName: Create: Storage\command" "" '$PythonCmd "$Dir_K7Z\Source\$AppFileName" "-cs" "%1"'
			WriteRegStr 	HKCR "Directory\shell\$AppName: Create ...\command" "" '$PythonCmd "$Dir_K7Z\Source\$AppFileName" "-c" "%1"'

			WriteRegStr 	HKCR "*\shell\$AppName: Create: Default\command" "" '$PythonCmd "$Dir_K7Z\Source\$AppFileName" "-cd" "%1"'
			WriteRegStr 	HKCR "*\shell\$AppName: Create: Storage\command" "" '$PythonCmd "$Dir_K7Z\Source\$AppFileName" "-cs" "%1"'
			WriteRegStr 	HKCR "*\shell\$AppName: Create ...\command" "" '$PythonCmd "$Dir_K7Z\Source\$AppFileName" "-c" "%1"'
			WriteRegStr 	HKCR "*\shell\$AppName: Extract: Default\command" "" '$PythonCmd "$Dir_K7Z\Source\$AppFileName" "-ed" "%1"'
			WriteRegStr 	HKCR "*\shell\$AppName: Extract: Beneath\command" "" '$PythonCmd "$Dir_K7Z\Source\$AppFileName" "-ebd" "%1"'
			WriteRegStr 	HKCR "*\shell\$AppName: Extract ...\command" "" '$PythonCmd "$Dir_K7Z\Source\$AppFileName" "-e" "%1"'

			WriteRegStr 	HKCR "*\shell\$AppName: Test\command" "" '$PythonCmd "$Dir_K7Z\Source\$AppFileName" "-td" "%1"'

		SectionEnd

	SectionGroupEnd

	Section "UnInstaller" Sec-I-UnInstaller

		WriteRegStr 	HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\$AppName" "DisplayName" "$AppName $AppVer - Basic Archiver"
		WriteRegStr 	HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\$AppName" "UninstallString" "$Dir_K7Z\$AppName-UnInstall.EXE"
		WriteRegStr 	HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\$AppName" "Publisher" "Chris Giles"
		WriteRegStr 	HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\$AppName" "HelpLink" "http://k7z.SourceForge.net/"
		WriteRegDWORD 	HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\$AppName" "NoModify" 1
		WriteRegDWORD 	HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\$AppName" "NoRepair" 1
		WriteRegDWORD 	HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\$AppName" "VersionMajor" 0
		WriteRegDWORD 	HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\$AppName" "VersionMinor" 6

	SectionEnd

SectionGroupEnd

;--------------------------------
; Descriptions

	;Language strings (English)
	LangString DESC_Sec-Qt	 				${LANG_ENGLISH} "Launches the Qt website to facilitate the downloading of this prerequisite"
	LangString DESC_Sec-K7Z 				${LANG_ENGLISH} "Installs $AppName $AppVer"
	LangString DESC_Sec-7Zip 				${LANG_ENGLISH} "Launches the 7-Zip website to facilitate the downloading of this prerequisite"
	LangString DESC_Sec-PyQt				${LANG_ENGLISH} "Launches the PyQt website to facilitate the downloading of this prerequisite"
	LangString DESC_Sec-MinGW 				${LANG_ENGLISH} "Launches the MinGW website to facilitate the downloading of this prerequisite"
	LangString DESC_Sec-Python 				${LANG_ENGLISH} "Launches the Python website to facilitate the downloading of this prerequisite"
	LangString DESC_Sec-FileMenuTools		${LANG_ENGLISH} "Launches the 'FileMenu Tools' website to facilitate the downloading of this prerequisite"
	LangString DESC_Sec-ShortCuts 			${LANG_ENGLISH} "Adds an 'Archiving\$AppName' folder to the Start Menu"
	;LangString DESC_Sec-ShellMenu-Common	${LANG_ENGLISH} "Adds common '$AppName' entries to Explorer's Shell Menu"
	LangString DESC_Sec-ShellMenu-Neat		${LANG_ENGLISH} "Adds '$AppName' entries neatly to Explorer's Shell Menu"
	LangString DESC_Sec-ShellMenu-Messy		${LANG_ENGLISH} "Adds '$AppName' entries messily to Explorer's Shell Menu"
	LangString DESC_Sec-UnInstaller 		${LANG_ENGLISH} "Adds a '$AppName' entry to the Control Panel's 'Add/Remove Programs'"

	;Assign language strings to sections
	!insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
		!insertmacro 	MUI_DESCRIPTION_TEXT ${Sec-I-Qt} 					$(DESC_Sec-Qt)
		!insertmacro 	MUI_DESCRIPTION_TEXT ${Sec-I-K7Z}					$(DESC_Sec-K7Z)
		!insertmacro 	MUI_DESCRIPTION_TEXT ${Sec-I-7Zip}	 				$(DESC_Sec-7Zip)
		!insertmacro 	MUI_DESCRIPTION_TEXT ${Sec-I-PyQt} 					$(DESC_Sec-PyQt)
		!insertmacro 	MUI_DESCRIPTION_TEXT ${Sec-I-MinGW} 				$(DESC_Sec-MinGW)
		!insertmacro 	MUI_DESCRIPTION_TEXT ${Sec-I-Python} 				$(DESC_Sec-Python)
		!insertmacro 	MUI_DESCRIPTION_TEXT ${Sec-I-FileMenuTools}			$(DESC_Sec-FileMenuTools)
		!insertmacro 	MUI_DESCRIPTION_TEXT ${Sec-I-ShortCuts} 			$(DESC_Sec-ShortCuts)
		;!insertmacro 	MUI_DESCRIPTION_TEXT ${Sec-I-ShellMenu-Common} 		$(DESC_Sec-ShellMenu-Common)
		!insertmacro 	MUI_DESCRIPTION_TEXT ${Sec-I-ShellMenu-Neat} 		$(DESC_Sec-ShellMenu-Neat)
		!insertmacro 	MUI_DESCRIPTION_TEXT ${Sec-I-ShellMenu-Messy}		$(DESC_Sec-ShellMenu-Messy)
		!insertmacro 	MUI_DESCRIPTION_TEXT ${Sec-I-UnInstaller} 			$(DESC_Sec-UnInstaller)
	!insertmacro MUI_FUNCTION_DESCRIPTION_END


;--------------------------------
; Uninstaller Section

SectionGroup /e "un.Program"

	Section "un.K7Z"

		; SetAutoClose true

		ReadRegStr $Dir_K7Z HKLM "Software\Archiving\$AppName" "Path"

		StrCmp 	$Dir_K7Z "" Skipped

			RMDir /r "$Dir_K7Z\Build\"
			RMDir /r "$Dir_K7Z\Desktop\"
			RMDir /r "$Dir_K7Z\Doc\"
			RMDir /r "$Dir_K7Z\Source\"

			Delete "$Dir_K7Z\$AppName-UnInstall.EXE"

			DeleteRegKey HKLM "SOFTWARE\Archiving\$AppName"

		Skipped:

	SectionEnd

SectionGroupEnd

SectionGroup /e "un.Windows"

	Section "-un.ShortCuts"

		!insertmacro 	MUI_STARTMENU_GETFOLDER Application $MUI_TEMP

		; Delete empty start menus
		Delete 	"$SMPROGRAMS\$MUI_TEMP\*.LNK"
		StrCpy 	$MUI_TEMP "$SMPROGRAMS\$MUI_TEMP"

		startMenuDeleteLoop:

			RMDir /r $MUI_TEMP
			GetFullPathName $MUI_TEMP "$MUI_TEMP\.."

			IfErrors startMenuDeleteLoopDone

			StrCmp $MUI_TEMP $SMPROGRAMS startMenuDeleteLoopDone startMenuDeleteLoop

		startMenuDeleteLoopDone:

	SectionEnd

	SectionGroup /e "un.Shell Menu"

		Section "-un.Neat"

		SectionEnd

		Section "un.Messy"

			DeleteRegKey 	HKCR "$AppName.1"

			DeleteRegKey 	HKCR "Directory\shell\$AppName: Create: Default"
			DeleteRegKey 	HKCR "Directory\shell\$AppName: Create: Storage"
			DeleteRegKey 	HKCR "Directory\shell\$AppName: Create ..."

			DeleteRegKey 	HKCR "*\shell\$AppName: Create: Default"
			DeleteRegKey 	HKCR "*\shell\$AppName: Create: Storage"
			DeleteRegKey 	HKCR "*\shell\$AppName: Create ..."

			DeleteRegKey 	HKCR "*\shell\$AppName: Extract: Default"
			DeleteRegKey 	HKCR "*\shell\$AppName: Extract ..."

			DeleteRegKey 	HKCR "*\shell\$AppName: Test"

		SectionEnd

	SectionGroupEnd

	Section "un.UnInstaller"

		DeleteRegKey 	HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\$AppName"

	SectionEnd

SectionGroupEnd

;--------------------------------
; Functions Section

Function 	.onInit

	StrCpy 			"$AppName" 			"K7Z"
	StrCpy 			"$AppFileName"		"K7Z.pyw"
	StrCpy 			"$AppVer"			"0.6"
	StrCpy			"$PythonCmd"		"Python"

	; Previous path
	ReadRegStr 		$Dir_K7Z 	HKLM 	"SOFTWARE\Archiving\$AppName" "Path"

	StrCmp $Dir_K7Z "" Default_K7Z

    Default_K7Z:
		StrCpy 			"$Dir_K7Z" 			"C:\Program Files\Archiving\$AppName\"

	;!insertmacro MUI_LANGDLL_DISPLAY

FunctionEnd

Function 	un.onInit

	StrCpy 			"$AppName" 			"K7Z"
	StrCpy 			"$AppFileName"		"K7Z.pyw"
	StrCpy 			"$AppVer"			"0.6"

	;!insertmacro MUI_LANGDLL_DISPLAY

FunctionEnd

Function	ReplaceString

	StrCpy $1 $R9

	${WordReplace} '$Dir_K7Z' '\' '\\' '+*' $Dir_K7Z_DB
	${WordReplace} '$R9' 'C:\\Program Files\\Archiving\\$AppName' '$Dir_K7Z_DB' '+*' $R9

	;StrCmp $1 $R9 +2
	;IntOp $R0 $R0 + 1
	;$R0   count of changed lines

	Push $0

FunctionEnd
