# Migration Guides

Migrate from other AI frameworks to vynix.

## Available Migration Guides

- **[From LangChain](from-langchain.md)** - Migrate LangChain workflows to
  vynix
- **[From CrewAI](from-crewai.md)** - Convert CrewAI crews to vynix workflows
- **[From AutoGen](from-autogen.md)** - Adapt AutoGen conversations for vynix

## Migration Philosophy

**Zero-Disruption Migration**: Keep your existing code and gradually adopt
vynix orchestration.

```python
# Your existing workflow runs unchanged
async def existing_workflow(input_data):
    return await your_current_implementation(input_data)

# Orchestrate with vynix
builder.add_operation(operation=existing_workflow)
```

## Migration Strategies

### **Gradual Adoption**

1. Wrap existing workflows as custom operations
2. Add vynix orchestration around them
3. Gradually convert individual components
4. Gain orchestration benefits without disruption

### **Hybrid Workflows**

- Mix existing framework code with native vynix operations
- Coordinate multiple frameworks in single workflow
- Best of all worlds approach

### **Full Migration**

- Translate framework patterns to vynix equivalents
- Leverage vynix's superior orchestration capabilities
- Gain performance and simplicity benefits

## Why Migrate?

- **Parallel Execution**: vynix runs operations concurrently by default
- **Simpler Code**: Less boilerplate, cleaner abstractions
- **Framework Agnostic**: Orchestrate any tool, not just one ecosystem
- **Production Ready**: Built-in monitoring, error handling, performance control
