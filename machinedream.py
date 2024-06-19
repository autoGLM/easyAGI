import random
import logging
import os
import requests
from typing import List, Tuple, Union

class MachineDreamer:
    def __init__(self, memory_bank: List[str], creativity_factor: float = 1.0, api_key: str = None):
        """
        Initialize the Machine Dreamer.
        :param memory_bank: A list of past experiences or data points.
        :param creativity_factor: A multiplier to adjust the randomness in idea generation.
        :param api_key: API key for the language model.
        """
        self.memory_bank = self._validate_memory_bank(memory_bank)
        self.creativity_factor = self._validate_creativity_factor(creativity_factor)
        self.api_key = api_key or os.getenv('AI_MODEL_API_KEY')
        self.evaluation_metrics = {'relevance': 0.5, 'novelty': 0.5}
        self._setup_logging()

    def _setup_logging(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def _validate_memory_bank(self, memory_bank: List[str]) -> List[str]:
        """
        Validate the memory bank to ensure it is a list.
        :param memory_bank: Memory bank to validate.
        :return: Validated memory bank.
        """
        if not isinstance(memory_bank, list):
            logging.warning("Invalid memory bank type. Expected a list.")
            return []
        return memory_bank

    def _validate_creativity_factor(self, creativity_factor: float) -> float:
        """
        Validate the creativity factor to ensure it is a positive number.
        :param creativity_factor: Creativity factor to validate.
        :return: Validated creativity factor.
        """
        if isinstance(creativity_factor, (int, float)) and creativity_factor > 0:
            return creativity_factor
        logging.warning("Invalid creativity factor. Using default value of 1.0.")
        return 1.0

    def _random_combination(self) -> str:
        """
        Create a random combination of elements from the memory bank.
        :return: A novel combination of elements.
        """
        try:
            num_elements = min(3, len(self.memory_bank))
            elements = random.sample(self.memory_bank, k=int(num_elements * self.creativity_factor))
            return ' + '.join(elements)
        except ValueError as e:
            logging.error(f"Error in random combination generation: {e}")
            return ""

    def dream(self) -> Tuple[str, float]:
        """
        Simulate the dreaming process by generating a creative combination of memory elements.
        :return: A tuple of the creative idea and its evaluated score.
        """
        idea = self._random_combination()
        if idea:
            evaluated_idea = self._evaluate_idea(idea)
            return evaluated_idea
        return "", 0

    def _evaluate_idea(self, idea: str) -> Tuple[str, float]:
        """
        Evaluate the generated idea based on predefined metrics and language model.
        :param idea: The idea to be evaluated.
        :return: A tuple of the idea and its evaluated score.
        """
        relevance_score, novelty_score = self._query_language_model(idea)
        total_score = (relevance_score * self.evaluation_metrics['relevance'] +
                       novelty_score * self.evaluation_metrics['novelty'])
        return idea, total_score

    def _query_language_model(self, idea: str) -> Tuple[float, float]:
        """
        Send a query to a language model to evaluate the idea.
        :param idea: The idea to be evaluated.
        :return: A tuple of relevance score and novelty score.
        """
        if not self.api_key:
            logging.warning("API key not set. Unable to query the language model.")
            return 0, 0

        try:
            response = requests.post(
                "https://api.example.com/language_model",
                headers={"Authorization": f"Bearer {self.api_key}"},
                json={"idea": idea},
                timeout=10
            )
            response.raise_for_status()
            data = response.json()
            return data.get('relevance_score', 0), data.get('novelty_score', 0)
        except requests.RequestException as e:
            logging.error(f"Error querying the language model: {e}")
            return 0, 0

    def update_memory(self, new_data: Union[str, List[str]]):
        """
        Update the memory bank with new experiences or data points.
        :param new_data: New data to be added to the memory bank.
        """
        if isinstance(new_data, list):
            self.memory_bank.extend(new_data)
        elif isinstance(new_data, str):
            self.memory_bank.append(new_data)
        else:
            logging.warning("Invalid data type for memory update. Expecting string or list.")

    def adjust_creativity(self, new_factor: float):
        """
        Adjust the creativity factor to increase or decrease randomness in idea generation.
        :param new_factor: New creativity factor.
        """
        self.creativity_factor = self._validate_creativity_factor(new_factor)

    def set_evaluation_metrics(self, relevance: float, novelty: float):
        """
        Set the evaluation metrics for ideas.
        :param relevance: Weight for relevance in idea evaluation.
        :param novelty: Weight for novelty in idea evaluation.
        """
        if all(isinstance(metric, (int, float)) for metric in [relevance, novelty]):
            self.evaluation_metrics['relevance'] = relevance
            self.evaluation_metrics['novelty'] = novelty
        else:
            logging.warning("Invalid metric values. Expecting numbers.")

# Example Usage
if __name__ == "__main__":
    memory_bank = ['Data Point A', 'Experience B', 'Idea C', 'Observation D']
    dreamer = MachineDreamer(memory_bank, creativity_factor=1.2, api_key="your_api_key_here")

    # Generating and evaluating a creative solution
    creative_solution, score = dreamer.dream()
    print("Creative Solution:", creative_solution, "Score:", score)

    # Updating the memory bank with new data
    dreamer.update_memory(['Insight E', 'Fact F'])
