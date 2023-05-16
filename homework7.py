# PPHA 30537
# Spring 2023
# Homework 7

# YOUR NAME HERE

# YOUR CANVAS NAME HERE
# YOUR GITHUB USER NAME HERE

# Due date: Monday May 15th before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.

##################

# Question 1: Explore the data APIs available from Pandas DataReader.  Pick
# any two countries, and then 
#   a) Find two sets of data for each that cover these places for overlapping 
#      time periods.  There should be exactly four dataframes and four individual
#      downloads (e.g. do not use one line to download two datasets).
#      - At least one should be from the World Bank, and at least one should
#        not be from the World Bank.
#      - At least one should have a frequency that does not match the others,
#        e.g. annual, quarterly, monthly.
#   b) Adjust the data so that all four are at the same frequency (you'll have
#      to look this up), then merge them together into one long (tidy) format
#      dataframe.
#   c) Finally, go back and change your earlier code so that the
#      countries and dates are set in variables at the top of the file.  Your
#      final result for parts a and b should allow you to (hypothetically) 
#      modify these values easily so that your code would download the data
#      and merge for different countries and dates.
#      - You do not have to leave your code from any previous way you did it
#        in the file. If you did it this way from the start, congrats!
#      - You do not have to account for the validity of all the possible 
#        countries and dates, e.g. if you downloaded the US and Canada for 
#        1990-2000, you can ignore the fact that maybe this data for some
#        other two countries aren't available at these dates.
#   d) Clean up any column names and values so that the data is consistent
#      and clear, e.g. don't leave some columns named in all caps and others
#      in all lower-case, or a column of mixed strings and integers.  Write 
#      the dataframe you've created out to a file named q1.csv, and commit
#      it to your repo.



# Question 2: On the following Harris School website:
# https://harris.uchicago.edu/academics/design-your-path/certificates/certificate-data-analytics
# There is a list of six bullet points under "Required courses" and ten 
# bullet points under "Elective courses".  Using requests and BeautifulSoup: 
#   - Collect the text of each of these bullet points
#   - Add each bullet point to the csv_doc list below as strings (following 
#     the header already specified). The first string you add should be: 
#     'required,PPHA 30535 or PPHA 30537,Data and Programming for Public Policy I\n'
#     (recall that \n is the new-line character in text)
#   - Using context management, write the contents of csv_doc out to a file named q2.csv
#   - Finally, import Pandas and test loading q2.csv with the read_csv function.
#     Use asserts to test that the dataframe has 16 rows and three columns.

csv_doc = ['type,code,course title\n']
