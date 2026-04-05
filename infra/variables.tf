variable "location" { type = string }
variable "environment" { type = string }
variable "project_name" { type = string }
variable "tags" { type = map(string) }
variable "aks_node_count" { type = number }
variable "aks_vm_size" { type = string }
