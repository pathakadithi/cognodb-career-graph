
from career.database import driver


def seed_database():
    with driver.session() as session:

        # -------------------------
        # Clear existing data
        # -------------------------
        session.run("MATCH (n) DETACH DELETE n")

        # -------------------------
        # Skills
        # -------------------------
        session.run("""
            CREATE
                (:Skill {name: 'Python'}),
                (:Skill {name: 'Django'}),
                (:Skill {name: 'SQL'}),
                (:Skill {name: 'PyTorch'}),
                (:Skill {name: 'Machine Learning'}),
                (:Skill {name: 'Docker'}),
                (:Skill {name: 'React'}),
                (:Skill {name: 'Git'})
        """)

        # -------------------------
        # Technologies
        # -------------------------
        session.run("""
            CREATE
                (:Technology {name: 'OpenCV'}),
                (:Technology {name: 'MediaPipe'}),
                (:Technology {name: 'TensorFlow'}),
                (:Technology {name: 'FastAPI'}),
                (:Technology {name: 'PostgreSQL'})
        """)

        # -------------------------
        # Candidate
        # -------------------------
        session.run("""
            CREATE (:Candidate {
                name: 'Adithi',
                experience_level: 'Fresher'
            })
        """)

        # -------------------------
        # Jobs
        # -------------------------
        session.run("""
            CREATE
                (:Job {
                    title: 'Machine Learning Engineer',
                    company: 'TechAI'
                }),
                (:Job {
                    title: 'Python Developer',
                    company: 'CloudSoft'
                }),
                (:Job {
                    title: 'Full Stack Developer',
                    company: 'WebWorks'
                })
        """)

        # -------------------------
        # Projects
        # -------------------------
        session.run("""
            CREATE
                (:Project {
                    name: 'Breast Cancer Detection System'
                }),
                (:Project {
                    name: 'Sign Language Recognition'
                }),
                (:Project {
                    name: 'Stock Prediction Portal'
                })
        """)

        # -------------------------
        # Candidate → Skills
        # -------------------------
        session.run("""
            MATCH (c:Candidate {name: 'Adithi'})
            MATCH (s:Skill)
            WHERE s.name IN [
                'Python',
                'SQL',
                'PyTorch',
                'Machine Learning',
                'Git',
                'Django',
                'React'
            ]
            CREATE (c)-[:HAS_SKILL]->(s)
        """)

        # -------------------------
        # Candidate → Projects
        # -------------------------
        session.run("""
            MATCH (c:Candidate {name: 'Adithi'})
            MATCH (p1:Project {name: 'Breast Cancer Detection System'})
            MATCH (p2:Project {name: 'Sign Language Recognition'})
            MATCH (p3:Project {name: 'Stock Prediction Portal'})

            CREATE
                (c)-[:BUILT]->(p1),
                (c)-[:BUILT]->(p2),
                (c)-[:BUILT]->(p3)
        """)

        # -------------------------
        # Project → Skills
        # -------------------------
        session.run("""
            MATCH (p:Project {name: 'Breast Cancer Detection System'})
            MATCH (s:Skill)
            WHERE s.name IN [
                'Python',
                'PyTorch',
                'Machine Learning'
            ]
            CREATE (p)-[:USES]->(s)
        """)

        session.run("""
            MATCH (p:Project {name: 'Sign Language Recognition'})
            MATCH (s:Skill)
            WHERE s.name IN [
                'Python',
                'PyTorch',
                'Machine Learning'
            ]
            CREATE (p)-[:USES]->(s)
        """)

        session.run("""
            MATCH (p:Project {name: 'Stock Prediction Portal'})
            MATCH (s:Skill)
            WHERE s.name IN [
                'Python',
                'Django',
                'React',
                'SQL'
            ]
            CREATE (p)-[:USES]->(s)
        """)

        # -------------------------
        # Project → Technologies
        # -------------------------
        session.run("""
            MATCH (p:Project {name: 'Breast Cancer Detection System'})
            MATCH (t:Technology {name: 'TensorFlow'})
            CREATE (p)-[:USES_TECHNOLOGY]->(t)
        """)

        session.run("""
            MATCH (p:Project {name: 'Sign Language Recognition'})
            MATCH (t:Technology)
            WHERE t.name IN [
                'OpenCV',
                'MediaPipe',
                'TensorFlow'
            ]
            CREATE (p)-[:USES_TECHNOLOGY]->(t)
        """)

        session.run("""
            MATCH (p:Project {name: 'Stock Prediction Portal'})
            MATCH (t:Technology)
            WHERE t.name IN [
                'PostgreSQL',
                'FastAPI'
            ]
            CREATE (p)-[:USES_TECHNOLOGY]->(t)
        """)

        # -------------------------
        # Job → Required Skills
        # -------------------------
        session.run("""
            MATCH (j:Job {title: 'Machine Learning Engineer'})
            MATCH (s:Skill)
            WHERE s.name IN [
                'Python',
                'PyTorch',
                'Machine Learning',
                'SQL',
                'Docker'
            ]
            CREATE (j)-[:REQUIRES]->(s)
        """)

        session.run("""
            MATCH (j:Job {title: 'Python Developer'})
            MATCH (s:Skill)
            WHERE s.name IN [
                'Python',
                'Django',
                'SQL',
                'Git',
                'Docker'
            ]
            CREATE (j)-[:REQUIRES]->(s)
        """)

        session.run("""
            MATCH (j:Job {title: 'Full Stack Developer'})
            MATCH (s:Skill)
            WHERE s.name IN [
                'Python',
                'Django',
                'React',
                'SQL',
                'Git'
            ]
            CREATE (j)-[:REQUIRES]->(s)
        """)

        print("Database seeded successfully!")


if __name__ == "__main__":
    seed_database()
