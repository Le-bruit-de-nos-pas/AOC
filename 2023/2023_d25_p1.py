
import networkx as nx


def main():
  with open('input.txt') as f:
    lines = f.read().splitlines()

  g = nx.Graph()

  for line in lines:
    left , right = line.split(":")
    for node in right.strip().split():
      g.add_edge(left, node)
      g.add_edge(node, left)

  
  g.remove_edges_from(nx.minimum_edge_cut(g))
  a, b = nx.connected_components(g) 
  
  print(len(a) * len(b))


if __name__ == "__main__":
    main()
