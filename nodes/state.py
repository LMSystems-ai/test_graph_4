"""
State definition for test_graph
"""

from typing import Dict, Any, TypedDict


class State(TypedDict):
    """State for the test_graph workflow."""
    # Define your state fields here
    input: str
    output: Any