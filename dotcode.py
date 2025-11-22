from graphviz import Digraph
import os

flow = Digraph("Research_Process", format="PNG")  # use pdf (or png)
flow.attr(rankdir="TB", size="20,8", fontname="Times New Roman",fontweight="bold")
flow.node_attr.update(fontname="Times New Roman", fontsize="20", penwidth = "3")
flow.edge_attr.update(fontname="Times New Roman", fontsize="20")

# Step 1: 
flow.node("data", "Data" , 
          shape="box", style="filled", fillcolor="lightblue")

# Step 2: 
flow.node("prep", "Preprocessing", shape="box", style="filled", fillcolor="lightblue")
flow.node("format", "Data Formatting\n(Correct datatypes)")
flow.node("dup", "Remove Missing values")
flow.node("feat_eng", "Feature Engineering")
flow.node("feat_tran", "Feature Transformation")
flow.node("feat_sel", "Feature Selection")

# Step 3: 
flow.node("analysis", "Analysis", shape="box", style="filled", fillcolor="lightblue")
flow.node("eda", "Analysis 1")
flow.node("bins", "Analysis 2")

# Step 4: 
flow.node("ml", "Machine Learning Models", shape="box", style="filled", fillcolor="lightblue")
flow.node("models", "Linear Models")
flow.node("eval", "Model Evaluation")

# Sequential flow
flow.edge("data", "prep")
flow.edge("prep", "analysis")
flow.edge("analysis", "ml")

#  details
flow.edge("prep", "format")
flow.edge("format", "dup")
flow.edge("dup", "feat_eng")
flow.edge("feat_eng", "feat_tran")
flow.edge("feat_tran", "feat_sel")

#  details
flow.edge("analysis", "eda")
flow.edge("eda", "bins")

#  details
flow.edge("ml", "models")
flow.edge("models", "eval")

# Render to PDF
flow.render("research_flowchart", view=True)

