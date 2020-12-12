import pandas as pd
df = pd.read_csv(#ตาราง)
df['โอกาศติด'] = df[#'คะแนนที่ต้องการ']/df['คะแนนที่ได้']*100
print(df)
