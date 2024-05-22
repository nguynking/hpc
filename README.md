# hpc

a simple text classification app using docker.

> [!NOTE]
> the app is in the most basic form to reduce the docker image size (for faster build and iteration), which contains the frontend and api, and I'm currently classifying the text by using a random function :)
>
>  we need to use huggingface and pytorch later for the final app.

# usage

1. open your terminal and clone the project into your local computer
```bash
git clone https://github.com/nguynking/hpc.git
```

2. navigate to the project directory
```bash
cd hpc/
```

3. build and start docker containers
```bash
docker-compose up --build
```

4. navigating to `http://localhost:7860` in your web browser (e.g. Chrome, Edge...) to use the interface

5. if you want to stop the application, use command `Ctrl + C`

6. if you want to run the application again, open terminal and run following command:
```bash
docker-compose up
```
