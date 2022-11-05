# -*- coding: utf-8 -*-

# avg2.py

# a simple program to average two exam scores
# Illustrates use of multiple input

def main():
        print("This program computes the average of two exam scores.")
        
        score1, score2 = eval(input("Enter two scores separated by a comma: "))
        average = (score1 + score2)/2
        
        print("The aveage of the scores is", average)

main()
