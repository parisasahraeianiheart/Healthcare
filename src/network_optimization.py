from gurobipy import Model, GRB, quicksum
import pandas as pd

def load_data(file_path):
    """Load the dataset from a CSV file."""
    return pd.read_csv(file_path)

def build_optimization_model(data):
    """Build and solve a network optimization model for comorbidity progression."""
    # Create model
    model = Model("Comorbidity Progression Optimization")

    # Decision variables
    patients = data["PatientID"].tolist()
    severity = data["Severity"].tolist()
    progression_rate = data["ProgressionRate"].tolist()

    # Create variables for treatment allocation
    treatment = model.addVars(patients, vtype=GRB.BINARY, name="Treatment")

    # Objective function: Minimize total severity and progression rate
    model.setObjective(
        quicksum(treatment[p] * severity[i] * progression_rate[i] for i, p in enumerate(patients)),
        GRB.MINIMIZE
    )

    # Constraints: Allocate treatment to a subset of patients
    model.addConstr(quicksum(treatment[p] for p in patients) <= 3, "MaxTreatments")

    # Solve model
    model.optimize()

    # Print results
    if model.status == GRB.OPTIMAL:
        print("Optimal solution found:")
        for p in patients:
            if treatment[p].x > 0.5:
                print(f"Patient {p} receives treatment.")
    else:
        print("No optimal solution found.")

if __name__ == "__main__":
    # Load data and build model
    data = load_data("data/comorbidity_sample_data.csv")
    build_optimization_model(data)
