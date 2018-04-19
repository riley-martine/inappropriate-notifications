# Inappropriate Notifications
Ever want to get inappropriate notifications on your computer while you're presenting? Well now you can!

Based off of the homepage of https://muzzleapp.com/.
Check out their website to see an example of what this does.

This program uses notifications from https://muzzleapp.com/notifications/notifications.json, as well as those we came up with ourself.

User names and images downloaded from https://randomuser.me.

## Requirements
### Linux
python3.6+
libnotify

### Windows
python3.6+
win10toast (installed automatically)

## Usage
`git clone https://github.com/riley-martine/inappropriate-notifications.git`

`cd inappropriate-notifications`

`python3.6 setup.py install`

`inappropriate-notifications`

## Caveats (To fix / to do)
* Only tested on Ubuntu and Windows 10 (MacOS and Windows 7 on roadmap)
* Relies on libnotify on Linux
* Icons are for Mac apps and need to be replaced with the ones you use
* No fields on notifications (reply, dismiss) where applicable
* Does not pull names/images from people you know when applicable
* Only suited to work env -- students don't need messages about getting fired
* Not a pypi package
* No tests
* ctrl-c when running command line should fail nicer
* Right-to-left names mess up first line
