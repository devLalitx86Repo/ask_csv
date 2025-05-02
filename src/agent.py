import os
import pandas as pd
from langchain_experimental.agents import create_csv_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

class CSVAnalyzer:
    def __init__(self):
        self.agent = None
        self.df = None
        self.temp_file_path = None
        
    def load_csv(self, file_path):
        """Load and validate CSV file"""
        try:
            self.df = pd.read_csv(file_path)
            # Save the DataFrame to a temporary file for the agent
            self.temp_file_path = file_path
            return True, "CSV loaded successfully"
        except Exception as e:
            return False, f"Error loading CSV: {str(e)}"
    
    def initialize_agent(self):
        """Initialize the CSV agent with OpenAI"""
        try:
            llm = ChatOpenAI(
                model=os.getenv("MODEL_NAME", "gpt-3.5-turbo"),
                temperature=0
            )
            self.agent = create_csv_agent(
                llm,
                self.temp_file_path,
                verbose=True
            )
            return True, "Agent initialized successfully"
        except Exception as e:
            return False, f"Error initializing agent: {str(e)}"
    
    def analyze(self, question):
        """Analyze the CSV data based on the user's question"""
        try:
            if not self.agent:
                return False, "Agent not initialized. Please load a CSV file first."
            
            response = self.agent.run(question)
            return True, response
        except Exception as e:
            return False, f"Error analyzing data: {str(e)}" 