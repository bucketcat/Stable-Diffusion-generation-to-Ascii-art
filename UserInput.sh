#!/bin/bash

# Accept user input for prompt and steps
read -p "Enter prompt: " prompt
read -p "Enter steps: " steps

# Call Python script with user input
python ascii2.py "$prompt" "$steps"
 read -p "Press any key to exit"
