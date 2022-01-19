# Testing on Another System
**Below are the terminal commands used to run the web application on another machine**

The commands, are namely,
```
docker pull cmpe327group7/qbay:v1
docker run -p 8081:8081 cmpe327group7/qbay:v1 python3 -m qbay
```

C:\Users\brand\OneDrive - Queen's University\Documents\GitHub\CMPE327-Group7>docker pull cmpe327group7/qbay:v1
v1: Pulling from cmpe327group7/qbay
Digest: sha256:6f2bfa5de46662af09235c0496bce1a18f19e58048c0e16fc22d1815fcd37e78
Status: Image is up to date for cmpe327group7/qbay:v1
docker.io/cmpe327group7/qbay:v1

C:\Users\brand\OneDrive - Queen's University\Documents\GitHub\CMPE327-Group7>docker run -p 8081:8081 cmpe327group7/qbay:v1 python3 -m qbay
 * Serving Flask app 'qbay' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://172.17.0.2:8081/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 421-344-021
172.17.0.1 - - [27/Nov/2021 12:30:23] "GET / HTTP/1.1" 302 -
172.17.0.1 - - [27/Nov/2021 12:30:23] "GET /home HTTP/1.1" 200 -