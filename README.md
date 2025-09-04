# ansible-install-tools

A set of Ansible playbooks for automated installation of DevOps tools

---
##  how to start

```bash
git clone https://github.com/tanyadream/ansible-install-tools.git
cd ansible-install-tools

# setup (inventory) та vars (group_vars)
how to add servers:
write all servers in hosts, run a playbook with limits, for example:
ansible-playbook -i inventory/hosts.ini playbook.yml --limit devops_nodes --forks 20
if you use dynamic inventory, you need to configure the server list, edit the dynamic_inventory.py 
ansible-playbook -i inventory/dynamic_inventory.py playbook.yml --limit devops_nodes --forks 20

# Run playbook
ansible-playbook -i inventory playbook.yml
