
from __future__ import print_function
import matplotlib.pyplot as plt

import os
import pprint
import tempfile

from typing import Dict, Text

import numpy as np



X=np.arange(0.0,1.0,0.01)
Y=X[::-1]

training_data = [
    ['The Shawshank Redemption',1994,'142 min','Drama',9.3,'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.','Frank Darabont','Tim Robbins',28341469,1],
    ['The Godfather',1972,'175 min','Crime, Drama',9.2,"An organized crime dynasty's aging patriarch transfers control of his clandestine empire to his reluctant son.",'Francis Ford Coppola','Marlon Brando',134966411,2],
    ['The Dark Knight',2008,'152 min','Action, Crime, Drama',9,'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.','Christopher Nolan','Christian Bale',53858444,3],
    ['The Godfather: Part II',1974,'202 min','Crime, Drama',9,'The early life and career of Vito Corleone in 1920s New York City is portrayed, while his son, Michael, expands and tightens his grip on the family crime syndicate.','Francis Ford Coppola','Al Pacino',57300000,4],
    ['12 Angry Men',1957,'96 min','Crime, Drama',9,'A jury holdout attempts to prevent a miscarriage of justice by forcing his colleagues to reconsider the evidence.','Sidney Lumet','Henry Fonda',436000,5],
    ['The Lord of the Rings: The Return of the King',2003,'201 min','Action, Adventure, Drama',8.9,"Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.",'Peter Jackson','Elijah Wood',642758,6],
]

header = ["Series_Title","Released_Year","Runtime","Genre","Rating","Overview","Director","Star","No_of_Votes","Identifiant"]
def unique_vals(rows, col):
    """Find the unique values for a column in a dataset."""
    return set([row[col] for row in rows])

