import pandas as pd
df = pd.read_csv(#ตาราง)
df['โอกาศติด'] = df[#'คะแนนที่ได้']/df['100']*100
print(df)