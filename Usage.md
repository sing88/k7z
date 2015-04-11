
---


# Contents #



---


# Application Menus #

Launch Q7Z/#7Z from the following application menus.

## Linux ##

K Menu --> Utilities --> Q7Z

## Windows ##

Start Menu --> All Programs --> Archiving --> #7Z


---


# Context Menus #

Right-click on directories and/or files within the following applications to view the Q7Z/#7Z context menus.

## Linux ##

Konqueror, Dolphin, Nautilus, Thunar

## Windows ##

Windows Explorer


---


# Proxy #

## Linux ##

The proxy server defined by your `$http_proxy` environment variable will be used.  For example, add the following to your `~/.bash_profile` or equivalent and restart KDE:

```
export http_proxy=http://[user:password@]proxy.isp.com[:80]/
```


---


# Scheduling #

## Linux ##

### Cron ###

In your three-hourly cron directory, create an executable shell script like the following:

```
#!/bin/zsh


# Env
export DISPLAY=:0

# Local
if [ -w "/media/Exchange/Backup/J7Z/" ]; then
    /usr/bin/J7Z.sh aci -p "Local" -l "Personal"
    /usr/bin/J7Z.sh aci -p "Local" -l "Programming"
    /usr/bin/J7Z.sh aci -p "Local" -l "Work"
fi

# Storage
if [ -w "/media/Storage/Backup/J7Z/" ]; then
    /usr/bin/J7Z.sh aci -p "Storage" -l "Personal"
    /usr/bin/J7Z.sh aci -p "Storage" -l "Programming"
    /usr/bin/J7Z.sh aci -p "Storage" -l "Work"
fi
```

If it will be executed by 'root', create symbolic links to your `Profiles` and `Lists` dirs in equivalent dirs below `/root/`.