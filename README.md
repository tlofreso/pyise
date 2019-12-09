# pyise (Currently under development)
Python module for Cisco ISE

Usage:
```
>>> 
>>> from ise import Ise
>>> ise = Ise(host='127.0.0.1', user='un', password='pw')
>>> 
>>> # Get all endpoint groups:
>>> ise.endpoints.get_groups()
>>> 
>>> # Get all endpoints:
>>> ise.endpoints.get_endpoints()
>>> 
>>> # Get endpoints by mac:
>>> ise.endpoints.get_by_mac('00:00:00:00:00:00')
>>> 
```