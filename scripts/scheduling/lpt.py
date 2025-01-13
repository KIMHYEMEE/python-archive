import pandas as pd

class LPT:
    def __init__(self,example):
        self.m, self.p = example

        self.df = self.to_dataframe()
    
    def __call__(self):
        self.schedule, self.machine_loads = self.get_schedule()
        obj = self.get_objective(self.machine_loads)

        return {'schedule':self.schedule,
                'obj':obj}

    def to_dataframe(self):
        df = pd.DataFrame({'Task':[f"Task{i+1}" for i in range(len(self.p))],
                        'proc_time':self.p})
        df.sort_values('proc_time',ascending=False).reset_index(drop=False)
        
        return df
    
    def get_schedule(self):
        machine_loads = [0] * self.m

        schedule = {f"Machine{i+1}":[] for i in range(self.m)}

        for idx, r in self.df.iterrows():
            task_time = r['proc_time']
            min_machine_index = machine_loads.index(min(machine_loads))
            schedule[f"Machine{min_machine_index+1}"].append(r['Task'])
            machine_loads[min_machine_index] += task_time
        
        machine_loads = {f"Machine{m+1}":load for m,load in zip(range(len(machine_loads)),machine_loads)}
        
        return schedule, machine_loads
    
    def get_objective(self,machine_loads):
        return max(machine_loads.values())
    
# example1 (worst case)
m = 4
p = [7,7,6,6,5,5,4,4,4]
ex1 = (m,p)

lpt1 = LPT(ex1)
print(lpt1())
print(lpt1.machine_loads)


# exaple2
m = 6
p = [6,6,6,7,7,8,8,9,9,10,10,11]
ex2 = (m,p)

lpt2 = LPT(ex2)
print(lpt2())
print(lpt2.machine_loads)