def class_counts(rows):
    
    counts = {}  # a dictionary of label -> count.
    for row in rows:
        # in our dataset format, the label is always the last column
        label = row[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts

def is_numeric(value):
    """Test if a value is numeric."""
    return isinstance(value, int) or isinstance(value, float)

class Question:
    def __init__(self, column, value):
        self.column = column
        self.value = value

    def match(self, example):
        # Compare the feature value in an example to the
        # feature value in this question.
        val = example[self.column]
        if is_numeric(val):
            return val == self.value
        else:
            return val == self.value

    def __repr__(self):
        # This is just a helper method to print
        # the question in a readable format.
        condition = "=="
        if is_numeric(self.value):
            condition = "=="
        return "Is %s %s %s?" % (
            header[self.column], condition, str(self.value))

def partition(rows, question):
    """Partitions a dataset.
    cette partie permet de partitionner la base de données en des petits groupes

    For each row in the dataset, check if it matches the question. If
    so, add it to 'true rows', otherwise, add it to 'false rows'.
    """
    true_rows, false_rows = [], []
    for row in rows:
        if question.match(row):
            true_rows.append(row)
        else:
            false_rows.append(row)
    return true_rows, false_rows

def gini(rows):
    """
    la méthode du coefficient Gini impurity est l'une des méthodes utilisées au niveau de l'algorithme de l'arbre de décision
    ce coefficient nous donne une idée sur la division optimale: le niveau où va diviser la base de données
    plus le coefficient de gini est petit, plus la division est meilleure
    """
    counts = class_counts(rows)
    impurity = 1
    for lbl in counts:
        prob_of_lbl = counts[lbl] / float(len(rows))
        impurity -= prob_of_lbl**2
    return impurity

def info_gain(left, right, current_uncertainty):
    """Information Gain.

    The uncertainty of the starting node, minus the weighted impurity of
    two child nodes.
    """
    p = float(len(left)) / (len(left) + len(right))
    return current_uncertainty - p * gini(left) - (1 - p) * gini(right)

def find_best_split(rows):
    """Find the best question to ask by iterating over every feature / value
    and calculating the information gain."""
    best_gain = 0  # keep track of the best information gain
    best_question = None  # keep train of the feature / value that produced it
    current_uncertainty = gini(rows)
    n_features = len(rows[0]) - 1  # number of columns

    for col in range(n_features):  # for each feature

        values = set([row[col] for row in rows])  # unique values in the column

        for val in values:  # for each value

            question = Question(col, val)

            # try splitting the dataset
            true_rows, false_rows = partition(rows, question)

            # Skip this split if it doesn't divide the
            # dataset.
            if len(true_rows) == 0 or len(false_rows) == 0:
                continue

            # Calculate the information gain from this split
            gain = info_gain(true_rows, false_rows, current_uncertainty)

            # You actually can use '>' instead of '>=' here
            # but I wanted the tree to look a certain way for our
            # toy dataset.
            if gain >= best_gain:
                best_gain, best_question = gain, question

    return best_gain, best_question

class Leaf:
    """A Leaf node classifies data.

    This holds a dictionary of class (e.g., "Apple") -> number of times
    it appears in the rows from the training data that reach this leaf.
    """

    def __init__(self, rows):
        self.predictions = class_counts(rows)
class Decision_Node:
    """A Decision Node asks a question.

    This holds a reference to the question, and to the two child nodes.
    """

    def __init__(self,
                 question,
                 true_branch,
                 false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch
def build_tree(rows):
    gain, question = find_best_split(rows)

    if gain == 0:
        return Leaf(rows)

    true_rows, false_rows = partition(rows, question)
   
    true_branch = build_tree(true_rows)
    # Recursively build the false branch.
    false_branch = build_tree(false_rows)
   
   

    # Return a Question node.
    # This records the best feature / value to ask at this point,
    # as well as the branches to follow
    # dependingo on the answer.
    return Decision_Node(question, true_branch, false_branch)


def print_tree(node, spacing=""):
    """World's most elegant tree printing function."""

    #cas où on est arivé à une feuille (un résultat)
    if isinstance(node, Leaf):
        print (spacing + "Predict", node.predictions)
        return

    # Print the question at this node
    print (spacing + str(node.question))
   
    # Call this function recursively on the true branch
    print (spacing + '--> True:')
    print_tree(node.true_branch, spacing + "  ")
   
    # Call this function recursively on the false branch
    print (spacing + '--> False:')
    print_tree(node.false_branch, spacing + "  ")
   

my_tree = build_tree(training_data)
print_tree(my_tree)

def classify(row, node):
    """See the 'rules of recursion' above."""

    # Base case: we've reached a leaf
    if isinstance(node, Leaf):
        return node.predictions

    # Decide whether to follow the true-branch or the false-branch.
    # Compare the feature / value stored in the node,
    # to the example we're considering.
    if node.question.match(row):
        return classify(row, node.true_branch)
    else:
        return classify(row, node.false_branch)

def print_leaf(counts):
    """A nicer way to print the predictions at a leaf."""
    total = sum(counts.values()) * 1.0
    probs = {}
    for lbl in counts.keys():
        probs[lbl] = str(int(counts[lbl] / total * 100)) + "%"
    return probs

# Evaluate
testing_data = [
    ['The Shawshank Redemption',1994,'142 min','Drama',9.3,'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.','Frank Darabont','Tim Robbins',28341469,1],
    ['The Godfather',1972,'175 min','Crime, Drama',9.2,"An organized crime dynasty's aging patriarch transfers control of his clandestine empire to his reluctant son.",'Francis Ford Coppola','Marlon Brando',134966411,2],
    ['The Dark Knight',2008,'152 min','Action, Crime, Drama',9,'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.','Christopher Nolan','Christian Bale',53858444,3],
    ['The Godfather: Part II',1974,'202 min','Crime, Drama',9,'The early life and career of Vito Corleone in 1920s New York City is portrayed, while his son, Michael, expands and tightens his grip on the family crime syndicate.','Francis Ford Coppola','Al Pacino',57300000,4],
    ['12 Angry Men',1957,'96 min','Crime, Drama',9,'A jury holdout attempts to prevent a miscarriage of justice by forcing his colleagues to reconsider the evidence.','Sidney Lumet','Henry Fonda',436000,5],
    ['The Lord of the Rings: The Return of the King',2003,'201 min','Action, Adventure, Drama',8.9,"Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.",'Peter Jackson','Elijah Wood',642758,6],
]
for row in testing_data:
    print ("Actual: %s. Predicted: %s" %
           (row[-1], print_leaf(classify(row, my_tree))))

"""Gini=Ginx(X,Y)
plt.plot(X,Gini)
plt.axhline(y=0.5,color='r',linestyle='--')
plt.title('Gini Impurity Graph')
plt.xlabel('P1=1')
plt.ylabel('Impurity Measure')
plt.ylim([0,1.1])
plt.show()"""