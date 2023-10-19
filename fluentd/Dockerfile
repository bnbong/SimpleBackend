# image based on fluentd v1.14-1
FROM fluent/fluentd:v1.14.3-debian-arm64-1.0

# Use root account to use apk
USER root

# below RUN includes plugin as examples elasticsearch is not required# you may customize including plugins as you wish
RUN apt-get update && \
    apt-get install -y --no-install-recommends sudo build-essential ruby-dev && \
    gem uninstall -I elasticsearch && \
    gem install elasticsearch -v 7.17.0 && \
    gem install fluent-plugin-elasticsearch && \
    gem sources --clear-all && \
    apt-get purge -y --auto-remove build-essential ruby-dev && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/local/bundle/cache/*.gem


USER fluent