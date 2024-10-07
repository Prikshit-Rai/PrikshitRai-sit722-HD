# Sets global variables for this Terraform project.

variable app_name {
  default = "taskHDprikshit"
}

variable resource_group_name {
  default = "taskHDprikshit.azurecr.io"
}

variable location {
  default = "eastus"
}

variable kubernetes_version {    
  default = "1.29.2"
}
