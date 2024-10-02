# Basic Splunk App

## Using Splunk (Enterprise) to Make a Basic Dashboard That Collects Weather Data (In London in This Case)

### Install Splunk Enterprise:

- [Link to Splunk Enterprise](https://www.splunk.com/en_us/download/splunk-enterprise.html)
- Install Splunk.
- Navigate to `/Applications/splunk/bin`.
- Run: 
  ```bash
  ./splunk start
  ```
  
### Getting Data In:
#### Scripted inputs:
- Navigate to /Applications/Splunk/etc/apps/search/local
- Add inputs.conf
```
#   Version 9.3.1

[script://./bin/<script-name>]
disabled = false
index = <your-index-name>
interval = 900
sourcetype = json_no_timestamp
```
#### i.e.
```
[script://$SPLUNK_HOME/etc/apps/search/bin/weathergetter.py]
disabled = false
host = Jacks-MacBook-Pro-29.local
index = weathergetter
interval = 900.0
sourcetype = json_no_timestamp
```

- Navigate to /Applications/Splunk/etc/apps/search/bin
- Create a directory for your input
- Change to the directory
- Create the script and add the shebang path #!/usr/bin/env python3
- (OPTIONAL) Make sure the script is an executable:  chmod u+x <script--name>
- Navigate to /Applications/Splunk//bin
- Restart splunk: ./splunk restart

### Working with the data:
- Goto http://127.0.0.1:8000 and login
- Goto search & reporting
- See if the data is there (Search with Splunk's SPL):
```
index=<your-index-name>
```

- If you don’t see any data, check error logs and go from there:
```
index=_internal "error"
```

