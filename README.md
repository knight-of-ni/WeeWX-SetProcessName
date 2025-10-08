# WeeWX-SetProcessName
WeeWX extension to change the process name to any desired text.

# Description
Have you ever done `ps -A |grep weewx` only to find that it returned nothing?  WeeWX has traditionally shown in the process list as just "python" or "python3".

This extension changes that. By default it sets the name to "weewxd", but you can set it to whatever name you desire. Now one can use applications such as Zabbix to monitor the status of weewx by its name.  If you run multiple instances of WeeWX on the same machine, you can now set each to its own name.

# Installation

```
sudo apt install python3-setproctitle
sudo weectl extension install https://github.com/knight-of-ni/WeeWX-SetProcessName/archive/master.zip
```
