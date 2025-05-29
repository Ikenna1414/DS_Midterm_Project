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

from collections import Counter

# def encode_tags(df, min_count=10):
#     """
#     One-hot encodes tags from each row, keeping only those that appear at least `min_count` times.

#     Args:
#         df (pd.DataFrame): The DataFrame with a 'tags' column (list of strings).
#         min_count (int): Minimum frequency a tag must have to be encoded.

#     Returns:
#         pd.DataFrame: The original DataFrame with new binary columns for common tags.
#     """
#     # Count frequency of each tag
#     tag_counter = Counter(tag for tags in df["tags"].dropna() for tag in tags)

#     # Keep only common tags
#     common_tags = {tag for tag, count in tag_counter.items() if count >= min_count}

#     # Add a new binary column for each common tag
#     for tag in common_tags:
#         df[f"tag_{tag}"] = df["tags"].apply(lambda x: int(tag in x) if isinstance(x, list) else 0)

#     return df

from collections import Counter

def get_tag_counts(df):
    """
    Flattens all tags and returns a Counter of tag frequencies.

    Args:
        df (pd.DataFrame): The DataFrame with a 'tags' column.

    Returns:
        collections.Counter: A frequency count of all tags in the dataset.
    """
    return Counter(tag for tags in df["tags"].dropna() for tag in tags)


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



def drop_columns(df, columns):
    """
    Drops specified columns from the DataFrame (only if they exist).

    Args:
        df (pd.DataFrame): Your data.
        columns (list): A list of column names to drop.

    Returns:
        pd.DataFrame: The DataFrame without the specified columns.
    """
    # Create a new list with only the columns that exist in the DataFrame
    existing_columns = []
    for col in columns:
        if col in df.columns:
            existing_columns.append(col)

    # Drop only the columns that exist
    return df.drop(columns=existing_columns)