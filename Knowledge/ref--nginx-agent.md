---
category: knowledge
tags:
  - nginx
platform: n/a
status: done
created: 2026-06-17
aliases:
  - 1. Installing from NGINX Repo
---

# 1. Installing from NGINX Repo
### A.  In Ubuntu
1. Create the `/etc/ssl/nginx` directory:
    ```shell
    sudo mkdir -p /etc/ssl/nginx
    ```

2. Log in to [MyF5 Customer Portal](https://account.f5.com/myf5/) and download your `nginx-repo.crt` and `nginx-repo.key` files.

3.  the files to the `/etc/ssl/nginx/` directory:
    ```shell
    sudo cp nginx-repo.crt nginx-repo.key /etc/ssl/nginx/
    ```

4. Install the prerequisites:
    ```shell
    sudo apt-get install apt-transport-https lsb-release ca-certificates wget gnupg2 ubuntu-keyring
    ```

5. Download and add [NGINX signing key](https://cs.nginx.com/static/keys/nginx_signing.key):
    ```shell
    wget -qO - https://cs.nginx.com/static/keys/nginx_signing.key | gpg --dearmor | sudo tee /usr/share/keyrings/nginx-archive-keyring.gpg >/dev/null
    ```

6. Create `apt` configuration `/etc/apt/apt.conf.d/90pkgs-nginx`:
    ```
    Acquire::https::pkgs.nginx.com::Verify-Peer "true";
    Acquire::https::pkgs.nginx.com::Verify-Host "true";
    Acquire::https::pkgs.nginx.com::SslCert     "/etc/ssl/nginx/nginx-repo.crt";
    Acquire::https::pkgs.nginx.com::SslKey      "/etc/ssl/nginx/nginx-repo.key";
    ```

7. Add the `nginx-agent` repository:
    ```shell
    echo "deb [signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] https://pkgs.nginx.com/nginx-agent/ubuntu/ `lsb_release -cs` agent" \
      | sudo tee /etc/apt/sources.list.d/nginx-agent.list
    ```

8. To install `nginx-agent`, run the following commands:
    ```shell
    sudo apt update
    sudo apt install nginx-agent
    ```

9. Verify the installation:
    ```shell
    sudo nginx-agent -v
    ```
