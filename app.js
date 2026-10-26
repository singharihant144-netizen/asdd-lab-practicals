const labs = [
  {
    n: "01", title: "Jira Agile", tag: "PROJECT MANAGEMENT", color: "peach", icon: "▦",
    aim: "Create a Scrum project, add work items, plan a sprint, and track tasks on a Jira board.",
    before: "Browser, internet, and an Atlassian/Jira account. Templates and labels may vary.",
    steps: [
      ["Sign in", "Open atlassian.com/software/jira and sign in or create an account."],
      ["Create a project", "Choose Create project and select Scrum / Software Development if offered."],
      ["Name it", "Use ASDD Scrum Demo, choose an available project type, and create it."],
      ["Add work items", "In Backlog, create the College Recommendation App epic and tasks such as Prepare college data, Create login page, and Test recommendations. If Epics are unavailable, use regular tasks."],
      ["Plan a sprint", "Move at least two tasks into a sprint. Set a short duration and goal; start the sprint if permitted."],
      ["Update the board", "Move one task from To Do to In Progress, then Done."],
      ["Verify", "Confirm tasks and statuses appear on the board or backlog."]
    ],
    success: "A Jira project exists, work items are visible, and board columns show their current statuses.",
    errors: [["No Scrum template", "Choose the closest available project template; screen labels may differ."],["Cannot start sprint", "Add at least one work item and check project permissions."],["Don't see CI/CD", "A repository and workflow must be connected separately; don't claim the integration until it is."]],
    keywords: "jira agile scrum project board backlog sprint issue task epic template status to do"
  },
  {
    n: "02", title: "Git version control", tag: "SAVE YOUR PROGRESS", color: "lilac", icon: "⌘",
    aim: "Initialize a Git repository, stage and commit files, create a feature branch, and merge it into main.",
    before: "Install Git from git-scm.com/downloads. Replace the sample commit name and email with your own.",
    steps: [
      ["Check Git", "Run the version command.", "git --version"],
      ["Set your identity", "Use your own details for commits.", "git config --global user.name \"Your Name\"\ngit config --global user.email \"you@example.com\""],
      ["Create a folder", "Run in PowerShell.", "mkdir git-practical\ncd git-practical"],
      ["Make a sample file", "Create README.md, or run:", "Set-Content README.md \"Git practical demo\""],
      ["Initialize", "Start the repository and inspect it.", "git init\ngit status"],
      ["Stage and commit", "Save the first snapshot.", "git add README.md\ngit commit -m \"Initial commit\""],
      ["Set main and branch", "Rename the default branch, then create a feature branch.", "git branch -M main\ngit switch -c feature"],
      ["Make a feature change", "Add a line to README.md and save a second commit.", "Add-Content README.md \"Feature branch change\"\ngit add README.md\ngit commit -m \"Add feature change\""],
      ["Merge and verify", "Merge the feature into main and inspect the history.", "git switch main\ngit merge feature\nGet-Content README.md\ngit status\ngit log --oneline --graph --all"]
    ],
    success: "README.md contains both lines, git status reports a clean working tree, and history shows both commits.",
    errors: [["Author identity unknown", "Repeat the configuration step with a valid name and email."],["File not found", "Confirm the file name and current folder."],["Nothing to commit", "Make a real change before staging."],["git switch unavailable", "On older Git versions, use git checkout equivalents."]],
    keywords: "git version control repository commit branch merge push pull config identity author file stage status nothing to commit"
  },
  {
    n: "03", title: "GitHub Actions CI", tag: "AUTOMATE THE CHECKS", color: "mint", icon: "↗",
    aim: "Run a workflow automatically whenever code is pushed to main.",
    before: "Git, VS Code, and a GitHub account. Create an empty repository called CI-Demo; replace OWNER with your username.",
    steps: [
      ["Create the repository", "Create CI-Demo on GitHub."],
      ["Clone it", "Copy the repository URL and run:", "git clone https://github.com/OWNER/CI-Demo.git\ncd CI-Demo"],
      ["Create a sample", "Create hello.txt containing: Hello Continuous Integration."],
      ["Add the workflow file", "Create .github/workflows/ci.yml. Check that it is not accidentally named ci.yml.txt."],
      ["Paste this workflow", "Use spaces for indentation, not tabs.", "name: CI Demo\non:\n  push:\n    branches: [main]\n  pull_request:\n    branches: [main]\njobs:\n  verify:\n    runs-on: ubuntu-latest\n    steps:\n      - name: Check out repository\n        uses: actions/checkout@v4\n      - name: Confirm CI ran\n        run: |\n          echo \"Continuous Integration Pipeline Executed Successfully\"\n          ls -la"],
      ["Commit and push", "Run from the repository folder.", "git add .\ngit commit -m \"Add CI workflow\"\ngit branch -M main\ngit push -u origin main"],
      ["Verify", "Open repository → Actions → latest run and wait for completion."]
    ],
    success: "The workflow finishes with a green check and logs Continuous Integration Pipeline Executed Successfully.",
    errors: [["Workflow missing", "Verify the exact .github/workflows/ci.yml path and commit it."],["Push rejected", "Use an empty repository or pull remote changes before pushing."],["Red X", "Inspect the first failing step and YAML indentation."]],
    keywords: "github actions workflow ci continuous integration yaml yml red x green check push rejected branch main checkout"
  },
  {
    n: "04", title: "Docker a Python app", tag: "IN A CONTAINER", color: "blue", icon: "⬡",
    aim: "Build a Docker image and run a simple Python program inside a container.",
    before: "Install Docker Desktop and wait until its engine is running.",
    steps: [
      ["Create a folder", "Create and open docker-practical in VS Code.", "mkdir docker-practical\ncd docker-practical"],
      ["Create app.py", "Paste this one-line program:", "print(\"Hello from Docker!\")"],
      ["Create Dockerfile", "Name it Dockerfile with no extension.", "FROM python:3.11-slim\nWORKDIR /app\nCOPY app.py .\nCMD [\"python\", \"app.py\"]"],
      ["Check Docker", "Confirm the client and engine are available.", "docker --version\ndocker info"],
      ["Build the image", "Run from the folder containing Dockerfile. The final dot is required.", "docker build -t myapp ."],
      ["Verify and run", "Check that myapp exists, then launch a temporary container.", "docker images\ndocker run --rm myapp"]
    ],
    success: "The image list contains myapp and the container prints: Hello from Docker!",
    errors: [["docker not recognized", "Install Docker Desktop and reopen the terminal."],["Engine unavailable", "Start Docker Desktop and wait for it to be ready."],["Can't download the image", "Check internet or proxy access and retry."],["Virtualization prompt", "Enable virtualization / WSL 2 using Docker's official setup instructions."]],
    keywords: "docker python container image build run engine desktop dockerfile virtualization wsl2 hello"
  },
  {
    n: "05", title: "Docker Compose", tag: "TWO SERVICES, ONE COMMAND", color: "yellow", icon: "▤",
    aim: "Run an Nginx web service and a Redis service together using Docker Compose.",
    before: "Docker Desktop must be running. Use the modern docker compose command.",
    steps: [
      ["Create this structure", "Inside docker-compose-demo, create the app folder and files.", "docker-compose-demo/\n  app/\n    index.html\n    Dockerfile\n  docker-compose.yml"],
      ["Create app/index.html", "Use this page content.", "<!DOCTYPE html>\n<html><head><title>Docker Compose</title></head><body>\n<h1>Hello Students!</h1>\n<p>Web service is running successfully.</p>\n<p>This application is deployed using Docker Compose.</p>\n</body></html>"],
      ["Create app/Dockerfile", "Build the Nginx page.", "FROM nginx:alpine\nCOPY index.html /usr/share/nginx/html/index.html"],
      ["Create docker-compose.yml", "Indent with spaces. Redis is a separate service; this page does not query Redis.", "services:\n  web:\n    build: ./app\n    ports:\n      - \"8080:80\"\n  redis:\n    image: redis:7-alpine"],
      ["Start and inspect", "Run inside docker-compose-demo.", "docker compose up --build -d\ndocker compose ps"],
      ["Open and stop", "Visit localhost:8080. After verification, stop both services.", "docker compose down"]
    ],
    success: "The page displays Hello Students!, Web service is running successfully, and This application is deployed using Docker Compose. Both services run.",
    errors: [["Browser page unavailable", "Check docker compose ps and docker compose logs web. Make sure port 8080 is free."],["YAML error", "Use spaces and indent both services under services:."],["Redis not visible on page", "Redis runs separately; the sample webpage does not query Redis."],["Where is the page?", "Open http://localhost:8080."]],
    keywords: "docker compose redis nginx localhost 8080 page port yaml compose up down ps services web"
  },
  {
    n: "06", title: "Kubernetes", tag: "DEPLOY · SCALE · DELETE", color: "pink", icon: "◉",
    aim: "Deploy two Nginx Pods, scale the deployment to three, verify it, and delete it.",
    before: "Install Docker Desktop, Minikube, and kubectl from official sources. Start Docker Desktop first.",
    steps: [
      ["Start the cluster", "Run Minikube, then check that the node becomes Ready.", "minikube start\nkubectl get nodes"],
      ["Create deployment.yaml", "Save this manifest.", "apiVersion: apps/v1\nkind: Deployment\nmetadata:\n  name: myapp\nspec:\n  replicas: 2\n  selector:\n    matchLabels:\n      app: myapp\n  template:\n    metadata:\n      labels:\n        app: myapp\n    spec:\n      containers:\n        - name: nginx\n          image: nginx:stable\n          ports:\n            - containerPort: 80"],
      ["Apply and check Pods", "Run from the folder containing deployment.yaml. Wait for two Pods to show Running.", "kubectl apply -f deployment.yaml\nkubectl get pods"],
      ["Scale to three", "Check the deployment and Pods again.", "kubectl scale deployment myapp --replicas=3\nkubectl get deployment myapp\nkubectl get pods"],
      ["Delete and verify", "After recording results, remove the deployment. Its managed Pods are removed too.", "kubectl delete deployment myapp\nkubectl get deployments"]
    ],
    success: "The node reports Ready; two Pods become Running, then three after scaling. After deletion, myapp is no longer listed.",
    errors: [["Minikube fails", "Check Docker Desktop and virtualization; inspect the error message."],["Pods stay Pending", "Run kubectl describe pod POD_NAME and inspect the Events at the bottom. Check cluster resources and whether the image can be pulled."],["ImagePullBackOff", "Check internet and run kubectl describe pod POD_NAME to see the image pull error."],["Resource not found", "Check spelling and run kubectl get deployments / kubectl get pods."],["What does delete remove?", "Deleting the Deployment removes its managed Pods too."]],
    keywords: "kubernetes kubectl minikube pod pods deployment scale nginx ready imagepullbackoff not found delete replicas"
  },
  {
    n: "07", title: "Flask CI/CD", tag: "TEST THEN DEPLOY", color: "lavender", icon: "⚗",
    aim: "Create a Flask app, run pytest automatically on pushes to main, and define a deployment job that runs only after tests pass.",
    before: "GitHub-hosted runners can run tests. Remote deployment needs a Linux server you control, configured SSH secrets, and a prepared service.",
    steps: [
      ["Create project files", "Make my-flask-app with app.py, requirements.txt, test_app.py, and .gitignore."],
      ["Write app.py", "Paste this app.", "from flask import Flask\napp = Flask(__name__)\n\n@app.route(\"/\")\ndef home():\n    return \"Hello! Application deployed automatically using GitHub Actions.\"\n\nif __name__ == \"__main__\":\n    app.run()"],
      ["Add requirements", "In requirements.txt:", "Flask\npytest\nwaitress"],
      ["Add the test", "In test_app.py:", "from app import app\n\ndef test_home():\n    client = app.test_client()\n    response = client.get(\"/\")\n    assert response.status_code == 200\n    assert b\"Hello\" in response.data"],
      ["Add .gitignore", "Exclude generated and private files.", ".venv/\n__pycache__/\n.pytest_cache/\n.env"],
      ["Install and test locally", "In PowerShell:", "py -m venv .venv\n.venv\\Scripts\\Activate.ps1\npython -m pip install --upgrade pip\npip install -r requirements.txt\npytest -q"],
      ["Create and push the repository", "Create an empty GitHub repository, replace OWNER, then push the app.", "git init\ngit add .\ngit commit -m \"Initial Flask app and tests\"\ngit branch -M main\ngit remote add origin https://github.com/OWNER/my-flask-app.git\ngit push -u origin main"],
      ["Add deploy workflow", "Create .github/workflows/deploy.yml. Tests run first; deployment runs only for a push to main after tests pass. Requires a prepared server and secrets.", "name: Flask CI-CD\non:\n  push:\n    branches: [main]\n  pull_request:\n    branches: [main]\njobs:\n  test:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - uses: actions/setup-python@v5\n        with:\n          python-version: \"3.12\"\n      - run: |\n          python -m pip install --upgrade pip\n          pip install -r requirements.txt\n      - run: pytest -q\n  deploy:\n    needs: test\n    if: github.event_name == 'push' && github.ref == 'refs/heads/main'\n    runs-on: ubuntu-latest\n    steps:\n      - name: Deploy to configured Linux server\n        env:\n          SERVER_HOST: ${{ secrets.SERVER_HOST }}\n          SERVER_USERNAME: ${{ secrets.SERVER_USERNAME }}\n          SERVER_SSH_KEY: ${{ secrets.SERVER_SSH_KEY }}\n        run: |\n          test -n \"$SERVER_HOST\"\n          test -n \"$SERVER_USERNAME\"\n          test -n \"$SERVER_SSH_KEY\"\n          mkdir -p ~/.ssh\n          printf '%s\\n' \"$SERVER_SSH_KEY\" > ~/.ssh/id_key\n          chmod 600 ~/.ssh/id_key\n          ssh -i ~/.ssh/id_key -o StrictHostKeyChecking=accept-new \\\n            \"$SERVER_USERNAME@$SERVER_HOST\" \\\n            'cd /opt/my-flask-app && git pull origin main && python3 -m pip install -r requirements.txt && sudo systemctl restart my-flask-app'"],
      ["Add server secrets safely", "If using a server, open repository Settings → Secrets and variables → Actions. Add SERVER_HOST, SERVER_USERNAME, SERVER_SSH_KEY. Never put secrets in source code."],
      ["Push and verify", "Commit the workflow, push to main, and open GitHub → Actions."]
    ],
    success: "Locally, pytest -q should report one test passed. GitHub Actions tests should pass. Deployment is only claimed when a real prepared server and valid secrets are configured.",
    errors: [["ModuleNotFoundError", "Activate the intended environment and install requirements.txt."],["pytest can't find tests", "Run pytest from the project root."],["Workflow error", "Check .github/workflows/deploy.yml and YAML indentation."],["SSH failure", "Verify host, username, key, server path, and service. Never expose secrets."],["Need local Windows server?", "Run waitress-serve --host=127.0.0.1 --port=5000 app:app, then open http://127.0.0.1:5000."]],
    keywords: "flask pytest ci cd actions deploy ssh secrets server requirements waitress tests module not found"
  }
];

