# KEKSWITCH, (By SD)


# installation:

```
# <sudo / doas> apt-get install python-tk
//replace apt-get with your package manager

$ pip3 install cryptography

$ git clone https://github.com/Contaigen-II/kekswitch.git

$ cd kekswitch

$ chmod u+x install.sh

$ ./install.sh makefile
//note: Do NOT run this as root

# <sudo / doas> ./install.sh
```

# Uninstall

```
# <sudo / doas> rm -rf /tmp/kekswitch

# <sudo / doas> rm /usr/share/logo.png

# <sudo / doas> rm /usr/share/kekswitch

$ systemctl disable kekswitchctl

# <sudo / doas> rm /etc/systemd/system/kekswitchctl.service
```

# Changing max password retries

```
# <sudo / doas> nano /tmp/kekswitch/max-retries

//change the text here to a valid number, make sure to *NOT* add any extra lines by pressing enter.

//then, do ctrl + s, ctrl + x
```

The main reason I added this is as follows:

Potentially the user of kekswitch could have some family member[s] (kids, spouse, elders) that don't understand that messing with a killswitch could destroy or damage the PC.

If you believe that you fall under the above mentioned category of users, please follow these guidelines:

```
Back up your computer's files on an external drive; There are things other than kekswitch that could harm or delete your files, it's not paranoia it's just being smart.

If you think that people could accidentally trigger kekswitch, inform them about it.
```

I would like to be as user-friendly as possible with this, and as such I cannot allow such a posibility to potentially happen without trying my best to curb it.

# notes:

Your password is stored in /tmp/kekswitch/password
if you wish to edit it, follow these steps:

```
# <sudo / doas> nano /tmp/kekswitch/password

//Replace whatever's written with your password, do not add any new lines by pressing enter or something.
```