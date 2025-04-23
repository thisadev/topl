import graphviz

def generate_dfa_nfa_graphs():
    """Generates the DFA and NFA graph definitions."""

    # NFA Graph
    nfa_graph = {
        'states': ['q0', 'q1', 'q2', 'q3'],
        'alphabet': ['i', 'f', 'a-z'],
        'transitions': {
            'q0': {'i': ['q1']},
            'q1': {'f': ['q2'], 'a-z': ['q3']},
            'q2': {},
            'q3': {'a-z': ['q3']},
        },
        'start_state': 'q0',
        'accept_states': ['q2', 'q3']
    }

    # DFA Graph
    dfa_graph = {
        'states': ['A', 'B', 'C', 'D'],
        'alphabet': ['i', 'f', 'a-z'],
        'transitions': {
            'A': {'i': 'B', 'f': 'D', 'a-z': 'D'},
            'B': {'f': 'C', 'a-z': 'D'},
            'C': {},
            'D': {'i': 'D', 'f': 'D', 'a-z': 'D'}
        },
        'start_state': 'A',
        'accept_states': ['C', 'D']
    }

    return nfa_graph, dfa_graph

def create_graphviz_graph(graph_data, graph_type):
    """Creates a Graphviz graph object from the graph data."""

    dot = graphviz.Digraph(comment=f'{graph_type} Graph')
    dot.attr(rankdir='LR')  # Left-to-right layout

    for state in graph_data['states']:
        if state in graph_data['accept_states']:
            dot.node(state, shape='doublecircle')
        else:
            dot.node(state)

    dot.node(graph_data['start_state'], shape='circle', style='filled', fillcolor='lightblue') #mark start state

    for state, transitions in graph_data['transitions'].items():
        for symbol, next_states in transitions.items():
            if isinstance(next_states, list):  # NFA
                for next_state in next_states:
                    dot.edge(state, next_state, label=symbol)
            else:  # DFA
                dot.edge(state, next_states, label=symbol)

    return dot

def save_graph_as_image(dot, filename):
    """Saves the Graphviz graph as an image."""
    dot.render(filename, format='png', cleanup=True)
    print(f"Graph saved as {filename}.png")

if __name__ == "__main__":
    nfa_data, dfa_data = generate_dfa_nfa_graphs()

    nfa_dot = create_graphviz_graph(nfa_data, "NFA")
    save_graph_as_image(nfa_dot, "nfa_graph")

    dfa_dot = create_graphviz_graph(dfa_data, "DFA")
    save_graph_as_image(dfa_dot, "dfa_graph")