const escapeHtml = (s) => String(s).replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;","'":"&#39;"}[c]));
const grid = document.querySelector("#lab-grid");
grid.innerHTML = labs.map((lab, i) => `<article class="lab-card ${lab.color} reveal" style="--i:${i}">
  <button class="card-main" aria-expanded="false" aria-controls="detail-${lab.n}">
    <div class="card-top"><span class="card-number">${lab.n} / 07</span><span class="card-icon">${lab.icon}</span></div>
    <div class="card-tag">${lab.tag}</div><h3>${lab.title}</h3><p>${lab.aim}</p><div class="card-bottom"><span>OPEN PRACTICAL</span><span class="card-arrow">↗</span></div>
  </button>
  <div class="lab-detail" id="detail-${lab.n}" hidden>
    <div class="detail-heading"><span class="section-index">[ PRACTICAL ${lab.n} ]</span><h4>What you’ll do</h4><p>${lab.aim}</p></div>
    <div class="detail-before"><b>BEFORE YOU START</b><p>${lab.before}</p></div>
    <div class="steps-list">${lab.steps.map(([head, desc, code], n) => `<div class="step"><span class="step-num">${String(n + 1).padStart(2,"0")}</span><div><h5>${escapeHtml(head)}</h5><p>${escapeHtml(desc)}</p>${code ? `<pre><code>${escapeHtml(code)}</code></pre>` : ""}</div></div>`).join("")}</div>
    <div class="expected"><span>✓ EXPECTED RESULT</span><p>${lab.success}</p></div>
    <div class="fixes"><h5>When something goes wrong</h5>${lab.errors.map(([h, d]) => `<p><b>${escapeHtml(h)}:</b> ${escapeHtml(d)}</p>`).join("")}</div>
    <a class="detail-source" href="asdd-hack-aa2.docx" download>Save the full original guide ↘</a>
  </div>
</article>`).join("");

