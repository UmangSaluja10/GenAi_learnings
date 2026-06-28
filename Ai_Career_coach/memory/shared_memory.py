"""
Shared Memory
Acts as a common storage for all agents
"""

class SharedMemory:
    """
    Share memory accessible by every agent
    """

    def __init__(self):
        self.memory = {}

    def add(self, key: str, value: str) -> None:
        """
        Store data
        """

        self.memory[key] = value

    def get(self,key: str) -> str:
        """
        retrieve memory
        """
        return self.memory.get(key)
    
    def exist(self, key: str)-> bool:
        """
        Chcek if the key exists
        """
        return key in self.memory
    
    def clear(self) -> None:
        """
        Clear memory
        """

        self.memory.clear()

    def display(self) -> None:
        """
        Print current memory
        """

        print("="*50)
        for key, value in self.memory.items():
            print(f"{key}")
            print(value)
            print("="*50) 