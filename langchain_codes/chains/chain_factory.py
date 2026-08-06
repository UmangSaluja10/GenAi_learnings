from services.llm_service import get_model
from parser.output_parser import output_parser
from runnable.input_processor import input_processor

model = get_model()

def build_chain(prompt):
    return (
        input_processor | prompt | model | output_parser
    )

