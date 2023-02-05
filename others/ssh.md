#   SSH

Secure SHell Protocol

공개키 암호화를 통해 Shell 통신 내용을 암호화한다.

##  실습 (Mac 기준)
`ssh-keygen -t rsa`을 통해 ~/.ssh 디렉토리 하위에 공개키 `{key name}.pub` 생성 (`key name` 파일은 비밀키)

server에서 ssh의 기본 포트 22번을 사용하지 않으면 `-p` 옵션을 통해 포트번호를 지정해야 한다.

### cloudflared
1.  cloudflared에서 직접 tunnel을 뚫는 방법
2.  screen을 사용하는 법

```sh
# in client, in ~/.ssh/config
Host *.trycloudflare.com
  HostName %h
  User root
  Port 22
    ProxyCommand /opt/homebrew/bin/cloudflared access ssh --hostname %h
```

```sh
# in server, for every instance launch
# 이는 cloudflare의 proxy 주소가 매 실행 때마다 바뀌기 때문이다.
wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -P ~
chmod +x cloudflared-linux-amd64
apt update && apt install -y screen
screen -dm ~/cloudflared-linux-amd64 --url ssh://localhost:22 --logfile cloudflared.log
sleep 10
cat cloudflared.log
```