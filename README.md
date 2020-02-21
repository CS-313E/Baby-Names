# Baby-Names
Complete a program that allows a user to query a data base of the 1000 most popular baby names in the United States per decade for the past 11 decades under the constraints described below. As always, you may add helper functions and should do so to provide structure to the program and reduce redundancy. One additional constraint: You must use a Dictionary in the solution. You are encouraged to use functions in the String, List and Dictionary classes to make the program easier to write. The Dictionary class has lots of functions that can make your job easier and one of the goals of this assignment is to learn those functions.

Your program will be processing a file with data obtained from the Social Security Administration. They provide a web site showing the distribution of names chosen for children over the last 100 years in the US (www.ssa.gov/OACT/babynames/).

The data represent the 1000 most popular boy and girl names for children born in the US going back to 1900. The data can be boiled down to a single text file as shown below. On each line we have the name, followed by the rank of that name in 1900, 1910, 1920, ..., 2000 (11 numbers). A rank of 1 was the most popular name that year, while a rank of 997 was not very popular. A 0 means the name did not appear in the top 1000 that year at all. The lines are in alphabetical order.

...
Sam 58 69 99 131 168 236 278 380 467 408 466
Samantha 0 0 0 0 0 0 272 107 26 5 7
Samara 0 0 0 0 0 0 0 0 0 0 886
Samir 0 0 0 0 0 0 0 0 920 0 798
Sammie 537 545 351 325 333 396 565 772 930 0 0
Sammy 0 887 544 299 202 262 321 395 575 639 755
Samson 0 0 0 0 0 0 0 0 0 0 915
Samuel 31 41 46 60 61 71 83 61 52 35 28
Sandi 0 0 0 0 704 864 621 695 0 0 0
Sandra 0 942 606 50 6 12 11 39 94 168 257
...

Note, a 0 in the data file means the name was not ranked in the top 1000 for the corresponding decade. It has some unknown rank greater than 1000. When you store a 0 from the data file in your Dictionary objects you may use something other than 0 if you think it will make your algorithms easier to implement. (Recall altering the way data is stored to fit our needs is part of the magic of programming.)

We see that Sam was #58 in 1900 and is slowly moving down. Samantha is moving up strong to #7. Samir barely appears in 1980, but by 2000 is up to #798. The database is for children born in the US, so ethnic trends show up when immigrants have kids.

Suggested steps for implementing the program.

0. Create an empty dictionary to hold the baby names. Open the file names.txt and read each line of data. The baby names become the key and the rankings are stored in a list that becomes the value. You may store a rank of a 0 as 1001.

1. Create a loop in which you display the menu choices. Read the user's choice and call a function to perform the necessary action. If the user chooses to quit, break out of the loop.

2. Write a function that returns True if a name exists in the dictionary and False otherwise.

3. Write a function that returns all the rankings for a given name.

4. Write a function that returns a list of names that have a rank in all the decades in sorted order by name.

5. Write a function that displays all the names that have a rank in a given decade in order of rank.

6. Write a function to display all names that are getting more popular in every decade. We must be sure that the popularity is increasing. In particular, if we have two 0s, we do not know for sure which one is less popular. But if we have only one 0 we know it is less popular than any other entry. This means that 0 (if present) must only be there for the first decade. The output must be sorted by name.

7. Write a function to display all names that are getting less popular in every decade. We must be sure that the popularity is decreasing. In particular, if we have two 0s, we do not know for sure which one is less popular. But if we have one 0 then we know that it is less popular than any other entry. This means 0 can only be present in the last decade (if there is any 0). The output must be sorted by name.

The menu choices are:

to search for names.
to display data for one name.
to display all names that appear in one decade in order of rank.
to display all names that appear in all decades.
to display all names that are more popular in every decade.
to display all names that are less popular in every decade.
to quit
The sample output is shown. Some of the output may not adhere strictly to the constraints that we have specified above.

8. You must use try-except-finally block in your code. You will read the file names.txt locally. After you have read in a line from the file you may have to change the encoding to utf8.

line = str (line, encoding = 'utf8')
