# ansible-example1

This example demonstrates the ability of ansible to gather data from a group of nodes, parse the data and then launch python scripts locally to manipulate and store the date.

It does the following:

* Gathers output from "show ip int brief"
* Parses the output using textfsm
* Stores the data from each switch into csv files
* Adds the csv files into a workbook
