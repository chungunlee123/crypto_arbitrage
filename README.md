# CIT - 5900 - Final Project

## Dependencies
- Requests (pip install requests)
- Selenium (pip install selenium)
- PyJWT (pip install PyJWT)

## Chrome and ChromeDriver Setup
1. To run the project first [download Docker](https://docs.docker.com/get-docker/)
2. Run ```docker --version``` to verify it is correctly installed in your computer.
3. For Windows: Run the standalone-chrome container which contains chrome and chromedriver (necessary to run the selenium webcrawler).
```cmd
docker run -d -p 4444:4444 --shm-size="2g" selenium/standalone-chrome:dev
```
4. For Mac: Run the standalone-chrome container which contains chrome and chromedriver (necessary to run the selenium webcrawler).
```cmd
docker run --rm -it -p 4444:4444 -p 5900:5900 -p 7900:7900 --shm-size 2g seleniarm/standalone-chromium:latest
```
5. Verify that the container is running
```
docker ps
```
6. Open ```localhost:4444``` on your to go to the selenium dashboard.
7. Run main.py to start the program
```
python main.py
```

## Watching the webcrawler work
1. Open ```localhost:7900``` on your browser to go to the NoVnc screen
2. Connect using password: secret

## Troubleshooting
1. When closing down the program though a KeyInterrupt it might be necessary to stop the chromedriver container and restart it before executing the program again. Run the following commands:
```cmd
docker ps
# Find the ID of the chromedriver container
docker stop <Container ID>
# Finally re run the chromedriver container
docker run -d -p 4444:4444 --shm-size="2g" selenium/standalone-chrome:dev
```
