from faker import Faker
import pandas as pd
import random
import matplotlib.pyplot as plt

# Initialize Faker
fake = Faker()

# -------------------------------
# 1. Generate Fake Patient Data
# -------------------------------
def generate_patient_data(n=50):
    """Generate n fake patient records."""
    patients = []

    for i in range(1, n + 1):
        patient = {
            "ID": i,
            "Name": fake.name(),
            "Age": random.randint(1, 100),
            "Gender": random.choice(["Male", "Female", "Other"])
        }
        patients.append(patient)

    return patients


# -------------------------------
# 2. Categorize by Age Groups
# -------------------------------
def analyze_age_groups(df):
    """Add AgeGroup column and print distribution."""
    bins = [0, 12, 19, 35, 50, 65, 120]
    labels = ["Child", "Teen", "Young Adult", "Adult", "Middle Age", "Senior"]

    df["AgeGroup"] = pd.cut(df["Age"], bins=bins, labels=labels, right=False)

    print("\n--- Age Group Distribution ---")
    print(df["AgeGroup"].value_counts())
    print("\n")

    return df


# -------------------------------
# 3. Test Script
# -------------------------------
def test_script():
    print("Generating fake patient dataset...\n")

    data = generate_patient_data(50)
    df = pd.DataFrame(data)

    print("--- Sample Data (first 10 rows) ---")
    print(df.head(10))

    # Add age group column
    df = analyze_age_groups(df)

    # Save CSV
    df.to_csv("patient_data.csv", index=False)
    print("Dataset saved as patient_data.csv")

    # -------------------------------
    # 4. Plot Age Group Distribution
    # -------------------------------
    age_group_counts = df["AgeGroup"].value_counts().sort_index()

    plt.figure(figsize=(8, 5))
    age_group_counts.plot(kind='bar')

    plt.title("Age Group Distribution")
    plt.xlabel("Age Groups")
    plt.ylabel("Number of Patients")
    plt.tight_layout()

    plt.show()  


# -------------------------------
# Run Script
# -------------------------------
if __name__ == "__main__":
    test_script()


