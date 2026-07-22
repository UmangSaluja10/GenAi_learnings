"""
CodingChain

This module combines:
Prompt -> Model -> Output_parser
into a single reusable LangChain pipeline
"""

from services.llm_service import get_model
from prompts.coding_prompt import coding_prompt
from parser.output_parser import output_parser

model = get_model()
coding_chain = (coding_prompt | model | output_parser)

