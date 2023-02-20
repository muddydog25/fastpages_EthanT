---
toc: true
title: Flask/Python Deployment Guide
author: Team OrbOrb (Ethan Tran)
description: Description of key methods process used to deploy a Flask/Python website; AWS EC2, Docker, docker-compose, and Nginx 
permalink: /deploy
categories: [6.B, C7.0, C7.1, C7.2]
tags: [aws, ec2. docker, nginx, certbot, dns]
type: pbl
---

## Server Setup and Initial Deployment
> Development Operations (DevOps) begins with server setup.    
### Amazon Web Services (AWS): Electric Cloud Compute (EC2) Setup
- To begin, head to  the "Instances" dropdown on AWS and select "Instances."

<img src="https://user-images.githubusercontent.com/109186517/220186297-adf65729-a8db-4506-ae03-cd75273d92d0.png"></img>

- From here, a variety of instances will show up. For this project, depending on which teacher you have, select either "NCS.cf Yeung CSP" or "NCS.gq Mort CSP"

<img src="https://user-images.githubusercontent.com/109186517/220186519-ca92be0c-c9e6-4173-bbdb-9715a13a8a69.png"></img>

- Then, run
```bash
$ sudo docker ps # This allows you to observe the ports that are currently being used
``` 

## docker-compose.yml & Dockerfile
- Next, head to VSCode on your local machine and update the docker-compose.yml and Docker files.
- Select a port that is not used and change the left side of docker-compose.yml port to be an unussed port XYZ:8086.  The "XYZ" would be the port that you have selected. 
- The right side 8086 matches the port you have used in your Docker file in two locations - 8080 is typically used as an internal port.  

- In VSCode, open up your terminal. Run ``` sudo docker-compose up ``` and make sure it builds properly. Type localhost:XYZ in your browser (XYZ is the unused port you have selected).  Check for any errors occur in the Terminal. If this fails, please be sure to review the previous steps.
- If all is well, make sure to commit your changes to docker-compose.yml & Dockerfile

### Clone and Change Directory to project location
> This command allows you to clone your GitHub repository onto the AWS instance. In this example, the GitHub HTTPs link is: https://github.com/nighthawkcoders/flask_portfolio.git.  
- Head back to either the instance "NCS.cf Yeung CSP" or "NCS.gq Mort CSP" on AWS

**Note**
> Your repository should be using the  APCSP flask_portfolio as a template 
- Once you are in the instance, run

```bash
ls # Check the other repository names, make sure that the one the name you select does not match the ones that appear when running this command
```
- Next, run

```bash
$ cd
$ git clone https://github.com/nighthawkcoders/flask_portfolio.git my-unique-name 
# Replace "my-unique-name- with your desired name for this repository, it is recommended that your table number and period are featured in this name to avoid confusion among groups
$ cd my-unique-name
```

- Once you are in your repository, run

```bash
docker-compose up -d --build 
```

- To make sure that your application is running, run the following command 

```bash
curl localhost:XYZ # Replace XYZ with the port you have selected
```


## Test preparation for Docker Web Application using IP for Internet Access
Each student scrum team will perform Nginx test and verify Group Web Project is working on EC2 instance.  This step is can only support a single Web Application at a time.

This Step is dependent on...
- EC2 Public IPs: 3.233.212.71
- Docker Port: 8086

Enable Nginx to retrieve default Web Application using IP Address from internet request (Reverse Proxy)!

* Install Nginx on Ubuntu servers
```bash
$ sudo apt install nginx
```

* Go to location of Nginx server configuration files
```bash
$ cd /etc/nginx/sites-available
```

* Open editor to Create your own "Nginx test configuration".  
```bash
$ sudo nano my-unique-file # Replace "my-unique-file" with the name you wish to call your nginx file
```

* Edit your own Nginx server configuration making modifications to:
    * IP Address: 3.233.212.71
    * docker-compose, proxy pass Port: 8086

