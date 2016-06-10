# DefCon API

## Overview
A simple Flask-based API to expose the Rackspace DefCon lights.

## Endpoints
The API currently supports the following calls:
* /v1/status - Returns the currently set status on the unit.
* /v1/status/<int> - Sets the DefCon status to a value between 1 and 5.
* /v1/up - Increments the DefCon status from the current value.
* /v1/down - Decrements the DefCon status from the current value.  
* /v1/party - Engage / disengage party mode.

## Installation
> Steps pending.

There are several standalon runtime solutions for Flask - [See here](http://flask.pocoo.org/docs/0.11/deploying/wsgi-standalone). Using Twisted you can run the DefCon API with the following command:
> twistd -n web --port 80 --wsgi defcon.app

## Configuration
Configuration is handled in the config.yml file.  Both *pin_map* and *strobe_pin* fields are specifically used to define the BCM pin locations associated with the various DefCon lights. 
The *defcon_state* field is only used to track the last known state of the defcon unit. This value is held in memory but written to file to ensure the defcon unit returns to the same state on restart.

### Config example ###
```yaml
defcon_state: 3
pin_map:
  1: 13
  2: 11
  3: 9
  4: 22
  5: 29
strobe_pin: 0
```
