
---


# Contents #



---


# 1.1.5 #

## All ##

  * Unlocked two more modern 7-Zip compression algorithms

## Linux ##

  * Nautilus and Thunar context menus install at runtime

## Windows ##

  * Start menu entry no longer requires file associations


---


# 1.1.0 #

## All ##

  * Skins and styles can be randomised each session
  * Added support for more downloadable skins and styles
  * Clearing the history also cleans 'Output' directory
  * Improved the batch-mode command-line arguments
  * Any profile can be specified at the command-line
  * Error message shown when skin/style change failed
  * Corrected handling when previous skin is absent
  * List of JAR files is now sorted before searching
  * Fixed profile handling if a combo-box has the focus
  * Output directory is always checked before archiving
  * Made several minor changes to the code structure

## Linux ##

  * Removed Apache-Ant check when source is absent


---


# 1.0.1 #

## All ##

  * Changed the method used for viewing files
  * Tidied up much of the archiving thread code

## Linux ##

  * The prebuilt archive doesn't need the JDK
  * GNU Tar is no longer a mandatory dependency
  * BSD-Tar can now be used instead of GNU-Tar
  * Forced the Makefile to build in serial mode


---


# 1.0.0 #

## All ##

  * Ported the #7Z and Q7Z source code to Java SE
  * The application was renamed to J7Z accordingly
  * This means both #7Z and Q7Z are now deprecated
  * The GUI is now skinnable via downloadable L&Fs
  * External options can be configured via the GUI
  * The 'Profile' menu has been simplified slightly
  * Added the 'Switches' capability for extractions
  * Removed two rarely used GUI options for clarity
  * Changed the on-disk format of archiving profiles
  * Made several minor changes to the code structure

## Linux ##

  * Makefile checks dir/file permissions were set

## Windows ##

  * Installer now downloads dependencies at runtime


---


# 0.9.1 #

## All ##

  * Added the ability to toggle the Auto-Quit state
  * Enhanced the information notification techniques
  * Improvements were made to the update checking code
  * Made several minor changes to the code structure


---


# 0.9.0 #

## All ##

  * Custom volume sizes can be specified and saved
  * Added MRU lists to text fields for convenience
  * Contents of MRU lists can be cleared if desired
  * Moved 'Name' fields to add room for 'Dir' fields
  * The dialog box sizes are now fully adjustable
  * Dialog widgets are now auto-spaced for clarity
  * The main form size is remembered between sessions
  * Improved the clarity of the licensing conditions
  * Added a link to each license in the 'Help' menu
  * Made several minor changes to the code structure

## Linux ##

  * Upgraded the source code for Python v3 support
  * Increased the effectiveness of the 'Stop' button
  * The Makefile enforces building before installing
  * Made some structural improvements to the Makefile
  * Added basic build and installation instructions
  * Deprecated distribution-specific build scripts

## Windows ##

  * Profiles and lists are stored in per-user area
  * The '7zG' executable-locating code was improved
  * Several aspects of the installer were enhanced


---


# 0.8.1 #

## Windows ##

  * Now works on 32/64-bit versions of Windows XP/Vista/7
  * Restructured the layout of the Shell Menu for clarity
  * Added the "All Files" search filter when finding archives
  * Changed recursion switch to stop finding non-wildcards


---


# 0.8.0 #

## All ##

  * Main dialog: redesigned to reduce clutter
  * Switches option: to add custom command-line arguments
  * Icons: borrowed from the Oxygen theme when possible
  * Menu entries: added 'Verbose' and 'Review' for debugging
  * Verbose mode: now more consistently implemented
  * Tarball option: removed to simplify the execution code
  * Code structure: several minor changes

## Linux ##

  * Options files: to choose preferred external apps
  * Autopackage script: is now available for all distributions
  * Help menu: added a link to the Autopackage website
  * XZ format: is now also available for compression
  * KDE4 Service Menus: now feature the proper separators again
  * GNU Tar: is now used to create BZip2 and GZip archives
  * Permissions: are now preserved when extracting archives
  * Destination folder: is now created before archiving
  * Python processes: now use the new 'subprocess' module

## Windows ##

  * Dialog widgets: are now auto-spaced for clarity


