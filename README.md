# [TelegramIFTTTMacroDroidStats](https://github.com/viduxsh/TelegramIFTTTMacroDroidStats)

[![LICENSE](https://img.shields.io/badge/license-MIT-lightgrey.svg)](https://github.com/viduxsh/TelegramIFTTTMacroDroidStats/blob/main/LICENSE)

 A script that scan a json telegram chat and creates graphs.

## How it works
### The project works with MacroDroid, IFTTT and Telegram
### You have to set Macrodroid with a trigger notification on battery % change.
### The notification made by MacroDroid is like:
#### Title:
```
{device_manufacturer} {device_model} Android {android_version} SDK {android_version_sdk}
```
#### Notification text:
```
<br>Power {power}<br><br>{battery}%<br><br>{battery_temp}°C<br><br>{ssid}<br><br>{wifi_strength}dBm<br><br>{ip}<br><br>{ip6}<br><br>{last_loc_latlong}<br><br>{last_loc_speed_kmh}km/h<br><br>{system_time}
```
#### Settings: overwrite existing notification.
### Set IFTTT with:
```
if(
    Notification received from a specific app(AppName:MacroDroid)
)
then(
    Send telegram message(
        MessageText:<b>NotificationTitle</b><br>NotificationMessage<br><br>Received ReceivedAt,
    WebPagePreview:Enabled
    )
)
```
### The script needs a telegram chat export in json like this:
```
{
 "name": "IFTTT",
 "type": "bot_chat",
 "id": int,
 "messages": [{
   "id": int,
   "type": "message",
   "date": "yyyy-mm-ddThh:mm:ss",
   "date_unixtime": "unixtime",
   "from": "IFTTT",
   "from_id": "userid",
   "text": [
    {
     "type": "bold",
     "text": "Productor Phone Name Android N SDK N"
    },
    "\n\nPower On/Off\n\nbattery%\n\nbattery_temp°C\n\n",
    {
     "type": "bot_command",
     "text": "wifi_name"
    },
    "\n\nwifi_powerdBm\n\n",
    {
     "type": "link",
     "text": "ip"
    },
    "\n\nipv6\n\nlat,lon\n\nspeedkm/h\n\n",
    {
     "type": "phone",
     "text": "unixtime"
    },
    "\n\nReceived MOnth dd, yyyy at hh:mmAM/PM"
   ],
   "text_entities": [
    {
     "type": "bold",
     "text": "Productor Phone Name Android N SDK N"
    },
    {
     "type": "plain",
     "text": "\n\nPower On/Off\n\nbattery%\n\nbattery_temp°C\n\n"
    },
    {
     "type": "bot_command",
     "text": "wifi_name"
    },
    {
     "type": "plain",
     "text": "\n\nwifi_powerdBm\n\n"
    },
    {
     "type": "link",
     "text": "ip"
    },
    {
     "type": "plain",
     "text": "\n\nipv6\n\nlat,lon\n\nspeedkm/h\n\n"
    },
    {
     "type": "phone",
     "text": "unixtime"
    },
    {
     "type": "plain",
     "text": "\n\nReceived MOnth dd, yyyy at hh:mmAM/PM"
    }
   ]
  },
  {
    ...
  },
  {
    ...
  }
 ]
}
```