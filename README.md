<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Awais_agent — AI Tic-Tac-Toe (Project Overview)</title>
  <style>
    body{font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial; line-height:1.6; max-width:980px; margin:24px auto; padding:0 20px; color:#111;}
    h1,h2{color:#0b5cff}
    pre{background:#f4f4f4;padding:12px;border-radius:6px;overflow:auto}
    code{background:#f0f0f0;padding:2px 6px;border-radius:4px}
    .row{display:flex;gap:16px;flex-wrap:wrap}
    .card{border:1px solid #e6e6e6;padding:12px;border-radius:8px;flex:1 1 280px;background:#fff}
    img{max-width:100%;height:auto;border-radius:6px;border:1px solid #ddd}
    .small{font-size:0.9rem;color:#444}
    footer{margin-top:28px;padding-top:12px;border-top:1px solid #eee;color:#555}
    a.button{display:inline-block;padding:8px 12px;background:#0b5cff;color:white;border-radius:6px;text-decoration:none}
  </style>
</head>
<body>
  <h1>Awais_agent — AI Tic-Tac-Toe</h1>
  <p class="small">Generated HTML overview for the <strong>Ai_agent</strong> project (extracted from the uploaded ZIP).</p>

  <h2>Project summary</h2>
  <p>This repository implements an AI-powered Tic-Tac-Toe game. It contains:</p>
  <ul>
    <li>A Python minmax-based AI implementation.</li>
    <li>Game logic and an agent that plays optimally using the Minimax algorithm.</li>
    <li>A simple web version (HTML + CSS) for playing in the browser.</li>
    <li>Preview images that visualize the Minimax game tree.</li>
  </ul>

  <h2>Key files & directory structure</h2>
  <pre>
Awais_agent/
└─ AI-Tic-Tac-Toe/
   ├─ minimax/               # Minimax algorithm implementation (Board, Player, main)
   ├─ tictactoe/             # Python game + agent + teacher scripts
   ├─ preview/               # Images (game tree, diagrams)
   ├─ Webversion/            # CSS for web UI
   ├─ index.html             # Browser playable version
   └─ play.py                # Starter script to run the game
  </pre>

  <h2>Algorithms used</h2>
  <div class="row">
    <div class="card">
      <h3>Minimax (game-tree search)</h3>
      <p>The AI uses the <strong>Minimax</strong> algorithm to search the game tree of Tic-Tac-Toe moves. Minimax explores possible moves recursively, assuming both players play optimally:</p>
      <ul>
        <li><strong>Maximizer</strong> (AI) chooses moves to maximize its score.</li>
        <li><strong>Minimizer</strong> (human/opponent) chooses moves to minimize the AI's score.</li>
        <li>Terminal states (win/lose/draw) are assigned numeric scores and propagated back up the tree.</li>
      </ul>
      <p class="small">This guarantees optimal play for Tic-Tac-Toe (the game is small enough to search exhaustively).</p>
    </div>

    <div class="card">
      <h3>Other components</h3>
      <p>The project also contains an <code>agent.py</code> and a <code>teacher.py</code> script — these orchestrate game play and can be extended to support training, heuristics, or logging game outcomes.</p>
    </div>
  </div>

  <h2>How it works (high-level)</h2>
  <ol>
    <li>User or script starts the game (via <code>play.py</code> or <code>index.html</code>).</li>
    <li>The game engine (Board / game.py) tracks the board state and legal moves.</li>
    <li>When it's the AI's turn, the Minimax routine evaluates possible moves and returns the best one.</li>
    <li>Moves are applied until a terminal state (win/draw) is reached, and the result is shown.</li>
  </ol>
  <h2>Images / Visuals</h2>
  <p>Below are the preview images included in the project. They are useful for documentation and explaining the Minimax tree.</p>
  <div class="row">
    <div class="card">
      <h4>Minimax game tree</h4>
      <img src="AI-Tic-Tac-Toe/preview/tic-tac-toe-minimax-game-tree.png" alt="minimax game tree">
    </div>
    <div class="card">
      <h4>Simplified G-tree</h4>
      <img src="AI-Tic-Tac-Toe/preview/simplified-g-tree.png" alt="simplified g tree">
    </div>
    <div class="card">
      <h4>Minimax diagram</h4>
      <img src="AI-Tic-Tac-Toe/preview/minimax_img.png" alt="minimax image">
    </div>
  </div>

  <h2>Files you may want to read first</h2>
  <ul>
    <li><code>AI-Tic-Tac-Toe/minimax/Tic-Tac-Toe.py</code> — main minimax implementation.</li>
    <li><code>AI-Tic-Tac-Toe/tictactoe/agent.py</code> — AI agent interface to the game engine.</li>
    <li><code>AI-Tic-Tac-Toe/play.py</code> — entry point to launch CLI gameplay.</li>
    <li><code>AI-Tic-Tac-Toe/index.html</code> — simple browser UI.</li>
  </ul>

  <h2>Usage examples</h2>
  <pre>
# Play a single match (CLI)
python play.py

# Serve the web UI and open in browser
python -m http.server 8000
# open http://localhost:8000/AI-Tic-Tac-Toe/index.html
  </pre>

  <h2>Extending the project</h2>
  <p>You can extend the project by:</p>
  <ul>
    <li>Adding alpha-beta pruning to improve search speed (useful when adding heuristics).</li>
    <li>Replacing Minimax with Monte Carlo Tree Search (MCTS) for other games.</li>
    <li>Building a simple Flask server around the Python agent to provide an API for the web UI.</li>
    <li>Adding logging and a match history to <code>teacher.py</code> for training/analytics.</li>
  </ul>

  <h2>License & contribution</h2>
  <p>Add your preferred license (e.g., MIT) to the repo root. To contribute, open issues and PRs. Suggested branch workflow: <code>main</code> for stable code, feature branches for new work.</p>

  <footer>
    <p>README generated for <strong>Awais_agent</strong>. If you want a README.md instead, or a polished GitHub README with badges and copy-ready markdown, say "make README.md".</p>
    <p><a class="button" href="file:///mnt/data/Awais_agent_unzipped/Awais_agent/README.html" target="_blank">Open generated README.html</a></p>
  </footer>
</body>
</html>
