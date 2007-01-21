### K7Z Makefile


# Defines

ifndef KDEDIR
	KDEDIR = /usr/
endif

ifndef USER
	USER = $(LOGNAME)
endif

ifndef HOME
	HOME = /home/$(USER)/
endif


# Aliases

all: Main_Ui.py Main_RCC.py Settings_Ui.py Settings_RCC.py
	@echo ""
	@echo "Making K7Z.  Before installing K7Z, please peruse the README."
	@echo ""


install: Install.AllUsers


install-user: Install.CurrentUser


uninstall: UnInstall.AllUsers


uninstall-user: UnInstall.CurrentUser


clean:
	@echo ""
	@echo "Cleaning the K7Z objects."
	@echo ""
	rm -f ../Source/Main_*
	rm -f ../Source/Settings_*
	rm -f ../Source/*.pyc
	@echo ""
	@echo "The K7Z objects have been cleaned."
	@echo ""


# Installers

Install.AllUsers :
	@echo ""
	@echo "Installing K7Z for all users."
	@echo "Only root can run 'make install'.  Others should instead run: 'make install-user'"
	@echo "Before using this unstable script, please thoroughly read the Installation section of the README."
	@echo ""
	make uninstall
	make clean
	make all
	mkdir -p $(KDEDIR)/share/apps/K7Z/
	cp -r ../Doc/ $(KDEDIR)/share/apps/K7Z/
	cp -r ../Desktop/ $(KDEDIR)/share/apps/K7Z/
	cp -r ../Source/ $(KDEDIR)/share/apps/K7Z/
	chmod 777 $(KDEDIR)/share/apps/K7Z/Source/
	chmod 775 $(KDEDIR)/share/apps/K7Z/Source/K7Z.pyw
	mkdir -p $(KDEDIR)/bin/
	ln -fs $(KDEDIR)/share/apps/K7Z/Source/K7Z.pyw $(KDEDIR)/bin/K7Z.pyw
	mkdir -p $(KDEDIR)/share/apps/konqueror/servicemenus/
	cp -u ../Desktop/Context/Live/* $(KDEDIR)/share/apps/konqueror/servicemenus/
	rm -f ~$(USER)/.kde/share/apps/konqueror/servicemenus/K7Z*
	mkdir -p $(KDEDIR)/share/applnk/Utilities/File/
	cp ../Desktop/KMenu/* $(KDEDIR)/share/applnk/Utilities/File/
	mkdir -p $(KDEDIR)/share/icons/hicolor/32x32/actions/
	ln -fs $(KDEDIR)/share/apps/K7Z/Source/Images/actions/ark* $(KDEDIR)/share/icons/hicolor/32x32/actions/
	mkdir -p $(KDEDIR)/share/icons/hicolor/32x32/apps/
	ln -fs $(KDEDIR)/share/apps/K7Z/Source/Images/apps/K7Z* $(KDEDIR)/share/icons/hicolor/32x32/apps/
	@echo ""
	@echo "Finished.  To run K7Z, enter: K7Z.pyw &"
	@echo ""

Install.CurrentUser :
	@echo ""
	@echo "Installing K7Z for current user.  In the case of errors, please view the README."
	@echo ""
	make uninstall-user
	make clean
	make all
	mkdir -p $(HOME)/.kde/share/apps/K7Z/
	cp -r ../Doc/ $(HOME)/.kde/share/apps/K7Z/
	cp -r ../Desktop/ $(HOME)/.kde/share/apps/K7Z/
	cp -r ../Source/ $(HOME)/.kde/share/apps/K7Z/
	chmod 775 $(HOME)/.kde/share/apps/K7Z/Source/K7Z.pyw
	mkdir -p $(HOME)/bin/
	ln -fs $(HOME)/.kde/share/apps/K7Z/Source/K7Z.pyw $(HOME)/bin/K7Z.pyw
	mkdir -p $(HOME)/.kde/share/apps/konqueror/servicemenus/
	#rm -f $(HOME)/.kde/share/apps/konqueror/servicemenus/K7Z.marker.*
	rm -f $(HOME)/.kde/share/apps/konqueror/servicemenus/K7Z*
	cp -u ../Desktop/Context/Live/* $(HOME)/.kde/share/apps/konqueror/servicemenus/
	mkdir -p $(HOME)/.kde/share/applnk/Utilities/File/
	cp ../Desktop/KMenu/* $(HOME)/.kde/share/applnk/Utilities/File/
	mkdir -p $(HOME)/.kde/share/icons/hicolor/32x32/actions/
	ln -fs $(HOME)/.kde/share/apps/K7Z/Source/Images/actions/ark* $(HOME)/.kde/share/icons/hicolor/32x32/actions/
	mkdir -p $(HOME)/.kde/share/icons/hicolor/32x32/apps/
	ln -fs $(HOME)/.kde/share/apps/K7Z/Source/Images/apps/K7Z* $(HOME)/.kde/share/icons/hicolor/32x32/apps/
	@echo ""
	@echo "Finished.  You should add $(HOME)/bin to the PATH variable in your ~/.bash_profile or equivalent."
	@echo "Then restart KDE.  To run K7Z, enter: K7Z.pyw &"
	@echo ""


# Uninstallers

UnInstall.AllUsers :
	@echo ""
	@echo "Removing K7Z for all users."
	@echo "Only root can run 'make uninstall'.  Others should instead run: 'make uninstall-user'"
	@echo "Before using this unstable script, please thoroughly read the UnInstallation section of the README."
	@echo ""
	rm -f $(KDEDIR)/share/icons/hicolor/32x32/actions/ark*
	rm -f $(KDEDIR)/share/icons/hicolor/32x32/apps/K7Z*
	rm -f $(KDEDIR)/share/apps/konqueror/servicemenus/K7Z*
	rm -f $(KDEDIR)/share/applnk/Utilities/File/K7Z*
	rm -f $(KDEDIR)/bin/K7Z*
	rm -rf $(KDEDIR)/share/apps/K7Z/
	rm -f ~$(USER)/.kde/share/apps/konqueror/servicemenus/K7Z*
	@echo ""
	@echo "K7Z has been removed."
	@echo ""

UnInstall.CurrentUser :
	@echo ""
	@echo "Removing K7Z for current user.  In the case of errors, please view the README."
	@echo ""
	rm -f $(HOME)/.kde/share/icons/hicolor/32x32/actions/ark*
	rm -f $(HOME)/.kde/share/icons/hicolor/32x32/apps/K7Z*
	rm -f $(HOME)/.kde/share/apps/konqueror/servicemenus/K7Z*
	rm -f $(HOME)/.kde/share/applnk/Utilities/File/K7Z*
	rm -f $(HOME)/bin/K7Z*
	rm -rf $(HOME)/.kde/share/apps/K7Z/
	@echo ""
	@echo "K7Z has been removed."
	@echo ""


# Objects

Main_Ui.py :
	pyuic4 ../Source/Main.ui -o ../Source/Main_ui.py

Main_RCC.py :
	pyrcc4 ../Source/Main.qrc -o ../Source/Main_rc.py

Settings_Ui.py :
	pyuic4 ../Source/Settings.ui -o ../Source/Settings_ui.py

Settings_RCC.py :
	pyrcc4 ../Source/Settings.qrc -o ../Source/Settings_rc.py
