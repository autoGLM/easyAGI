# easyAGI (c) Gregory L. Magnusson GPLv3 2024
# openmindx (c) Gregory L. Magnusson MIT license 2024
# mastermind (c) codephreak MIT licence 2024

easy Autonomous General Intelligence

## Introduction

easyAGI is the UIUX to **openmindx** to create an easy-to-use Autonomous General Intelligence (AGI) solution creator designed to solve a wide range of problems using the power of API calls including OpenAI's GPT-4 model. This codebase provides a simple interface for users to input problems and receive intelligent solutions in real-time. mastermind is the controller of agency.

## Features

- Simple user interface to input problems and receive solutions.
- Utilizes OpenAI's GPT-4 model for generating solutions.
- Continuously runs, allowing for multiple queries until the user decides to exit.
- Modular design for easy extension and integration with other systems.

## Requirements

- Python 3.6+
- OpenAI API key
- `python-dotenv` package

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/openmindx/easyAGI
   cd easyAGI
   python3 -m venv easyagi
   source easyagi/bin/activate
   pip install -r requirements.txt
   python3 easyAGI.py

