import matplotlib.pyplot as plt
import data_importer as di
import pandas as pd
from scipy import stats


data = di.read_data()
data_v_a = data[(data['virus'] == 'Так') & (data['therapy'] == 'Ні')]
data_v_b = data[(data['virus'] == 'Так') & (data['therapy'] == 'Так')]
data_n_a = data[(data['virus'] == 'Ні') & (data['therapy'] == 'Ні')]
data_n_b = data[(data['virus'] == 'Ні') & (data['therapy'] == 'Так')]

# avg_days = data['days'].mean()


def get_days_distribution(df):
    max_days = df['days'].max()
    full_index = [x for x in range(1, max_days + 1)]
    distribution = data['days'].value_counts().sort_index().reindex(index=full_index, fill_value=0)
    distribution_normalized = distribution / distribution.sum()

    return distribution_normalized


def show(df):
    df.plot.bar()
    plt.show()


def randomize(distr, N):
    xk = [i for i in distr.index]
    pk = [distr[i] for i in distr.index]

    return stats.rv_discrete(values=(xk, pk)).rvs(size=N)


d_n_a_distr = get_days_distribution(data_n_a)
# show(d_n_a_distr)
d_n_a_rand = randomize(d_n_a_distr, 100)

data_for_calc = []
for data in [data_v_a, data_v_b, data_n_a, data_n_b]:
    data_distr = get_days_distribution(data)
    data_rand = randomize(data_distr, 100)
    data_for_calc.append(data_rand)

# distribution_cumulative = distribution.cumsum()
# distribution_cumulative.plot.bar()
# plt.show()
#
# S = distribution_cumulative.iloc[-1] - distribution_cumulative
# S.plot.bar()
# plt.show()
#
# H = pd.Series(data=[(S[i] - S[i+1]) * i / S[i] for i in full_index[:-1]], index=full_index[:-1])
# H.plot.bar()
# plt.show()
#
# D_hosp = sum([H[i] * S[i-1] for i in full_index[1:-1]]) / S[1]



print()
