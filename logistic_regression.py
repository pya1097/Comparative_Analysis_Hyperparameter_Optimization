import itertools
import csv

max_iter_values = [100, 50, 500, 1000, 5000]
C_values = [1, 0.05, 0.5, 5, 10, 100]
tol_values = [0.0001, 0.001, 0.003, 0.005, 0.0003, 0.0005, 0.0008]
fit_intercept_values = [True, False]
dual_values = [False]
penalty_values = ['l2', 'None']

# Generate combinations
combinations = itertools.product(max_iter_values, C_values, tol_values, fit_intercept_values, dual_values, penalty_values)

# Open a CSV file in write mode
with open('../data/combinations.csv', 'w', newline='') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile, delimiter=',')
    
    # Write header
    csv_writer.writerow(["max_iter", "C", "tol", "fit_intercept", "dual", "penalty"])
    
    # Write combinations
    for combo in combinations:
        csv_writer.writerow(combo)

print("Combinations written to combinations.csv")
