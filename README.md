# Smart Hunter Notes
"Smart Hunter Notes" is a web-based application designed to be a high-performance "Hunter Notes" system for Monster Hunter World, replicating the in-game aesthetic with modern Single Page Application (SPA) functionality.

## Project Overview
The project aims to provide an interactive and visually authentic experience for Monster Hunter World players, offering detailed information about monsters, their physiology, and rewards. It leverages modern web technologies for a responsive and dynamic user interface, while incorporating AI capabilities for enhanced user interaction.

## Technical Stack
* **Frontend:** Svelte + Tailwind CSS
* **Backend:** Golang (API), PostgreSQL (Persistent Data), Redis (Caching/Session Store)
* **AI/Orchestration:** Python (**FastAPI**) for image recognition (identifying monsters from screenshots to auto-navigate) and agentic workflow management.
* **DevOps:** Docker, GitHub CI/CD

## Key Features Implemented (Initial Skeleton)
* **SvelteKit Project Structure:** A foundational SvelteKit application is set up with TypeScript, Tailwind CSS, and Prettier.
* **Page Flip Transition:** A basic page-flip animation is implemented for route changes, providing a visual transition between different views.
* **Monster Data Display:** The application can fetch and display a list of monsters from `monsters.json`, complete with their names, types, and associated icons.
* **Basic Routing:** Navigation between the main monster list and individual monster detail pages is established, allowing users to view detailed information for each monster.
* **Golang API Placeholder:** A basic Go HTTP server is set up with placeholder endpoints (`/api/hello`, `/api/monsters`). This serves as the main backend structure.
* **Python AI Service Placeholder:** A basic **FastAPI** application is set up with an endpoint `/identify-monster` that simulates image recognition (currently returns a dummy monster name). This serves as the initial structure for integrating the Agno AI vision feature.

## Getting Started###Frontend (SvelteKit)
**Prerequisite:** Ensure the **Backend (Golang API)** is running before starting the frontend.

1. Navigate to the `hunter-notes-frontend` directory:
```bash
cd hunter-notes-frontend
```

2. Install dependencies:
```bash
npm install

```

3. Run the development server:
```bash
npm run dev -- --open

```

The application should open in your browser, displaying the monster list, with data fetched from the Go API.

### Backend (Golang API)

1. Navigate to the `hunter-notes-backend-go` directory:
```bash
cd hunter-notes-backend-go

```

2. Run the Go application:
```bash
go run main.go

```

The Go API will run on `http://localhost:8080`, serving monster data to the frontend.

### AI Service (Python)
1. Navigate to the `hunter-notes-ai-service` directory:
```bash
cd hunter-notes-ai-service

```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate

```

3. Install dependencies:
```bash
pip install -r requirements.txt

```

4. Run the **FastAPI** application using Uvicorn (assuming `app.py` is the main file):
```bash
uvicorn app:app --reload --port 5001

```

The Python AI service will run on `http://localhost:5001`. You can test the `/identify-monster` endpoint with a POST request containing an image file.

## Next Steps
* Refine the UI/UX to precisely match the Monster Hunter World aesthetic (parchment textures, serif fonts, rustic borders).
* Implement interactive physiology on monster detail pages, highlighting drop rates on specific part clicks.
* Integrate actual image recognition logic into the Python (Agno) service.
* Develop the Golang API backend to serve monster data from PostgreSQL, and integrate with Redis for caching.
* Set up PostgreSQL and Redis databases.
* Design and implement the "Build Recommender" backend architecture.