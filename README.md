### INSTALLING FOR UNIX BASED OS:
    In a bash script, run:
    source ./run.sh
    
    or
    
    cd src
    python3 -m venv venv-fizzbuzz
    source ./venv-fizzbuzz/bin/activate
    pip3 install -r requirement-dev.txt

##### FOR RUNNING THE SCRIPT:
For default run between 1 and 100:

    python3 main.py
    
    or
    
    python3 main.py run

For running the script in a given range:

    python3 main.py range start end
    
Where "start" and "end" are the lower and upper limit respectively.

##### FOR RUNNING ALL THE TESTS:
    python3 -m pytest test.py

### INSTALLING USING DOCKER:
In the root directory run: (docker and docker-compose required)

    docker build --tag fizzbuzz:latest ./    
   
##### RUNNING THE SCRIPT USING DOCKER:
In the root directory run: (docker and docker-compose required)

    docker run --rm --entrypoint=python3 fizzbuzz:latest main.py
    
    or
    
    docker run --rm --entrypoint=python3 fizzbuzz:latest main.py run    
    
For running the script using docker-compose in a given range:

    docker run --rm --entrypoint=python3 fizzbuzz:latest main.py range start end
    
Where "start" and "end" are the lower and upper limit respectively

##### FOR RUNNING ALL THE TESTS USING DOCKER:
    docker run --rm --entrypoint=python3 fizzbuzz:latest -m pytest test.py
    
### INSTALLING USING DOCKER-COMPOSE:
In the root directory run: (docker and docker-compose required)

    docker-compose up -d    
   
##### RUNNING THE SCRIPT USING DOCKER-COMPOSE:
In the root directory run: (docker and docker-compose required)

    docker-compose exec fizzbuzz python3 main.py
    
    or
    
    docker-compose exec fizzbuzz python3 main.py run    
    
For running the script using docker-compose in a given range:

    docker-compose exec fizzbuzz python3 main.py range start end
    
Where "start" and "end" are the lower and upper limit respectively

##### FOR RUNNING ALL THE TESTS USING DOCKER-COMPOSE:
    docker-compose exec fizzbuzz python3 -m pytest test.py
