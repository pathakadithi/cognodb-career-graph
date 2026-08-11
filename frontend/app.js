const API = "https://cognodb-career-graph.onrender.com/api";
const CANDIDATE = "Adithi";


function createBadges(items) {
    if (!items || items.length === 0) {
        return "<span class='badge'>None</span>";
    }

    return items
        .map(item => `<span class="badge">${item}</span>`)
        .join("");
}


/* =========================
   Candidate
========================= */

async function loadCandidate() {

    const container = document.getElementById("candidate");

    try {

        const response = await fetch(
            `${API}/candidate/?name=${CANDIDATE}`
        );

        if (!response.ok) {
            throw new Error("Failed to load candidate");
        }

        const candidate = await response.json();

        container.innerHTML = `
            <h3>${candidate.name}</h3>

            <p>
                <strong>Experience:</strong>
                ${candidate.experience_level}
            </p>

            <p>
                <strong>Skills:</strong>
            </p>

            <div class="skills">
                ${createBadges(candidate.skills)}
            </div>
        `;

    } catch (error) {

        container.innerHTML = `
            <p class="loading">
                Unable to load candidate profile.
            </p>
        `;

        console.error("Candidate error:", error);
    }
}


/* =========================
   Job Matches
========================= */

async function loadJobMatches() {

    const container = document.getElementById("job-matches");

    try {

        const response = await fetch(
            `${API}/job-match/`
        );

        if (!response.ok) {
            throw new Error("Failed to load job matches");
        }

        const jobs = await response.json();

        container.innerHTML = "";

        jobs.forEach(job => {

            const card = document.createElement("div");

            card.className = "card";

            card.innerHTML = `
                <h3>${job.title}</h3>

                <p>
                    <strong>Company:</strong>
                    ${job.company}
                </p>

                <p>
                    <strong>Matched Skills:</strong>
                </p>

                <div class="skills">
                    ${createBadges(job.matched_skills)}
                </div>

                <p>
                    <strong>Required Skills:</strong>
                </p>

                <div class="skills">
                    ${createBadges(job.required_skills)}
                </div>

                <p class="match">
                    Match: ${job.match_percentage}%
                </p>
            `;

            container.appendChild(card);
        });

    } catch (error) {

        container.innerHTML = `
            <p class="loading">
                Unable to load job matches.
            </p>
        `;

        console.error("Job matches error:", error);
    }
}


/* =========================
   Skill Gaps
========================= */

async function loadSkillGaps() {

    const container = document.getElementById("skill-gaps");

    try {

        const response = await fetch(
            `${API}/skill-gaps/?candidate=${CANDIDATE}`
        );

        if (!response.ok) {
            throw new Error("Failed to load skill gaps");
        }

        const gaps = await response.json();

        container.innerHTML = "";

        gaps.forEach(job => {

            const card = document.createElement("div");

            card.className = "card";

            const hasMissingSkills =
                job.missing_skills &&
                job.missing_skills.length > 0;

            card.innerHTML = `
                <h3>${job.title}</h3>

                <p>
                    <strong>Company:</strong>
                    ${job.company}
                </p>

                <p>
                    <strong>Missing Skills:</strong>
                </p>

                <div class="skills">
                    ${
                        hasMissingSkills
                            ? job.missing_skills
                                .map(skill =>
                                    `<span class="badge missing">${skill}</span>`
                                )
                                .join("")
                            : `<span class="badge no-gap">No skill gap</span>`
                    }
                </div>
            `;

            container.appendChild(card);
        });

    } catch (error) {

        container.innerHTML = `
            <p class="loading">
                Unable to load skill gaps.
            </p>
        `;

        console.error("Skill gaps error:", error);
    }
}


/* =========================
   Projects
========================= */

async function loadProjects() {

    const container = document.getElementById("projects");

    try {

        const response = await fetch(
            `${API}/projects/`
        );

        if (!response.ok) {
            throw new Error("Failed to load projects");
        }

        const projects = await response.json();

        container.innerHTML = "";

        projects.forEach(project => {

            const card = document.createElement("div");

            card.className = "card project-card";

            card.innerHTML = `
                <h3>${project.name}</h3>

                <p>
                    <span class="label">Skills:</span>
                </p>

                <div class="skills">
                    ${createBadges(project.skills)}
                </div>

                <p>
                    <span class="label">Technologies:</span>
                </p>

                <div class="skills">
                    ${createBadges(project.technologies)}
                </div>
            `;

            container.appendChild(card);
        });

    } catch (error) {

        container.innerHTML = `
            <p class="loading">
                Unable to load projects.
            </p>
        `;

        console.error("Projects error:", error);
    }
}


/* =========================
   Load Dashboard
========================= */

loadCandidate();
loadJobMatches();
loadSkillGaps();
loadProjects();
