# test_math_solver.py
from utils.math_solver import math_solver

def run_math_tests():
    print("🧪 Starting Math Solver Test Suite...\n")
    
    test_cases = [
        # Basic arithmetic
        ("2 + 2", "4"),
        ("10 * 5 + 3", "53"),
        ("(5 + 3) * 2", "16"),
        ("2 to the power of 8", "256"),
        
        # Natural language math
        ("what is five times three", "15"),
        ("calculate pi multiplied by 10", "31.4"),  # Approximate
        ("square root of 169", "13"),
        ("two plus two divided by two", "3"),
        
        # Algebra
        ("solve for x in 2x + 5 = 15", "x = 5"),
        ("find y when 3y - 7 = 14", "y = 7"),
        ("solve z in z/2 = 8", "z = 16"),
        ("solve x^2 = -1", "No solution"),  # Imaginary
        
        # Calculus
        ("derivative of x^2 + 3x", "2*x + 3"),
        ("differentiate sin(x) + cos(x)", "cos(x) - sin(x)"),
        ("integrate x^2 + 3", "x**3/3 + 3*x"),
        ("integration of 2x + 5", "x**2 + 5*x"),
        
        # Edge cases
        ("what is 5 divided by 0", "Error"),
        ("solve for x in x + y = 5", "specify a variable")
    ]

    passed = 0
    for i, (problem, expected) in enumerate(test_cases, 1):
        print(f"Test {i}: {problem}")
        try:
            result = math_solver.handle(problem)
            
            # Normalize results for comparison
            result_clean = result.lower()
            expected_in_result = expected.lower() in result_clean
            
            if expected_in_result:
                print(f"✅ PASSED | Output: {result}")
                passed += 1
            else:
                print(f"❌ FAILED | Expected: {expected} | Got: {result}")
            
        except Exception as e:
            print(f"💥 CRASHED | Exception: {str(e)}")
        
        print("-" * 60)
    
    print(f"\n📊 Test Results: {passed}/{len(test_cases)} Passed")
    if passed == len(test_cases):
        print("🎉 All math tests passed successfully!")
    else:
        print("⚠️ Some tests failed. Review the outputs above.")

if __name__ == "__main__":
    run_math_tests()