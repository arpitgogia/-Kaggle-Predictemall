import numpy
import pandas as pd
from matplotlib import pyplot as plt
data_frame = pd.read_csv('300k.csv', low_memory=False)

pokemon_ids = data_frame['pokemonId'].values

plt.hist(pokemon_ids, bins=np.arange(pokemon_ids.min(), pokemon_ids.max() + 1), align='left')
plt.show()