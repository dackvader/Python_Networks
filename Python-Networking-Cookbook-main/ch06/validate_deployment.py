import napalm

driver = napalm.get_network_driver("ios")

conn_details = {
    "hostname" : '<insert host>',
    "username" : '<insert user>',
    "password" : '<insert password>',
    "optional_args": {
        "port": 22 # change if your port is different
    }
}

device = driver(**conn_details)
device.open()
out = device.compliance_report("compliance.yaml")
print(out)
device.close()
