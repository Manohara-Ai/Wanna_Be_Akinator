# Wanna Be Akinator

**Wanna Be Akinator** is a Pokémon guessing game inspired by the classic Akinator game. It utilizes machine learning algorithms to identify Pokémon based on user responses. The project features implementations of decision trees and random forests to enhance guessing accuracy, with a focus on user interaction to construct input vectors for the model.

## Project Structure

- **`decision_tree.py`**: Contains the implementation of the decision tree algorithm.
- **`random_forest.py`**: Builds on `decision_tree.py` to implement the random forest algorithm.
- **`synthesis.py`**: Handles user interaction, asking questions to construct an input vector for the model to guess Pokémon.
- **`main.py`**: Integrates all components and executes the application.
- **'hot_encoded_resource.csv'**: Contains the dataset on which the decision tree trains

## Features

- **Decision Tree-Based Guessing**: Uses decision tree algorithms to make Pokémon guesses.
- **Random Forest Enhancement**: Implements random forest for improved prediction accuracy.
- **User Interaction**: Asks questions to users and constructs input vectors dynamically.

## Future Improvements
The current implementation’s accuracy is largely dependent on synthesis.py, which might affect performance. Planned improvements include:

Smart synthesis.py with Neural Networks: Implementing a more intelligent version of synthesis.py using neural networks to enhance the accuracy of guesses and user interaction.

## Requirements

- numpy
- pytorch
- other required libraries

## Contributor

B M Manohara @Manohara-Ai
