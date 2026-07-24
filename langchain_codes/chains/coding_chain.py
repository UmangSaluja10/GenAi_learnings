"""
CodingChain

This module combines:
Prompt -> Model -> Output_parser
into a single reusable LangChain pipeline
"""

from services.llm_service import get_model
from prompts.coding_prompt import coding_prompt
from parser.output_parser import output_parser
from runnable.input_processor import input_processor

model = get_model()
coding_chain = (input_processor | coding_prompt | model | output_parser)

