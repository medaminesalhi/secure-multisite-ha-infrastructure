Vagrant.configure("2") do |config|
  config.vm.box_check_update = false
  config.vm.define "opnsense-a" do |fw|

    fw.vm.box = "opnsense"

    fw.vm.hostname = "opnsense-salhi"

    fw.vm.network "private_network",
      ip: "10.0.2.1",
      virtualbox__intnet: "site-a-lan",
      auto_config: false

    fw.vm.provider "virtualbox" do |vb|

      vb.name = "OPNsense-Site-A"

      vb.memory = 4096

      vb.cpus = 2

      vb.gui = true

    end
  end
  servers = [


    {
      name: "haproxy-master",
      ip: "10.0.2.5",
      cpu: 1,
      ram: 2048,
      role: "haproxy"
    },


    {
      name: "haproxy-backup",
      ip: "10.0.2.6",
      cpu: 1,
      ram: 2048,
      role: "haproxy"
    },


    {
      name: "web-server",
      ip: "10.0.2.7",
      cpu: 1,
      ram: 2048,
      role: "web"
    },


    {
      name: "mysql-server",
      ip: "10.0.2.8",
      cpu: 1,
      ram: 3072,
      role: "database"
    }

  ]

  servers.each do |server|


    config.vm.define server[:name] do |machine|
      machine.vm.box = "ubuntu/jammy64"
      machine.vm.hostname = server[:name]
      machine.vm.network "private_network",
        ip: server[:ip],
        virtualbox__intnet: "site-a-lan"
      machine.vm.provider "virtualbox" do |vb|
        vb.name = server[:name]


        vb.memory = server[:ram]


        vb.cpus = server[:cpu]

      end
    end
  end
end