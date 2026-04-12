module "resource_group" {
  source   = "./modules/resource_group"
  name     = "${var.project_name}-${var.environment}-rg"
  location = var.location
  tags     = var.tags
}

module "networking" {
  source              = "./modules/networking"
  name_prefix         = "${var.project_name}-${var.environment}"
  location            = var.location
  resource_group_name = module.resource_group.name
}

module "storage_account" {
  source              = "./modules/storage_account"
  name                = var.storage_account_name
  location            = var.location
  resource_group_name = module.resource_group.name
  tags                = var.tags
}

module "acr" {
  source              = "./modules/acr"
  name                = var.acr_name
  location            = var.location
  resource_group_name = module.resource_group.name
  tags                = var.tags
}

module "log_analytics" {
  source              = "./modules/log_analytics"
  name                = "${var.project_name}-${var.environment}-law"
  location            = var.location
  resource_group_name = module.resource_group.name
  tags                = var.tags
}

module "app_insights" {
  source              = "./modules/app_insights"
  name                = "${var.project_name}-${var.environment}-appi"
  location            = var.location
  resource_group_name = module.resource_group.name
  workspace_id        = module.log_analytics.id
  tags                = var.tags
}

module "key_vault" {
  source              = "./modules/key_vault"
  name                = var.key_vault_name
  location            = var.location
  resource_group_name = module.resource_group.name
  tenant_id           = var.tenant_id
  tags                = var.tags
}

module "aml_workspace" {
  source                  = "./modules/aml_workspace"
  name                    = "${var.project_name}-${var.environment}-mlw"
  location                = var.location
  resource_group_name     = module.resource_group.name
  storage_account_id      = module.storage_account.id
  key_vault_id            = module.key_vault.id
  application_insights_id = module.app_insights.id
  container_registry_id   = module.acr.id
  tags                    = var.tags
}

module "aks" {
  source              = "./modules/aks"
  name                = "${var.project_name}-${var.environment}-aks"
  location            = var.location
  resource_group_name = module.resource_group.name
  dns_prefix          = "${var.project_name}-${var.environment}"
  node_count          = var.aks_node_count
  vm_size             = var.aks_vm_size
  subnet_id           = module.networking.aks_subnet_id
  tags                = var.tags
}

module "monitoring" {
  source              = "./modules/monitoring"
  name_prefix         = "${var.project_name}-${var.environment}"
  resource_group_name = module.resource_group.name
  app_insights_id     = module.app_insights.id
  log_analytics_id    = module.log_analytics.id
}