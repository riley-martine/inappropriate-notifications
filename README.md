# inappropriate-notifications
Ever want to get inappropriate notifications while you're presenting? Well now you can!

Based off of the homepage of https://muzzleapp.com/

Using notifications from https://muzzleapp.com/notifications/notifications.json

Using users from https://randomuser.me

## Requirements
python3.6+

## Usage
`python notify.py <time between notifications (optional)>`

## Caveats (To fix)
* Only tested on linux
* Relies on notify-send
* Icons are for Mac apps and need to be replaced with the ones you use
* Notifications don't stay very long
* No fields on notifications (reply, dismiss) where applicable
* Does not pull names/images from people you know when applicable
* Only suited to work env -- students don't need messages about getting fired
