terraform {
  backend "azurerm" {
    resource_group_name  = "REPLACE_TFSTATE_RG"
    storage_account_name = "REPLACE_TFSTATE_STORAGE"
    container_name       = "tfstate"
    key                  = "chatbot-dev.tfstate"
  }
}
