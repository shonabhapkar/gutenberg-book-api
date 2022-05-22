d-tect_api

D-tect API s a inbound connector
It is used for giving inputs to bots.

```text
{"ModuleName":"D-tect_API","Sections":{"Execution":{"Representation":"KeyValue","Properties":{}},"Communication":{"Representation":"KeyValue","Properties":{"servername":{"Editable":"True","ControlType":"Textbox","DefaultValue":"localhost","OtherValues":[]},"exchange_type":{"Editable":"True","ControlType":"Textbox","DefaultValue":"topic","OtherValues":[]},"username":{"Editable":"True","ControlType":"Textbox","DefaultValue":"test","OtherValues":[]},"password":{"Editable":"True","ControlType":"Textbox","DefaultValue":"test","OtherValues":[]}}}}}
```

### Version History
### v5.0.8

```text
Following requirements are changed in setup.py:
1. base-connector>=5.0.8
2. uvicorn==0.16.0 (python3.6 support)
```

### v5.0.7

```text
1. Added ClientCode as an input parameter to get the User.
2. Changed d-tect API response.
```

#### v5.0.6

```text
resolve conflict in dependencies
```

#### v5.0.5

```text
resolve conflict in dependencies
```

#### v5.0.4

```text
1. Following requests are handled
A] External new transaction request
B] Intrabot new transaction request
C] External new transaction ack request
2. pending request is handled in convert_request_to_dtect_format()
```

#### v5.0.3

```text
1. Added R_Id to the new transaction message
```

#### v5.0.2

```text
1. Added new key InputSourceFileName in input
```

#### v5.0.1

```text
1. Using new version of base connector
```

#### v5.0.0

```text
1. Base Version
```
