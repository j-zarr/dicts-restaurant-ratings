"""Restaurant rating lister."""

"""Restaurant name and score"""

scores = {}

#process file
file = open('scores.txt')

for line in file:
    line = line.rstrip().split(":")  # OR line = line.split(":")
    scores[line[0]] = line[1] #add name and rating to score dict

#prompt user
print("Add the restaurant and rating")
restaurant = input("restaurant name: ")
rating = input("restaurant rating: ")

scores[restaurant] = rating #add user input to scores dict

file.close()

#sort and print final scores
sorted__scores = sorted(scores.items()) #sort scores in abc order -> this is a list of tuples (name, rating)

for name, rating in sorted__scores: #print name and rating from sorted_scores
    print (f"{name}: {rating}")
      





