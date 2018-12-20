FROM docker.elastic.co/beats/metricbeat:6.5.4
COPY metricbeat.yml /usr/share/metricbeat/metricbeat.yml
USER root
RUN chown root:metricbeat /usr/share/metricbeat/metricbeat.yml
USER root