document.querySelectorAll(".card-main").forEach(button => button.addEventListener("click", () => {
  const detail = document.getElementById(button.getAttribute("aria-controls"));
  const open = button.getAttribute("aria-expanded") === "true";
  button.setAttribute("aria-expanded", String(!open)); detail.hidden = open;
}));

const messages = document.querySelector("#chat-messages");
const form = document.querySelector("#chat-form");
const input = document.querySelector("#chat-input");
function addMessage(text, side) {
  const row = document.createElement("div"); row.className = `message ${side}`;
  const bubble = document.createElement("span"); bubble.textContent = text; row.appendChild(bubble); messages.appendChild(row); messages.scrollTop = messages.scrollHeight;
}
function replyTo(question) {
  const q = question.toLowerCase();
  if (/smlds|iris|titanic|breast.?cancer|california housing|housing|pca|bootstrap|ridge|lasso|elastic.?net|hypothesis|p.?value|vif|cook.?s|mle|sampling|classification|regression|pandas|dataset|csv|scikit|seaborn|sklearn|standardscaler/i.test(q)) {
    if (/no module named|modulenotfound|importerror|install package/i.test(q)) return "For SMLDS, install the experiment dependencies in your active Python environment with: python -m pip install numpy pandas matplotlib seaborn scikit-learn scipy statsmodels. Then restart the notebook or VS Code kernel and run the script again. If the error names one specific package, check that package in the same interpreter VS Code is using.";
    if (/file not found|filenotfound|read_csv|csv path|dataset path/i.test(q)) return "The supplied data files are in smlds/datasets/. Check the exact spelling and run from the folder you expect. For a local file, use a path such as pd.read_csv('smlds/datasets/iris.csv'). Some original scripts use sklearn or Seaborn loaders instead of the CSV, so inspect the loader at the top of the script.";
    if (/connection|internet|url|fetch|download.*dataset/i.test(q)) return "Some original SMLDS scripts load built-in Seaborn or scikit-learn datasets and may need internet on the first run. The CSVs are included under smlds/datasets/ for local use. Switch the loader to pd.read_csv with the right CSV filename, then check column names because CSV headers may differ from the built-in dataset.";
    if (/convergence|did not converge|converge/i.test(q)) return "For an SMLDS model convergence warning, confirm the features are scaled, then check the model's max_iter and parameter settings. A warning is not the same as a successful fit; inspect the output and compare models only after the estimator finishes.";
    if (/could not convert|found unknown categories|input contains nan|nan|missing value/i.test(q)) return "For an SMLDS preprocessing error, inspect the selected feature columns and missing-value counts first. Impute or remove missing rows deliberately, encode text categories before fitting, and apply the same fitted transformations to train and test data.";
    const rankedSMLDS = smldsExperiments.map(experiment => {
      const words = (experiment.dataset + " " + experiment.title + " " + experiment.file).toLowerCase().split(/[^a-z0-9.+-]+/).filter(word => word.length > 2);
      return {experiment, score: words.reduce((n, word) => n + (q.includes(word) ? (word.length > 5 ? 2 : 1) : 0), 0)};
    }).sort((a,b) => b.score - a.score);
    if (rankedSMLDS[0]?.score > 0) {
      const item = rankedSMLDS[0].experiment;
      return `For ${item.dataset} — ${item.title}, open the complete ${item.file} script in the SMLDS Lab tab and check the first traceback line. Confirm the dataset columns, required imports, and train/test transformations match the code. The supplied CSVs are available in the dataset cards; original scripts may use a built-in loader instead.`;
    }
  }
  const ranked = labs.map(l => {
    const terms = (l.keywords + " " + l.title + " " + l.aim).toLowerCase().split(/[^a-z0-9.+-]+/).filter(w => w.length > 2);
    const score = terms.reduce((n, w) => n + (q.includes(w) ? (w.length > 5 ? 2 : 1) : 0), 0);
    return { lab: l, score };
  }).sort((a,b) => b.score - a.score);
  const best = ranked[0];
  if (!best || best.score < 2) return "I don’t see that exact issue in the guides yet. Which subject (ASDD or SMLDS), dataset or practical, and experiment are you on? Share the first error line and check the file path, spelling, required imports, and whether the data source is reachable.";
  const lab = best.lab;
  const matched = lab.errors.find(([h,d]) => (h + " " + d).toLowerCase().split(/[^a-z0-9.+-]+/).some(w => w.length > 4 && q.includes(w)));
  const relevantStep = lab.steps.map(s => ({s, score:(s[0]+" "+s[1]+" "+(s[2]||"")).toLowerCase().split(/[^a-z0-9.+-]+/).filter(w=>w.length>3&&q.includes(w)).length})).sort((a,b)=>b.score-a.score)[0];
  let text = `For ${lab.title}: ${matched ? matched[1] : lab.errors[0][1]} `;
  text += `Next check: ${relevantStep && relevantStep.score ? relevantStep.s[0]+" — "+relevantStep.s[1] : lab.steps[0][1]} `;
  text += `The guide’s success check is: ${lab.success}`;
  if (lab.n === "07") text += " Remember, remote deploy needs a prepared Linux server and GitHub secrets; never paste a secret into chat or source code.";
  if (lab.n === "06" && /delete|remove/i.test(q)) text += " Deleting the Deployment also removes its managed Pods.";
  return text;
}
function send(text) { const trimmed = text.trim(); if (!trimmed) return; addMessage(trimmed, "user"); window.setTimeout(() => addMessage(replyTo(trimmed), "bot"), 260); }
form.addEventListener("submit", e => { e.preventDefault(); send(input.value); input.value = ""; });
messages.addEventListener("click", e => { if (e.target.matches(".suggestions button")) send(e.target.textContent); });
document.querySelector(".chat-minimize").addEventListener("click", () => {
  messages.innerHTML = `<div class="message bot"><span>Hey! Tell me what you’re trying and what error you see. I’ll help you troubleshoot using the ASDD practicals. ✨</span></div><div class="suggestions"><button>Docker won’t start</button><button>My workflow is red</button><button>Pods aren’t running</button></div>`;
});
document.querySelector(".chat-fab").addEventListener("click", () => { document.querySelector("#help").scrollIntoView({behavior:"smooth"}); window.setTimeout(() => input.focus(), 500); });
const menu = document.querySelector(".menu-toggle");
menu.addEventListener("click", () => { const open = menu.getAttribute("aria-expanded") === "true"; menu.setAttribute("aria-expanded", String(!open)); document.querySelector(".topbar nav").classList.toggle("nav-open", !open); });
document.querySelectorAll(".topbar nav a").forEach(a => a.addEventListener("click", () => { menu.setAttribute("aria-expanded","false"); document.querySelector(".topbar nav").classList.remove("nav-open"); }));

