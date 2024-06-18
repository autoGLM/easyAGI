easy Autonomous General Intelligence

## Introduction

easyAGI is the UIUX to **openmindx** to deploy an easy-to-use Autonomous General Intelligence (AGI) solution created from decision. Designed to solve a wide range of problems using the power of API calls including OpenAI's GPT-4 model. This codebase provides a simple interface for users to input problems and receive intelligent decision as solution in real-time. This openmindx expression is a point of departure framework for a machine capable of self devleopment into a robust autonomous general intelligence.

Improvements will follow. While the design plans for an AGI have spanned 20 years of casual thinking 1 year of study and this easyAGI was deployed in 1 day with the help of python3 easyAGI.py; currently the default number of tokens in reasoning.py and SocraticReasoning.py is set quite low at 100 tokens. The field will become dynamic. This current setup is unique as you can watch the machine "think" through premise and truth table.


# openmindx

## Introduction

Welcome to **OPENMINDx**, an advanced AI-driven solution designed to facilitate autonomous general intelligence (AGI) through a sophisticated and user-friendly interface, **easyAGI**. openmindx leverages cutting-edge machine learning, deep learning, and natural language processing technologies to deliver seamless, intuitive, and highly effective AGI experiences.

## Features

### Autonomous General Intelligence
- **Dynamic Problem Solving**: OpenMindX is equipped with recursive AGI capabilities to provide reasoning from logic. easyAGI dynamically understands solving a wide range of problems through natural language input.
- **BDI Model Integration**: Incorporates the Belief-Desire-Intention (BDI) model to enhance decision-making processes and action planning.

### EasyAGI User Interface
- **Intuitive Design**: EasyAGI offers a clean, user-friendly interface that simplifies interaction with the AGI system from the terminal using python3. Users can easily input problems, receive solutions, and manage conversation history.
- **Real-Time Feedback**: Provides instant solutions and conclusions based on user input, facilitating continuous learning and adaptation.

### Memory Management
- **Persistent Storage**: Stores conversation history in a local `memory` folder, ensuring that all interactions are saved for future reference.
- **Dynamic Loading and Deletion**: Load previous conversations or delete memory as needed, providing flexibility and control over the stored data.

### Enhanced Reasoning and Logic
- **Socratic Reasoning**: Utilizes Socratic questioning techniques to challenge and refine premises, ensuring robust and logical conclusions.
- **Logic Tables**: Implements logic tables to evaluate and verify logical expressions, enhancing the system's reasoning capabilities.

### Self-Healing Capabilities (in progress)
- **Error Handling**: Automatically detects and handles errors, ensuring the system remains stable and reliable.
- **Dynamic Adjustment**: Allows for real-time adjustment of system settings to optimize performance and response quality.

## Features

- Simple terminal interface to input problems and receive solutions.
- custom API inclusion including OpenAI's GPT-4 model for generating solutions.
- Continuously runs, allowing for multiple queries until the user decides to exit.
- local context from memory
- Modular design for easy extension and integration with other systems.

## future

- integration with an executable environment
- expand self_healing.py
- include mastermind.agency.py
- llama2 integrations
- mastermind as the controller of agency.

## Requirements

- Python 3.6+
- API key openai GPT-4o
- `python-dotenv` package

## Installation venv recommended

Clone the repository:
   ```bash
   git clone https://github.com/openmindx/easyAGI
   cd easyAGI
   python3 -m venv easyagi
   source easyagi/bin/activate
   pip install -r requirements.txt
   python3 easyAGI.py
   ```

