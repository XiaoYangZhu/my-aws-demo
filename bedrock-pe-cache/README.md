# Bedrock Document Q&A Tool

This tool leverages Amazon Bedrock and Claude 3.7 Sonnet to provide intelligent document question-answering capabilities.

## Overview

The `bedrock_pe_cache.py` script enables users to ask questions about documents and receive comprehensive, well-structured answers with relevant quotes and citations. It uses Amazon Bedrock's runtime API to access the Claude 3.7 Sonnet model.

## Features

- **Document Input Flexibility**: Accept documents from URLs or local files
- **Intelligent Question Answering**: Analyze documents and extract relevant information to answer user queries
- **Structured Responses**: Responses include:
  - Relevant quotes from the document
  - Comprehensive answers with citations to the quotes
  - Clear formatting with proper organization
- **Command-line Interface**: Easy-to-use CLI with flexible options

## Usage

```bash
# Query a document from a URL
python bedrock_pe_cache.py --url https://example.com/document.html --query "What are the key points in this document?"

# Query a document from a local file
python bedrock_pe_cache.py --file path/to/document.txt --query "Summarize the main arguments."

# Default example (uses an AWS blog post)
python bedrock_pe_cache.py --query "What techniques are discussed for enhancing conversational AI?"
```

## How It Works

1. The script takes a document (from URL or file) and a user query as input
2. It provides detailed instructions to the Claude model on how to analyze the document
3. The model identifies relevant quotes from the document
4. The model formulates a comprehensive answer based on these quotes
5. The response includes both the quotes and the answer with citations

## Requirements

- Python 3.x
- boto3
- requests
- AWS credentials configured with access to Amazon Bedrock

## Response Format

Responses follow a structured format:

1. **Relevant quotes**: Numbered excerpts from the document that address the query
2. **Answer**: A comprehensive response that cites the relevant quotes using bracketed numbers

This format ensures transparency in how the model arrived at its conclusions while providing a well-organized answer.
