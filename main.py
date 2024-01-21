import numpy as np 
import random as rd
import math


class Main(object):
    def __init__(self,r, k, width, height):

        # variables
        self.r, self.k = r, k
        self.width, self.height = width, height

        self.grid, self.active = [], []
        self.w = self.r / np.sqrt(2)

        self.cols = int(self.width / self.w)
        self.rows = int(self.height / self.w)
        self.grid = [None] * (self.cols * self.rows)

        # STEP 1 initiation
        x = rd.uniform(0, width)
        y = rd.uniform(0, height)
        pos = (x,y)

        i = int(x/self.w)
        j = int(y/self.w)

        self.grid[i+j*self.cols] = pos
        self.active.append(pos)


    def find_distance(self, position1, position2):
        '''find distance between position 1 and position 2 '''
        X = position1[0] - position2[0]
        Y = position1[1] - position2[1]
        diff = X*X + Y*Y
        distance = np.sqrt(diff)
        return distance   


    def calculate_variance(self, num_list):
        '''this function calculates the variance of a given list of data '''
        num_len = len(num_list)
        arr = np.array(num_list)
        sum_nums = np.sum(arr)

        mean_val = sum_nums/num_len      # mean of the numbers

        sum_diff = 0
        for val in num_list:
            diff = (mean_val - val)**2
            sum_diff = sum_diff + diff

        var = sum_diff/num_len
        # print(var)
        return var    


    def draw(self):
        ''' main loop for generating hyperuniform strucuture'''
        if len(self.active) > 0:
            randIndex = rd.randint(0, len(self.active) - 1)
            pos = self.active[randIndex]
            found = False

            for n in range(self.k):
                angle = rd.uniform(0, 2 * math.pi)
                m = rd.uniform(self.r, 2 * self.r)
                sample_x = pos[0] + math.cos(angle) * m
                sample_y = pos[1] + math.sin(angle) * m
                sample = (sample_x, sample_y)

                col = int(sample_x / self.w)
                row = int(sample_y / self.w)

                if 0 <= col < self.cols and 0 <= row < self.rows:
                    ok = True
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if 0 <= col + i < self.cols and 0 <= row + j < self.rows:
                                neighbor = self.grid[(col + i) + (row + j) * self.cols]
                                if neighbor:
                                    d = np.sqrt((sample_x - neighbor[0])**2 + (sample_y - neighbor[1])**2)

                                    if d < self.r:
                                        ok = False
                                    # break

                    if ok:
                        found = True
                        self.grid[col + row * self.cols] = sample
                        self.active.append(sample)
                    # break

            if not found:
                self.active.pop(randIndex)
        
        return self.grid
    

    def centering_structure(self, coords, original_range_min, original_range_max, target_range_min, target_range_max):
        '''get centered (0,0) based coordinates'''
        converted_coords = []
        for x, y in coords:
            converted_x = ((x - original_range_min) / (original_range_max - original_range_min)) * (target_range_max - target_range_min) + target_range_min
            converted_y = ((y - original_range_min) / (original_range_max - original_range_min)) * (target_range_max - target_range_min) + target_range_min
            converted_coords.append((converted_x, converted_y))
        return converted_coords
    
