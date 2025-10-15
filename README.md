# WeeWX-SetProcessName
WeeWX extension to change the process name to any desired text.

# Description
Have you ever done `ps -A |grep weewx` only to find that it returned nothing?  WeeWX has traditionally shown in the process list as just "python" or "python3".

This extension changes that. By default it sets the name to "weewxd", but you can set it to whatever name you desire. Now one can use applications such as Zabbix to monitor the status of weewx by its name.  If you run multiple instances of WeeWX on the same machine, you can set each instance to a unique name.

# Installation
This extension requires python setproctitle. Install it in a manner appropriate for your environment. For example:

**PIP**
```
sudo pip install setproctitle
```
**APT**
```
sudo apt install python3-setproctitle
```
**DNF**
```
sudo dnf install python3-setproctitle
```

**Use weectl to install the exension**
```
sudo weectl extension install https://github.com/knight-of-ni/WeeWX-SetProcessName/archive/master.zip
```
The default process name is "weewxd". If you wish to change that, change the name parameter found under [SetProcessName] in weewx.conf.
