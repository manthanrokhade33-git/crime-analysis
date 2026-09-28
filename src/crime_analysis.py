import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


# -----------------------------
# 1. Project paths
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "crime_data.csv"
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)


# -----------------------------
# 2. Load dataset
# -----------------------------

df = pd.read_csv(DATA_FILE)

print("\n===== CRIME ANALYSIS =====\n")

print("Dataset loaded successfully!")
print(f"Total records: {len(df)}")

print("\nFirst 5 records:")
print(df.head())


# -----------------------------
# 3. Basic information
# -----------------------------

print("\nDataset information:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())


# -----------------------------
# 4. Crime type analysis
# -----------------------------

crime_counts = df["Crime_Type"].value_counts()

print("\nCrime type distribution:")
print(crime_counts)


# -----------------------------
# 5. City-wise analysis
# -----------------------------

city_counts = df["City"].value_counts()

print("\nCity-wise crime count:")
print(city_counts)


# -----------------------------
# 6. Gender analysis
# -----------------------------

gender_counts = df["Victim_Gender"].value_counts()

print("\nVictim gender distribution:")
print(gender_counts)


# -----------------------------
# 7. Status analysis
# -----------------------------

status_counts = df["Status"].value_counts()

print("\nCase status:")
print(status_counts)


# -----------------------------
# 8. Average victim age
# -----------------------------

average_age = df["Victim_Age"].mean()

print(f"\nAverage victim age: {average_age:.2f}")


# -----------------------------
# 9. Crime type chart
# -----------------------------

plt.figure(figsize=(10, 6))

sns.countplot(
    data=df,
    x="Crime_Type",
    order=crime_counts.index
)

plt.title("Crime Type Distribution")
plt.xlabel("Crime Type")
plt.ylabel("Number of Cases")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(OUTPUT_DIR / "crime_type_distribution.png")
plt.show()


# -----------------------------
# 10. City-wise chart
# -----------------------------

plt.figure(figsize=(10, 6))

sns.countplot(
    data=df,
    x="City",
    order=city_counts.index
)

plt.title("Crime Cases by City")
plt.xlabel("City")
plt.ylabel("Number of Cases")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(OUTPUT_DIR / "crime_by_city.png")
plt.show()


# -----------------------------
# 11. Crime status chart
# -----------------------------

plt.figure(figsize=(8, 5))

status_counts.plot(kind="bar")

plt.title("Crime Case Status")
plt.xlabel("Status")
plt.ylabel("Number of Cases")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(OUTPUT_DIR / "case_status.png")
plt.show()


print("\nAnalysis completed successfully!")
print(f"Charts saved in: {OUTPUT_DIR}")