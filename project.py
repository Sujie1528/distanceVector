
import network_simulator

# Network 0
#
#
# E0
# | \
# |  \
# |7  \2
# |    \
# |     \
# E2 --- E1
#     1
#
network0 = [
    [(1, 2), (2, 7)],         # E0
    [(0, 2), (2, 1)],         # E1
    [(0, 7), (1, 1 )],        # E2
]

simulator = network_simulator.NetworkSimulator(network0, 499, 3)
simulator.run()
simulator.display_forwarding_table(0)
simulator.display_forwarding_table(1)
simulator.display_forwarding_table(2)
print(simulator.route_packet(0, 2))
print("Running ....") if input("Run next Simulation Y/N ") == "Y" else exit



# Network 1
#
#    1
# E0 --- E1
# | \    |
# |  \   |
# |7  \3 | 1
# |    \ |
# |     \|
# E3 --- E2
#     2
#
network1 = [
    [(1, 1), (2, 3), (3, 7)], # E0
    [(0, 1), (2, 1)],         # E1
    [(0, 3), (1, 1), (3, 2)], # E2
    [(0, 7), (2, 2)],         # E3
]

simulator = network_simulator.NetworkSimulator(network1, 499, 3)
simulator.run()
simulator.display_forwarding_table(0)
simulator.display_forwarding_table(1)
simulator.display_forwarding_table(2)
simulator.display_forwarding_table(3)
print(simulator.route_packet(0, 3))
print("Running ....") if input("Run next Simulation Y/N ") == "Y" else exit


# Network 2
#
#    1
# E0 --- E1
# | \    | \
# |  \   |  \
# |3  \4 | 4 |
# |    \ |   |
# |     \|   |
# E3     E2  / 1
#  \________/
#
network2 = [
    [(1, 1), (2, 4), (3, 3)], # E0
    [(0, 1), (2, 4), (3, 1)], # E1
    [(0, 4), (1, 4)],         # E2
    [(0, 3), (1, 1)],         # E3
]

simulator = network_simulator.NetworkSimulator(network2, 499, 3)

simulator.run()
simulator.display_forwarding_table(0)
simulator.display_forwarding_table(1)
simulator.display_forwarding_table(2)
print(simulator.route_packet(0, 3))
print("Running ....") if input("Run next Simulation Y/N ") == "Y" else exit


# Network 3
#
#     1      2
# E0 --- E1 --- E2
# | \    |      |
# |  \5  |3     |1
# |   \  |      |
# |3   \-E3     E4
# |            /
# E5 ---------/
#          8
#
network3 = [
    [(1, 1), (3, 5), (5, 3)], # E0
    [(0, 1), (2, 2), (3, 3)], # E1
    [(1, 2), (4, 1)],         # E2
    [(0, 5), (1, 3)],         # E3
    [(2, 1), (5, 8)],         # E4
    [(0, 3), (4, 8)],         # E5
]

simulator = network_simulator.NetworkSimulator(network3, 49, 1)

simulator.run()
simulator.display_forwarding_table(0)
simulator.display_forwarding_table(5)
simulator.display_forwarding_table(3)
print(simulator.route_packet(5, 3))
print("Running ....") if input("Run next Simulation Y/N ") == "Y" else exit


# Network 4
#
#     1                 5
# E0 --- E1         E4 --- E5
# |      |          /\   / |
# |      |3       4/ 1\ /2 |
# |2  8  |    1   /    X   |5
# |  /---E2 ---- E3---/ \  |
# | /-----------/        \-E6
# E7       6               |
#  \----------------------/
#              15
#
network4 = [
    [(1, 1), (7, 2)],                  # E0
    [(0, 1), (2, 3)],                  # E1
    [(1, 3), (3, 1), (7, 8)],          # E2
    [(2, 1), (4, 4), (5, 2), (7, 6)],  # E3
    [(3, 4), (5, 5), (6, 1)],          # E4
    [(3, 2), (4, 5), (6, 5)],          # E5
    [(4, 1), (5, 5), (7, 15)],         # E6
    [(0, 2), (2, 8), (3, 6), (6, 15)], # E7
]



simulator = network_simulator.NetworkSimulator(network4, 40, 1)

simulator.run()
simulator.display_forwarding_table(0)
simulator.display_forwarding_table(1)
simulator.display_forwarding_table(7)
print(simulator.route_packet(5, 7))
print("Running ....") if input("Run next Simulation Y/N ") == "Y" else exit
 


