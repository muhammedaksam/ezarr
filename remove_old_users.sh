#!/bin/bash

# shut down all ezarr containers referenced by docker-compose.yml 
# If you previously had ezarr installed somewhere else you have to do this manually in the directory where the docker-compose file is.
sudo docker compose down

# Remove old users and group
for user in sonarr radarr lidarr readarr mylar audiobookshelf bazarr prowlarr jackett plex overseerr jellyseerr qbittorrent sabnzbd; do
    if id "$user" &>/dev/null; then
        sudo userdel "$user"
    fi
done

if getent group mediacenter &>/dev/null; then
    sudo groupdel mediacenter
fi
