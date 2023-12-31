sudo usermod -aG docker $USER
docker volume create fastapiserver_mariadb_data
docker volume create fastapiserver_uptime_kuma
docker volume create fastapiserver_heimdall_data
docker volume create fastapiserver_jenkins_data
docker volume create fastapiserver_nginx_proxy_manager_data
docker volume create fastapiserver_nginx_proxy_manager_letsencrypt
docker volume create fastapiserver_es_data
docker volume create fastapiserver_portainer_data
docker network create fastapiserver_efk_net
docker network create fastapiserver_tool_net
docker network create fastapiserver_service_net
