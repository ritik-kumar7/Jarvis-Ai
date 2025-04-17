# utils/math_solver.py
from .base_solver import BaseSolver
from sympy import sympify, solve, diff, integrate, symbols, sqrt, sin, cos, Eq
from sympy.parsing.sympy_parser import (parse_expr, standard_transformations, 
                                       implicit_multiplication)
import re
from sympy.core.sympify import SympifyError

class MathSolver(BaseSolver):
    def __init__(self):
        self.transformations = standard_transformations + (implicit_multiplication,)
        self.x, self.y, self.z = symbols('x y z')
        
        self.word_to_num = {
            'zero': '0', 'one': '1', 'two': '2', 'three': '3',
            'four': '4', 'five': '5', 'six': '6', 'seven': '7',
            'eight': '8', 'nine': '9', 'ten': '10', 'pi': 'pi'
        }
        
        self.operator_map = {
            'divided by': '/', 'times': '*', 'plus': '+', 'minus': '-',
            'multiplied by': '*', 'square root of': 'sqrt',
            'to the power of': '**', 'raised to': '**', '^': '**'
        }

    def handle(self, query: str, context: str = "") -> str:
        try:
            query = query.lower().strip()
            
            if 'square root of' in query:
                num = query.split('square root of')[-1].strip()
                num = self._replace_words_with_numbers(num)
                return f"Square root: {sqrt(float(num))}"
            
            if any(op in query for op in ['/0', 'divided by zero']):
                return "Error: Division by zero"

            processed = self._preprocess_input(query)
            
            if any(word in processed for word in ['solve for', 'find']):
                return self._solve_equation(query)
            elif any(word in processed for word in ['derivative', 'differentiate']):
                return self._solve_derivative(processed)
            elif any(word in processed for word in ['integrate', 'integration']):
                return self._solve_integral(processed)
            else:
                return self._solve_basic(processed)
                
        except SympifyError:
            return "Error: Invalid math expression"
        except Exception as e:
            return f"Math error: {str(e)}"

    def _preprocess_input(self, text):
        """Convert natural language to math expressions"""
        # Replace number words
        for word, num in self.word_to_num.items():
            text = re.sub(rf'\b{word}\b', num, text)
        
        # Replace operators
        for word, symbol in self.operator_map.items():
            text = text.replace(word, symbol)
            
        # Clean up
        text = re.sub(r'(calculate|what is|find|the|value of|)', '', text).strip()
        return text

    def _solve_basic(self, expr):
        """Solve basic arithmetic"""
        try:
            expr = parse_expr(expr, transformations=self.transformations)
            result = expr.evalf()
            if result.is_Integer:
                return f"Result: {int(result)}"
            return f"Result: {result}"
        except:
            return "Error: Could not evaluate expression"

    def _solve_equation(self, text):
        """Solve equations"""
        try:
            # Extract variable
            var_match = re.search(r'(solve for|find)\s+([a-zA-Z])', text)
            if not var_match:
                return "Please specify a variable to solve for"
            var = var_match.group(2)
            
            # Extract equation
            if 'in' in text:
                expr = text.split('in')[-1].strip()
            elif 'when' in text:
                expr = text.split('when')[-1].strip()
            else:
                expr = text.split(var)[-1].strip()
            
            # Handle equation
            if '=' in expr:
                lhs, rhs = expr.split('=', 1)
                expr = f"Eq({lhs.strip()}, {rhs.strip()})"
            
            # Parse and solve
            solution = solve(parse_expr(expr, transformations=self.transformations), symbols(var))
            
            if not solution:
                return "No solution found"
            
            if len(solution) == 1:
                return f"Solution: {var} = {solution[0]}"
            return f"Solutions: {', '.join(str(s) for s in solution)}"
        except Exception as e:
            return f"Error solving equation: {str(e)}"

    def _solve_derivative(self, text):
        """Find derivatives"""
        try:
            expr_text = text.replace('derivative of', '').replace('differentiate', '').strip()
            expr = parse_expr(expr_text, transformations=self.transformations)
            derivative = diff(expr, self.x)
            return f"Derivative: {derivative}"
        except:
            return "Error: Could not compute derivative"

    def _solve_integral(self, text):
        """Calculate integrals"""
        try:
            expr_text = text.replace('integrate', '').replace('integration of', '').strip()
            expr = parse_expr(expr_text, transformations=self.transformations)
            integral = integrate(expr, self.x)
            return f"Integral: {integral} + C"
        except:
            return "Error: Could not compute integral"

    def _replace_words_with_numbers(self, text):
        """Helper to convert words to numbers"""
        for word, num in self.word_to_num.items():
            text = re.sub(rf'\b{word}\b', num, text)
        return text

# Create instance (no longer abstract)
math_solver = MathSolver()