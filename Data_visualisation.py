
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load dataset
df = pd.read_csv("clean_dataset.csv")
df.columns = df.columns.str.strip()

# Create folder
os.makedirs("Charts", exist_ok=True)

# Find columns
yield_col = "Yield_Tons"
season_col = "Season"
disease_col = "Disease_Risk"

# Check yield column
if yield_col not in df.columns:
    raise ValueError(
        f"Yield_Tons not found. Available columns: {df.columns.tolist()}"
    )

df[yield_col] = pd.to_numeric(
    df[yield_col], errors="coerce"
)

df = df.dropna(subset=[yield_col])

# Create 4 graphs
fig, ax = plt.subplots(2, 2, figsize=(14, 10))

# GRAPH 1: HISTOGRAM
ax[0, 0].hist(
    df[yield_col],
    bins=15,
    edgecolor="black"
)
ax[0, 0].set_title("Crop Yield Distribution")
ax[0, 0].set_xlabel("Yield (Tons)")
ax[0, 0].set_ylabel("Frequency")

# GRAPH 2: PIE CHART
if disease_col in df.columns:
    risk = df[disease_col].value_counts()
    ax[0, 1].pie(
        risk,
        labels=risk.index,
        autopct="%1.1f%%",
        startangle=90
    )
    ax[0, 1].set_title("Disease Risk Distribution")
else:
    ax[0, 1].text(0.5, 0.5, "Disease column unavailable",
                  ha="center", va="center")

# GRAPH 3: BOX PLOT
if season_col in df.columns:
    seasons = df[season_col].dropna().unique()
    box_data = [
        df.loc[df[season_col] == s, yield_col].dropna()
        for s in seasons
    ]

    ax[1, 0].boxplot(
        box_data,
        tick_labels=seasons
    )
    ax[1, 0].set_title("Yield Variation by Season")
    ax[1, 0].set_xlabel("Season")
    ax[1, 0].set_ylabel("Yield (Tons)")
else:
    ax[1, 0].text(0.5, 0.5, "Season column unavailable",
                  ha="center", va="center")

# GRAPH 4: SCATTER PLOT
numeric = df.select_dtypes(include="number").columns.tolist()

other_columns = [
    c for c in numeric if c != yield_col
]

if other_columns:
    x_col = other_columns[0]

    ax[1, 1].scatter(
        df[yield_col],
        df[x_col],
        alpha=0.7
    )

    ax[1, 1].set_title("Yield vs " + x_col)
    ax[1, 1].set_xlabel("Yield (Tons)")
    ax[1, 1].set_ylabel(x_col)
else:
    ax[1, 1].text(0.5, 0.5, "No other numeric column available",
                  ha="center", va="center")

# Final layout
fig.suptitle(
    "AGRICULTURE CROP ANALYTICS",
    fontsize=16
)

plt.tight_layout()

# Save image
plt.savefig(
    "Charts/All_4_Graphs.png",
    dpi=300
)

plt.show()

print("SUCCESS: All 4 graphs generated!")
print("Check Charts/All_4_Graphs.png")
