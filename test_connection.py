from neo4j import GraphDatabase

URI = "bolt+s://db-e2b6270b.databases.cognodb.com"
USERNAME = "cognodb"
PASSWORD = "4ec252259f8900557da52a8aa1aafd90"

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD),
)

driver.verify_connectivity()

print("Connected to CognoDB successfully!")

driver.close()