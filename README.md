# Hangman WIP

## Table of Content 
1. [Desciption](#description)
1. [Installation Instruction](#installation-instruction)
1. [Usage Instructions](#usage-instructions)
1. [File Structure](#file-structure)
1. [License Information](#license-information)


## Description
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

The project is built over several milestones as follow:

### Milestone 1: Environment Setup

Milestone 1 involves setting up the development environment, including the creation of a Conda environment named hangman_env. This ensures a consistent and isolated environment for running the game. Follow the installation instructions in the README to create the environment and install the necessary dependencies

### Milestone 2: Word Management and User Input

In this milestone, a naw module milestone_2.py has been added to the project, enhancing the game's functionality. This module handles the management of words, including the ability to input new words, choose a random word, get user guesses, and check the validity of the guesses. The module allows for a more dynamic and interactive experience for both users and developers.

### Milestone 3:  User Guess Validation and Word Checking

Milestone 3 introduces milestone_3.py, which builds upon the previous milestones. It includes functions for validating the user's guess, checking if the guess is in the chosen word, and providing appropriate feedback. This adds a crucial layer of interactivity and improves the overall gaming experience.

## Installation Instruction

### **Clone the Repository:**

```bash
   git clone https://github.com/MosElAgab/hangman938.git
   cd filepath/hangman938
```
### **Create and Activate Conda Environment**

```bash
    conda env create -f hangman_env.yml -n hangman_env
    conda activate hangman_env
```
### **Install Dependencies:**
```bash
    pip install -r requirements.txt
```
### **Run the Hangman Game:**
```bash
    #TODO
```
### **Updating the Conda Environment (if needed)**
```bash
    #TODO
    # FIXME
    conda env update -f hangman_env.yml -n hangman_env --prune
```

## Usage Instructions


## File Structure
```bash
.
├── README.md
├── hangman
│   └── hangman_Template.py
├── hangman_env.yml
├── milestones
│   ├── __pycache__
│   │   └── milestone_2.cpython-312.pyc
│   ├── milestone_2.py
│   └── milestone_3.py
└── requirements.txt
```

## License Information
MIT License

Copyright (c) 2023 Mostafa El Agab

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
