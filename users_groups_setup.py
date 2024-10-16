import os


class UserGroupSetup:
    def __init__(self, root_dir='/'):
        self.root_dir = root_dir
        os.system('sudo groupadd mediacenter -g 13000')
        os.system('sudo usermod -a -G mediacenter $USER')
        os.system(
            '/bin/bash -c "sudo mkdir -pv ' + self.root_dir + '/media/{tv,movies,music,books,comics,audiobooks,podcasts,audiobookshelf-metadata,downloads/{torrent,usenet}} -m 775'
            ' ; sudo chown $(id -u):mediacenter ' + self.root_dir + '/media'
            ' ; sudo chown $(id -u):mediacenter ' + self.root_dir + '/media/{tv,movies,music,books,comics,audiobooks,podcasts,audiobookshelf-metadata,downloads/{torrent,usenet}}"'
        )

    def create_config_dir(self, service_name):
        os.system(
            f'sudo mkdir -p {self.root_dir}/configs/{service_name} -m 775' # -m 775 gives read/write access to the whole mediacenter group, change to 755 for only read
            f' ; sudo chown -R {service_name}:mediacenter {self.root_dir}/configs/{service_name}'
            f' ; sudo chown $(id -u):mediacenter {self.root_dir}/configs'
        )

    def sonarr(self):
        os.system(
            '/bin/bash -c "sudo useradd sonarr -u 13001'
            ' ; sudo mkdir -pv ' + self.root_dir + '/media/tv -m 775'
            ' ; sudo chown -R sonarr:mediacenter ' + self.root_dir + '/media/tv"'
        )
        self.create_config_dir('sonarr')
        os.system('sudo usermod -a -G mediacenter sonarr')

    def radarr(self):
        os.system(
            '/bin/bash -c "sudo useradd radarr -u 13002'
            ' ; sudo mkdir -pv ' + self.root_dir + '/media/movies -m 775'
            ' ; sudo chown -R radarr:mediacenter ' + self.root_dir + '/media/movies"'
        )
        self.create_config_dir('radarr')
        os.system('sudo usermod -a -G mediacenter radarr')

    def bazarr(self):
        os.system('/bin/bash -c "sudo useradd bazarr -u 13013"')
        self.create_config_dir('bazarr')
        os.system('sudo usermod -a -G mediacenter bazarr')

    def lidarr(self):
        os.system(
            '/bin/bash -c "sudo useradd lidarr -u 13003'
            ' ; sudo mkdir -pv ' + self.root_dir + '/media/music -m 775'
            ' ; sudo chown -R lidarr:mediacenter ' + self.root_dir + '/media/music"'
        )
        self.create_config_dir('lidarr')
        os.system('sudo usermod -a -G mediacenter lidarr')

    def readarr(self):
        os.system(
            '/bin/bash -c "sudo useradd readarr -u 13004'
            ' ; sudo mkdir -pv ' + self.root_dir + '/media/books -m 775'
            ' ; sudo chown -R readarr:mediacenter ' + self.root_dir + '/media/books"'
        )
        self.create_config_dir('readarr')
        os.system('sudo usermod -a -G mediacenter readarr')

    def mylar3(self):
        os.system(
            '/bin/bash -c "sudo useradd mylar -u 13005'
            ' ; sudo mkdir -pv ' + self.root_dir + '/media/comics -m 775'
            ' ; sudo chown -R mylar:mediacenter ' + self.root_dir + '/media/comics"'
        )
        self.create_config_dir('mylar')
        os.system('sudo usermod -a -G mediacenter mylar')

    def audiobookshelf(self):
        os.system(
            '/bin/bash -c "sudo useradd audiobookshelf -u 13014'
            ' ; sudo mkdir -pv ' + self.root_dir + '/media/{audiobooks,podcasts,audiobookshelf-metadata} -m 775'
            ' ; sudo chown -R audiobookshelf:mediacenter ' + self.root_dir + '/media/{audiobooks,podcasts,audiobookshelf-metadata}"'
        )
        self.create_config_dir('audiobookshelf')
        os.system('sudo usermod -a -G mediacenter audiobookshelf')

    def prowlarr(self):
        os.system('sudo useradd prowlarr -u 13006')
        self.create_config_dir('prowlarr')
        os.system('sudo usermod -a -G mediacenter prowlarr')

    def qbittorrent(self):
        os.system('sudo useradd qbittorrent -u 13007')
        os.system('sudo usermod -a -G mediacenter qbittorrent')

    def overseerr(self):
        os.system('sudo useradd overseerr -u 13009')
        self.create_config_dir('overseerr')
        os.system('sudo usermod -a -G mediacenter overseerr')

    def plex(self):
        os.system('sudo useradd plex -u 13010')
        self.create_config_dir('plex')
        os.system('sudo usermod -a -G mediacenter plex')

    def sabnzbd(self):
        os.system('sudo useradd sabnzbd -u 13011')
        self.create_config_dir('sabnzbd')
        os.system('sudo usermod -a -G mediacenter sabnzbd')

    def jellyseerr(self):
        os.system('sudo useradd jellyseerr -u 13012')
        self.create_config_dir('jellyseerr')
        os.system('sudo usermod -a -G mediacenter jellyseerr')
    
    def jackett(self):
        os.system('sudo useradd jackett -u 13008')
        self.create_config_dir('jackett')
        os.system('sudo usermod -a -G mediacenter jackett')
