import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel("Hotel_reviews.xlsx")

print("Οι στηλες που εχει το αρχειο ειναι οι εξης: \n \n", df.columns)

#
origin_countries = df['origin_country'].value_counts()

origin_countries = df['origin_country'].value_counts().head(30)

# Plot
plt.figure(figsize=(18, 10))
origin_countries.plot(kind='bar')  # Bar plot for counts
plt.title('Top 30 Origin Countries')
plt.xlabel('Country')
plt.ylabel('Count')

# ✅ Set x-ticks (country names)
plt.xticks(ticks=range(len(origin_countries)), labels=origin_countries.index, rotation=75)

plt.tight_layout()
plt.savefig("top_origin_countries.png", dpi=300)