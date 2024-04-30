"""
1.Create an activity folder and an activity.py file inside of it.
2.Create 5 variables and output them in the command prompt in the following format:
    a."I am < name (string)> , and I am < age (integer)> years old, I work as a < occupation (string)> , and my rating for < movie (string)> is < rating (decimal)> %"
3.Create 3 variables, num1, num2, and num3
    a.Get the product of num1 and num2
    b.Check if num1 is less than num3
    c.Add the value of num3 to num2
4.Create a git repository named s01 inside your provided GitLab Subfolder.
5.Initialize a git repository, stage the files in preparation for a commit, create a commit with the message Add Activity Code and push the changes to the remote repository.
"""
name = "Pansa"
age = 27
occupation = "actress"
movie = "23.5"
rating = 100.00

print(f"I am {name}, and I am {age} years old, I work as a {occupation}, and my rating for {movie} is {rating}%")

num1 = 22 
num2 = 7
num3 = 27

product = num1*num2
print(product)
print(num1<num3)
print(num3+num2)