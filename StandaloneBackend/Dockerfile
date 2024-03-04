FROM ubuntu:latest

# Installing packages
RUN apt-get update 
RUN apt-get -y upgrade 
RUN apt-get install -y openssh-server
RUN apt-get install -y htop
RUN apt-get install -y nano
RUN apt-get install -y neofetch
RUN apt-get install -y rsyslog
RUN apt-get install -y dbus
RUN apt-get install -y sudo
RUN apt-get install -y net-tools
RUN apt-get install -y git 
RUN apt-get install -y python3
RUN apt-get install -y python3-pip

# Configure SSH
RUN sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin no/' /etc/ssh/sshd_config


# Start services
RUN service dbus start 
RUN systemctl enable ssh 
RUN service ssh start


# Copy scripts and files
WORKDIR /root/
COPY script.sh .

COPY dependalayzer.py .


# Set permissions
RUN chmod +x script.sh 

EXPOSE 22
CMD [ "/bin/sh"]
ENTRYPOINT ["/root/script.sh"]
