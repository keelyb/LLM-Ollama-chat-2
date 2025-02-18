# Prerequisites 

- install ollama

- https://ollama.com/

# Run a model

From a command line interface:

- ollama run llama2

# list models
- ollama list 

# Create Superman assistant:
- ollama create superman -f ./modelfileSuperman.txt
- ollama list 
- ollama run superman

/bye  

# Create MIDIman assistant:
- ollama create midiman -f ./modelfileMIDI.txt
- ollama list 
- ollama run midiman

# Create DNAman assistant:
- ollama create dnaman -f ./modelfileDNA.txt
- ollama list 
- ollama run dnaman

# Run gradio web interface

- In order to run the gradio interface, install the python prerequisites:

- ONE TIME: In VSCODE or command line, create a gradio-env for python.
- python -m venv gradio-env

- Each time: When opening a new VSCode or new commandline, initialize your gradio python env.
- source gradio-env/bin/activate

- ONE time install:
- install python per your OS.
- pip install requests
- pip install gradio

# RUN python gradio interface:
- python main.py

- In browser, open:
- http://127.0.0.1:7860

# REFERENCES
- https://github.com/jmorganca/ollama/tree/main/docs
- https://www.gradio.app/guides/quickstart
- https://www.gradio.app/guides/creating-a-chatbot-fast
