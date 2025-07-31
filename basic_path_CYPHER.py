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

# exactly n hop paths that lead back to originating node (may include double travels)
def loopbacks(hyperlink, n):
    cypher = f"""
    MATCH (n)
    WHERE n.hlink = $hlink
    MATCH p = (n)-[*{n}]->(n)
    RETURN p
    """
    result = session.run(cypher, hlink=hyperlink)
    for record in result:
        print(record["p"])
    print()


# find orphans
def orphans():
    cypher = """
    MATCH (n)
    WHERE NOT (n)--()
    RETURN n"""

    result = session.run(cypher)
    for record in result:
        print(dict(record["n"]))
    print()

# ----------------------------------------------------------------------
# RUN
# ----------------------------------------------------------------------

# exactly 2 hop paths that lead back to originating node
hyperlink = "https://www.law.cornell.edu/constitution-conan/amendment-1/access-and-editorial-discretion-in-broadcast-media"
loopbacks(hyperlink, 2)

#find orphans
orphans()