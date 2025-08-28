
LioN Directive Language (LNDL)

**intelligent event** is a situation that requires decision making, the states and data associated with such an event is called **work**. A **work function** defines and implements the logic of carrying out work, and a **worker** handles intelligent events to desired situation. 


😐
❌
🦁
🙃
😊
🦙
🦜

| Categories |                                      | [DSPy](https://github.com/stanfordnlp/dspy) | [Autogen](https://github.com/microsoft/autogen) | [vynix](https://github.com/lion-agi/lionagi) 🦁 | [LlamaIndex](https://github.com/run-llama/llama_index) 🦙 | [LangChain](https://github.com/langchain-ai/langchain)🦜 |
| ---------- | ------------------------------------ | ------------------------------------------- | ----------------------------------------------- | ------------------------------------------------- | --------------------------------------------------------- | -------------------------------------------------------- |
|            | Animal as logo                       | ❌                                           | ❌                                               | ✅                                                 | ✅                                                         | ✅                                                        |
|            | How difficult does it go up to?      | very very difficult                         | very very difficult                             | very very difficult                               | very very difficult                                       | very very difficult                                      |
|            |                                      |                                             |                                                 |                                                   |                                                           |                                                          |
| RAG        | Load / store                         | Native                                      | ❌                                               | via 🦙, 🦜                                        | Native                                                    | Native                                                   |
|            | Indexing                             |                                             | ❌                                               | via 🦙                                            | Native                                                    | Native                                                   |
|            | Retrieval                            | Native                                      | ❌                                               | via 🦙                                            | Native                                                    | Native                                                   |
|            |                                      |                                             |                                                 |                                                   |                                                           |                                                          |
| LLM        | API                                  | ✅                                           | limited                                         | ✅                                                 | ✅                                                         | ✅                                                        |
|            | Local                                | ✅                                           | limited                                         | ✅                                                 | ✅                                                         | ✅                                                        |
|            | Async                                | ❌                                           | ✅                                               | ✅                                                 | ✅                                                         | ✅                                                        |
|            |                                      |                                             |                                                 |                                                   |                                                           |                                                          |
| Tool       | Tool use                             | Native                                      | Native                                          | Native                                            | via 🦜                                                    | Native                                                   |
|            | parallel                             | Native                                      | Native                                          | Native                                            | via 🦜                                                    | Native                                                   |
|            | async parallel                       | ❌                                           | Native                                          | Native                                            | via 🦜                                                    | Native                                                   |
|            | toolkit                              | limited                                     | limited                                         | limited                                           | extensive                                                 | extensive                                                |
|            | Tool Orchestration                   | hard 🙃                                     | medium 😐                                       | easy 😊                                           | medium 😐                                                 | hard 🙃                                                  |
|            | custom tool difficulty               | hard 🙃                                     | easy 😊                                         | easy 😊                                           | medium 😐                                                 | hard 🙃                                                  |
|            |                                      |                                             |                                                 |                                                   |                                                           |                                                          |
| Agent      | advanced prompting                   | ✅                                           | ✅                                               | ✅                                                 | ✅                                                         | ✅                                                        |
|            | Memory                               | ❌                                           | Native                                          | Native                                            | via 🦜                                                    | Native                                                   |
|            | graph based                          | ❌                                           | ❌                                               | Native                                            | ❌                                                         | Native on LangGraph                                      |
|            | Multi-agent collaboration difficulty | hard 🙃                                     | easy 😊                                         | easy 😊                                           | medium 😐                                                 | hard 🙃                                                  |
|            | Multi-step reasoning difficulty      | easy 😊                                     | easy 😊                                         | easy 😊                                           | hard 🙃                                                   | hard 🙃                                                  |
|            | Deterministic                        | high                                        | low                                             | high                                              | medium                                                    | medium                                                   |
|            |                                      |                                             |                                                 |                                                   |                                                           |                                                          |
| Other      | Compatibility with others            | Low                                         | Medium                                          | High                                              | High                                                      | High                                                     |
|            | Dataset                              | ✅                                           | ❌                                               | ❌                                                 | ✅                                                         | ✅                                                        |
|            | Declarative                          | ✅                                           | ✅                                               | ✅                                                 | ❌                                                         | ❌                                                        |
|            | Compilation                          | ✅                                           | ❌                                               | ❌                                                 | ❌                                                         | ❌                                                        |
|            | Auto tuning                          | ✅                                           | ✅                                               | ❌                                                 | ✅                                                         | ✅                                                        |
|            | Difficulty  structured output        | easy 😊                                     | ❌                                               | easy 😊                                           | medium 😐                                                 | hard 🙃                                                  |
|            | Pure python core                     | ✅                                           | ✅                                               | ✅                                                 | ❌                                                         | ❌                                                        |
|            | Pydantic OOP                         | ✅                                           | ❌                                               | ✅                                                 | ✅                                                         | ✅                                                        |
|            | num dependency                       | 2673                                        | 1490                                            | 36                                                | 4193                                                      | 12714                                                    |
|            | complex ones                         | pandas, oai, optuna, dataset                | pandas, oai, flaml, docker                      | pandas                                            | 🤔                                                        | 🤔                                                       |



Concepts:

intelligent event,  intelligent model,  work,  work function,  worker,  form, task,  flow,  workflow, mail, signal, directive




|||DSPy|vynix|LlamaIndex|LangChain / LangGraph|




|RAG|Index, Load, Chunk, Store|/|via LL, LC|Native and awesome|Native|
||Retrieve|Native|via LL, LC|Native and awesome|Native|
|||||||
|LLM|API|via OpenAI…|Native|via OpenAI…|via OpenAI…|
||Async API|/|Native|via OpenAI…|via OpenAI…|
||Local|via Ollama…|via Ollama…|via Ollama…|via Ollama…|
||Async Local|/|via Ollama…|via Ollama…|via Ollama…|
|||||||
|Agents|memory|/|Native|via LC|Native|
||tool use|Native|Native|via LC|Native|
||parallel tool use|Native|Native|via LC|Native|
||async parallel tool use|/|Native|via LC|Native|
||built-in toolkit|limited|limited|extensive|extensive|
||difficulty building custom tool|hard|easy|medium|hard|
||Graph Based|/|Native|/|Native (LangGraph)|
|||||||
|Others|DataSet|Yes|/|Yes|Yes|
||Declarative|Yes|Yes|/|/|
||AutoTuning|Native|/|Yes|Yes|
||Structured Output (difficulty)|Easy|Easy|Medium|Hard|
||pure python core|Yes|Yes|/|/|
||pydantic OOP|Yes|Yes|Yes|Yes|
||depend on others here?|/|/|LC|/|
||# of dependencies (from github dependency)|2673|36|4193|12714|
||complex dependencies (according to GPT)|Pandas, OpenAI, Optuna, and Datasets|pandas, aiohttp|???|???|
||Community|enthuisastic|crying|enthuisastic|enthuisastic|




|row1|row2|



| - |-|DSPy|vynix|LlamaIndex|LangChain|
|RAG


   
|||DSPy|vynix|LlamaIndex|LangChain / LangGraph|
|RAG|Index, Load, Chunk, Store|/|via LL, LC|Native and awesome|Native|
||Retrieve|Native|via LL, LC|Native and awesome|Native|
|||||||
|LLM|API|via OpenAI…|Native|via OpenAI…|via OpenAI…|
||Async API|/|Native|via OpenAI…|via OpenAI…|
||Local|via Ollama…|via Ollama…|via Ollama…|via Ollama…|
||Async Local|/|via Ollama…|via Ollama…|via Ollama…|
|||||||
|Agents|memory|/|Native|via LC|Native|
||tool use|Native|Native|via LC|Native|
||parallel tool use|Native|Native|via LC|Native|
||async parallel tool use|/|Native|via LC|Native|
||built-in toolkit|limited|limited|extensive|extensive|
||difficulty building custom tool|hard|easy|medium|hard|
||Graph Based|/|Native|/|Native (LangGraph)|
|||||||
|Others|DataSet|Yes|/|Yes|Yes|
||Declarative|Yes|Yes|/|/|
||AutoTuning|Native|/|Yes|Yes|
||Structured Output (difficulty)|Easy|Easy|Medium|Hard|
||pure python core|Yes|Yes|/|/|
||pydantic OOP|Yes|Yes|Yes|Yes|
||depend on others here?|/|/|LC|/|
||# of dependencies (from github dependency)|2673|36|4193|12714|
||complex dependencies (according to GPT)|Pandas, OpenAI, Optuna, and Datasets|pandas, aiohttp|???|???|
||Community|enthuisastic|crying|enthuisastic|enthuisastic|




