import re 

class TicketPreprocessor:

    def __init__(self, data):
        """
        Initialize the preprocessor with a Ticket object.

        Args:
            data (str): The ticket data to preprocess.
        """
        self.data = data

    def clean_description(self, desc: str) -> str:
        """
        Lowercase and strip extra spaces from text description.

        Args:
            desc (str): The text description to clean.

        Returns:
            str: The cleaned text description.
        """
        desc = desc.lower().strip()
        desc = re.sub(r'\s+', ' ', desc)
        return desc
    
    def remove_special_characters(text: str) -> str:
        """
        Remove special characters from text.

        Args:
            text (str): The text to process.

        Returns:
            str: The text without special characters.
        """
        return re.sub(r'[^a-zA-Z0-9\s]', '', text)
    
    def preprocess(self) -> str:
        """
        Preprocess a single ticke

        Returns:
            str: The preprocessed ticket data.
        """
        if not isinstance(self.data, str):
            raise ValueError("Input data must be a string.")
        desc = self.clean_description(self.data)
        desc = self.remove_special_characters(desc)
        return desc