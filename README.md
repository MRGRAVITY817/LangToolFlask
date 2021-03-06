# Lang Tool Flask
![ex_launchshot](./img/launchshot.png)  
This is a tiny Python project build with "Flask" and "Language Tool" library.  
For more info about Language Tool, head to below url.
- Language tool: https://languagetool.org/?l=en&utm_source=google&utm_medium=cpc&utm_campaign=spell_checker&utm_term=grammar%20check&gclid=CjwKCAiA57D_BRAZEiwAZcfCxVFriLSMPLx-NBuZ72P-Rgt2Tr-qHzNwekN1VW0BBbouQHJ4aaJZKxoCfkoQAvD_BwE

---
## Prerequisite
You need Docker to run this project. Find the best option to install it for your OS.
- Docker Desktop(Windows, Mac): https://www.docker.com/products/docker-desktop
- Docker Engine(Linux): https://hub.docker.com/search?q=&type=edition&offering=community&operating_system=linux

---
## How to start?

1. Build the Dockerfile using build.sh file.
   
   ```sh
   chmod 700 build.sh
   ./build.sh 
   ```
2. Run the Docker image using rundock.sh
   ```sh
   chmod 700 rundock.sh
   ./rundock.sh
   ```

3. If it's working like the image below, head to http://localhost:5000 to test the site.
   ![ex_screenshot](./img/screenshot.png)
