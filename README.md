#Major
##Current Scenario
* Monitoring services
    * alarm on failure/events
    * analysis
    * report on the current system states.

##Problem/Pain points
* No traceback of occurence of event.
* No prediction exists prior to failure.
* Process/Service monitoring is nowhere.

##Objective
To create an infrastructural solution to solve the existing problems.

##Expectations(to be changed later)
* cross platform
* lowest resource consumption on client end
* must be able to provide verbose logs and notifications
* must support realtime analysis, push notifications.

##Tech stack
* Go(client) - remote endpoints
* Python - server
* rabbitmq/kafka
* Cassandra
* Titan graph engine (implemented in Java) + mogwai(python lib to connect with Titan)
* React(frontend)

##Working
*Add image here*


##Implementation
Classes
-------
* **Machine**
    * **Service** (Class)
    * **Process** (Class)
    * State