# RabbitMQ Streams using Python

## Requirements:

- Make (optional)
- Docker
- Pyenv
- Python >3.9


## Disclaimer:
If you haven't make installed and doesn't want it, you can read commands from Makefile and execute them in terminal.


## Setup project:
```commandline
    make create-venv
    make setup
    make containers-up
```

## Publishing messages:
```commandline
    python publisher/publish.py message
```


## Running consumer:
```commandline
    python consumer/consume.py
```