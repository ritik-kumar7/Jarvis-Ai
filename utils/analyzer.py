
from utils.brain import BaseSolver
from .base_solver import BaseSolver
import pandas as pd
import numpy as np
from io import StringIO

class DataAnalyzer(BaseSolver):
    def handle(self, query: str, context: str = "") -> str:
        try:
            if "csv" in query or "excel" in query:
                return self._analyze_data_file(query)
            elif "analyze" in query:
                return self._analyze_raw_data(query)
            return "I can analyze CSV/Excel data or raw data tables."
        except Exception as e:
            return f"Analysis error: {str(e)}"
    
    def _analyze_data_file(self, query: str) -> str:
        # In real implementation, you would get file path from query
        # This is a simulation
        data = """Name,Age,Salary
        John,28,50000
        Alice,32,75000
        Bob,45,60000"""
        
        df = pd.read_csv(StringIO(data))
        analysis = f"""
        Data Analysis Report:
        - Total records: {len(df)}
        - Average age: {df['Age'].mean():.1f} years
        - Average salary: ${df['Salary'].mean():,.2f}
        - Oldest: {df.loc[df['Age'].idxmax()]['Name']} ({df['Age'].max()} years)
        - Highest salary: {df.loc[df['Salary'].idxmax()]['Name']} (${df['Salary'].max():,})
        """
        return analysis
    
    def _analyze_raw_data(self, query: str) -> str:
        # Extract data from query (simplified)
        if "numbers" in query:
            numbers = [int(n) for n in query.split() if n.isdigit()]
            if not numbers:
                return "No numbers found to analyze."
            
            analysis = f"""
            Number Analysis:
            - Count: {len(numbers)}
            - Sum: {sum(numbers)}
            - Average: {np.mean(numbers):.2f}
            - Median: {np.median(numbers)}
            - Min/Max: {min(numbers)}/{max(numbers)}
            """
            return analysis
        return "Please provide data to analyze."