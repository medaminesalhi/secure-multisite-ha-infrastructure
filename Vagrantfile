
Vagrant.configure("2") do |config|

  config.vm.box_check_update = false

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

      # Reseau LAN partage avec OPNsense
      machine.vm.network "private_network",
        ip: server[:ip],
        virtualbox__intnet: "lan"

      machine.vm.provider "virtualbox" do |vb|

        vb.name = server[:name]
        vb.memory = server[:ram]
        vb.cpus = server[:cpu]

        # Eviter le chevauchement avec le LAN 10.0.2.0/24
        vb.customize [
          "modifyvm", :id,
          "--natnet1", "10.0.3.0/24"
        ]

      end
    end
  end
end
