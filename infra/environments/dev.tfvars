location       = "eastus"
environment    = "dev"
project_name   = "chatbot"
tags           = { env = "dev", project = "azure-mlops-chatbot-hf-tf" }
aks_node_count = 2
aks_vm_size    = "Standard_DC2s_v3"
tenant_id      = "2d3f1375-ba4a-4e58-88cf-fa9961f1d43c"
acr_name       = "subhasischatbotdevacr"
storage_account_name = "subhasischatbotdevst"
key_vault_name = "subhasischatbotdevkv"