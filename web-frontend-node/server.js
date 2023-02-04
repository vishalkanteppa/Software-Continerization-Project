const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const axios = require('axios');

//TODO make use of configmap

const HOST = '0.0.0.0';
const PORT = 8080;
const API_HOST = 'rest-api';
const API_PORT = 1337;
const HTML_DIR = path.join(__dirname, '/html/');

const app = express();

app.use(bodyParser.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  res.sendFile(path.join(HTML_DIR, 'index.html'));
});

app.get('/create_new_post', (req, res) => {
  res.sendFile(path.join(HTML_DIR, 'create_new_post.html'));
});

function toDateTime(secs) { // https://stackoverflow.com/questions/4611754/javascript-convert-seconds-to-a-date-object
    var t = new Date(1970, 0, 1); // Epoch
    t.setSeconds(secs);
    return t;
}

app.get('/view_new_posts', (req, res) => {
  var response_html = '';

  response_html += '<title>Simple blog</title>';
  response_html += '<a href="/">Go back to home page</a><br>';
  response_html += '<h1>Newest posts:</h1>'
  
  axios.get('http://' + API_HOST + ':' + API_PORT + '/new_posts').then(function (api_response) {
    for (const post of api_response.data) {
      response_html += '<h2>' + post.name + ' (' + toDateTime(post.time).toLocaleString('en-GB', { timeZone: 'UTC' }) + ')</h2>';
      response_html += '<p>' + post.content + '</p>';
    }

    res.send(response_html);
  });
});

app.post('/create_new_post', (req, res) => {
  console.log(req.body);
  console.log(req.body.name);
  console.log(req.body.content);
  axios.post('http://' + API_HOST + ':' + API_PORT + '/create_new_post', JSON.stringify({name: req.body.name, content: req.body.content}), {headers: {'Content-Type': 'application/json'}}).then(function (api_response) {
    res.sendFile(path.join(HTML_DIR, 'create_success.html'));
  });
});

app.listen(PORT, HOST, () => {
  console.log(`Listening on http://${HOST}:${PORT}`);
});