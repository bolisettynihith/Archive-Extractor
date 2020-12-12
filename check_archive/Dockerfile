FROM ubuntu:18.04 as build


RUN apt update; apt -y --autoremove full-upgrade
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -yq --no-install-recommends \
    python3 python3-pip unzip unrar
RUN pip3 install flask
RUN pip3 install requests

RUN bash -c "useradd -m joyhopkins -s /bin/bash"
RUN bash -c "echo joyhopkins:My_l0nG_P4ssW0DR_i5__s4f3_tO_CRacK | chpasswd"

COPY start.sh /root/start.sh

COPY project /home/joyhopkins/project

RUN chown -R joyhopkins:joyhopkins /home/joyhopkins/project/ && \
    chmod -R 744 /home/joyhopkins/project/

EXPOSE 5001

ENTRYPOINT ["bash", "/root/start.sh"]