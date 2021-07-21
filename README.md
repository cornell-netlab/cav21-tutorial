# Introduction

This repository contains source code for the demos used in the P4 Verification Tutorial presented by Nate Foster at CAV '21.

# Overview

There are four directories:

* [learning](learning): contains Python code for an SDN controller (`controller.py`) that implements a standard Ethernet learning application, as well as accompanying P4 code for the data plane (`learning.p4`).

* [source_routing](source_routing): contains P4 code for a data plane (`source_routing.p4`) that implements source routing, as well as Python scripts for sending (`send.py`) and receiving (`receive.py`) packets with source routing headers.

* [traffic_matrix](traffic_matrix): contains Python code for an SDN controller (`controller.py`) that implements a newtork monitoring application that collects a traffic matrix, as well as accompanying P4 code for the data plane (`monitoring.p4`).

* [verification](verification): contains P4 code (`nat.p4`) for a data plane that implements an access control list and network address translation, as well as an accompanying symbolic control plane interface (`nat.p4a`). Note that the P4 code is in an older dialect of the language, P4_14.

# Running the code

To run the first three examples, you will need a version of Petr4 that can interact with Linux network interfaces, as well as scripts for running Petr4 in Mininet. Development versions can be found on the `mininet-interface` branch of the [Petr4](https://github.com/cornell-netlab/petr4) repository. The fourth example requires `p4v` which is proprietary software developed by Barefoot Networks, an Intel company. 

# Credits

This code draws on material developed by the Petr4 and p4v research teams as well as the [P4.org tutorials repository](https://github.com/p4lang/p4) repository. Mina Tahmasbi Arashloo and Samwise Parkinson collaborated on the development of these exercises.



