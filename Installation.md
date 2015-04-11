
---


# Contents #



---


# Dependencies #

## All ##

### Required ###

  * [Java](http://www.java.com/) v1.6

## Linux ##

### Required ###

  * [Make](http://www.gnu.org/software/make/), [P7Zip](http://p7zip.sourceforge.net/)

#### P7Zip ####

  * The full package includes '7z', '7za' and '7zr' binaries.
  * '7z' operates on a wider range of archive types, which is preferred.
  * Fedora users should install both the "p7zip" and "p7zip-plugins" packages.

### Recommended ###

  * [Tar](http://www.gnu.org/software/tar/), [GZip](http://www.gzip.org/), [BZip2](http://bzip.org/), [XZ](http://tukaani.org/xz/)


---


# Installation #

## All ##

Ensure that you've installed the applications listed in the above 'Dependencies' section first.

## Linux ##

### Build ###

```
cd Build
make all
```

### Install ###

#### System ####
```
cd Build
sudo make install
```

#### User ####
```
cd Build
make install-user
```

Add `$HOME/bin/` to the `$PATH` variable in your `~/.bash_profile` or equivalent and restart KDE.

### File Managers ###

  * J7Z shell menus are available for the file managers of the major desktop environments.
  * KDE (Dolphin), Gnome (Nautilus) and Xfce (Thunar) are currently supported.
  * The relevant configuration files should be copied from the 'Desktop' directory.

## Windows ##

### Install ###

#### System ####

  * Launch the J7Z setup executable file and follow the installation instructions


---


# Removal #

## Linux ##

### Uninstall ###

#### System ####
```
cd Build
sudo make uninstall
```

#### User ####
```
cd Build
make uninstall-user
```

## Windows ##

### Uninstall ###

#### System ####
Start Menu --> All Programs --> Archiving --> J7Z --> UnInstall