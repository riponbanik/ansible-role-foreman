Ansible Role to install and configure Foreman
[![Build Status](https://travis-ci.org/riponbanik/ansible-role-foreman.svg?branch=master)](https://travis-ci.org/riponbanik/ansible-role-foreman)

## Requirements
Foreman require hostname to be fqdn. Use Ansible hostname module to change hostname to fqdn or use the following role variable to change hostname e.g.

foreman_hostname: foreman.vagrantup.com

## Role Variables
Available variables are listed below, along with default values (see `defaults/main.yml`):

# Install and configure puppet master and puppet db
install_puppet_master: true

## Dependencies

None.

## Example Playbook

    - hosts: servers
      vars_files:
        - vars/main.yml
      roles:
        - role: riponbanik.foreman 
          install_puppet_master: false

## License

MIT / BSD


## Refernces
Documentation is avaiable from Foreman Website [https://www.theforeman.org/]

# Issues
* Build fails when using docker in travisci due to hostname setting, tested with kitchen-ansible using hyperv vagrant machine

## Author Information

This role was created in 2018 by [Ripon Banik ](https://www.linkedin.com/in/ripon-banik-79956b23/)

