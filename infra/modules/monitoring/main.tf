resource "azurerm_monitor_action_group" "this" {
  name                = "${var.name_prefix}-ag"
  resource_group_name = var.resource_group_name
  short_name          = "chatag"
}
resource "azurerm_monitor_metric_alert" "requests" {
  name                = "${var.name_prefix}-requests-alert"
  resource_group_name = var.resource_group_name
  scopes              = [var.app_insights_id]
  description         = "Placeholder alert for application telemetry"
  severity            = 3
  frequency           = "PT5M"
  window_size         = "PT5M"
  criteria {
    metric_namespace = "Microsoft.Insights/components"
    metric_name      = "requests/count"
    aggregation      = "Count"
    operator         = "GreaterThan"
    threshold        = 0
  }
}
