packer {

  required_plugins {

    virtualbox = {

      version = ">= 1.0.0"

      source = "github.com/hashicorp/virtualbox"

    }

  }

}



source "virtualbox-iso" "opnsense" {


  vm_name = var.vm_name


  guest_os_type = "FreeBSD_64"


  iso_url = var.opnsense_iso



  iso_checksum = "sha256:1efd5dc9fa12a1f93571183fe5e3823e22e332872de8417fafb5e4e4d48d5dcd"



  cpus = var.cpu


  memory = var.memory


  disk_size = var.disk_size



  headless = false



  boot_wait = "10s"



  boot_command = [

    "<wait10>",

    "<enter>"

  ]

  ssh_username = "root"

  ssh_password = "opnsense"

  shutdown_command = "shutdown -p now"


}



build {

  sources = [

    "source.virtualbox-iso.opnsense"

  ]

}