**Requirements** 
- A unique name for your file
- DNS name for server
[Link to Jeffery F's DNS Domain Guide](https://moonpiedumplings.github.io/quartotest/posts/duckdns/)

- Change the port in proxy_pass line to the one you have previously selected
    
```nginx
server {
    listen 80;
    listen [::]:80;
    server_name 3.233.212.71;
    location / {
        proxy_pass http://localhost:8086;
        # Simple requests
        if ($request_method ~* "(GET|POST)") {
                add_header "Access-Control-Allow-Origin"  *;
        }
        # Preflight requests
        if ($request_method = OPTIONS ) {
                add_header "Access-Control-Allow-Origin"  *;
                add_header "Access-Control-Allow-Methods" "GET, POST, OPTIONS, HEAD";
                add_header "Access-Control-Allow-Headers" "Authorization, Origin, X-Requested-With, Content-Type, Accept";
                return 200;
        }
    }
}
```

### Activating Nginx configuration
* Activate/enabled Nginx server configuration:
  * nginx configuration file: test 
```bash
$ sudo ln -s /etc/nginx/sites-available/my-unique-file /etc/nginx/sites-enabled # Replace "my-unique-file" with the name of your nginx file
$ sudo nginx -t
```

* If there are errors, something is wrong...
    * Perhaps you are missing semicolon at the end of server)name or proxy_pass lines.
    * Perhaps link to file in sites-enabled is bad as a result of bad syntax in ```ln -a``` command.  
        * There are two directories ```/etc/nginx/sites-available``` and ```/etc/nginx/sites-enabled```.  
        * The 1st is for preliminary editing, the second is for activation.  Perform ```ls``` in ```/etc/nginx/sites-enabled``` and make sure all the names look correct.  
        * Correct by ```rm``` of mistake in ```/etc/nginx/sites-enabled``` without deleting original file in ```/etc/nginx/sites-available```.  Then repeat ```ln -s``` command.

* If there are no errors, restart NGINX so the server to activate ```/etc/nginx/sites-enabled``` files:
```bash
$ sudo systemctl restart nginx
```
- Check that your server is running on the browser using the domain using http://mydomain 
- Replace "mydomain" with the domain you have previously selected


## Final preparation the Docker Web Application using DNS for Internet Access
There are additional steps to this preparation. We need to direct the internet to the AWS server running the Web Application, this is done using Domain Name Service (DNS).   After being directed to the Web Server, the server needs to respond to the HTTP (Hyper Text Transfer Protocol) request.  The proxy of HTTP to your Web Application is manged by Nginx.   Finally, we will Secure HTTP (HTTPS), with a utility called Certbot.

### Certbot configuration
Each student scrum team will learn Certbot on on AWS EC2 test server, establish working https web application.  The final configuration will be on AWS server managed by Teachers or Student DevOps Engineers.

```bash
$ sudo certbot --nginx
```
- Make sure that your domain appears on the list of names to activate HTTPS for

Saving debug log to /var/log/letsencrypt/letsencrypt.log
Plugins selected: Authenticator nginx, Installer nginx

Which names would you like to activate HTTPS for?
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
1: coolcodersjava.pw
2: www.coolcodersjava.pw
3: ajarcade.duckdns.org
4: flowhealth.duckdns.org
5: goatedgroup.duckdns.org
6: jasj-inventory.duckdns.org
7: recipies.duckdns.org
8: ssvgcars.duckdns.org
9: userapi.duckdns.org
10: fr0st.ml
11: www.fr0st.ml
12: agenda.nighthawkcodescrums.gq
13: coolcoders.nighthawkcodescrums.gq
14: escaperoom.nighthawkcodescrums.gq
15: frost.nighthawkcodescrums.gq
16: jame.nighthawkcodescrums.gq
17: lawnmowers.nighthawkcodescrums.gq
18: loopholegames.nighthawkcodescrums.gq
19: musicmania.nighthawkcodescrums.gq
20: nba.nighthawkcodescrums.gq
21: sadv.nighthawkcodescrums.gq
22: ssjn.nighthawkcodescrums.gq
23: stocks.nighthawkcodescrums.gq
24: striver.nighthawkcodescrums.gq
25: tngc.nighthawkcodescrums.gq
26: white.nighthawkcodescrums.gq
27: workwatch.nighthawkcodescrums.gq
28: cars.nighthawkcodingsociety.com
29: dolphin.nighthawkcodingsociety.com
30: saakd.nighthawkcodingsociety.com
31: pythonalflask.tk
32: www.pythonalflask.tk
33: teambrobro.tk
34: www.teambrobro.tk
35: teamcheeseatimetime.tk
36: www.teamcheeseatimetime.tk
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Select the appropriate numbers separated by commas and/or spaces, or leave input
blank to select all options shown (Enter 'c' to cancel): # ENTER YOUR CORRESPONDING NUMBER

