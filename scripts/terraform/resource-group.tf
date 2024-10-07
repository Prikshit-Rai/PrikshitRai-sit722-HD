#
# Creates a resource group for flixtube in your Azure account.
#
resource "azurerm_resource_group" "taskHDprikshit" {
  name     = var.app_name
  location = var.location
}
