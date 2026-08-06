from prompts.question_prompt import question_prompt
from chains.chain_factory import build_chain

question_chain = build_chain(question_prompt)