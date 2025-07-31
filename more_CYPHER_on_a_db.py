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

# top 10 nodes by indegree
def top_10_by_indegree():
    cypher = """
    MATCH (n)
    WITH n, COUNT { MATCH ()-->(n) } AS indegree
    ORDER BY indegree DESC
    LIMIT 10
    RETURN n, indegree
    """
    result = session.run(cypher)
    for record in result:
        node = record["n"]
        indegree = record["indegree"]
        print(f"Node: {dict(node)}  |  Indegree: {indegree}")
    print()

# top 10 nodes by outdegree
def top_10_by_outdegree():
    cypher = """
    MATCH (n)
    WITH n, COUNT { MATCH (n)-->() } AS outdegree
    ORDER BY outdegree DESC
    LIMIT 10
    RETURN n, outdegree
    """
    result = session.run(cypher)
    for record in result:
        node = record["n"]
        outdegree = record["outdegree"]
        print(f"Node: {dict(node)}  |  Outdegree: {outdegree}")
    print()


# ----------------------------------------------------------------------
# RUN
# ----------------------------------------------------------------------

top_10_by_indegree()
top_10_by_outdegree()

driver.close()