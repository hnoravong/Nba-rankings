import pandas as pd

# Load your cleaned data
df = pd.read_json("players_clean.json")

# Example user-selected weights
weights = {
    "points_per_game": 40,
    "assists_per_game": 20,
    "rebounds_per_game": 15,
    "games_played": 15,
    "fg_pct": 10,
    "turnovers_per_game": 10
}

# Stats where LOWER is better
negative_stats = {"turnovers_per_game"}

def normalize_column(series, reverse=False):
    min_val = series.min()
    max_val = series.max()

    # Avoid division by zero if all values are the same
    if max_val == min_val:
        return pd.Series([1.0] * len(series), index=series.index)

    normalized = (series - min_val) / (max_val - min_val)

    if reverse:
        normalized = 1 - normalized

    return normalized

def generate_rankings(dataframe, weights_dict):
    df = dataframe.copy()

    # Start everyone at 0
    df["ranking_score"] = 0.0

    # Keep track of contribution from each stat if you want to explain rankings later
    for stat, weight in weights_dict.items():
        if stat not in df.columns:
            raise ValueError(f"Column '{stat}' not found in dataset.")

        reverse = stat in negative_stats
        normalized_col = normalize_column(df[stat], reverse=reverse)

        contribution_col = f"{stat}_contribution"
        df[contribution_col] = normalized_col * weight

        df["ranking_score"] += df[contribution_col]

    # Sort highest score first
    df = df.sort_values(by="ranking_score", ascending=False).reset_index(drop=True)

    # Add rank numbers
    df["rank"] = df.index + 1

    return df

ranked_df = generate_rankings(df, weights)

# Show top 20
print(
    ranked_df[
        [
            "rank",
            "player_name",
            "team",
            "ranking_score",
            "points_per_game",
            "assists_per_game",
            "rebounds_per_game",
            "games_played",
            "fg_pct",
            "turnovers_per_game"
        ]
    ].head(20)
)

# Optional: save rankings
ranked_df.to_csv("rankings_output.csv", index=False)
ranked_df.to_json("rankings_output.json", orient="records", indent=2)