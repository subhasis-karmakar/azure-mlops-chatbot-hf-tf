terraform {
  backend "azurerm" {
    resource_group_name  = "ml-rg"
    storage_account_name = "subhasisterraformstate"
    container_name       = "tfstate"
    key                  = "chatbot-dev.tfstate"
  }
}
