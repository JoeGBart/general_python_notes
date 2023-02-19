import pandas as pd

df_gen = pd.read_csv("laptops.csv", dtype=str, chunksize=50)

co = 1
df_list = []
for df in df_gen:
    df_list += [df]
    print(co)
    co += 1

print(len(df_list))
full_df = pd.concat(df_list)
print(full_df.size)
