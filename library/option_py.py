#!/usr/bin/env python3
from ansible.module_utils.basic import *

def main():
    module = AnsibleModule(
        argument_spec = dict(
            size=dict(required=False, type='str'), 
            filepath=dict(required=True, type='str') 
        )
    )
    rc, stdout, stderr = module.run_command("ls /")
    changed = False

    if True:
        module.exit_json(changed=changed, 
            rc=1, stdout=stdout, stderr=stderr, msg="unko")
    else:
        module.fail_json(changed=True, msg="unko")

main()

