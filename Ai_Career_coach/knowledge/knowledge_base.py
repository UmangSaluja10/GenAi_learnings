"""
Knowledge Base

Provides domain-specific knowledge to AI agents

Responsibilities:
1. Load knowledge from a JSON file.
2. Retrieve the knowledge based on a search key.
3. Hide the underlying data source from AI agents.
4. Prepare the project for future RAG implementation.
"""

import json
from pathlib import Path
#Type hint
from typing import Any

class KnowledgeBase:
    """
    Loads and manages domain specific knowledge
    Currently, knowledge is loaded from a JSON file
    Later, the implementation can be replaced with a Vector Database
    """

    def __init__(self, knowledge_file: str) -> None:
        """
        Initializes the KnowledgeBase with a JSON file containing knowledge.

        Args:
            knowledge_file (str): Path to the JSON file containing knowledge.
        """
        self._knowledge = self._load_knowledge(knowledge_file)
        

    def _load_knowledge(self, knowledge_file: str) -> dict[str,Any]:
        """
        Loads knowledge from a JSON file.

        Args:
            knowledge_file (str): Path to the JSON file containing knowledge.
        Returns:
            Dictionary containing knowledge
        """
        file_path = Path(knowledge_file)
        if not file_path.exists():
            raise FileNotFoundError(f"Knowledge file not found: {knowledge_file}")
        
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
        
    def get(self, key: str) -> Any:
        """
        Retrieves knowledge based on a search key.

        Args:
            key (str): The key to search for in the knowledge base.
        Returns:
            The value associated with the key, or None if the key is not found.
        """
        return self._knowledge.get(key, None)
    
    def retrieve(self,query:str) -> dict:
        query = query.lower()
        for key, value in self._knowledge.items():
            if key.lower().replace("_"," ")in query:
                return value
            
        return {}

    def get_all(self) -> dict[str, Any]:
        """
        Retrieves all knowledge in the knowledge base.

        Returns:
            Dictionary containing all knowledge.
        """
        return self._knowledge
    
    def exists(self, key: str) -> bool:
        """
        Checks if a key exists in the knowledge base.

        Args:
            key (str): The key to check for existence.
        Returns:
            True if the key exists, False otherwise."""
        return key in self._knowledge
    
    def display(self) -> None:
        """
        Displays the entire knowledge base in a readable format.
        """
        print("\n"+"="*50)
        print("Knowledge Base:")
        print("="*50)
        if not self._knowledge:
            print("Knowledge base is empty.")
            return
        for key, value in self._knowledge.keys():
            print(f"- {key}")