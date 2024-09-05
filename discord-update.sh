# Author: Stephen Jones
# Created early 2023
# Last updated 2024-09-05

# Since Discord doesn't automatically update in Linux distributions, this script
# will perform the update process when called.
#
# This script downloads and installs the latest Discord update, then launches
# Discord as a detached process.

sudo printf "\nroot permissions granted for installation will expire in 15 minutes...\n\n"

killall Discord
cd /tmp
wget -O discord_latest.deb https://discord.com/api/download/stable\?platform\=linux\&format\=deb
sudo apt install ./discord_latest.deb
rm discord_latest.deb

sudo printf "Discord updated. Launching...\n"
nohup discord > /dev/null 2>&1 &