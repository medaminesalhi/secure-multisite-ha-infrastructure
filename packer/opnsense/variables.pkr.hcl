variable "opnsense_iso" {

  type = string

  default = "OPNsense-26.7-dvd-amd64.iso"

}


variable "vm_name" {

  type = string

  default = "opnsense-builder"

}


variable "cpu" {

  type = number

  default = 2

}


variable "memory" {

  type = number

  default = 4096

}


variable "disk_size" {

  type = number

  default = 20000

}