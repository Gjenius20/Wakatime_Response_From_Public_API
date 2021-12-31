//How To Get Wakatime api With javascript
const axios = require("axios").default;
const fs = require("fs");

const user_API = "Your_Api_Key"; //You can get this key from your wakatime option Or you can visit //https://wakatime.com/settings/api-key then paste that key
let url = `https://wakatime.com/api/v1/users/current/stats/last_7_days?api_key=${user_API}`;

axios.get(url).then(function (res) {
  console.log(res.data); //done you get your Json api response

  // const ret_data = res.data.data;
  // fs.writeFileSync(`retrive.json`, JSON.stringify(ret_data));
});