if ("IntersectionObserver" in window) {
  const observer = new IntersectionObserver(entries => entries.forEach(entry => { if (entry.isIntersecting) { entry.target.classList.add("is-visible"); observer.unobserve(entry.target); } }), {threshold:.12});
  document.querySelectorAll(".reveal").forEach(el => observer.observe(el));
} else {
  document.querySelectorAll(".reveal").forEach(el => el.classList.add("is-visible"));
}

// The two study areas behave as keyboard-accessible tabs. The shared aa help remains available below them.
const tabButtons = [...document.querySelectorAll(".site-tab")];
const tabPanels = [...document.querySelectorAll(".site-panel")];
function activateTab(button, moveFocus = false) {
  tabButtons.forEach(item => {
    const selected = item === button;
    item.setAttribute("aria-selected", String(selected));
    item.tabIndex = selected ? 0 : -1;
    item.classList.toggle("is-active", selected);
  });
  tabPanels.forEach(panel => { panel.hidden = panel.id !== button.getAttribute("aria-controls"); });
  document.querySelector(".topbar nav").classList.remove("nav-open");
  document.querySelector(".menu-toggle").setAttribute("aria-expanded", "false");
  if (moveFocus) button.focus();
  if (button.id === "tab-viva" || button.id === "tab-smlds") document.querySelector(".topbar").scrollIntoView({behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth"});
}
tabButtons.forEach((button, index) => {
  button.addEventListener("click", () => activateTab(button));
  button.addEventListener("keydown", event => {
    let next = index;
    if (event.key === "ArrowRight") next = (index + 1) % tabButtons.length;
    else if (event.key === "ArrowLeft") next = (index - 1 + tabButtons.length) % tabButtons.length;
    else if (event.key === "Home") next = 0;
    else if (event.key === "End") next = tabButtons.length - 1;
    else return;
    event.preventDefault(); activateTab(tabButtons[next], true);
  });
});

// SMLDS catalogue: full supplied scripts and their CSV datasets are available as separate downloads.
const smldsDatasets = window.smldsDatasets || [];
const smldsExperiments = window.smldsExperiments || [];
const datasetGrid = document.querySelector("#smlds-datasets");
const experimentGrid = document.querySelector("#smlds-experiments");
const smldsFilter = document.querySelector("#smlds-filter");
const smldsSearch = document.querySelector("#smlds-search");
const smldsCount = document.querySelector("#smlds-result-count");
const smldsEmpty = document.querySelector("#smlds-empty");
const copyStatus = document.querySelector("#copy-status");
if (datasetGrid && smldsDatasets.length) {
  datasetGrid.innerHTML = smldsDatasets.map((dataset, index) => `<article class="dataset-card dataset-${escapeHtml(dataset.tone)}"><div class="dataset-card-top"><span class="dataset-index">0${index + 1}</span><span class="dataset-glyph" aria-hidden="true">${["◉","⌂","❀","⚓"][index]}</span></div><h3>${escapeHtml(dataset.title)}</h3><p>${escapeHtml(dataset.description)}</p><div class="dataset-stats"><span>${dataset.rows.toLocaleString()} rows</span><span>${dataset.columns} columns</span></div><a class="dataset-download" href="${escapeHtml(dataset.url)}" download>Download CSV <span>↘</span></a></article>`).join("");
}
if (experimentGrid && smldsExperiments.length) {
  if (smldsFilter) smldsFilter.innerHTML += smldsDatasets.map(dataset => `<option value="${escapeHtml(dataset.id)}">${escapeHtml(dataset.title)}</option>`).join("");
  experimentGrid.innerHTML = smldsExperiments.map((experiment, index) => `<article class="smlds-experiment" data-experiment="${escapeHtml(experiment.id)}" data-dataset="${escapeHtml(experiment.datasetId)}" data-search="${escapeHtml((experiment.dataset+" "+experiment.title+" "+experiment.file).toLowerCase())}"><div class="smlds-experiment-head"><span class="experiment-index">${String(index + 1).padStart(2,"0")}</span><span class="dataset-tag">${escapeHtml(experiment.dataset)}</span></div><h3>${escapeHtml(experiment.title)}</h3><p class="experiment-file"><code>${escapeHtml(experiment.file)}</code></p><div class="experiment-actions"><button class="button primary small-button copy-experiment" type="button" data-copy-experiment="${escapeHtml(experiment.id)}">Copy full experiment</button><a class="button outline small-button" href="${escapeHtml(experiment.url)}" download>Download .py</a></div><details class="source-preview"><summary>View complete script <span>↘</span></summary><pre><code>${escapeHtml(experiment.code)}</code></pre></details></article>`).join("");
  function filterSMLDS() {
    const query = (smldsSearch?.value || "").trim().toLowerCase();
    const selected = smldsFilter?.value || "all";
    let visible = 0;
    experimentGrid.querySelectorAll(".smlds-experiment").forEach(card => {
      const match = (selected === "all" || card.dataset.dataset === selected) && (!query || card.dataset.search.includes(query) || card.textContent.toLowerCase().includes(query));
      card.hidden = !match;
      if (match) visible++;
    });
    if (smldsCount) smldsCount.textContent = `${visible} of ${smldsExperiments.length} experiments shown`;
    if (smldsEmpty) smldsEmpty.hidden = visible !== 0;
  }
  smldsSearch?.addEventListener("input", filterSMLDS);
  smldsFilter?.addEventListener("change", filterSMLDS);
  filterSMLDS();
  experimentGrid.addEventListener("click", async event => {
    const button = event.target.closest("[data-copy-experiment]");
    if (!button) return;
    const experiment = smldsExperiments.find(item => item.id === button.dataset.copyExperiment);
    if (!experiment) return;
    try {
      if (navigator.clipboard?.writeText) await navigator.clipboard.writeText(experiment.code);
      else {
        const field = document.createElement("textarea"); field.value = experiment.code; field.setAttribute("readonly", ""); field.style.position = "fixed"; field.style.opacity = "0"; document.body.appendChild(field); field.select();
        const copied = document.execCommand("copy"); field.remove(); if (!copied) throw new Error("Copy unavailable");
      }
      button.textContent = "Copied full experiment ✓";
      if (copyStatus) copyStatus.textContent = `${experiment.title} for ${experiment.dataset} copied in full.`;
      window.setTimeout(() => { button.textContent = "Copy full experiment"; }, 2200);
    } catch {
      if (copyStatus) copyStatus.textContent = "Clipboard access was blocked. Open View complete script and select the code to copy it.";
    }
  });
}

// The viva bank switches between the ASDD source PDF and SMLDS experiment-based questions.
let activeVivaTrack = "asdd";
const asddExperiments = window.vivaExperiments || [];
const smldsVivaExperiments = window.smldsVivaExperiments || [];
const vivaTracks = [...document.querySelectorAll("[data-viva-track]")];
const vivaHeroEyebrow = document.querySelector("#viva-hero-eyebrow");
const vivaDownload = document.querySelector("#viva-download");
const vivaBankDescription = document.querySelector("#viva-bank-description");
const vivaSourceNote = document.querySelector("#viva-source-note");
const vivaChecklistTitle = document.querySelector("#viva-checklist-title");
const vivaChecklistList = document.querySelector("#viva-checklist-list");
const searchBox = document.querySelector("#viva-search");
const experimentFilter = document.querySelector("#viva-filter");
const vivaGroups = document.querySelector("#viva-groups");
const resultCount = document.querySelector("#viva-result-count");
const emptyState = document.querySelector("#viva-empty");
function currentVivaExperiments() { return activeVivaTrack === "smlds" ? smldsVivaExperiments : asddExperiments; }
function renderViva() {
  const experiments = currentVivaExperiments();
  if (!experiments.length || !searchBox || !experimentFilter || !vivaGroups) return;
  const totalQuestions = experiments.reduce((count, item) => count + item.questions.length, 0);
  experimentFilter.innerHTML = `<option value="all">All ${experiments.length} experiment sets</option>` + experiments.map(exp => `<option value="${escapeHtml(exp.number)}">${escapeHtml(exp.number)} · ${escapeHtml(exp.title)}</option>`).join("");
  vivaGroups.innerHTML = experiments.map(exp => `<section class="viva-group" data-experiment="${escapeHtml(exp.number)}"><div class="viva-group-heading"><span class="viva-group-num">${escapeHtml(exp.number)}</span><div><small>${activeVivaTrack === "smlds" ? escapeHtml(exp.dataset) : `EXPERIMENT ${Number(exp.number)}`}</small><h3>${escapeHtml(exp.title)}</h3></div><span class="group-count">${exp.questions.length} questions</span></div><div class="question-list">${exp.questions.map(item => `<details class="viva-question" data-search="${escapeHtml((item.question+" "+item.answer).toLowerCase())}"><summary><span class="q-number">Q${item.number}</span><span class="q-title">${escapeHtml(item.question)}</span><span class="q-toggle" aria-hidden="true">+</span></summary><div class="q-answer"><span>SHORT ANSWER</span><p>${escapeHtml(item.answer)}</p></div></details>`).join("")}</div></section>`).join("");
  resultCount.textContent = `${totalQuestions} questions · ${experiments.length} experiment sets`;
  if (emptyState) emptyState.hidden = true;
  const answerToggle = document.querySelector("#answers-toggle");
  if (answerToggle) answerToggle.textContent = "Show all answers";
  searchBox.value = "";
  const trackFilter = experimentFilter.value;
  if (!experiments.some(exp => exp.number === trackFilter)) experimentFilter.value = "all";
  const asddTrack = activeVivaTrack === "asdd";
  vivaTracks.forEach(button => {
    const selected = button.dataset.vivaTrack === activeVivaTrack;
    button.classList.toggle("is-active", selected); button.setAttribute("aria-selected", String(selected)); button.tabIndex = selected ? 0 : -1;
  });
  if (vivaHeroEyebrow) vivaHeroEyebrow.innerHTML = asddTrack ? '<i class="live-dot"></i> ASDD · SIX EXPERIMENTS · 124 QUESTIONS' : '<i class="live-dot"></i> SMLDS · 26 EXPERIMENTS · 104 QUESTIONS';
  if (vivaDownload) {
    vivaDownload.href = asddTrack ? "asdd-viva-questions.pdf" : "#question-bank";
    vivaDownload.textContent = asddTrack ? "Download ASDD viva PDF ↓" : "SMLDS questions below ↓";
    vivaDownload.toggleAttribute("download", asddTrack);
  }
  if (vivaBankDescription) vivaBankDescription.textContent = asddTrack ? "ASDD questions from six experiment sets. Try answering before you open the short model explanation." : "SMLDS questions cover all 26 supplied experiments and four datasets. Try answering before you open the short model explanation.";
  if (vivaSourceNote) vivaSourceNote.innerHTML = asddTrack ? 'ASDD questions are based on the supplied viva study guide. Use them to revise, then describe your own setup and results. <a href="asdd-viva-questions.pdf" download>Download the original PDF ↗</a>' : 'These model questions and concise answers were written from the 26 supplied SMLDS experiment scripts. Check the code and your own output when preparing an explanation.';
  if (vivaChecklistTitle) vivaChecklistTitle.textContent = asddTrack ? "Before you walk in" : "SMLDS topics to rehearse";
  if (vivaChecklistList) {
    const items = asddTrack ? ["I can state the objective and main tool for every experiment.","I can explain Jira, the backlog, and a Sprint.","I can explain Git staging, commits, branches, and merging.","I can name the CI trigger and success check.","I can describe the Dockerfile, image, container, and output.","I can explain Nginx, Redis, port 8080:80, and localhost:8080.","I can explain Kubernetes Pods, Deployments, and replicas.","I know the actual project and resource names from my own setup."] : ["I can explain sampling, the Central Limit Theorem, and bootstrap resampling.","I can distinguish classification from regression and explain the metrics used.","I can explain preprocessing, scaling, missing values, and data leakage.","I can describe tree ensembles, regularization, PCA, and clustering.","I can choose between a t-test, chi-square test, ANOVA, and permutation test.","I can interpret p-values, confidence intervals, residuals, VIF, and Cook’s Distance.","I can explain MLE and identify the parameters estimated in my chosen experiment.","I can name the dataset columns and describe my actual result without inventing it."];
    vivaChecklistList.innerHTML = items.map(item => `<li>${escapeHtml(item)}</li>`).join("");
  }
}
function filterViva() {
    const experiments = currentVivaExperiments();
    const totalQuestions = experiments.reduce((count, item) => count + item.questions.length, 0);
    const query = searchBox.value.trim().toLowerCase();
    const selected = experimentFilter.value;
    let visible = 0;
    vivaGroups.querySelectorAll(".viva-group").forEach(group => {
      let shownInGroup = 0;
      const groupMatches = selected === "all" || selected === group.dataset.experiment;
      group.querySelectorAll(".viva-question").forEach(card => {
        const match = groupMatches && (!query || card.dataset.search.includes(query));
        card.hidden = !match;
        if (match) { shownInGroup++; visible++; }
      });
      group.hidden = shownInGroup === 0;
    });
    resultCount.textContent = `${visible} of ${totalQuestions} questions shown · ${experiments.length} experiment sets`;
    emptyState.hidden = visible !== 0;
  }
searchBox.addEventListener("input", filterViva);
experimentFilter.addEventListener("change", filterViva);
document.querySelector("#answers-toggle").addEventListener("click", event => {
    const cards = [...vivaGroups.querySelectorAll(".viva-question:not([hidden])")];
    const openAll = cards.some(card => !card.open);
    cards.forEach(card => { card.open = openAll; });
    event.currentTarget.textContent = openAll ? "Hide all answers" : "Show all answers";
  });
vivaTracks.forEach((button, index) => {
  button.addEventListener("click", () => { activeVivaTrack = button.dataset.vivaTrack; renderViva(); });
  button.addEventListener("keydown", event => {
      let next = index;
      if (event.key === "ArrowRight") next = (index + 1) % vivaTracks.length;
      else if (event.key === "ArrowLeft") next = (index - 1 + vivaTracks.length) % vivaTracks.length;
      else if (event.key === "Home") next = 0;
      else if (event.key === "End") next = vivaTracks.length - 1;
      else return;
      event.preventDefault();
      activeVivaTrack = vivaTracks[next].dataset.vivaTrack; renderViva(); vivaTracks[next].focus();
  });
});
renderViva();
if (!asddExperiments.length && resultCount) resultCount.textContent = "The question list could not be loaded. Use the PDF download to open the complete guide.";

const commandGroups = [
  ["Git", [["git --version","Check installed version"],["git config --global user.name \"Your Name\"","Set commit author name"],["git config --global user.email \"you@example.com\"","Set commit author email"],["git init","Initialize repository"],["git status","Check file status"],["git add .","Stage changes"],["git commit -m \"Initial commit\"","Record changes"],["git log --oneline","View commit history"],["git branch feature","Create branch"],["git checkout feature","Switch branch"],["git checkout main","Switch to main"],["git merge feature","Merge branch"]]],
  ["GitHub", [["git clone <repo-url>","Clone remote repository"],["git push origin main","Push main branch"]]],
  ["Docker", [["docker --version","Check Docker"],["docker build -t myapp .","Build image"],["docker images","List images"],["docker run myapp","Run container"]]],
  ["Compose", [["docker compose up --build","Build/start services"],["docker compose ps","Check status"],["docker compose down","Stop/remove containers"]]],
  ["Kubernetes", [["minikube start","Start local cluster"],["kubectl get nodes","List nodes"],["kubectl apply -f deployment.yaml","Apply YAML resources"],["kubectl get pods","List Pods"],["kubectl scale deployment myapp --replicas=3","Scale to 3 replicas"],["kubectl delete deployment myapp","Delete Deployment"]]]
];
const commandList = document.querySelector("#command-list");
if (commandList) commandList.innerHTML = commandGroups.map(([group, commands]) => `<section><h3>${escapeHtml(group)}</h3>${commands.map(([command,purpose]) => `<div class="command-row"><code>${escapeHtml(command)}</code><span>${escapeHtml(purpose)}</span></div>`).join("")}</section>`).join("");
