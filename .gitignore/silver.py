def clean_silver(df):
    return (
        df.filter(
            df["type"].isin("Movie", "TV Show")
        )
        .dropDuplicates()
    )