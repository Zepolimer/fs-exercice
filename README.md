# fs-exercice

You are required to code a chat application between a user and an agent.
A front-end application sends user messages to a back-end server, which replies back with the
agent's answer.

<br/>

#### Required:
- Separate the chat system into two sibling folders: “front” and “back”, where both
applications can be run independently. 
- The back-end server implements a RESTful service, exchanging JSON data with GET or
POST methods. 
- Each user message is sent to the back-end with the entire chat history. On the other
hand, the server replies with the agent’s reply only, without including the entire chat
history. 
- A chat history is required to be a series of alternate "user" and "agent" messages. If that
is not the case - for example, two consecutive "user" messages - the history should be
considered invalid. 
- If the server receives an invalid chat history, it should reply with a 400 Bad Request.

#### Not required:
- The agent’s replies can be static content, meaning some fixed content. There's no need
to simulate a real agent.
- The text can appear on the front page in block, without streaming word by word.
- Chat persistence.
- User management (multi-user management, user authentication, etc.)

<br/>

## Back CMD using FastAPI, Pydantic
### Using Docker
#### Build the Docker image and install the full project
```commandline
make start
```
#### Debug container and launch server
```commandline
make debug
uvicorn main:app --host 0.0.0.0 --port 8000
```
#### Debug container and launch tests
```commandline
make debug
python3 -m unittest
```
#### Stop containers
```commandline
make stop
```
<br/>

### Without Docker
#### 1. Move to src folder
```commandline
cd back/src
```
#### 2. Install dependencies
```commandline
python3 install -r requirements.txt
```
#### 3.1 Launch server
```commandline
python3 -m uvicorn main:app --reload
```
#### 3.2 Launch tests
```commandline
python3 -m unittest
```

<br/>

## Front using React, TailwindCSS
### Using Docker
#### Build the Docker image and install the full project
```commandline
make start
```
#### Debug container and run app
```commandline
make debug
yarn start
```
#### Stop containers
```commandline
make stop
```
<br/>

### Without Docker
#### 1. Move to src folder
```commandline
cd front
```
#### 2. Install dependencies
```commandline
yarn install
```
#### 3. Run app
```commandline
yarn start
```