'''
Code for an entity in the network. This is where you should implement the
distance-vector algorithm.
'''

from packet import Packet

class Entity:
    '''
    Entity that represents a node in the network.

    Each function should be implemented so that the Entity can be instantiated
    multiple times and successfully run a distance-vector routing algorithm.
    '''

    def __init__(self, entity_index, number_entities):
        '''
        This initialization function will be called at the beginning of the
        simulation to setup all entities.

        Arguments:
        - `entity_index`:    The id of this entity.
        - `number_entities`: Number of total entities in the network.

        Return Value: None.
        '''
        # Save state
        self.index = entity_index
        self.number_of_entities = number_entities

    def initialize_costs(self, neighbor_costs):
        '''
        This function will be called at the beginning of the simulation to
        provide a list of neighbors and the costs on those one-hop links.

        Arguments:
        - `neighbor_costs`:  Array of (entity_index, cost) tuples for
                             one-hop neighbors of this entity in this network.

        Return Value: This function should return an array of `Packet`s to be
        sent from this entity (if any) to neighboring entities.
        '''
        self.neighbors = [x[0] for x in neighbor_costs]
        vector = [999] * self.number_of_entities
        vector[self.index] = 0
        
        for link in neighbor_costs:
            vector[link[0]] = link[1]
            
        self.vector = vector
        
        packets = []    
        next_hop = [0] * self.number_of_entities
        next_hop[self.index] = self.index
        
        for neighbor in self.neighbors:
            next_hop[neighbor] = neighbor
            packets.append(Packet(neighbor, vector))
            
        self.next_hop = next_hop
            
        return packets

    def update(self, packet):
        '''
        This function is called when a packet arrives for this entity.

        Arguments:
        - `packet`: The incoming packet of type `Packet`.

        Return Value: This function should return an array of `Packet`s to be
        sent from this entity (if any) to neighboring entities.
        '''
        packets = []
        updated = False
        new_info = [x + self.vector[packet.get_source()] for x in packet.get_costs()]
        for i in range(self.number_of_entities):
            if  new_info[i] < self.vector[i]:
                self.vector[i] = new_info[i]
                self.next_hop[i] = packet.get_source()
                updated = True
                
        if updated:
            for neighbor in self.neighbors:
                packets.append(Packet(neighbor, self.vector))
            
        return packets
        

    def get_all_costs(self):
        '''
        This function is used by the simulator to retrieve the calculated routes
        and costs from an entity. This is most useful at the end of the
        simulation to collect the resulting routing state.

        Return Value: This function should return an array of (next_hop, cost)
        tuples for _every_ entity in the network based on the entity's current
        understanding of those costs. The array should be sorted such that the
        first element of the array is the next hop and cost to entity index 0,
        second element is to entity index 1, etc.
        '''
        hop_cost = [(0,0)] * self.number_of_entities
        for i in range(self.number_of_entities):
            hop_cost[i] = (self.next_hop[i], self.vector[i])
        return hop_cost

    def forward_next_hop(self, destination):
        '''
        Return the best next hop for a packet with the given destination.

        Arguments:
        - `destination`: The final destination of the packet.

        Return Value: The index of the best neighboring entity to use as the
        next hop.
        '''
        return self.next_hop[destination]
