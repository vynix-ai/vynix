![PyPI - Version](https://img.shields.io/pypi/v/lionagi?labelColor=233476aa&color=231fc935) ![PyPI - Downloads](https://img.shields.io/pypi/dm/lionagi?color=blue)



[PyPI](https://pypi.org/project/lionagi/) | [Documentation](https://ocean-lion.com/Welcome) | [Discord](https://discord.gg/xCkA5ErGmV)

```
Documentation for v0.0.300+ is in progress

To contribute, you need to make a fork first, and then make pull request from your fork. 
```
  
# Language InterOperable Network - LION

**Powerful Intelligent Workflow Automation**

lionagi is an intelligent agentic workflow automation framework. It introduces advanced ML models into any existing workflows and data infrastructure.


### Currently, it can

- interact with almost any models including local*
- run interactions in parallel for most models (OpenRouter, OpenAI, Ollama, litellm...)
- produce structured pydantic outputs with flexible usage\*\*
- automate workflow via graph based agents
- use advanced prompting techniques, i.e. ReAct (reason-action)
- …

### It aims to:

- provide a centralized agent-managed framework for, "ML-powered tools coordination".
- The ways of coordination and possible path can occur among nodes is what we also refers to as `workflow` (the concept of workflow is still in design).
- such that, people can utilize intelligence to solve their problems in real life.
- achieve the goal by dramatically lowering the barrier of entries for creating use-case/domain specific tools.


All notebooks should run, as of 0.0.313,

\* if there are models on providers that have not been configured, you can do so by configuring your own AI providers, and endpoints. 

\*\* Structured Input/Output, Graph based agent system, as well as more advanced prompting techniques are undergoing fast interations...

### Why Automating Workflows?

Intelligent AI models such as [Large Language Model (LLM)](https://en.wikipedia.org/wiki/Large_language_model), introduced new possibilities of human-computer interaction. LLMs is drawing a lot of attention worldwide due to its “one model fits all”, and incredible performance. One way of using LLM is to use as search engine, however, this usage is complicated by the fact that LLMs [hallucinate](https://arxiv.org/abs/2311.05232).

What goes inside of a LLM is more akin to a [black-box](https://pauldeepakraj-r.medium.com/demystifying-the-black-box-a-deep-dive-into-llm-interpretability-971524966fdf), lacking interpretability, meaning we don’t know how it reaches certain answer or conclusion, thus we cannot fully trust/rely the output from such a system. 

<img width="500" alt="ReAct flow" src="https://github.com/lion-agi/lionagi/assets/122793010/fabec1eb-fa8e-4ce9-b75f-b7aca4809c0f">


Another approach of using LLM is to treat them as [intelligent agent](https://arxiv.org/html/2401.03428v1), that are equipped with various tools and data sources. A workflow conducted by such an intelligent agent have clear steps, and we can specify, observe, evaluate and optimize the logic for each decision that the `agent` made to perform actions. This approach, though we still cannot pinpoint how LLM output what it outputs, but the flow itself is **explainable**.

vynix `agent` can manage and direct other agents, can also use multiple different tools in parallel.

<img width="700" alt="parallel agents" src="https://github.com/lion-agi/lionagi/assets/122793010/ab263a6a-c7cc-40c3-8c03-ba1968df7309">



✅ : Done

〰️ : Not started

🛠️: In progress

| Folder             | Module             | written | Can run | Doc |
| ------------------ | ------------------ | ------- | ------- | --- |
| Action             | function_calling   | ✅       | ✅       | 〰️  |
|                    | manual             | 〰️      | 〰️      | 〰️  |
|                    | node               | ✅       | ✅       | 〰️  |
|                    | tool_manager       | ✅       | ✅       | 〰️  |
|                    | tool               | ✅       | ✅       | 〰️  |
|                    |                    |         |         |     |
| agent              | base_agent         | ✅       | 🛠️     | 〰️  |
| agent.evaluator    | evaluator          | 🛠️     | 🛠️     | 〰️  |
|                    | score              | 🛠️     | 🛠️     | 〰️  |
|                    | vote               | 🛠️     | 🛠️     | 〰️  |
| agent.learner      | learn              | 🛠️     | 🛠️     | 〰️  |
|                    | learner            | 🛠️     | 🛠️     | 〰️  |
| agent.planner      | plan               | 🛠️     | 🛠️     | 〰️  |
|                    |                    |         |         |     |
| collections.abc    | component          | ✅       | ✅       | 〰️  |
|                    | concepts           | ✅       | ✅       | 〰️  |
|                    | exceptions         | ✅       | ✅       | 〰️  |
|                    |                    |         |         |     |
| collections        | exchange           | ✅       | ✅       | 〰️  |
|                    | flow               | ✅       | ✅       | 〰️  |
|                    | model              | ✅       | ✅       | 〰️  |
|                    | pile               | ✅       | ✅       | 〰️  |
|                    | progression        | ✅       | ✅       | 〰️  |
|                    |                    |         |         |     |
| directive.engine   | ast_evaluator      | 🛠️     | 〰️      | 〰️  |
|                    | sandbox            | 🛠️     | 〰️      | 〰️  |
|                    | script_engine      | 🛠️     | 〰️      | 〰️  |
| directive.parser   | base               | 🛠️     | 〰️      | 〰️  |
|                    | syntax.txt         | 🛠️     | 〰️      | 〰️  |
| directive.template | base               | 🛠️     | 〰️      | 〰️  |
|                    | schema             | 🛠️     | 〰️      | 〰️  |
| directive.unit     | templates          | ✅       | ✅       | 〰️  |
|                    | unit               | ✅       | 🛠️     | 〰️  |
|                    | parallel_unit      | 🛠️     | 🛠️     | 〰️  |
|                    |                    |         |         |     |
| director           | direct             | 🛠️     | 〰️      | 〰️  |
|                    | director           | 🛠️     | 〰️      | 〰️  |
|                    |                    |         |         |     |
| execute            | base               | 🛠️     | 〰️      | 〰️  |
|                    | branch_executor    | 🛠️     | 〰️      | 〰️  |
|                    | instruction_map    | 🛠️     | 〰️      | 〰️  |
|                    | neo4j_executor     | 🛠️     | 〰️      | 〰️  |
|                    | structure_executor | 🛠️     | 〰️      | 〰️  |
|                    |                    |         |         |     |
| generic            | edge               | ✅       | ✅       | 〰️  |
|                    | graph              | ✅       | ✅       | 〰️  |
|                    | node               | ✅       | ✅       | 〰️  |
|                    | hyperedge          | 🛠️     |         | 〰️  |
|                    | tree_node          | ✅       | ✅       | 〰️  |
|                    | tree               | ✅       | ✅       | 〰️  |
|                    |                    |         |         |     |
| mail               | mail               | ✅       | ✅       | 〰️  |
|                    | mail_manager       | ✅       | ✅       | 〰️  |
|                    | package            | ✅       | ✅       | 〰️  |
|                    | start_mail         | ✅       | ✅       | 〰️  |
|                    |                    |         |         |     |
| message            | action_request     | ✅       | ✅       | 〰️  |
|                    | action_response    | ✅       | ✅       | 〰️  |
|                    | assistant_response | ✅       | ✅       | 〰️  |
|                    | instruction        | ✅       | ✅       | 〰️  |
|                    | message            | ✅       | ✅       | 〰️  |
|                    | system             | ✅       | ✅       | 〰️  |
|                    |                    |         |         |     |
| report             | base               | ✅       | ✅       | 〰️  |
|                    | form               | ✅       | ✅       | 〰️  |
|                    | report             | ✅       | ✅       | 〰️  |
|                    |                    |         |         |     |
| rule               | base               | ✅       | ✅       | 〰️  |
|                    | action             | ✅       | ✅       | 〰️  |
|                    | boolean            | ✅       | ✅       | 〰️  |
|                    | choice             | ✅       | ✅       | 〰️  |
|                    | mapping            | ✅       | ✅       | 〰️  |
|                    | number             | ✅       | ✅       | 〰️  |
|                    | rulebook           | ✅       | ✅       | 〰️  |
|                    | string             | ✅       | ✅       | 〰️  |
|                    |                    |         |         |     |
| session            | branch             | ✅       | ✅       | 〰️  |
|                    | directive-mixin    | 🛠️     | 〰️      | 〰️  |
|                    | session            | 🛠️     | 〰️      | 〰️  |
|                    |                    |         |         |     |
| validator          | validator          | ✅       | ✅       | 〰️  |
|                    |                    |         |         |     |
| structure          | chain              | 🛠️     | 🛠️     | 〰️  |
|                    | tree               | 〰️      | 〰️      | 〰️  |
|                    | graph              | 〰️      | 〰️      | 〰️  |
|                    | forest             | 〰️      | 〰️      | 〰️  |
|                    |                    |         |         |     |
| work               | work function      | ✅       | ✅       | 〰️  |
|                    | work queue         | ✅       | ✅       | 〰️  |
|                    | work               | ✅       | ✅       | 〰️  |
|                    | worker             | ✅       | ✅       | 〰️  |
|                    | worklog            | ✅       | ✅       | 〰️  |
|                    |                    |         |         |     |





### Community

We encourage contributions to vynix and invite you to enrich its features and capabilities. Engage with us and other community members [Join Our Discord](https://discord.gg/7RGWqpSxze)

### Citation

When referencing vynix in your projects or research, please cite:

```bibtex
@software{Li_vynix_2023,
  author = {Haiyang Li},
  month = {12},
  year = {2023},
  title = {vynix: Towards Automated General Intelligence},
  url = {https://github.com/lion-agi/lionagi},
}
```


### Requirements
Python 3.10 or higher. 

