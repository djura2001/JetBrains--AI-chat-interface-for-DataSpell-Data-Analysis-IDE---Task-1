def greater_filtration(df, threshold, cat):
    if cat not in df.columns:
        raise ValueError(f"Column '{cat}' not found")

    filtered_df = df[df[cat] > threshold]
    return filtered_df
def lower_filtration(df, threshold, cat):
    if cat not in df.columns:
        raise ValueError(f"Column '{cat}' not found")

    filtered_df = df[df[cat] < threshold]
    return filtered_df
def filter_numeric_columns(df):

    
    return df.select_dtypes(include=["number"])
def sort_by_column(df, column, ascending=True):
    
    return df.sort_values(by=column, ascending=ascending)
def normalize_numeric_columns(df):
    
    numeric_cols = df.select_dtypes(include=["number"])
    df[numeric_cols.columns] = (numeric_cols - numeric_cols.min()) / (numeric_cols.max() - numeric_cols.min())
    return df
def rename_columns_to_lowercase(df):
    
    df.columns = [col.lower() for col in df.columns]
    return df
def add_sum_column(df, column1, column2, new_column_name):
    
    df[new_column_name] = df[column1] + df[column2]
    return df
def select_column(df, column_name):
    return df[[column_name]]
