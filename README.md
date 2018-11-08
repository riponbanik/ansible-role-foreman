Ansible Role to install and configure Foreman
[![Build Status](https://travis-ci.org/riponbanik/ansible-role-foreman.svg?branch=master)](https://travis-ci.org/riponbanik/ansible-role-foreman)
Documentation is avaiable from Foreman Website [https://www.theforeman.org/]

## Requirements
Foreman require hostname to be fqdn. Use Ansible hostname module to change hostname to fqdn

## Role Variables
Available variables are listed below, along with default values (see `defaults/main.yml`):

# Install and configure puppet master and puppet db
require_puppet: true

## Dependencies

None.

## Example Playbook

    - hosts: servers
      vars_files:
        - vars/main.yml
      roles:
        - role: riponbanik.foreman 
          require_puppet: false

## License

MIT / BSD

## Author Information

This role was created in 2018 by [Ripon Banik ](https://www.linkedin.com/in/ripon-banik-79956b23/)

