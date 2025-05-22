def encode_tags(df):

    """Use this function to manually encode tags from each sale.
    You could also provide another argument to filter out low 
    counts of tags to keep cardinality to a minimum.
       
    Args:
        pandas.DataFrame

    Returns:
        pandas.DataFrame: modified with encoded tags
    """
    tags = df["tags"].tolist()
    # create a unique list of tags and then create a new column for each tag
        
    return df

def drop_all_null_columns(df):
    """
    Drops columns from the DataFrame where all values are null.

    Args:
        pd.DataFrame

    Returns:
    pd.DataFrame: Cleaned DataFrame with all-null columns removed.
    """
    return df.dropna(axis=1, how='all')


def fill_missing_with_mean(df, columns):
    """
    Fills missing values in specified numeric columns with the column mean.

    Args:
        pd.DataFrame: The DataFrame to modify.
        columns : List of column names to fill.

    Returns:
        pd.DataFrame: DataFrame with missing values filled.
    """
    df[columns] = df[columns].apply(lambda col: col.fillna(col.mean()))
    return df