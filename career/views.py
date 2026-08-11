from rest_framework.decorators import api_view
from rest_framework.response import Response

from .database import driver


@api_view(["GET"])
def health_check(request):
    try:
        driver.verify_connectivity()

        return Response({
            "status": "success",
            "message": "CognoDB connection successful"
        })

    except Exception as e:
        return Response({
            "status": "error",
            "message": str(e)
        }, status=500)


@api_view(["GET"])
def get_jobs(request):
    result = driver.execute_query(
        """
        MATCH (j:Job)
        RETURN j.title AS title, j.company AS company
        ORDER BY j.title
        """
    )

    jobs = []

    for record in result.records:
        jobs.append({
            "title": record["title"],
            "company": record["company"]
        })

    return Response(jobs)


@api_view(["GET"])
def job_match(request):
    candidate_name = request.GET.get("candidate", "Adithi")

    result = driver.execute_query(
        """
        MATCH (c:Candidate {name: $candidate_name})-[:HAS_SKILL]->(s:Skill)
        WITH c, collect(s.name) AS candidate_skills

        MATCH (j:Job)-[:REQUIRES]->(required:Skill)
        WITH
            j,
            candidate_skills,
            collect(required.name) AS required_skills

        WITH
            j,
            candidate_skills,
            required_skills,
            [skill IN required_skills
             WHERE skill IN candidate_skills] AS matched_skills

        RETURN
            j.title AS title,
            j.company AS company,
            matched_skills,
            required_skills
        ORDER BY size(matched_skills) DESC
        """,
        candidate_name=candidate_name
    )

    matches = []

    for record in result.records:
        matched_skills = record["matched_skills"]
        required_skills = record["required_skills"]

        match_percentage = (
            len(matched_skills) / len(required_skills) * 100
            if required_skills
            else 0
        )

        matches.append({
            "title": record["title"],
            "company": record["company"],
            "matched_skills": matched_skills,
            "required_skills": required_skills,
            "match_percentage": round(match_percentage, 2)
        })

    return Response(matches)


@api_view(["GET"])
def skill_gaps(request):
    candidate_name = request.GET.get("candidate", "Adithi")

    result = driver.execute_query(
        """
        MATCH (c:Candidate {name: $candidate_name})-[:HAS_SKILL]->(s:Skill)
        WITH c, collect(s.name) AS candidate_skills

        MATCH (j:Job)-[:REQUIRES]->(required:Skill)
        WITH
            j,
            candidate_skills,
            collect(required.name) AS required_skills

        WITH
            j,
            [skill IN required_skills
             WHERE NOT skill IN candidate_skills] AS missing_skills

        RETURN
            j.title AS title,
            j.company AS company,
            missing_skills
        ORDER BY size(missing_skills)
        """,
        candidate_name=candidate_name
    )

    gaps = []

    for record in result.records:
        gaps.append({
            "title": record["title"],
            "company": record["company"],
            "missing_skills": record["missing_skills"]
        })

    return Response(gaps)


@api_view(["GET"])
def get_projects(request):
    candidate_name = request.GET.get("candidate", "Adithi")

    result = driver.execute_query(
        """
        MATCH (c:Candidate {name: $candidate_name})-[:BUILT]->(p:Project)

        OPTIONAL MATCH (p)-[:USES]->(s:Skill)
        OPTIONAL MATCH (p)-[:USES_TECHNOLOGY]->(t:Technology)

        RETURN
            p.name AS name,
            collect(DISTINCT s.name) AS skills,
            collect(DISTINCT t.name) AS technologies

        ORDER BY p.name
        """,
        candidate_name=candidate_name
    )

    projects = []

    for record in result.records:
        projects.append({
            "name": record["name"],
            "skills": record["skills"],
            "technologies": record["technologies"]
        })

    return Response(projects)


@api_view(["GET"])
def career_profile(request):
    candidate_name = request.GET.get("candidate", "Adithi")

    result = driver.execute_query(
        """
        MATCH (c:Candidate {name: $candidate_name})

        OPTIONAL MATCH (c)-[:HAS_SKILL]->(s:Skill)

        OPTIONAL MATCH (c)-[:BUILT]->(p:Project)
        OPTIONAL MATCH (p)-[:USES]->(ps:Skill)
        OPTIONAL MATCH (p)-[:USES_TECHNOLOGY]->(t:Technology)

        RETURN
            c.name AS name,
            c.experience_level AS experience_level,
            collect(DISTINCT s.name) AS skills,
            collect(DISTINCT {
                name: p.name,
                skills: ps.name,
                technology: t.name
            }) AS projects
        """,
        candidate_name=candidate_name
    )

    if not result.records:
        return Response(
            {"error": "Candidate not found"},
            status=404
        )

    record = result.records[0]

    projects_data = {}

    for project in record["projects"]:
        if project["name"] is None:
            continue

        project_name = project["name"]

        if project_name not in projects_data:
            projects_data[project_name] = {
                "name": project_name,
                "skills": [],
                "technologies": []
            }

        if project["skills"] and project["skills"] not in projects_data[project_name]["skills"]:
            projects_data[project_name]["skills"].append(project["skills"])

        if project["technology"] and project["technology"] not in projects_data[project_name]["technologies"]:
            projects_data[project_name]["technologies"].append(project["technology"])

    return Response({
        "name": record["name"],
        "experience_level": record["experience_level"],
        "skills": record["skills"],
        "projects": list(projects_data.values())
    })

@api_view(["GET"])
def candidate_profile(request):
    candidate_name = request.GET.get("name", "Adithi")

    result = driver.execute_query(
        """
        MATCH (c:Candidate {name: $candidate_name})
        OPTIONAL MATCH (c)-[:HAS_SKILL]->(s:Skill)

        RETURN
            c.name AS name,
            c.experience_level AS experience_level,
            collect(s.name) AS skills
        """,
        candidate_name=candidate_name
    )

    if not result.records:
        return Response(
            {"error": "Candidate not found"},
            status=404
        )

    record = result.records[0]

    return Response({
        "name": record["name"],
        "experience_level": record["experience_level"],
        "skills": record["skills"]
    })