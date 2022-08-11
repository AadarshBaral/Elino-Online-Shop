# This app uses redis as a caching service 
To install redis in windows, we need (windows subsystem for linux)-install wsl with **Powser shell**
            ```
            wsl --install
            wsl --install -d <Distribution Name>.
            ```

## Install redis
```
sudo apt-add-repository ppa:redislabs/redis
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install redis server

```
## Start redis 'Use Ubuntu Terminal' 
```
redis-server
```
Use a separate terminal to run redis cli
```
redis-cli
```
Check if redis is running by `ping` it returns  `pong`

### Installing redis in django 
# Refer to this documentation for further instructions
[Starting django-redis](https://github.com/jazzband/django-redis)