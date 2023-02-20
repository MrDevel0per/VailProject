import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics as stats



def analyzeRuns(ds):
    ds.drop(["id", "info"], axis=1, inplace=True)
    #First, we will calculate and print the mean, median, and average
    print("Mean: ", np.mean(ds))
    print("Mode: ", stats.mode(ds))
    #If ds == vail_runs, then we will plot the histogram via difficulty
    #If ds == bc_runs, then we will plot the histogram via difficultyNumber
    if ds == vail_runs:
        ds.hist("difficulty", bins=4)
    else:
        ds.hist("difficultyNumber", bins=4)
    plt.show()

def main():
    vail_runs = pd.read_csv("../CSVs/VailSkiRuns.csv")
    vail_lifts = pd.read_csv("../CSVs/VailLifts.csv")
    bc_runs = pd.read_csv("../CSVs/bcSkiRuns.csv")
    bc_lifts = pd.read_csv("../CSVs/bcLifts.csv")
    analyzeRuns(vail_runs)
    analyzeRuns(bc_runs)

main()