---


# 0.7.5 #

## All ##

  * Documentation: now available in HTML thanks to Zim
  * Help menu: added a link to the Zim website
  * Code structure: several minor changes

## Linux ##

  * Paths: now looks beneath "~/.config/" for 'Lists' and 'Profiles'
  * KDE config script: now used to find user paths
  * Makefile: now checks for existence of dependencies
  * Context menu: initial integration in Gnome and Xfce
  * KDE 4: improved support for Dolphin and Konqueror
  * KDE 3: is no longer officially supported
  * Write access: to source dir for packaged installations
  * Extraction: UDF, XAR, LZMA and DMG/HFS archives are now recognised
  * Cron jobs: worked around new Qt 4.4 event-loop limitation
  * Licensing: now using the GNU General Public License v3
  * Dependencies raised: due to bugs below Qt 4.4.1 and PyQt 4.4.3
  * Recommendation: everyone should switch to Arch Linux

## Windows ##

  * Exclusions: ignore files and directories via wildcards
  * Installer: Improvements were made to the upgrading process
  * Position: of the main window is remembered between sessions


---


# 0.7.2 #

## Windows ##

  * Lists: manual 'Edit' option is now available
  * Local mode: 'l' option for sending archives to the current drive
  * Flash mode: 'f' option for sending archives to a flash disc
  * Remote mode: 'r' option for sending archives to a mounted remote site
  * Extraction: MSI and WIM archives are now recognised
  * Proxy support: now uses Internet Explorer proxy while updating


---


# 0.7.1 #

## Linux ##

  * Cron jobs: see the 'INSTALL' file for info
  * Lists: manual 'Edit' option is now available
  * Auto-exit: if operation fails when in invisible mode
  * Updating: fixed bug when proxy env variable is missing
  * Updating: no longer checks when in invisible mode
  * Invisible mode: no longer loads the QtGui module
  * Help menu: added a link to the Eric website
  * KDE 4: initial although limited support
  * Code structure: several changes

## Windows ##

  * Help menu and icons: subtle improvements
  * Structured fix: now keeps the initial tarball in the current directory


---


# 0.7.0 #

## All ##

  * Lists: for storing links to frequently archived dirs and files
  * List mode: 'L' option to specify a list file at the command-line
  * Separate mode: to create a different archive for each input
  * Flash profile: for transporting archives compatibly
  * Profiles: changed some compression and output path defaults
  * Code structure: several changes

## Linux ##

  * Exclusions: ignore files and directories via wildcards
  * Local mode: 'l' option for sending archives to the current drive
  * Proxy support: now uses 'http\_proxy' env variable while updating
  * Tests: for the existence of required external binaries when starting
  * Position: of the main window is remembered between sessions
  * Updating: removed the extra error dialogs when offline
  * Extraction: MSI and WIM archives are now recognised
  * Structured fix: now keeps the initial tarball in the current directory

## Windows ##

  * Update checking: threaded and improved code section
  * Multiple input files: can now be combined into an archive
  * Tooltips: for several dialog items
  * Profile saving: removed the inability to create a new filename
  * Profile actions: improved status strip message in certain cases
  * Licensing: Now using the GNU General Public License v3
  * Verbose mode: 'v' option for debugging purposes
  * URL links: for Fast Explorer and SharpDevelop in Help menu


---


# 0.6.3 #

## Linux ##

  * Remote mode: 'r' option for sending archives to a mounted remote site
  * Konq Service Menu: included separator and reordered the entries
  * Error message: is now displayed when the failed operation returned nothing
  * Error message: removed after the user cancels a profiling operation
  * Profile names: Now enforcing the ".txt" extension when saving profiles
  * Profile actions: improved status strip message in certain cases
  * Operation feedback: now slightly more accurate
  * Code structure: several minor changes


---


# 0.6.2 #

## Linux ##

  * Flash profile: for transporting archives compatibly
  * Flash mode: 'f' option for sending archives to a flash disc
  * Profile location: fixed a minor relocation issue


---


# 0.6.1 #

## All ##

  * Update option: to check for a newer release
  * Auto Updates: notification when a newer release is available
  * Help menu: subtle improvements
  * Code structure: several minor changes

