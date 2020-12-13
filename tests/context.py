import sys
import os

# Add parent directory to Python's search path for importing modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import artifact_calc
