import numpy as np

class DynamicTimeWarping:
    def __init__(self,x,y,dist_fn):
        self.distance, self.cost_matrix = self.get_distance(x,y,dist_fn)
        self.opt_path = self.get_path()

    def get_distance(self, x,y,dist_fn):
        m = len(x)
        n = len(y)

        dtw = np.zeros((m+1,n+1))

        dtw[0,1:] = np.inf

        dtw[1:,0] = np.inf

        for i in range(1,m+1):
            for j in range(1, n+1):
                cost = dist_fn(x[i-1],y[j-1])
                dtw[i,j] = cost + min(dtw[i-1,j],dtw[i,j-1],dtw[i-1,j-1])

        return dtw[m,n], dtw[1:,1:]
    
    def get_path(self):
        m,n = self.cost_matrix.shape
        opt_path = [(m-1,n-1)]
        
        i,j = m-1,n-1
        while i > 0 or j > 0:
            neighbors = []
            if i > 0 and j > 0:
                neighbors.append((i-1,j-1))
            if i > 0:
                neighbors.append((i-1,j))
            if j > 0:
                neighbors.append((i,j-1))
            
            i, j = min(neighbors, key=lambda p: self.cost_matrix[p[0],p[1]])

            opt_path.append((i,j))
        
        opt_path.reverse()

        return opt_path

def distance(a,b):
    return abs(a-b)

# test running

x = [1, 3, 4, 9, 8, 2, 1, 5, 7, 3]
y = [1, 6, 2, 3, 0, 9, 4, 3, 6, 3]


dtw = DynamicTimeWarping(x,y,distance)
dtw_distance = dtw.distance
print(dtw_distance)
print(dtw.opt_path)