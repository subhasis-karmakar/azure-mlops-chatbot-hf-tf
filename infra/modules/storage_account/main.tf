resource "azurerm_storage_account" "this" {
  name                     = substr(var.name, 0, 24)
  resource_group_name      = var.resource_group_name
  location                 = var.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  tags                     = var.tags
}
resource "azurerm_storage_container" "raw" {
  name                  = "raw"
  storage_account_name  = azurerm_storage_account.this.name
  container_access_type = "private"
}

resource "azurerm_storage_container" "processed" {
  name                  = "processed"
  storage_account_name  = azurerm_storage_account.this.name
  container_access_type = "private"
}

resource "azurerm_storage_container" "artifacts" {
  name                  = "artifacts"
  storage_account_name  = azurerm_storage_account.this.name
  container_access_type = "private"
}