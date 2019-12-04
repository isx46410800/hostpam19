# hostpam
FROM fedora:27
LABEL version="1.0"
LABEL author="Miguel Amorós"
LABEL subject="hostpam19:samba"
RUN dnf install -y vim util-linux-user-2.30.2-3.fc27.x86_64 finger passwd pam_mount nss-pam-ldapd authconfig samba-client cifs-utils
RUN mkdir /opt/docker
COPY * /opt/docker/
RUN chmod +x /opt/docker/startup.sh
WORKDIR /opt/docker
