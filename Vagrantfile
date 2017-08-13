# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  config.vm.box = "ubuntu/xenial64"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  config.vm.provider "virtualbox" do |vb|
    # Display the VirtualBox GUI when booting the machine
    #vb.gui = true
    # Customize the amount of memory on the VM:
    vb.memory = "4096"
  end
  #
  # View the documentation for the provider you are using for more
  # information on available options.
  #
  # expose port 8000 & 8008 to host
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.network "forwarded_port", guest: 8008, host: 8008

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y python-pip tcpdump unzip libpcap-dev
    pip install --upgrade pip
    pip install virtualenv
  SHELL
  config.vm.provision "shell", privileged: false, inline: <<-SHELL
    mkdir ~/venvs
    virtualenv ~/venvs/connmon
    source ~/venvs/connmon/bin/activate
    pip install honcho zmq chains
    wget -q https://github.com/joewalnes/websocketd/releases/download/v0.2.12/websocketd-0.2.12-linux_amd64.zip
    unzip websocketd-0.2.12-linux_amd64.zip -d ~/venvs/connmon/bin/
  SHELL
end
