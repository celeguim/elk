FROM docker.elastic.co/beats/filebeat:6.5.1
USER root
#COPY filebeat.yml /usr/share/filebeat/filebeat.yml
COPY filebeat.yml /usr/share/filebeat/filebeat2.yml
COPY ./filebeat.yml /usr/share/filebeat/filebeat3.yml
USER root
RUN chown root:filebeat /usr/share/filebeat/filebeat2.yml
RUN chown root:filebeat /usr/share/filebeat/filebeat3.yml
USER filebeat
