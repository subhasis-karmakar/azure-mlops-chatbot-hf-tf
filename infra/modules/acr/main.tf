resource "azurerm_container_registry" "this" {
  name=substr(var.name,0,50)
  resource_group_name=var.resource_group_name
  location=var.location
  sku="Basic"
  admin_enabled=false
  tags=var.tags
}
