#Client Module
##Objective
Collect system state, system logs(processes, services, etc.) and add to the redis queue(or rabbitmq)

##Dependencies
* [psutil](https://pypi.python.org/pypi?:action=display&name=psutil)

    pip install psutil
    
* Redis
    * [system installation](http://redis.io/download)
    * 
        pip install redis
    * pip install rq
    
##TODO
* add machine authentication while communicating.
 
