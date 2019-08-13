import matplotlib.pyplot as plt
import data_importer as di
import pandas as pd


data = di.read_data()

avg_days = data['days'].mean()

max_days = data['days'].max()
full_index = [x for x in range(1, max_days + 1)]
distribution = data['days'].value_counts().sort_index().reindex(index=full_index, fill_value=0)

distribution_normalized = distribution / distribution.sum()

distribution = distribution_normalized

distribution.plot.bar()
plt.show()

distribution_cumulative = distribution.cumsum()
distribution_cumulative.plot.bar()
plt.show()

S = distribution_cumulative.iloc[-1] - distribution_cumulative
S.plot.bar()
plt.show()

H = pd.Series(data=[(S[i] - S[i+1]) * i / S[i] for i in full_index[:-1]], index=full_index[:-1])
H.plot.bar()
plt.show()

D_hosp = sum([H[i] * S[i-1] for i in full_index[1:-1]]) / S[1]

data_v_a = data[(data['virus'] == 'Ні') & (data['therapy'] == 'Ні')]
data_v_b = data[(data['virus'] == 'Ні') & (data['therapy'] == 'Так')]
data_n_a = data[(data['virus'] == 'Так') & (data['therapy'] == 'Ні')]
data_n_b = data[(data['virus'] == 'Так') & (data['therapy'] == 'Так')]

print()
