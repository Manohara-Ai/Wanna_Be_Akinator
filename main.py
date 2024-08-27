import pandas as pd
import torch
from random_forest import RandomForest
from synthesis import Feature_Vector

data = pd.read_csv('hot_encoded_resource.csv')
X = data.drop(columns=['#', 'Name']).values
y = data['#'].values 
X, y = torch.tensor(X, dtype=torch.float32), torch.tensor(y, dtype=torch.int64)
pokemon_names = data['Name']

model = RandomForest()
model.fit(X, y)

vector = Feature_Vector()
test_vector = vector.predict_vector()

predictions = model.predict(test_vector.unsqueeze(dim=0))
print(f'I think you are thinking of {pokemon_names[predictions-1].values[0]}')
