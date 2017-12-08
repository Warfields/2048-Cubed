import random # For creating new tiles
import numpy as np # For arrays
class game:
    def __init__(self): 
        self.game_box = np.zeros((4,4,4)) #initially making the 4*4*4 array's value 0 or "nothing" for all positions
        first_position_list = [0,1,2,3]
        first_row_to_begin = random.choice(first_position_list) #Randomly generates starting pos
        first_column_to_begin = random.choice(first_position_list)
        first_depth_to_begin = random.choice(first_position_list)
        self.game_box[first_row_to_begin][first_column_to_begin][first_depth_to_begin] = 2 #placing the first 2 to begin the game in position selected randomly
        self.points = 0 #Score starts at zero
        
    def matrix(self): # exports current gamestate
        return self.game_box
    def up_movement(self):
        #def up_movement(self.game_box): #function for up movement
        i = 0
        for k in range(0,4): #looping through all 2D matrix's in cube
            for j in range(0,4): #looping through all four 4 columns
                if self.game_box[i][j][k]!=0 or self.game_box[i+1][j][k]!=0 or self.game_box[i+2][j][k]!=0 or self.game_box[i+3][j][k]!=0: #condition to check whether any members of a column is non-zero to proceed
                    if self.game_box[i][j][k]==0: #condition to check if first member of a column is zero
                        while self.game_box[i][j][k] == 0: #looping until the first member of a column becomes non zero i.e moving lower members to top
                            self.game_box[i][j][k] = self.game_box[i+1][j][k]
                            self.game_box[i+1][j][k] = self.game_box[i+2][j][k]
                            self.game_box[i+2][j][k] = self.game_box[i+3][j][k]
                            self.game_box[i+3][j][k] = 0
                             
                    if self.game_box[i+1][j][k]==0 and (self.game_box[i+2][j][k]!=0 or self.game_box[i+3][j][k]!=0): #condition to check if the second member of a column is zero and members below it are non-zero
                        while self.game_box[i+1][j][k]==0: #looping until second member of a column becomes non-zero i.e moving lower member upwards
                            self.game_box[i+1][j][k] = self.game_box[i+2][j][k]
                            self.game_box[i+2][j][k] = self.game_box[i+3][j][k]
                            self.game_box[i+3][j][k] = 0
                    if self.game_box[i+2][j][k] == 0 and self.game_box[i+3][j][k]!=0: #condition to check if the third member of a column is zero and member below it or the last member is non-zero         
                        while self.game_box[i+2]==0: #looping until the third member of a column becomes non-zero
                            self.game_box[i+2][j][k] = self.game_box[i+3][j][k] 
                            self.game_box[i+3][j][k] = 0
        self.up_addition()
    def up_addition(self):
        i=0
        for k in range(0,4):
            for j in range(0,4): #looping through all the columns
                if self.game_box[i][j][k]==self.game_box[i+1][j][k]: #condition to check if the first and second member of a column are equal or same
                    self.game_box[i][j][k]=self.game_box[i][j][k]+self.game_box[i+1][j][k] #adding first and second member of a column and storing it as the first member
                    self.points += self.game_box[i][j][k] ** 2 #adding point for joining simillar tiles
                    self.game_box[i+1][j][k]=self.game_box[i+2][j][k] #moving third member of a column to second position
                    self.game_box[i+2][j][k]=self.game_box[i+3][j][k] #moving fourth member of a column to third position
                    self.game_box[i+3][j][k]=0 #assigning fourth member of a column as 0 i.e nothing
         
                if self.game_box[i+1][j][k]==self.game_box[i+2][j][k]: #condition to check if the second and third member of a column are equal or same
                    self.game_box[i+1][j][k]=self.game_box[i+1][j][k]+self.game_box[i+2][j][k] #adding second and third member of a column and storing it as second member
                    self.points += self.game_box[i+1][j][k] ** 2 #adding self.points for joining simillar tiles
                    self.game_box[i+2][j][k]=self.game_box[i+3][j][k] #moving fourth member to third position
                    self.game_box[i+3][j][k]=0 #assigning the fourth member to 0 or nothing
         
                if self.game_box[i+2][j][k]==self.game_box[i+3][j][k]: #condition to check if the third and fourth member of a column are equal or same
                    self.game_box[i+2][j][k]=self.game_box[i+2][j][k]+self.game_box[i+3][j][k] #adding third and fourth member of a column and storing it a third member
                    self.points += self.game_box[i+2][j][k] ** 2 #adding self.points for joining simillar tiles
                    self.game_box[i+3][j][k]=0 #assigning fourth member to 0 or nothing
    def down_movement(self): #function for down movement
        i=0
        for k in range(0,4):
            for j in range(0,4): #looping through all the columns
                if self.game_box[i][j][k]!=0 or self.game_box[i+1][j][k]!=0 or self.game_box[i+2][j][k]!=0 or self.game_box[i+3][j][k]!=0: #condition to check if any members of a column is non-zero in order to begin
                    if self.game_box[i+3][j][k]==0: #condition to check if the last member(fourth member) of a column is zero
                        while self.game_box[i+3][j][k]==0: #looping until the fourth member of a column becomes non-zero i.e moving the upper members to the bottom
                            self.game_box[i+3][j][k]=self.game_box[i+2][j][k]
                            self.game_box[i+2][j][k]=self.game_box[i+1][j][k]
                            self.game_box[i+1][j][k]=self.game_box[i][j][k]
                            self.game_box[i][j][k]=0
         
                    if self.game_box[i+2][j][k]==0 and (self.game_box[i+1][j][k]!=0 or self.game_box[i][j][k]!=0): #condition to check if the third member of a column is zero and any members above it is non-zero
                        while self.game_box[i+2][j][k]==0: #looping until the third member of a column becomes non-zero
                            self.game_box[i+2][j][k]=self.game_box[i+1][j][k]
                            self.game_box[i+1][j][k]=self.game_box[i][j][k]
                            self.game_box[i][j][k]=0
         
                    if self.game_box[i+1][j][k]==0 and self.game_box[i][j][k]!=0: #condition to check if the second member of a column is zero and member above it(first member is non-zero)
                        while self.game_box[i+1][j][k]==0: #looping until the second member becomes non-zero
                            self.game_box[i+1][j][k]=self.game_box[i][j][k]
                            self.game_box[i][j][k]=0
        self.down_addition()
    def down_addition(self): #function for downward addition after downward movement
        i=0
        for k in range(0,4): #loop through all matrices
            for j in range(0,4): #looping through all the columns
                if self.game_box[i+3][j][k]==self.game_box[i+2][j][k]: #condition to check if the fourth member and third member of a column are equal or same
                    self.game_box[i+3][j][k]=self.game_box[i+3][j][k] + self.game_box[i+2][j][k] #Adding fourth and third member of a column and storing as the fourth member
                    self.points += self.game_box[i+3][j][k] ** 2 #adding self.points for joining simillar tiles
                    self.game_box[i+2][j][k]=self.game_box[i+1][j][k] #Moving the second member to third position in a column
                    self.game_box[i+1][j][k]=self.game_box[i][j][k] #Moving the first member to second position in a column
                    self.game_box[i][j][k]=0 #Assigning the first member of a column to zero
         
                if self.game_box[i+2][j][k]==self.game_box[i+1][j][k]: #condition to check if the third member and second member of a column are equal or same
                    self.game_box[i+2][j][k]=self.game_box[i+2][j][k]+self.game_box[i+1][j][k] #Adding third and second member of a column and storing as the third member
                    self.points += self.game_box[i+2][j][k] ** 2 #adding self.points for joining simillar tiles
                    self.game_box[i+1][j][k]=self.game_box[i][j][k] #Moving the first member to second position in a column
                    self.game_box[i][j][k]=0 #Assigning zero to the first member of a column
         
                if self.game_box[i+1][j][k]==self.game_box[i][j][k]: #condition to check if the seconf and first member of a column are equal or same
                    self.game_box[i+1][j][k]=self.game_box[i+1][j][k]+self.game_box[i][j][k] #Adding the second and first member of a column and storing as the second member
                    self.points += self.game_box[i+1][j][k] ** 2 #adding self.points for joining simillar tiles
                    self.game_box[i][j][k]=0 #Assigning zero to the first member of a column
    def left_movement(self): #function for left movement
        j=0
        for k in range(0,4): #loop through all 2D matrices
            for i in range(0,4): #looping through all the rows
         
                if self.game_box[i][j][k]!=0 or self.game_box[i][j+1][k]!=0 or self.game_box[i][j+2][k]!=0 or self.game_box[i][j+3][k]!=0: #condition to check if members of a row is non-zero to proceed
                    if self.game_box[i][j][k]==0: #Condition to check if the first member of a row is zero
                        while self.game_box[i][j][k]==0: #looping until the first member of a row becomes non-zero
                            self.game_box[i][j][k]=self.game_box[i][j+1][k]
                            self.game_box[i][j+1][k]=self.game_box[i][j+2][k]
                            self.game_box[i][j+2][k] = self.game_box[i][j+3][k]
                            self.game_box[i][j+3][k]=0
         
                    if self.game_box[i][j+1][k]==0 and (self.game_box[i][j+2][k]!=0 or self.game_box[i][j+3][k]!=0): #condition to check if second member of a row is zero and any members right to it is non-zero
                        while self.game_box[i][j+1][k]==0: #looping until the second member of a row becomes non-zero
                            self.game_box[i][j+1][k]=self.game_box[i][j+2][k]
                            self.game_box[i][j+2][k]=self.game_box[i][j+3][k]
                            self.game_box[i][j+3][k]=0
         
                    if self.game_box[i][j+2][k]==0 and (self.game_box[i][j+3][k]!=0): #condition to check if third member of a row is zero and the member right to it(fourth member is non-zero
                        while self.game_box[i][j+2][k]==0: #looping until the third member of a row becomes non-zero
                            self.game_box[i][j+2][k]=self.game_box[i][j+3][k]
                            self.game_box[i][j+3][k]=0
        self.left_addition()
    def left_addition(self): #function for left addition after left movement
        j=0
        for k in range(0,4):
            for i in range(0,4): #looping through all the rows
                if self.game_box[i][j][k]==self.game_box[i][j+1][k]: #condition to check if the first member of a row is equal to the second member of a row
                    self.game_box[i][j][k]=self.game_box[i][j][k]+self.game_box[i][j+1][k] #Adding the first and second member and storing result as first member of a row
                    self.points += self.game_box[i][j][k] ** 2 #adding self.points for joining simillar tiles
                    self.game_box[i][j+1][k]=self.game_box[i][j+2][k] #Moving the third member of a row to second position
                    self.game_box[i][j+2][k]=self.game_box[i][j+3][k] #Moving the fourth member of a row to third position
                    self.game_box[i][j+3][k]=0 #Assigning 0 to the fourth member of a row
         
                if self.game_box[i][j+1][k]==self.game_box[i][j+2][k]: #Condition to check if the second member of a row is equal to the third member of that row
                    self.game_box[i][j+1][k]=self.game_box[i][j+1][k]+self.game_box[i][j+2][k] #Adding second and third member of a row and storing as second member
                    self.points += self.game_box[i][j+1][k] ** 2 #adding self.points for joining simillar tiles
                    self.game_box[i][j+2][k]=self.game_box[i][j+3][k] #Moving the fourth member of a row to third position
                    self.game_box[i][j+3][k]=0 #Assigning zero to the fourth member of a row
         
                if self.game_box[i][j+2][k]==self.game_box[i][j+3][k]: #Condition to check if the third and fourth member of a row are equal or same
                    self.game_box[i][j+2][k]=self.game_box[i][j+2][k]+self.game_box[i][j+3][k] #Adding the third and the fourth member of a row
                    self.points += self.game_box[i][j+2][k] ** 2 #adding self.points for joining simillar tiles
                    self.game_box[i][j+3][k]=0 #Assigning zero to the fourth member of a row
    def right_movement(self): #function for right movement
        j=0
        for k in range(0,4):
            for i in range(0,4): #looping through all the rows
                if self.game_box[i][j][k]!=0 or self.game_box[i][j+1][k]!=0 or self.game_box[i][j+2][k]!=0 or self.game_box[i][j+3][k]!=0: #condition to check if any members of a row is non zero in order to proceed
                    if self.game_box[i][j+3][k]==0: #Condition to check if the last(fourth) member of a row is zero
                        while self.game_box[i][j+3][k]==0: #looping until the last member of a row becomes non-zero
                            self.game_box[i][j+3][k]=self.game_box[i][j+2][k]
                            self.game_box[i][j+2][k]=self.game_box[i][j+1][k]
                            self.game_box[i][j+1][k]=self.game_box[i][j][k]
                            self.game_box[i][j][k]=0
         
                    if self.game_box[i][j+2][k]==0 and (self.game_box[i][j+1][k]!=0 or self.game_box[i][j][k]!=0): #Condition to check if the third member of a row is zero and any member before it(first and second) is non-zero
                        while self.game_box[i][j+2][k]==0: #looping until the third member of a row becomes non-zero
                            self.game_box[i][j+2][k]=self.game_box[i][j+1][k]
                            self.game_box[i][j+1][k]=self.game_box[i][j][k]
                            self.game_box[i][j][k]=0
         
                    if self.game_box[i][j+1][k]==0 and self.game_box[i][j][k]!=0: #Condition to check if the second member of a row is zero and member before it(first member) is non-zero
                        while self.game_box[i][j+1][k]==0: #looping until the second member becomes non-zero
                            self.game_box[i][j+1][k]=self.game_box[i][j][k]
                            self.game_box[i][j][k]=0
        self.right_addition()     
    def right_addition(self): #function for right addition after right movement
        j=0
        for k in range(0,4):
            for i in range(0,4): #looping through all the rows
                if self.game_box[i][j+3][k]==self.game_box[i][j+2][k]: #Condition to check if the fourth and third member of a row are equal
                    self.game_box[i][j+3][k]=self.game_box[i][j+3][k] + self.game_box[i][j+2][k] #Adding the fourth and third member of a row and storing it as the fourth member
                    self.points += self.game_box[i][j+3][k] ** 2 #adding self.points for joining simillar tiles
                    self.game_box[i][j+2][k]=self.game_box[i][j+1][k] #Moving the second member of a row to third position
                    self.game_box[i][j+1][k]=self.game_box[i][j][k] #Moving the first member of a row to second position
                    self.game_box[i][j][k]=0 #Assigning zero to the first member of a row
         
                if self.game_box[i][j+2][k]==self.game_box[i][j+1][k]: #Condition to check if the third and second member of a row are equal or same
                    self.game_box[i][j+2][k]=self.game_box[i][j+2][k]+self.game_box[i][j+1][k] #Adding the third and second member and storing it as the third member
                    self.points += self.game_box[i][j+2][k] ** 2 #adding self.points for joining simillar tiles
                    self.game_box[i][j+1][k]=self.game_box[i][j][k] #Moving first member of a row to second position
                    self.game_box[i][j][k]=0 #Assigning zero to the first member of a row
         
                if self.game_box[i][j+1][k]==self.game_box[i][j][k]: #Condition to check if the second and first member of a row are equal or same
                    self.game_box[i][j+1][k]=self.game_box[i][j+1][k]+self.game_box[i][j][k] #Adding second and first member of a row and storing it as second member of that row
                    self.points += self.game_box[i][j+1][k] ** 2 #adding self.points for joining simillar tiles
                    self.game_box[i][j][k]=0 #Assigning zero to the first member of a row
    def forward_movement(self): #function for forward movement
        k = 0
        for j in range(0,4):
            for i in range(0,4):
                if self.game_box[i][j][k]!=0 or self.game_box[i][j][k+1]!=0 or self.game_box[i][j][k+2]!=0 or self.game_box[i][j][k+3]!=0:
                    if self.game_box[i][j][k] == 0:
                        while self.game_box[i][j][k]  == 0:
                            self.game_box[i][j][k] = self.game_box[i][j][k+1]
                            self.game_box[i][j][k+1] = self.game_box[i][j][k+2]
                            self.game_box[i][j][k+2] = self.game_box[i][j][k+3]
                            self.game_box[i][j][k+3] = 0

                    if self.game_box[i][j][k+1] == 0 and (self.game_box[i][j][k+2] !=0 or self.game_box[i][j][k+3]!=0):
                        while self.game_box[i][j][k+1] == 0:
                            self.game_box[i][j][k+1] = self.game_box[i][j][k+2]
                            self.game_box[i][j][k+2] = self.game_box[i][j][k+3]
                            self.game_box[i][j][k+3] = 0

                    if self.game_box[i][j][k+2] == 0 and self.game_box[i][j][k+3]!=0:
                        while self.game_box[i][j][k+2]==0:
                            self.game_box[i][j][k+2] = self.game_box[i][j][k+3]
                            self.game_box[i][j][k+3] = 0
        self.forward_addition()
    def forward_addition(self):
        k = 0
        for j in range(0,4):
            for i in range(0,4):
                if self.game_box[i][j][k] == self.game_box[i][j][k+1]:
                    self.game_box[i][j][k] = self.game_box[i][j][k] + self.game_box[i][j][k+1]
                    self.points += self.game_box[i][j][k] ** 2
                    self.game_box[i][j][k+1] = self.game_box[i][j][k+2]
                    self.game_box[i][j][k+2] = self.game_box[i][j][k+3]
                    self.game_box[i][j][k+3] = 0

                if self.game_box[i][j][k+1] == self.game_box[i][j][k+2]:
                    self.game_box[i][j][k+1] = self.game_box[i][j][k+2] + self.game_box[i][j][k+1]
                    self.points += self.game_box[i][j][k+1] ** 2
                    self.game_box[i][j][k+2] = self.game_box[i][j][k+3]
                    self.game_box[i][j][k+3] = 0

                if self.game_box[i][j][k+2] == self.game_box[i][j][k+3]:
                    self.game_box[i][j][k+2] = self.game_box[i][j][k+2] + self.game_box[i][j][k+3]
                    self.points += self.game_box[i][j][k+2] ** 2
                    self.game_box[i][j][k+3] = 0
    def backward_movement(self): #function for forward movement
        k = 0
        for j in range(0,4):
            for i in range(0,4):
                if self.game_box[i][j][k]!=0 or self.game_box[i][j][k+1]!=0 or self.game_box[i][j][k+2]!=0 or self.game_box[i][j][k+3]!=0:
                    if self.game_box[i][j][k+3] == 0:
                        while self.game_box[i][j][k+3]  == 0:
                            self.game_box[i][j][k+3] = self.game_box[i][j][k+2]
                            self.game_box[i][j][k+2] = self.game_box[i][j][k+1]
                            self.game_box[i][j][k+1] = self.game_box[i][j][k]
                            self.game_box[i][j][k] = 0

                    if self.game_box[i][j][k+2] == 0 and (self.game_box[i][j][k+1] !=0 or self.game_box[i][j][k]!=0):
                        while self.game_box[i][j][k+2] == 0:
                            self.game_box[i][j][k+2] = self.game_box[i][j][k+1]
                            self.game_box[i][j][k+1] = self.game_box[i][j][k]
                            self.game_box[i][j][k] = 0

                    if self.game_box[i][j][k+1] == 0 and self.game_box[i][j][k]!=0:
                        while self.game_box[i][j][k+1]==0:
                            self.game_box[i][j][k+1] = self.game_box[i][j][k]
                            self.game_box[i][j][k] = 0
        self.backward_addition()
    def backward_addition(self):
        k = 0
        self.points
        for j in range(0,4):
            for i in range(0,4):
                if self.game_box[i][j][k+3] == self.game_box[i][j][k+2]:
                    self.game_box[i][j][k+3] = self.game_box[i][j][k+3] + self.game_box[i][j][k+2]
                    self.points += self.game_box[i][j][k+3] ** 2
                    self.game_box[i][j][k+2] = self.game_box[i][j][k+1]
                    self.game_box[i][j][k+1] = self.game_box[i][j][k]
                    self.game_box[i][j][k] = 0

                if self.game_box[i][j][k+2] == self.game_box[i][j][k+1]:
                    self.game_box[i][j][k+2] = self.game_box[i][j][k+2] + self.game_box[i][j][k+1]
                    self.points += self.game_box[i][j][k+2] ** 2
                    self.game_box[i][j][k+1] = self.game_box[i][j][k]
                    self.game_box[i][j][k] = 0

                if self.game_box[i][j][k+1] == self.game_box[i][j][k]:
                    self.game_box[i][j][k+1] = self.game_box[i][j][k+1] + self.game_box[i][j][k]
                    self.points += self.game_box[i][j][k+1] ** 2
                    self.game_box[i][j][k] = 0
    def isWon(self): # If There are any 2048 tiles the player has won, Also addes new tiles to board
        row_indexes_with_zero = []
        column_indexes_with_zero = []
        depth_indexes_with_zero = []
        
        for i in range(0,4):
            for j in range(0,4):
                for k in range(0,4):
                    if self.game_box[i][j][k] == 0:
                        row_indexes_with_zero.append(i)
                        column_indexes_with_zero.append(j)
                        depth_indexes_with_zero.append(k)
                    if self.game_box[i][j][k] == 2048:
                        print "Congratulations!! You've successfully sumed up a 2048 tile"
                        return True
                        
        if len(row_indexes_with_zero) > 1:
            random_index = row_indexes_with_zero.index(random.choice(row_indexes_with_zero))
            row_to_place_entry = row_indexes_with_zero[random_index]
            column_to_place_entry = column_indexes_with_zero[random_index]
            depth_to_place_entry = depth_indexes_with_zero[random_index]
            self.game_box[row_to_place_entry][column_to_place_entry][depth_to_place_entry] = 2
            
        elif len(row_indexes_with_zero) == 1:
            row_to_place_entry = row_indexes_with_zero[0]
            column_to_place_entry = column_indexes_with_zero[0]
            depth_to_place_entry = depth_indexes_with_zero[0]
            self.game_box[row_to_place_entry][column_to_place_entry][depth_to_place_entry] = 2
        return False
    def printBoard(self): # prints current board to terminal
        print ("Points>>>>>>")
        print (self.points)
        print ("\n\n")
        print (self.game_box[0][0][0],"\t",self.game_box[0][1][0],"\t",self.game_box[0][2][0],"\t",self.game_box[0][3][0],"\t","\t",self.game_box[0][0][1],"\t",self.game_box[0][1][1],"\t",self.game_box[0][2][1],"\t",self.game_box[0][3][1],"\t","\t",self.game_box[0][0][2],"\t",self.game_box[0][1][2],"\t",self.game_box[0][2][2],"\t",self.game_box[0][3][2],"\t","\t",self.game_box[0][0][3],"\t",self.game_box[0][1][3],"\t",self.game_box[0][2][3],"\t",self.game_box[0][3][3],"\n")
        print (self.game_box[1][0][0],"\t",self.game_box[1][1][0],"\t",self.game_box[1][2][0],"\t",self.game_box[1][3][0],"\t","\t",self.game_box[1][0][1],"\t",self.game_box[1][1][1],"\t",self.game_box[1][2][1],"\t",self.game_box[1][3][1],"\t","\t",self.game_box[1][0][2],"\t",self.game_box[1][1][2],"\t",self.game_box[1][2][2],"\t",self.game_box[1][3][2],"\t","\t",self.game_box[1][0][3],"\t",self.game_box[1][1][3],"\t",self.game_box[1][2][3],"\t",self.game_box[1][3][3],"\n")
        print (self.game_box[2][0][0],"\t",self.game_box[2][1][0],"\t",self.game_box[2][2][0],"\t",self.game_box[2][3][0],"\t","\t",self.game_box[2][0][1],"\t",self.game_box[2][1][1],"\t",self.game_box[2][2][1],"\t",self.game_box[2][3][1],"\t","\t",self.game_box[2][0][2],"\t",self.game_box[2][1][2],"\t",self.game_box[2][2][2],"\t",self.game_box[2][3][2],"\t","\t",self.game_box[2][0][3],"\t",self.game_box[2][1][3],"\t",self.game_box[2][2][3],"\t",self.game_box[2][3][3],"\n")
        print (self.game_box[3][0][0],"\t",self.game_box[3][1][0],"\t",self.game_box[3][2][0],"\t",self.game_box[3][3][0],"\t","\t",self.game_box[3][0][1],"\t",self.game_box[3][1][1],"\t",self.game_box[3][2][1],"\t",self.game_box[3][3][1],"\t","\t",self.game_box[3][0][2],"\t",self.game_box[3][1][2],"\t",self.game_box[3][2][2],"\t",self.game_box[3][3][2],"\t","\t",self.game_box[3][0][3],"\t",self.game_box[3][1][3],"\t",self.game_box[3][2][3],"\t",self.game_box[3][3][3],"\n")
        
