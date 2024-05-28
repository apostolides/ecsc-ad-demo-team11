#!/bin/bash
chown -R ctflib:ctflib /opt/app/files
# Use socat to serve the service
while [ true ]; do
su -l ctflib -c "socat -dd TCP4-LISTEN:4242,reuseaddr,fork SYSTEM:'(cd /opt/app >/dev/null && exec python /opt/app/service.py)',pty,echo=0,raw,iexten=0" 1> /dev/null
done;
