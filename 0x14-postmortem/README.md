0x15. Postmortem


## Issue Summary

At 2:00 PM PT on 02-20-2017 Apache stopped running. Apache was running inside a Docker container and it was found that on querying the root, instead of returning the page holbertonschool.com, it was returning an error message. Resulting in denial of service to users and causing 0.1% of traffic loss. It took 20 minutes to fix the issue and at around 2:20 PM, Apache was restarted and website was fully operational by 2:30 PM PT. 


## Timeline
- 2:00 PM Betty found the issue while checking the server uptime.
- 2:05 PM load avearge was examined.
- 2:10 PM error logs were checked.
- 2:15 PM found the issue with ps -aux that apache was not running.
- 2:20 PM Apache start.
- 2:30 PM website was operational and available to users.

## Root Cause
Apache stopped working because of high 


## Resolution
Destroyed the container, created new and started Apache with service apache start.


## Preventive measures

