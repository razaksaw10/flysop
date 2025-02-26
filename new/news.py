{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "\n",
    "def guess_the_number():\n",
    "\tnumber_to_guess = random.randint(1, 100)\n",
    "\tguess = None\n",
    "\tattempts = 0\n",
    "\n",
    "\tprint(\"Welcome to the Number Guessing Game!\")\n",
    "\tprint(\"I have selected a number between 1 and 100. Can you guess what it is?\")\n",
    "\n",
    "\twhile guess != number_to_guess:\n",
    "\t\tguess = int(input(\"Enter your guess: \"))\n",
    "\t\tattempts += 1\n",
    "\n",
    "\t\tif guess < number_to_guess:\n",
    "\t\t\tprint(\"Too low! Try again.\")\n",
    "\t\telif guess > number_to_guess:\n",
    "\t\t\tprint(\"Too high! Try again.\")\n",
    "\t\telse:\n",
    "\t\t\tprint(f\"Congratulations! You've guessed the number in {attempts} attempts.\")\n",
    "\n",
    "guess_the_number()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to the Number Guessing Game!\n",
      "I have selected a number between 1 and 100. Can you guess what it is?\n",
      "Too high! Try again.\n",
      "Too low! Try again.\n",
      "Too high! Try again.\n",
      "Too high! Try again.\n",
      "Too low! Try again.\n",
      "Too low! Try again.\n",
      "Too high! Try again.\n",
      "Congratulations! You've guessed the number in 8 attempts.\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "def guess_the_number():\n",
    "\tnumber_to_guess = random.randint(1, 100)\n",
    "\tguess = None\n",
    "\tattempts = 0\n",
    "\n",
    "\tprint(\"Welcome to the Number Guessing Game!\")\n",
    "\tprint(\"I have selected a number between 1 and 100. Can you guess what it is?\")\n",
    "\n",
    "\twhile guess != number_to_guess:\n",
    "\t\tguess = int(input(\"Enter your guess: \"))\n",
    "\t\tattempts += 1\n",
    "\n",
    "\t\tif guess < number_to_guess:\n",
    "\t\t\tprint(\"Too low! Try again.\")\n",
    "\t\telif guess > number_to_guess:\n",
    "\t\t\tprint(\"Too high! Try again.\")\n",
    "\t\telse:\n",
    "\t\t\tprint(f\"Congratulations! You've guessed the number in {attempts} attempts.\")\n",
    "\n",
    "guess_the_number()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