## Linux ##

  * Application: renamed to Q7Z since it uses Qt
  * GUI: compressed the dialog item spacing

## Windows ##

  * MS NET Framework 2: now used instead of PyQt4
  * Coding language: switched to C# from Python


---


# 0.6.0 #

## All ##

  * Beneath option: to extract below the destination
  * Exception handling: possible crashes prevented
  * Code structure: now modular to increase efficiency

## Linux ##

  * GNU Tar: is now used to preserve file permissions
  * Invisible mode: 'i' option to hide the GUI
  * Verbose mode: 'v' option for debugging purposes
  * Extraction: now works properly in Slackware
  * CheckInstall: separate scripts for RedHat, Debian, Slackware
  * Slackware package: available thanks to 'LocoMojo'
  * Makefile: possible errors prevented
  * Write access: to source dir for performance increase

## Windows ##

  * Explorer: improved Shell Menu layout


---


# 0.5.0 #

## All ##

  * Profiles: to increase efficiency and variety
  * Destination option: to send the archive elsewhere
  * Structured option: to mirror source dir structure at destination
  * Documentation: now available from Help menu
  * Spanned archives: Recognition and testing
  * Toolbar: removed to speed up code execution
  * URLs: more efficient handling
  * Executable: extension renamed to .pyw
  * Code structure: several minor changes

## Linux ##

  * Installation: must now "cd Build/ ; make" first
  * Storage option: to the Konq Service Menu; set a storage location first!
  * Distribution: reduced file-sizes

## Windows ##

  * Initial support: read INSTALL.txt first for dependencies


---


# 0.4.1 #

## Linux ##

  * Qt 4.2: compatibility fixes
  * Icons: sync (left) and update (up)
  * Code structure: minor changes


---


# 0.4.0 #

## Linux ##

  * Sync option: exclude files removed from disc since last update of archive
  * Settings dialog: to allow for differing user preferences
  * Menubar: to house extra features
  * Toolbar: for common features
  * Statusbar: for feedback text
  * Titlebar: now reflects the current status
  * URLs: for the related websites
  * Source Files: permissions now reflect the file types
  * Code structure: minor changes


---


# 0.3.5 #

## Linux ##

  * Stop button: to cancel archiving
  * Fixed size:
    * CD: 720,000 KiB ≈ 703.1 MiB
  * Main dialog: inflexible extents
  * Tab ordering: is now more logical
  * Code structure: minor changes


---


# 0.3.0 #

## Linux ##

  * Scramble option: encrypt archive headers
  * Volumes option: and associated icons
    * Floppy: 1440 KiB ≈ 1.4 MiB
    * CD: 720,000 KiB ≈ 703.1 MiB
    * DVD: 4589843.75 KiB ≈ 4.3 GiB
  * Tarball option:
    * Manually: to create a tarball before archiving
    * Automatically: for BZip2 and GZip archives
  * GUI: is now more efficient
  * Homepage link: next to the feedback buttons
  * Usage statement: available via the 'h' command-line option
  * Code structure: has been improved


---


# 0.2.5 #

## Linux ##

  * Multiple file support: from the Konq Service Menu
  * Feedback buttons: for sending good or bad feedback to the author
  * Konq Service Menu: devices and media are now excluded
  * Print statements: turned off if successful


---


# 0.2.0 #

## Linux ##

  * Threaded operation: prevents the GUI from temporarily locking up
  * K Menu entry: Utilities --> File --> Q7Z
  * Konqueror Service Menu entries: Right-Click --> Actions --> Q7Z
    * If you think the Q7Z entry should be on the top level (i.e. next to Ark's entries), let me know.
  * Ark's icons: 'add folder' and 'extract'
  * 7-Zip's icon: in the K Menu and Konqueror Service Menu entries
  * Package specification: (.spec) file for use with 'CheckInstall'
  * ./CheckInstall script: to automate the process of using 'CheckInstall'
    * Tested only on Fedora Core 5 but should work on Debian & Slackware variants
    * Can anyone confirm that this is correct?
    * Send me the package and I'll happily post it here.


---


# 0.1.0 #

## Linux ##

  * Archives: folders
  * Extracts: archives
  * Tests: archives