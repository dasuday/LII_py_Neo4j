from neo4j import GraphDatabase

# ----------------------------------------------------------------------
# Database parameters
# ----------------------------------------------------------------------
NEO4J_URI = "bolt://localhost:7687"  
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "liicornell.org"
DATABASE = "liilinks"    
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Connection and session setup
# ----------------------------------------------------------------------
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

session = driver.session(database=DATABASE)

# ----------------------------------------------------------------------
# BUILD QUERIES
# ----------------------------------------------------------------------

# Count all nodes
def print_nodes_count():
    result = session.run("MATCH (n) RETURN count(n) AS node_count")
    count = result.single()["node_count"]
    print(f"Total nodes in database '{DATABASE}': {count}")
    print()

# print n nodes
def print_n_nodes(n):
    result = session.run("MATCH (n) RETURN n LIMIT " + str(n))

    print("First " + str(n) + " nodes in database '" + DATABASE + "':")
    for record in result:
        # Print the properties of each node
        node = record["n"]
        print(dict(node))  # or just print(node) for the whole Node object
        print()

# Look for a specific node by hlink

def find_node_by_hlink(hyperlink):
    cypher = """
    MATCH (n)
    WHERE n.hlink = $hlink
    RETURN n
    """
    result = session.run(cypher, hlink=hyperlink)
    for record in result:
        print(dict(record["n"]))
    print()

# ----------------------------------------------------------------------
# RUN
# ----------------------------------------------------------------------

# print n nodes; example call with n=10
print_n_nodes(10)

# Count all nodes
print_nodes_count()

# Look for a specific node by hlink
hlink = "https://www.law.cornell.edu/constitution-conan/amendment-1/access-and-editorial-discretion-in-broadcast-media"
find_node_by_hlink(hlink)

driver.close()