# examples
A collection of code examples you can use to access the U-M GPT Toolkit API service.  

**Common required parameters**  
  
Note that these parameters may be represented by slightly different naming conventions, depepending on script language and module requirements.  
   
api_base = "https://api.umgpt.umich.edu/azure-openai-api"  
API VERSION = "2025-04-01-preview" #This is not the model version  
model = "gpt-4.1" #chat deployment model name  
apiKey #your 32 character API key  
organization #a valid 6 digit shortcode  

Please create a package.json file in the same directory as your script with the following:

{
  "type": "module",
  "dependencies": {
    "openai": "^4.20.1"
  }
}

**References**  
  
[Azure OpenAI Service REST API reference](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference)
