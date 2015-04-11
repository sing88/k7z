
---


# Contents #



---


# Bugs #

## All ##

  * It sometimes doesn't seem to extract archives with multiple dots (.) in the filename
    * I'm having trouble reproducing this
  * Finish all of the remaining TODO and FIXME statements

## Linux ##

  * Perhaps try to call the 7-Zip library directly
  * Can't update local existing archives on Kubuntu
    * This was okay during a recent brief test
  * Test the unRAR 'wrong password' seg fault, even with correct pass
    * Fedora P7Zip doesn't seem to contain the RAR plug-in
  * Fix slight error when saving window position upon exit, causing it to move slightly upon startup
    * Maybe this only happens when using Compiz or Beryl
  * The 'Profiles' dir created within 'home' isn't removed when installing the new RPM

## Windows ##

  * The GUI locks up totally when updating some faulty archives
    * This was happening at DC when saving to 'Zip' files on the formerly FAT32 flash disk
    * Find one such faulty archive and debug to find where to fix the problem


---


# Improvements #

## All ##

  * Perhaps implement a splash screen using 'QSplashScreen' or 'TBA'
  * Show icons with the menu entries along the menu-bar's top level
  * Keep adjusting the tab ordering, after modifying the forms
  * Once the P7Zip/7-Zip stdout issue is fixed
    * Smooth progress bar, percentage listed in titlebar
    * Perhaps call the DLLs directly to achieve this
    * This was partly solved by the existence of the new 7zG executable
  * Extract '.tar.gz' and '.tar.bz2' archives twice to prevent seeing the '.tar' afterwards
  * Nahuel's suggestions:
    * A file browser, for choosing what to compress or extract
      * Maybe this would go against the 'basic' philosophy of J7Z
  * Hayden's suggestions
    * Perhaps find a way to list files within archives before extracting them
  * 'Clear' buttons for easier removal of data within line-edits
  * Max' further suggestions
    * Continue with backups even if some of the files screw up
    * Or possibly test for read permission of the input files before archiving
    * 7-Zip might have fixed this already by ignoring shared files by default
    * Try to be more like Keep for Linux in terms of automation
    * Maybe there were other suggestions too
  * Perhaps relocate the ".tmp" files to the Windows Temp folder instead
    * This might slow down efficiency if the dest archive is on a different drive
  * Pop-up password dialog for protected archives
  * Start contacting more freeware websites, possibly automatically via a PAD.xml submitting application
  * Find a way to move more of the methods out of the 'fMain' source file
  * Choose a formal testing framework and implement key tests
  * Download the Javadoc archive and add comments to the top of methods in the source code

## Linux ##

  * Move all of the start-up code into a slot from a signal when the main form has finished loading, to get it displaying quicker
    * Perhaps use [[QShowEvent](QShowEvent.md)] with QApplication or [[QMainWindow](QMainWindow.md)] from QWidget
    * This could be tricky, as [[QShowEvent](QShowEvent.md)] is also called when a window is restored after being hidden
    * Perhaps copy across some of the code from #7Z
  * Bring across the improved 'SectionFlag' code from FcronQ
  * Consider submitting a building script to SlackBuilds.org
  * Consider exporting "App-Name=Q7Z" in the env to simplify the post-install/removal scripts for packages
  * Perhaps use common files between Q7Z and Quamachi
    * Settings, TODO
    * Also do this with some of the documentation files
  * Decide again whether to use 'bInvisible' from 'Import' or 'Settings'
  * Streamline all the "Main.uiMain" stuff into 'Display' behind 'bInvisible' tests
    * Then remove all of the fragmented 'bInvisible' tests in other modules
  * Context menu integration in Nautilus and Thunar
    * Nautilus is done, but try to make it file/mime-type dependent; see: http://g-scripts.sourceforge.net/faq.php
    * Thunar is done, but need to move the 'uca.xml' file without messing up the original
    * Also consider making the "Top Level" context menu option relevant for these
  * Once the P7Zip/7-Zip stdout bug is fixed
    * Use KDE 4 job progress list

## Windows ##

  * Perhaps convert 'Settings' static stuff into privates with a global instance
  * Icons in the 'Type' combo-boxes if possible
    * A custom combo-box is needed for Java v1.6; I might wait for v1.7
    * An example of how to implement this is clearly documented on the Java website
  * Try again to put the Q7Z icon in the NSIS installer
    * Maybe it's only supposed to be shown in the Start Menu and Control Panel
  * Recent Q7Z implementations
    * Use classes containing defs; see Eric's 'SplashScreen.py' for more info


---


# Features #

## All ##

  * Let users choose the window opacity percentage
  * Extraction of multiple archives
  * Compress and email option
  * Add 'Shutdown When Done' option
  * Keep checking for new archiving options

## Linux ##

  * Try to make it work on FreeBSD
  * Perhaps put it on CNR.com after trying Freespire (again)
  * Look into creating building scripts for Gentoo (Sabayon), Foresight and FreeBSD

## Windows ##

  * Look into using the "compress shared files (-ssw) feature
    * Ensure that it won't cause errors for currently open files


---


# Shelves #

## All ##

## Linux ##

  * Consider using quotes around file names that are sent to P7Zip
    * Then trim them when executing; pull the code from S7Z
  * Perhaps use Java's own Tar, Zip and BZip2 libraries (if they even exist)
  * Take a closer look at the SMPlayer .spec file
  * Perhaps convert build process to use Apache-Ant (more), CMake, QMake, SCons or Setup.py
  * Try these installers as possible alternatives
    * InstallJammer, Zero Install Injector, BitRock, Klik
    * Consider just using 7-Zip's SFX module that can add a post-extraction (installation) script

## Windows ##