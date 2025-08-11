# **Collatz Conjecture Visualizer**

This repository contains a simple Python script to explore and visualize the fascinating **Collatz Conjecture**. It takes a positive integer from the user, generates the sequence according to the conjecture's rules, and then plots the sequence to show its progression.

## **The Collatz Conjecture**

The Collatz Conjecture is an unsolved problem in mathematics. It states that if you start with any positive integer and repeatedly apply the following rules, you will eventually reach the number 1:

* If the current number is **even**, divide it by 2\.  
* If the current number is **odd**, multiply it by 3 and add 1\.

The program helps you see this behavior in action for any number you choose.

## **Features**

* **Interactive User Input**: A simple command-line interface prompts you for an integer.  
* **Sequence Calculation**: Generates the complete Collatz sequence for the given starting number.  
* **Performance Metrics**: Reports the total number of steps to reach 1 and the highest value encountered in the sequence.  
* **Graphical Visualization**: Uses matplotlib to create a clear line graph of the sequence over time.

## **Prerequisites**

Before running the script, make sure you have Python installed. You also need the matplotlib library for plotting the graphs. If you don't have it, you can install it using pip:

pip install matplotlib

## **How to Run**

1. **Save the file**: Download the collatz\_conjecture.py file to your computer.  
2. **Open a terminal**: Navigate to the directory where you saved the file.  
3. **Execute the script**: Run the program with the following command:  
   python collatz\_conjecture.py

4. **Follow the prompts**: The program will ask you to "Enter a positive integer". Type in a number and press Enter. To exit the program, enter 0\.

## **Code Structure**

The script is broken down into a few key functions:

* collatz(n): This is the core function that calculates the entire sequence, tracks the steps, and finds the highest number.  
* evenfunction(n) and oddfunction(n): These are helper functions that apply the rules of the conjecture.  
* plot\_graph(log): This function uses the matplotlib library to create and display a plot from the generated sequence data.
