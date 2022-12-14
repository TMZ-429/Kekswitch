#!/bin/bash
install_directory="/usr/local/bin"
kekswitch_directory="$install_directory/kekswitch.d"

cp ./kek.py $install_directory/kekswitch
chmod +x $install_directory/kekswitch
chmod 755 $install_directory/kekswitch

mkdir $kekswitch_directory

read -p "Please make a Kekswitch password -> " password
printf $password > $kekswitch_directory/password
printf "9" > $kekswitch_directory/max-retries

echo "Finished installing."
