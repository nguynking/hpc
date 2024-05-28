# hpc

a multilingual extractive quesion answering system with XLM-RoBERTa using docker.

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

if you find that the `docker-compose build` command accumulates a lot of space on your computer's hard drive, you should use `docker system prune -a` to clean your filesystem.