Cert not yet due for renewal

You have an existing certificate that has exactly the same domains or certificate name you requested and isn't close to expiry.
(ref: /etc/letsencrypt/renewal/nighthawkcodingsociety.com-0001.conf)

What would you like to do?
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
1: Attempt to reinstall this existing certificate
2: Renew & replace the cert (limit ~5 per 7 days)
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Select the appropriate number [1-2] then [enter] (press 'c' to cancel): 2
Renewing an existing certificate
Performing the following challenges:
http-01 challenge for nighthawkcodingsociety.com
http-01 challenge for csa.nighthawkcodingsociety.com
http-01 challenge for cso.nighthawkcodingsociety.com
http-01 challenge for flm.nighthawkcodingsociety.com
Waiting for verification...
Cleaning up challenges
Deploying Certificate to VirtualHost /etc/nginx/sites-enabled/nighthawk_society
Deploying Certificate to VirtualHost /etc/nginx/sites-enabled/nighthawk_csa
Deploying Certificate to VirtualHost /etc/nginx/sites-enabled/nighthawk_csp
Deploying Certificate to VirtualHost /etc/nginx/sites-enabled/nighthawk_flm

Please choose whether or not to redirect HTTP traffic to HTTPS, removing HTTP access.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
1: No redirect - Make no further changes to the webserver configuration.
2: Redirect - Make all requests redirect to secure HTTPS access. Choose this for
new sites, or if you're confident your site works on HTTPS. You can undo this
change by editing your web server's configuration.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Select the appropriate number [1-2] then [enter] (press 'c' to cancel): 2
Traffic on port 80 already redirecting to ssl in /etc/nginx/sites-enabled/nighthawk_society
Traffic on port 80 already redirecting to ssl in /etc/nginx/sites-enabled/nighthawk_csa
Traffic on port 80 already redirecting to ssl in /etc/nginx/sites-enabled/nighthawk_csp
Traffic on port 80 already redirecting to ssl in /etc/nginx/sites-enabled/nighthawk_flm

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Your existing certificate has been successfully renewed, and the new certificate
has been installed.

The new certificate covers the following domains:
https://nighthawkcodingsociety.com, 
https://csa.nighthawkcodingsociety.com, 
https://csp.nighthawkcodingsociety.com, and
https://flm.nighthawkcodingsociety.com,

You should test your configuration at:
https://www.ssllabs.com/ssltest/analyze.html?d=nighthawkcodingsociety.com
https://www.ssllabs.com/ssltest/analyze.html?d=csa.nighthawkcodingsociety.com
https://www.ssllabs.com/ssltest/analyze.html?d=csp.nighthawkcodingsociety.com
https://www.ssllabs.com/ssltest/analyze.html?d=flm.nighthawkcodingsociety.com
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

IMPORTANT NOTES:
 - Congratulations! Your certificate and chain have been saved at:
   /etc/letsencrypt/live/nighthawkcodingsociety.com-0001/fullchain.pem
   Your key file has been saved at:
   /etc/letsencrypt/live/nighthawkcodingsociety.com-0001/privkey.pem
   Your cert will expire on 2022-03-06. To obtain a new or tweaked
   version of this certificate in the future, simply run certbot again
   with the "certonly" option. To non-interactively renew *all* of
   your certificates, run "certbot renew"
 - If you like Certbot, please consider supporting our work by:

   Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
   Donating to EFF:                    https://eff.org/donate-le

- Conclude this process by running ``` sudo certbot --nginx ```  and testing https://mydomain
- Replace "mydomain" with the domain you have previously selected

# Update Deployment

- To update your code, run

```bash
$ sudo docker-compose kill
Killing flask_portfolio_web_1 ... done
```

- From here, the server should be down and displaying a 502 error

```bash
$ git pull # This allows you to update your code
```

- Then, rebuild your container by running...

```bash
$ sudo docker-compose build --no-cache
```

**Note** 
- This step can take a few minutes

- Finally, run...

```bash
$ sudo docker-compose up -d
Recreating flask_portfolio_web_1 ... done
```

- If all of the steps have been completed properly, the server should be back up with the applied changes/updates