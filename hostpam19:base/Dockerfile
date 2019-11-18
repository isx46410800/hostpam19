# hostpam
FROM fedora:27
LABEL version="1.0"
LABEL author="Miguel Amorós"
LABEL subject="hostpam"
RUN dnf install -y procps vim iproute nmap util-linux-user-2.30.2-3.fc27.x86_64 finger passwd pam_mount nfs-utils
RUN mkdir /opt/docker
COPY * /opt/docker/
RUN chmod +x /opt/docker/startup.sh
WORKDIR /opt/docker
