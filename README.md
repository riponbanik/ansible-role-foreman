Ansible Role to install and configure Foreman

[![Build Status](https://travis-ci.org/riponbanik/ansible-role-foreman.svg?branch=master)](https://travis-ci.org/riponbanik/ansible-role-foreman)

Ubuntu VM in TravisCI has got issue, tested with kitchen-ansible using hyperv vagrant machine and Amazon ec2

## Requirements
Foreman require hostname to be fqdn. Use Ansible hostname module to change hostname to fqdn or use the following role variable to change hostname e.g.
   foreman_hostname: foreman.vagrantup.com

When the install is successful, foreman can be accessed using https://foreman_fqdn with default credentials below
 
   User: admin
   Password: password

## Role Variables
Available variables are listed below, along with default values (see `defaults/main.yml`):

   disable_puppet: true

By default, `all-in-one` Foreman installation includes a Puppet master, but this can be disabled with the above parameter

## Dependencies

VM (on-perm or cloud) is needed to install. Tested with the following OS -
 
   1. Redhat Enterprise Linux 7
   2. CentOS 7    
   3. Ubuntu 16.04 (Xenial)   

## Example Playbook

    - hosts: servers
      vars_files:
        - vars/main.yml
      roles:
        - role: riponbanik.foreman 
          foreman_hostname: foreman.vagrantup.com

## License

MIT / BSD


## Refernces
Documentation is avaiable from Foreman Website [https://www.theforeman.org/]


## Author Information

This role was created in 2018 by [Ripon Banik](https://www.linkedin.com/in/ripon-banik-79956b23/)

