# VYNIX - Versatile Yet Networked Intelligence eXchange

## An Agentic Intelligence SDK

Vynix is a robust framework for orchestrating multi-step AI operations with precise control. Bring together multiple models, advanced reasoning loops, tool integrations, and custom validations in a single coherent pipeline.

## Why Vynix?  

- **Structured**: Validate and type all LLM interactions with Pydantic.
- **Expandable**: Integrate multiple providers with minimal friction.
- **Controlled**: Use built-in safety checks, concurrency strategies, and advanced multi-step flows.
- **Transparent**: Debug easily with real-time logging, message introspection, and tool usage tracking.

## Installation

```
uv add vynix  # recommended

pip install vynix  # or install directly
```

## Quick Start

```python
from vynix import Branch, iModel

gpt4o = iModel(provider="openai", model="gpt-4o-mini")

hunter = Branch(
  system="you are a hilarious dragon hunter who responds in 10 word rhymes.",
  chat_model=gpt4o,
)

response = await hunter.communicate("I am a dragon")
print(response)
```

```
You claim to be a dragon, oh what a braggin'!
```

### Structured Responses

Use Pydantic to keep outputs structured:

```python
from pydantic import BaseModel

class Joke(BaseModel):
    joke: str

res = await hunter.operate(
    instruction="Tell me a short dragon joke",
    response_format=Joke
)
print(type(res))
print(res.joke)
```

```
<class '__main__.Joke'>
With fiery claws, dragons hide their laughter flaws!
```

### ReAct and Tools

Vynix supports advanced multi-step reasoning with ReAct. Tools let the LLM invoke external actions:

```
pip install "vynix[reader]"
```

```python
from vynix.tools.types import ReaderTool

gpt4o = iModel(provider="openai", model="gpt-4o-mini")

branch = Branch(chat_model=gpt4o, tools=[ReaderTool])
result = await branch.ReAct(
    instruct={
      "instruction": "Summarize my PDF and compare with relevant papers.",
      "context": {"paper_file_path": "/path/to/paper.pdf"},
    },
    extension_allowed=True,
    max_extensions=5,
    verbose=True,
)
print(result)
```

The LLM can open the PDF, read in slices, fetch references, and produce a final structured summary.

### MCP Integration

Vynix supports the Model Context Protocol for seamless tool integration:

```
pip install "vynix[mcp]"
```

```python
from vynix import load_mcp_tools

tools = await load_mcp_tools(".mcp.json", ["search", "memory"])

branch = Branch(chat_model=gpt4o, tools=tools)
result = await branch.ReAct(
    instruct={"instruction": "Research recent AI developments"},
    tools=["search_exa_search"],
    max_extensions=3
)
```

- **Dynamic Discovery**: Auto-discover and register tools from MCP servers
- **Type Safety**: Full Pydantic validation for tool interactions
- **Connection Pooling**: Efficient resource management with automatic reuse

### Observability & Debugging

Inspect messages:

```python
df = branch.to_df()
print(df.tail())
```

Action logs show each tool call, arguments, and outcomes. Verbose ReAct provides chain-of-thought analysis helpful for debugging multi-step flows.

### Multi-Model Orchestration

```python
from vynix import Branch, iModel

gpt4o = iModel(provider="openai", model="gpt-4o-mini")
sonnet = iModel(
  provider="anthropic",
  model="claude-3-5-sonnet-20241022",
  max_tokens=1000,
)

branch = Branch(chat_model=gpt4o)
analysis = await branch.communicate("Analyze these stats", chat_model=sonnet)
```

Seamlessly route to different models in the same workflow.

### CLI Model Integration

Vynix supports autonomous coding capabilities with persistent session management via a CLI endpoint.

```python
from vynix import iModel, Branch

def create_cli_model():
  return iModel(
      provider="cli_coder",
      endpoint="query_cli",
      model="sonnet",
      verbose_output=True,
  )

orchestrator = Branch(chat_model=create_cli_model())
response = await orchestrator.communicate("Explain the system architecture")

response2 = await orchestrator.communicate("How do these components fit together?")
```

### Fan-Out / Fan-In Orchestration

```python
from vynix.fields import LIST_INSTRUCT_FIELD_MODEL, Instruct

response3 = await orchestrator.operate(
  instruct=Instruct(
    instruction="create 4 research questions for parallel discovery",
    guidance="put into `instruct_model` field as part of your structured result message",
    context="I'd like to create an orchestration system for AI agents using vynix"
  ),
  field_models=[LIST_INSTRUCT_FIELD_MODEL],
)

len(response3.instruct_model)  # should be 4

async def handle_instruct(instruct):
  sub_branch = Branch(
    system="You are a diligent research expert.",
    chat_model=create_cli_model(),
  )
  return await sub_branch.operate(instruct=instruct)

from vynix.ln import alcall
responses = await alcall(response3.instruct_model, handle_instruct)

final_response = await orchestrator.communicate(
  "please synthesize these research findings into a final report",
  context=responses,
)
```

Key features: auto-resume sessions, fine-grained tool permissions, streaming support, and seamless integration with existing Vynix workflows.

### Optional Dependencies

```
"vynix[reader]"   - Reader tool for unstructured data and web pages
"vynix[ollama]"   - Ollama model support for local inference
"vynix[rich]"     - Rich output formatting for better console display
"vynix[schema]"   - Convert Pydantic schema to persistent Model classes
"vynix[postgres]" - Postgres support for storing and retrieving structured data
"vynix[graph]"    - Graph display for visualizing complex workflows
"vynix[sqlite]"   - SQLite support for lightweight data storage
```

## Community & Contributing

We welcome issues, ideas, and pull requests. Join our community to chat, get help, or contribute.

---

**🔷 Vynix**

> Because real AI orchestration demands more than a single prompt. Try it out and discover the next evolution in structured, multi-model, safe AI.
