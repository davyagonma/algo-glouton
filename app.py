import streamlit as st

def isFeasible(n, d):
    nPeriods = len(d[0])
    for k in range(nPeriods):
        if sum(d[i][k] for i in range(n)) > 1:
            return False
    return True

def optStockingCost(n, d):
    if not isFeasible(n, d):
        return "The given instance is not feasible."

    nPeriods = len(d[0])
    allDemands = []
    for k in range(nPeriods):
        for i in range(n):
            if d[i][k] == 1:
                allDemands.append(k)

    nDemands = len(allDemands)
    h = 0            
    t = allDemands[nDemands-1]
    production_plan = []

    while len(allDemands) != 0:
        deadline = allDemands.pop()
        if deadline >= t:
            h += (deadline - t)
            production_plan.append(t)
        else:
            allDemands.append(deadline)
        t -= 1

    return f"✅ Optimal stocking cost: {h}\n🛠️ Production plan: {list(reversed(production_plan))}"

def optStockingCost_IDS(n, d, stockingCostByItem):
    if not isFeasible(n, d):
        return "The given instance is not feasible."

    nPeriods = len(d[0])
    allDemands = []
    for i in range(n):
        for k in range(nPeriods):
            if d[i][k] == 1:
                allDemands.append((i, k))

    allDemands.sort(key=lambda x: x[1], reverse=True)

    h = 0
    t = allDemands[0][1]
    production_plan = []

    while len(allDemands) != 0:
        item, deadline = allDemands.pop()
        if deadline >= t:
            h += (deadline - t) * stockingCostByItem[item]
            production_plan.append((item, t))
        else:
            allDemands.append((item, deadline))
        t -= 1

    return f"✅ Optimal stocking cost: {h}\n🛠️ Production plan: {[(i, t) for i, t in reversed(production_plan)]}"

# Interface Streamlit
st.title("📦 Optimal Stocking Cost Solver (Greedy Algorithm)")
st.markdown("By **AGONMA Singbo Davy**, Master 1 Génie Logiciel – IFRI")

nItems = st.number_input("🔢 Number of items", min_value=1, value=2)
nPeriods = st.number_input("📅 Number of periods", min_value=1, value=5)

st.markdown("## 🧮 Enter the demand matrix")
demands = []
for i in range(nItems):
    row = st.text_input(f"Demand for item {i+1} (comma-separated, 0 or 1)", value="0,"*nPeriods)
    try:
        demand_row = tuple(int(x) for x in row.strip().split(",") if x.strip() != "")
        if len(demand_row) != nPeriods:
            st.error(f"❌ La ligne de l’item {i+1} doit contenir exactement {nPeriods} éléments.")
        else:
            demands.append(demand_row)
    except ValueError:
        st.error(f"❌ Erreur de saisie dans la ligne de l’item {i+1}. Utilise uniquement des 0 ou 1 séparés par des virgules.")

use_costs = st.checkbox("🔧 Use different stocking costs per item?")
if use_costs:
    stocking_costs = []
    for i in range(nItems):
        cost = st.number_input(f"Stocking cost for item {i+1}", min_value=0, value=1)
        stocking_costs.append(cost)
else:
    stocking_costs = None

if st.button("🚀 Calculate Optimal Stocking Cost"):
    try:
        if use_costs:
            result = optStockingCost_IDS(nItems, tuple(demands), tuple(stocking_costs))
        else:
            result = optStockingCost(nItems, tuple(demands))
        st.success(result)
    except Exception as e:
        st.error(f"❌ Error: {e}")
