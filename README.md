easy Autonomous General Intelligence
autonomous general learning model
# easyAGI is the goal, funAGI is the current working expression
<a href="https://github.com/autoGLM/funAGI">https://github.com/autoGLM/funAGI</a>

while this project is working several of the components are not integrated. Work on Autonomous General Learning Model is at the currently private repo <a href="https://github.com/autoGLM/easyGLM">easyGLM</a><br />

This version is second simplest yet highly functional decision from logic model that I have ever experienced. This project is an expansion upon a minimalist recursive approach to <a href="https://github.com/openmindx/agi">agi</a>.

 may the source be with you.

## Introduction

easyAGI is the UIUX to **openmindx** to deploy an easy-to-use Autonomous General Intelligence (AGI) solution from decision. Designed to solve a wide range of problems using the power of API calls including OpenAI's GPT-4 model. This codebase provides a simple interface for users to input problems and receive intelligent decision as solution in real-time. This openmindx expression is a point of departure framework for a machine capable of self devleopment into a robust autonomous general intelligence. The openmindx easyAGI is being used to continue the work on autoGLM (autonomous general learning model). The code is pure python3 so far and the .md files are markdown documentation of each component. Modular architecture is intentional for extending or including any aspect of autoGLM into existing projects is straightforward.

python3 easyAGI.py; currently the default number of tokens in reasoning.py and SocraticReasoning.py is set remarkably low at 100 tokens.  This is a basic point of departure archived for basic interaction with an API key using pure python. For the most minimalist python3 approach to GPT-4o API interactive example see <a href="https://github.com/openmindx/agi">agi</a>. This project repo is a continuation of the point of departure AGI found at <a href="https://github.com/openmindx/easyAGI">openmindx</a>

easyAGI is a modular, Python-based project designed to create an autonomous general intelligence (AGI) interface that leverages various AI models and reasoning frameworks. The project integrates multiple components such as belief-desire-intention (BDI) modeling, logic tables, self-healing systems, and API management to form a cohesive system capable of learning, reasoning, decision-making, and self-maintenance.
Key Components

    API Management:
        APIManager: Handles loading, adding, removing, and listing API keys interactively. It ensures the necessary API keys are available for different AI providers such as OpenAI, Groq, and Ollama.

    BDI Model:
        Belief: Represents beliefs with logical and reasoning capabilities.
        Desire: Defines goals or desires the system aims to achieve.
        Intention: Outlines plans based on beliefs and desires to accomplish goals.
        Goal: Evaluates conditions to determine if goals are fulfilled.
        Reward: Updates and tracks rewards based on achieved goals.

    Logic Tables:
        LogicTables: Manages logical variables and expressions, generates truth tables, and saves state to memory for reasoning processes.

    Reasoning and Socratic Reasoning:
        Reasoning: Adds, challenges, and draws conclusions from premises using models like GPT-4 or Groq.
        SocraticReasoning: Employs a Socratic method to challenge premises and derive logical conclusions.

    Self-Healing System:
        SelfHealingSystem: Monitors system health (CPU, memory, disk usage), attempts to heal the system if unhealthy, and ensures continuous operation.

    Memory Management:
        Memory: Handles saving, loading, and deleting conversation memories to ensure continuity and historical context.

    Chatter Models:
        GPT4o, GroqModel, OllamaModel: Interfaces with different AI providers to generate responses based on given knowledge.

    Main AGI Class:
        AGI: Integrates all components, manages API keys, perceives environment data, learns from data, makes decisions, and communicates responses in an interactive loop.

Key Files

    api.py: Manages API keys.
    bdi.py: Defines the BDI model components.
    chatter.py: Implements interfaces for different AI models.
    easyAGI.py: Main entry point that integrates all components and runs the AGI loop.
    logic.py: Manages logic tables and truth table generation.
    memory.py: Handles conversation memory management.
    reasoning.py: Implements reasoning functionalities.
    self_healing.py: Implements self-healing system functionalities.
    SocraticReasoning.py: Implements Socratic reasoning functionalities.
    test_self_healing.py: Unit tests for the self-healing system.

Project Goals

    Modular Expansion: The project is designed to be modular, allowing for easy addition of new components and models.
    Adaptive Learning: Implement continuous learning and adaptation from new data inputs.
    Comprehensive Reasoning: Enhance reasoning capabilities by integrating more sophisticated logical and Socratic reasoning methods.
    System Robustness: Ensure system reliability through self-healing mechanisms and robust memory management.

Next Steps

    Expand Reasoning Capabilities: Integrate more advanced reasoning algorithms and models.
    Improve Memory Management: Enhance the memory system to handle more complex interactions and historical data.
    Enhance Self-Healing: Develop more sophisticated self-healing methods, such as automated service restarts and resource management.
    API Integration: Add support for additional AI models and APIs to diversify the AGI's capabilities.
    User Interface: Develop a user-friendly interface to interact with the AGI system, making it accessible for various applications.


# easyAGI using openmindx to create autoGLM

## Requirements

- Python 3.6+
- API key openai GPT-4o
- `python-dotenv` package

## Installation venv recommended

Clone the repository:
   ```bash
   git clone https://github.com/autoGLM/easyAGI
   cd easyAGI
   python3 -m venv easyagi
   source easyagi/bin/activate
   pip install -r requirements.txt
   python3 easyAGI.py
   ```

