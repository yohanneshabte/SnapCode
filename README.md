# SnapCode
Im still looking for a good name for this so feel free to suggest one :)

## Why?
I just found a way to download snapcodes with or without the Bitmoji on them and thought it was really cool. Also, since SnapChat does not have an API, I found this to be even cooler because the method I used to get the snapcodes could be used in an unofficial SnapChat API in the future.

## Installation
```
$ git clone https://github.com/sdushantha/SnapCode.git
```
## Usage
```bash
usage: snapcode.py [-h] [-v] -u USERNAME [-b {True,False}]
```
The ```-b``` command lets you choose if you want Bitmoji face on the snapcode. If you put ```False```, the snapcode will just have the normal ghost.

The file will download to the directory where you ran ```snapcode.py``` from.
