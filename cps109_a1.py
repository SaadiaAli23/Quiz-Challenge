#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 23:05:25 2023

@author: saadiaali
"""

# Quiz maker and game
# Problem
# A quiz created by the user consisting of 3 questions in which the user creates the questions, provides some options, and the correct answer to each question. 
# Once the quiz is created the quiz should begin and should allow the players to input the number of players.
# Then each player should take turns answering each question.
# Once the players have answered all the question, they should be able to see if there is a winner or if there are any ties.
# Players should also be able to see their scores in percentage form. 
# If there are no ties, there should also be a scoreboard that ranks the players based on their scores.

#Instructions
file = open("cps109_a1_input.txt")
print(file.read())
file.close()

nplayers = int(input("\nEnter the number of players: ")) # Takes input from user to input the number of players who will be playing the quiz
players = {} # dictionary that holds all the players
for i in range(1, nplayers+1): # loops thorugh the number of players
    players["Player " + str(i)] = 0 # updates the dictionary and sets every player to 0 
turns = 0 
questions = []
options = []
answers = []
print("You will create 3 questions for your quiz.")
#user input for questions, options, and answers
question_1 = str(input("Enter Question 1: "))
questions.append(question_1)
opt_1 = input("\nEnter 2-4 options (seperated by commas in which there is one correct response: ")
options.append(opt_1)
ans_1 =  input("\nEnter the correct response to question 1: ")
answers.append(ans_1)

question_2 = str(input("\nEnter Question 2: "))
questions.append(question_2)
opt_2 = input("\nEnter 2-4 options in which there is one correct response: ")
options.append(opt_2)
ans_2 =  input("\nEnter the correct response to question 2: ")
answers.append(ans_2)

question_3 = str(input("\nEnter Question 3: "))
questions.append(question_3)
opt_3 = input("\nEnter 3 options in which there is one correct response: ")
options.append(opt_3)
ans_3 =  input("\nEnter the correct response to question 3: ")
answers.append(ans_3)

print('\n' * 15)
print("Lets begin the Quiz!")

while turns < nplayers : 
    for i in range(len(questions)): # For loop that loops through every question
        print("\nQuestion " + str(i+1) + ": " + questions[i])
        print("options: " + options[i])
        for j in players: # for loop that loops through the players so that every players gets a turn to input the answer
            print("\nPlayer " + str(int(j[-1])) + " its your turn:")
            answer = input("Enter answer: ")
            if answer == answers[i]:
                players[j] += 1
                turns += 1
            if answer != answers[i]:
                turns += 1
#print(players)

# Winner 
scores = list(players.values()) # Variable that converts the values in the dictionary to a list
scores.sort() # sort the list so that the values that are the same will be next to eachother and the following loop can check to see if there are any duplicates
Tie = 0
count = 0
maxx = max(players, key=players.get)
for s in range(len(scores)-1):
    if max(scores) == scores[s+1]:
        count += 1
    if scores[s] == scores[s+1]: # Check to see if any two players have the same score 
            Tie += 1
                # adds one to the variable 'Tie' (If there are any ties)
# If the count is more than 1 (more than one occurences of the same value), then print out Tie, otherwise print the winner
if count > 1:  
        print("\nTie! No Winner...")
else:
    print("\nThe Winner is.... ")
    print(maxx + "!")

#Scores 
print("\nScores:")
scores_store = []
for key, value in players.items(): # Loops through the dictionary (both the key and the value)
    percent = ( key + ":", str(round(value/3, 2)) + "%") 
    print('\n' + key + ":", str(round(value/3, 2)) + "%") # prints the percentage score (to 2 decimal places) corelating to each key (player)
    scores_store.append(percent) # Appends the key and corresponding value to a list (list of scores) 
#Scoreboard
final = []
while len(players) > 0: # While loop that repeats block of code until the dictionary, players, is empty
    for x, y in players.items(): # Loops through the key and value in the dictionary
            maxx = max(players.values()) # Finds the max value from the dictionary, players
            if y == maxx: 
                final.append(x) # appends the max value to a list named final
                break
    players.pop(x) # Remove the max value from the dictionary so that the next time the block of code runs, it finds the next largest value

print("\nScorebaord:  \n")
for p in range(len(final)):
        if Tie != 0: # Checks to see if there are any ties
            print("No scoreboard as there were one or more ties")
            break
        print(str(p+1) + ". " + final[p]) # prints player and ranks them based on the scores 

#output
outfile = open('cps109_a1_output.txt', 'w')
outfile.write("scores: " + str(scores_store))

outfile.close()    