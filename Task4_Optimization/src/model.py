import pulp
from src.utils import load_data, to_dict   # <-- FIXED import

def build_and_solve():
    # Load data
    demand_df, capacity_df, costs_df = load_data()

    # Convert demand and profit into dictionaries
    demand = to_dict(demand_df, "product", "demand")
    profit = to_dict(costs_df, "product", "profit_per_unit")

    # Extract resources dynamically
    resources = list(capacity_df["resource"])
    resource_avail = to_dict(capacity_df, "resource", "available")

    # Decision variables for each product
    products = list(demand.keys())
    x = {p: pulp.LpVariable(f"x_{p}", lowBound=0, cat="Integer") for p in products}

    # Define model
    model = pulp.LpProblem("Production_Optimization", pulp.LpMaximize)

    # Objective function: maximize total profit
    model += pulp.lpSum(profit[p] * x[p] for p in products), "Total_Profit"

    # Resource constraints (labor, machine, raw_material, budget)
    for r in resources:
        usage = to_dict(costs_df, "product", f"{r}_per_unit")
        model += pulp.lpSum(usage[p] * x[p] for p in products) <= resource_avail[r], f"{r}_Constraint"

    # Demand constraints
    for p in products:
        model += x[p] <= demand[p], f"Demand_{p}"

    # Solve the model
    status = model.solve(pulp.PULP_CBC_CMD(msg=False))

    # Return results
    return {
        "status": pulp.LpStatus[status],
        "production_plan": {p: x[p].value() for p in products},
        "total_profit": pulp.value(model.objective)
    }