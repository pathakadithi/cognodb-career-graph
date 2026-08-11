from django.urls import path

from .views import (
    health_check,
    get_jobs,
    job_match,
    skill_gaps,
    get_projects,
    career_profile,
    candidate_profile
)


urlpatterns = [
    path("health/", health_check),
    path("jobs/", get_jobs),
    path("job-match/", job_match),
    path("skill-gaps/", skill_gaps),
    path("projects/", get_projects),
    path("career-profile/", career_profile),
    path("candidate/", candidate_profile),
]