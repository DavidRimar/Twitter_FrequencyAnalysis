import pandas as pd


def normalize_volumes_concat(df_all, df_subset):

    df1 = df_all.rename(columns={'count': 'count1', 'day': 'day1'})
    df2 = df_subset.rename(columns={'count': 'count2'})

    df_final = pd.concat([df1, df2], axis=1)

    df_final['norm_vol'] = df_final['count2'] / df_final['count1']

    return df_final
