# Troubleshootings

##  initialize specified but the data directory has files in it. Aborting.
프로젝트에서 postgresql container의 volumne을 local에 mount하는 설정을 했었는데, 이를 mysql container로 바꾸는 과정에서 문제가 발생하는 것으로 추정한다.

[출처](https://stackoverflow.com/a/73217605)

```yml
## from
  volumes:
    - /host/dir:/var/lib/postgresql/data
## to
  volumes:
    - /host/dir:/var/lib/mysql/data
```

### resolution
[출처](https://github.com/docker-library/mysql/issues/757#issuecomment-812592680)

mysql db의 mount point를 다음과 같이 바꿔주면 된다.

```yml
## from
  volumes:
    - /host/dir:/var/lib/mysql
```

### error log

```sh
vscode-java-docker-db-1   | 2023-12-03 18:43:45+09:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
vscode-java-docker-db-1   | 2023-12-03 18:43:45+09:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.2.0-1.el8 started.
vscode-java-docker-db-1   | 2023-12-03 18:43:45+09:00 [Note] [Entrypoint]: Initializing database files
vscode-java-docker-db-1   | 2023-12-03T09:43:45.325386Z 0 [System] [MY-015017] [Server] MySQL Server Initialization - start.
vscode-java-docker-db-1   | 2023-12-03T09:43:45.326440Z 0 [Warning] [MY-011068] [Server] The syntax '--skip-host-cache' is deprecated and will be removed in a future release. Please use SET GLOBAL host_cache_size=0 instead.
vscode-java-docker-db-1   | 2023-12-03T09:43:45.326546Z 0 [System] [MY-013169] [Server] /usr/sbin/mysqld (mysqld 8.2.0) initializing of server in progress as process 80
vscode-java-docker-db-1   | 2023-12-03T09:43:45.327560Z 0 [ERROR] [MY-010457] [Server] --initialize specified but the data directory has files in it. Aborting.
vscode-java-docker-db-1   | 2023-12-03T09:43:45.327563Z 0 [ERROR] [MY-013236] [Server] The designated data directory /var/lib/mysql/ is unusable. You can remove all files that the server added to it.
vscode-java-docker-db-1   | 2023-12-03T09:43:45.327590Z 0 [ERROR] [MY-010119] [Server] Aborting
vscode-java-docker-db-1   | 2023-12-03T09:43:45.327853Z 0 [System] [MY-010910] [Server] /usr/sbin/mysqld: Shutdown complete (mysqld 8.2.0)  MySQL Community Server - GPL.
vscode-java-docker-db-1   | 2023-12-03T09:43:45.327977Z 0 [System] [MY-015018] [Server] MySQL Server Initialization - end.
vscode-java-docker-db-1 exited with code 1
```