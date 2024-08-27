import pandas as pd
import random
import torch

class Feature_Vector:
    def __init__(self):
        self.general = {
            'Gen 1': None,
            'Gen 2': None,
            'Gen 3': None,
            'Gen 4': None,
            'Gen 5': None,
            'Gen 6': None,
            'Legendary': None
        }
        self.type = {
            'Grass': None,
            'Fire': None,
            'Water': None,
            'Bug': None,
            'Normal': None,
            'Poison': None,
            'Electric': None,
            'Ground': None,
            'Fairy': None,
            'Fighting': None,
            'Psychic': None,
            'Rock': None,
            'Ghost': None,
            'Ice': None,
            'Dragon': None,
            'Dark': None,
            'Steel': None,
            'Flying': None
        }
        self.weakness = {
            'Grass': None,
            'Fire': None,
            'Water': None,
            'Bug': None,
            'Normal': None,
            'Poison': None,
            'Electric': None,
            'Ground': None,
            'Fairy': None,
            'Fighting': None,
            'Psychic': None,
            'Rock': None,
            'Ghost': None,
            'Ice': None,
            'Dragon': None,
            'Dark': None,
            'Steel': None,
            'Flying': None
        }
        self.data = pd.read_csv('hot_encoded_resource.csv').drop(columns='#')
        
    def deduce_general(self):
        while True:
            choice = input('Is your Pokémon legendary? (yes/no): ').strip().lower()
            if choice == 'yes':
                self.general['Legendary'] = 1
                self.data = self.data[self.data['Legendary'] == 1]
                break
            elif choice == 'no':
                self.general['Legendary'] = 0
                self.data = self.data[self.data['Legendary'] == 0]
                break
            else:
                print('Please answer with "yes" or "no".')

        generations = [1, 2, 3, 4, 5, 6]
        while len(generations) > 1:
            try:
                random_gen = random.choice(generations)
                choice = input(f'Is your Pokémon from an earlier generation than Generation {random_gen}? (yes/no): ').strip().lower()
                if choice == 'yes':
                    generations = [gen for gen in generations if gen < random_gen]
                elif choice == 'no':
                    generations = [gen for gen in generations if gen >= random_gen]
                else:
                    print('Please answer with "yes" or "no".')

                if not generations:
                    print("Error: No valid generations left. Please restart.")
                    return

            except Exception as e:
                print(f'An error occurred: {e}. Please refer to the user instructions and try again!')
                return


        remaining_gen = generations[0]
        for gen in self.general:
            if 'Gen' in gen:
                self.general[gen] = 1 if gen == f'Gen {remaining_gen}' else 0
        
        self.data = self.data[self.data[f'Gen {remaining_gen}'] == 1]

    def deduce_type(self):
        while sum(value if value is not None else 0 for value in self.type.values()) < 2:
            all_types = [key for key, value in self.type.items() if value is None]
            random_type = random.choice(all_types)
            choice = input(f'Is your Pokémon {random_type} type? (yes/no): ').strip().lower()
            if choice == 'yes':
                self.type[random_type] = 1
            elif choice == 'no':
                self.type[random_type] = 0
            else:
                print('Please answer with "yes" or "no".')
        self.type = {k: (v if v is not None else 0) for k, v in self.type.items()}

    def deduce_weakness(self):
        for i in range (len(self.weakness.items())):
            all_types = [key for key, value in self.weakness.items() if value is None]
            random_type = random.choice(all_types)
            choice = input(f'Is your Pokémon weak to {random_type} type? (yes/no): ').strip().lower()
            if choice == 'yes':
                self.weakness[random_type] = 1
            elif choice == 'no':
                self.weakness[random_type] = 0
            else:
                print('Please answer with "yes" or "no".')
        self.weakness = {k: (v if v is not None else 0) for k, v in self.weakness.items()}

    def predict_vector(self):
        self.deduce_general()
        self.deduce_type()
        self.deduce_weakness()
        vector = []
        vector.extend(list(self.type.values()))
        vector.extend(list(self.weakness.values()))
        vector.extend(list(self.general.values()))

        return torch.tensor(vector)