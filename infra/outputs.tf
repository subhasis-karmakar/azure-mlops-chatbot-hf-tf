output "resource_group_name" { value = module.resource_group.name }
output "storage_account_name" { value = module.storage_account.name }
output "acr_login_server" { value = module.acr.login_server }
output "workspace_name" { value = module.aml_workspace.name }
output "aks_name" { value = module.aks.name }
output "key_vault_name" { value = module.key_vault.name }
