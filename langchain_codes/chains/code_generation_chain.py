from prompts.code_generation_prompt import code_generation_prompt
from chains.chain_factory import build_chain 

code_generation_chain = build_chain(code_generation_prompt)
