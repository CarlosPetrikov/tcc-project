FROM grafana/grafana:latest
USER root
COPY grafana.db /var/lib/grafana/grafana.db
RUN chown 472:472 /var/lib/grafana/grafana.db \
    && chmod 660 /var/lib/grafana/grafana.db
USER 472
