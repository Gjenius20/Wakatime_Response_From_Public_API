# Project Title

Wakatime Response In javascript and python

## Description

just for refrence

## Getting Started

### Dependencies

> For Python:
* requests 
* json

> For Javascript/node.js:
* axios
* fs

## Code:

### Python:
```python
import requests 
import json

user_API = 'Your_Api_Key' #You can get this key from your wakatime option Or you can visit //https://wakatime.com/settings/api-key then paste that key
r = requests.get('https://wakatime.com/api/v1/users/current/stats/last_7_days?api_key=' + user_API)

print(json.loads(r.content))

```
### Javascript / Node.js:
```javascript
const axios = require("axios").default;
const fs = require("fs");

const user_API = "Your_Api_Key"; //You can get this key from your wakatime option Or you can visit //https://wakatime.com/settings/api-key then paste that key
let url = `https://wakatime.com/api/v1/users/current/stats/last_7_days?api_key=${user_API}`;

axios.get(url).then(function (res) {
  console.log(res.data);
});
```