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
 Refer to this documentation for further instructions
[Starting django-redis](https://github.com/jazzband/django-redis)



## Installing Celery
Installation only
Refer [documentation](https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html) for setup and usage inside Django
Read RealPython [Post](https://realpython.com/asynchronous-tasks-with-django-and-celery/) on celery 

 `pip install celery`

Starging celery:
`celery -A app_name worker -l info`

 Celery requires a message broker to handel requests from an exernal source. We will be using RabbiMQ

Install Rabbitmq from a browser
[Download](https://www.rabbitmq.com/install-windows.html#installer)
Download and Install Erlang
[Download](https://www.erlang.org/downloads)

Set Elang as System Variable: 
`ERLANG_HOME = C://path_to_erlang` **Make sure not to include /bin. Only Include the installation folder where bin is located**

**Start Rabbitmq use the rabbitmq shell provided**
`rabbitmq-plugins enable rabbitmq_management`

### Having confusions? Follow this tutorial => [Here](https://www.youtube.com/watch?v=V9DWKbalbWQ)

