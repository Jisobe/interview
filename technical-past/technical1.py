# // Technical Interview Question: Consecutive Count

# //// CHALLENGE 

# // Write a function that takes in two inputs: 1. A list ("data"), and 2. An Integer ("N") and returns a count representing the number of times the target repetition length is detected in the input data list. A target repetition of "N" is achieved if there are N consecutive values that are identical in the input data list. Also note, that a single sequence can include "overlaps", meaning you can reuse items from one repetition sequence in another. See the example below...

# //// EXAMPLE

# // Sample Input:
# // 1. data = ["D", "G", "C", "C", "C", "C", "E", "E", "E", "G", "B", "B", "B", "B", "B", "B", "D", "G", "G", "G"]
# // 2. target repetition length (N) = 4

# // Expected Output: 4 ... because there is a consecutive sequence of ["C", "C", "C", "C"], and *three* unique consecutive sequences of ["B", "B", "B", "B"] in the input data

def fun(data, N):
    matches = []
    for index, letter in enumerate(data):
        if index != len(data)-1:
            if data[index] == data[index + 1]:
                matches.append(letter)
                print(matches)


data = ["D", "G", "C", "C", "C", "C", "E", "E", "E", "G", "B", "B", "B", "B", "B", "B", "D", "G", "G", "G"]
N = 4
fun(data, N)