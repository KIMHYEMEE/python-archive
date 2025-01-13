import pandas as pd

# single machine
# minimize total weighted completion time
class WSPT:
    def __init__(self, weight, processing_time):
        self.w = weight
        self.p = processing_time

        self.df = self.to_dataframe()
        self.sort_priority()

    def __call__(self):
        schedule = self.get_schedule()
        obj = self.get_objective()

        return {'schedule':schedule,
                'obj':obj}

    def to_dataframe(self):
        idx = [f"Task{i+1}" for i in range(len(w))]
        df = pd.DataFrame({'Task':idx,
                            'weight':w,
                            'proc_time':p})
        
        return df
    
    def sort_priority(self):
        self.df['priority_index'] = self.df['weight'] / self.df['proc_time']
        self.df = self.df.sort_values('priority_index', ascending=False).reset_index(drop=True)

    def get_schedule(self):
        return self.df['Task'].to_list()

    def get_objective(self):
        # start time
        start_time = [0]
        for t in self.df['proc_time'][:-1]:
            start_time.append(start_time[-1]+t)
        self.df['start_time'] = start_time

        # completion time, weighted completiontime(wc)
        self.df['completion_time'] = self.df['start_time'] + self.df['proc_time']

        self.df['wc'] = self.df['weight'] * self.df['completion_time']

        return self.df['wc'].sum()


# example
w = [0,18,12,8,8,17,16]
p = [3,6,6,5,4,8,9]

# (a) find all optimal seqeunce
wspt1 = WSPT(w,p)
print(wspt1())

# (b) determine the effect of a change in p2 from 6 to 7 on the optimal sequence(s)
# (c) determine the effect of the change under (b) on the value of the objective

p[1] = 7
wspt2 = WSPT(w,p)
print(wspt2())
print(wspt2.df)