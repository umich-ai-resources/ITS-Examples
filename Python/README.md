# Examples
This is a collection of example code for accessing the U-M GPT Toolkit API service.  

**Common required parameters**  
  
Note that these parameters may be represented by slightly different naming conventions, depepending on script language and module requirements.  
   
MODEL = Model names (gpt-4o, gpt-4.1, and etc)  
API gateway URL = "https://api.umgpt.umich.edu/azure-openai-api"    
API VERSION = "2025-04-01-preview" #This is not the model version  
DEPLOYMENT_ID = "gpt-4.1" #chat deployment model name  
API_KEY #your 32 character API key  
ORGANIZATION #a valid 6 digit shortcode  

Please create a .env in the same directory as the script you want to run with the following:

MODEL=X  
OPENAI_API_BASE=https://api.umgpt.umich.edu/azure-openai-api  
OPENAI_API_KEY=X   
OPENAI_ORGANIZATION=X  
API_VERSION=2024-06-01  

Change the model, key, and organization (optional) to your parameters. Models can be displayed by running the get_models.py file; note that some models may be deprecated or unavailable. 

**References**  
  
[Azure OpenAI Service REST API reference](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference)
