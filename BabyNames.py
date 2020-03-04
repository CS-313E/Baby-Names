#  File: BabyNames.py 

#  Description:  allows a user to query a data base of the 1000 most popular baby names 
#   in the United States per decade for the past 11 decades under the constraints described 

#  Student Name: Jadesola Jaiyesimi  

#  Student UT EID: jaj3847

#  Course Name: CS 313E

#  Unique Number: 50295

#  Date Created:February 7th, 2020

#  Date Last Modified: February 10th, 2020



class BabyNames():
    """Class to store all the baby names"""
    
    # Initializes the dictionary that will hold all the baby names
    def __init__(self):
        self.names = 0  # key: name
        self.ranks = 0  # value: list of ranks

    # Reads in the file and adds to the dictionary
    def fill_data(self, file_name):
        self.file_name = file_name
        infile = open(self.file_name, 'r')
        data_lines = (infile.readlines())
        global d
        d = {} 
        for i in data_lines:
            list_=i.split()
            key = list_[0]
            x = list_[1:]
            d[(key)] = x    #create dictionary

    # True if a name exists in the dictionary and False otherwise.
    def contains_name (self, name):
        self.name = name
        if self.name in d.keys():   
            return True

    # Returns all the rankings for a given name. Assume the name exists
    def find_ranking(self, names):
        self.name = names
        rankings = d.get(self.name) #list of integers containing the rankings from all 11 decades
        rankings = list(rankings)
        return rankings
        
    # Returns a list of names that have a rank in all the decades in sorted order by name.
    def ranks_of_all_decades(self):
        alpha_rank= []
        i = 0 
        for value in d.values(): #alphabetical order containing all the names that have a rank
            if '0' not in value:
                alpha_rank.append(list(d.keys())[i])
            i+=1
        return alpha_rank
    
            
    #  Returns a list of all the names that have a rank in a given decade in order of rank.
    def ranks_of_a_decade(self, decade):
        self.decade = decade
        rank = []
        x = int((int(self.decade)-1900)/10) #list index for year
        for i in range(len(d.values())):    #list of values
            if list(d.values())[i][x] != '1001':
                rank.append((list(d.keys())[i], int(list(d.values())[i][x])))
            rank.sort(key = lambda x: x[1]) #sort tuple (name,rank)
        return rank
            
        
    # Return all names that are getting more popular in every decade. The list must be sorted by name.
    def getting_popular(self):
        x = []
        for i in range(len(d.values())): 
            low,high = 9,10 
            val = list(d.values())[i]
            while (int(val[low])) > (int(val[high])) and (high != 0): #constantly gets lower rank
                low -= 1
                high -= 1
            if high == 0 and val[1:] != '0':
                 x.append((list(d.keys())[i]))
        return x
            

    # Return all names that are getting less popular in every decade. The list must be sorted by name.
    def less_popular(self):
        x = []
        for i in range(len(d.values())): 
            low,high = 9,10 
            val = list(d.values())[i]
            for vals in range(len(val)):
                if val[vals] == '0':
                    val[vals] = '1001'
            while int(val[low]) < int(val[high]) and high != 0: #constantly get higher rank
                low -= 1
                high -= 1
            if high == 0 and val[:10] != '1001':
                 x.append((list(d.keys())[i]))
        return x


def main():
	# create the menu with choices 
    #my_dict = dict(name = '',year = '',ranking = '') #empty dictionary to hold baby names
    name_baby = BabyNames()
    name_baby.fill_data('names.txt')
    while True: 
        print('\nOptions:') #menu options
        print('Enter 1 to search for names.')
        print('Enter 2 to display data for one name.')
        print('Enter 3 to display all names that appear in only one decade.')
        print('Enter 4 to display all names that appear in all decades.')
        print('Enter 5 to display all names that are more popular in every decade.')
        print('Enter 6 to display all names that are less popular in every decade.')
        print('Enter 7 to quit.\n')
        user_input = input('Enter choice: ')
        if user_input == '7': #quit
            print('\nGoodbye.')
            infile.close()
            break

        elif user_input == '1':  #search for names
            name = input('Enter a name: ')
            print()
            x = name_baby.find_ranking(name)
            if name_baby.contains_name(name) == True:
                print('The matches with their highest ranking decade are:')
                for num in range(len(x)): #change 0 to 1001
                    if x[num] == '0':
                        x[num] = '1001'
                    minimum = x[0]
                    i = 0
                for a in range(len(x)): 
                    if int(x[a]) < int(minimum):
                        minimum = x[a]
                        i = int(a)  #year with minimum rank
                    year = 1900+(10*i)
                print(name,year)
            else:
                print(name,'does not appear in any decade.')

        elif user_input == '2': #display data for one name 
            name = input('Enter a name: ')
            print()
            x = name_baby.find_ranking(name)
            print(str(name)+': ',end='')
            print(*x,sep=' ')
            for num in range(11):
                year = 1900+(10*num)    #calculate year
                if x[num] == '1001':
                    x[num] = '0'
                print(str(year)+":",(x[num])) 

        elif user_input == '3': #display all names that appear in one decade in order of rank
            decade = input('Enter decade: ')
            print('The names are in order of rank:')
            for i in name_baby.ranks_of_a_decade(decade):
                print(str(i[0])+':',i[1])

        elif user_input == '4': #display all names that appear in all decades.
            rank = name_baby.ranks_of_all_decades()
            total = len(rank)
            print(total,'names appear in every decade. The names are:') 
            for i in rank :
                print(i)

        elif user_input == '5':# display all names that are more popular in every decade
            name = name_baby.getting_popular()
            print (len(name),'names are more popular in every decade.')
            for i in name:
                print(i) 
        elif user_input == '6':#to display all names that are less popular in every decade
            name = name_baby.less_popular()
            print (len(name),'names are less popular in every decade.')
            for i in name:
                print(i)
    infile.close()

if __name__ == '__main__':
	main()


