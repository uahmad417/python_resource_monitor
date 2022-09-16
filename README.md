# Description

python_resource_monitor is a simple python utility that attempts to gives statistics about system resources. It uses the psutil module give statistics about system resources and esssentially acts as a clone of the standard UNIX utilities such as netstat, ifconfig, df and ps.

# Dependencies

This utility requires the psutil module. Install it by:

```bash
pip install psutil
```

Currently the module only works in Windows systems

# Usage

To see different resources supported by the utility, enter:

```bash
python monitory.py -h
```

To see extended help about a resource, enter:

```bash
python monitor.py [Resource] -h
```

For ex:

```bash
python monitory.py disk -h
```
