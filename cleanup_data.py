import pandas as pd


def main() -> None:
    # Load the earthquake dataset
    file_path = "data/earthquakes.csv"
    earthquakes = pd.read_csv(file_path)

    print(f"Dataset shape {earthquakes.shape}")
    earthquakes.rename(columns={"magnitudo": "magnitude"}, inplace=True)

    print("\nFirst 5 rows:")
    print(earthquakes.head())

    print("\nSummary statistics:")
    print(earthquakes.describe())

    print(f"\n{earthquakes.duplicated().sum()} duplicate rows in the dataset")
    earthquakes = earthquakes.drop_duplicates()

    print(f"{earthquakes[earthquakes['magnitude'] < 0].shape[0]} rows with magnitude < 0")
    earthquakes = earthquakes[earthquakes["magnitude"] >= 0]

    earthquakes["state"] = earthquakes["state"].str.strip()

    state_abbreviation_mapping = {
        "AL": "Alabama",
        "AK": "Alaska",
        "AZ": "Arizona",
        "AR": "Arkansas",
        "CA": "California",
        "CO": "Colorado",
        "CT": "Connecticut",
        "DE": "Delaware",
        "FL": "Florida",
        "GA": "Georgia",
        "HI": "Hawaii",
        "ID": "Idaho",
        "IL": "Illinois",
        "IN": "Indiana",
        "IA": "Iowa",
        "KS": "Kansas",
        "KY": "Kentucky",
        "LA": "Louisiana",
        "ME": "Maine",
        "MD": "Maryland",
        "MA": "Massachusetts",
        "MI": "Michigan",
        "MN": "Minnesota",
        "MS": "Mississippi",
        "MO": "Missouri",
        "MT": "Montana",
        "NE": "Nebraska",
        "NV": "Nevada",
        "NH": "New Hampshire",
        "NJ": "New Jersey",
        "NM": "New Mexico",
        "NY": "New York",
        "NC": "North Carolina",
        "ND": "North Dakota",
        "OH": "Ohio",
        "OK": "Oklahoma",
        "OR": "Oregon",
        "PA": "Pennsylvania",
        "RI": "Rhode Island",
        "SC": "South Carolina",
        "SD": "South Dakota",
        "TN": "Tennessee",
        "TX": "Texas",
        "UT": "Utah",
        "VT": "Vermont",
        "VA": "Virginia",
        "WA": "Washington",
        "WV": "West Virginia",
        "WI": "Wisconsin",
        "WY": "Wyoming",
    }

    # For states in the dataset that are abbreviations, replace them with full names.
    earthquakes["state"] = earthquakes["state"].replace(state_abbreviation_mapping)

    # Save cleaned earthquakes to a new CSV file
    earthquakes.to_csv("data/earthquakes_cleaned.csv", index=False)

    # Group by state, sum magnitude, and average latitude/longitude
    earthquakes_grouped = earthquakes.groupby("state").agg(
        {"magnitude": "sum", "latitude": "mean", "longitude": "mean"}
    ).reset_index()

    print("\nGrouped data (first 5 rows):")
    print(earthquakes_grouped.head())

    earthquakes_grouped = earthquakes_grouped.sort_values(by="magnitude", ascending=False)

    print("\nGrouped + sorted data (first 5 rows):")
    print(earthquakes_grouped.head())

    # Save grouped earthquakes to a new CSV file
    earthquakes_grouped.to_csv("data/earthquakes_grouped.csv", index=False)


if __name__ == "__main__":
    main()
