from neo4j import GraphDatabase

# Connection details

# ----------------------------------------------------------------------
NEO4J_URI = "bolt://localhost:7687"    # Or your remote address
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "liicornell.org"
# ----------------------------------------------------------------------


# Connect to the Neo4j instance
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

session = driver.session()

# Run SHOW DATABASES query
result = session.run("SHOW DATABASES")
print("Name\t\tStatus")
print("-" * 30)
for record in result:
    # Print database name and status
    print(f"{record['name']}\t\t{record['currentStatus']}")

# Close the driver when done
driver.close()