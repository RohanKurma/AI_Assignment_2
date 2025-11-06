<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  
<body>
  <h1> Red–Blue Nim Game – AI Assignment (UTA CSE 4308/5360)</h1>

  <p>
    This project implements the <strong>Red–Blue Nim</strong> game for
    <em>Assignment 2</em> of <strong>CSE 4308/5360: Artificial Intelligence</strong>
    at the University of Texas at Arlington.
  </p>

  <p>
    The program demonstrates the use of
    <strong>Minimax Search</strong>, <strong>Alpha–Beta Pruning</strong>, and a
    <strong>Depth-Limited Alpha–Beta Search</strong> with a custom
    <strong>heuristic evaluation function</strong> for extra credit.  
    All algorithms follow the structure and pseudocode from
    <em>Russell &amp; Norvig’s “Artificial Intelligence: A Modern Approach” (4th Edition)</em>.
  </p>

  <hr />

  <h2>Features</h2>
  <ul>
    <li><strong>Two Game Modes:</strong>
      <ul>
        <li><code>standard</code> → The player who empties a pile <strong>loses</strong>.</li>
        <li><code>misere</code> → The player who empties a pile <strong>wins</strong>.</li>
      </ul>
    </li>
    <li><strong>Computer AI</strong> uses:
      <ul>
        <li>Minimax Search</li>
        <li>Alpha–Beta Pruning</li>
        <li>Depth-Limited Alpha–Beta Search (Extra Credit)</li>
      </ul>
    </li>
    <li><strong>Move Ordering for Efficiency:</strong>
      <ul>
        <li><em>Standard:</em> ('red', 2), ('blue', 2), ('red', 1), ('blue', 1)</li>
        <li><em>Misère:</em> Reversed order</li>
      </ul>
    </li>
    <li><strong>Interactive CLI Gameplay</strong> with input validation and turn-based output.</li>
  </ul>

  <hr />

  <h2>Algorithms Implemented</h2>
  <ul>
    <li><code>MINIMAX-SEARCH(game, state)</code></li>
    <li><code>ALPHA-BETA-SEARCH(game, state)</code></li>
    <li><code>ALPHA-BETA-LIMITED(game, state, depth)</code></li>
  </ul>
  <p>
    Each algorithm interacts with the game using:
    <code>TO-MOVE(s)</code>, <code>ACTIONS(s)</code>, <code>RESULT(s,a)</code>,
    <code>IS-TERMINAL(s)</code>, and <code>UTILITY(s,p)</code>.
  </p>

  <hr />

  <h2>File Structure</h2>
  <table>
    <tr><th>File</th><th>Description</th></tr>
    <tr><td><b>game.py</b></td><td>Implements the Red–Blue Nim environment using the AIMA game model.</td></tr>
    <tr><td><b>minimax.py</b></td><td>Contains Minimax, Alpha–Beta, and Depth-Limited Alpha–Beta search algorithms.</td></tr>
    <tr><td><b>red_blue_nim.py</b></td><td>Main driver for interactive gameplay.</td></tr>
    <tr><td><b>eval_function.txt</b></td><td>Describes the heuristic evaluation function (extra credit).</td></tr>
  </table>

  <hr />

  <h2>How to Run</h2>
  <p><strong>Command Line Syntax:</strong></p>
  <pre><code>python red_blue_nim.py &lt;num-red&gt; &lt;num-blue&gt; [version] [first-player] [depth]</code></pre>

  <table>
    <tr><th>Argument</th><th>Description</th><th>Default</th></tr>
    <tr><td>&lt;num-red&gt;</td><td>Number of red marbles</td><td>Required</td></tr>
    <tr><td>&lt;num-blue&gt;</td><td>Number of blue marbles</td><td>Required</td></tr>
    <tr><td>[version]</td><td>"standard" or "misere"</td><td>standard</td></tr>
    <tr><td>[first-player]</td><td>"computer" or "human"</td><td>computer</td></tr>
    <tr><td>[depth]</td><td>Optional integer for depth-limited search</td><td>None (full search)</td></tr>
  </table>

  <p><strong>Example Commands:</strong></p>
  <pre><code>
python red_blue_nim.py 3 4
python red_blue_nim.py 3 4 standard human
python red_blue_nim.py 5 6 misere computer 3
  </code></pre>

  <hr />

  <h2>Evaluation Function (Extra Credit)</h2>
  <p>
    The evaluation function estimates the desirability of a non-terminal state as:
  </p>

  <pre><code>
f(state, player) =
  -(2×red + 3×blue), if to_move == player
  +(2×red + 3×blue), otherwise
  </code></pre>

  <p>
    This heuristic rewards states where the opponent faces more remaining marbles.
    It is defined in <code>eval_function.txt</code> and used during Depth-Limited Alpha–Beta search.
  </p>

  <hr />

  <h2>Topics Covered</h2>
  <ul>
    <li>Adversarial Search</li>
    <li>Minimax Algorithm</li>
    <li>Alpha–Beta Pruning</li>
    <li>Depth-Limited Search</li>
    <li>Heuristic Evaluation Functions</li>
    <li>Game State Representation (AIMA-style)</li>
  </ul>

  <hr />

  <h2>References</h2>
  <p>
    Russell, S., &amp; Norvig, P. (2021).<br />
    <em>Artificial Intelligence: A Modern Approach (4th Edition)</em>.<br />
    Pearson Education.
  </p>

  <hr />

  <h2>Author</h2>
  <p>
    <strong>Rohan Kurma</strong><br />
    University of Texas at Arlington<br />
    UTA ID: 1002192255
  </p>

  <hr />

  <h2>Example Gameplay</h2>
  <pre><code>
===== Red–Blue Nim =====
Version: standard | First player: computer | Depth: Full search

Red marbles: 3 | Blue marbles: 4 | To move: computer
Computer thinking...

Computer chooses: ('red', 2)

Red marbles: 1 | Blue marbles: 4 | To move: human
Choose pile (red/blue): blue
How many marbles to remove (1 or 2)? 1
Red marbles: 1 | Blue marbles: 3 | To move: computer
Computer thinking...

Computer chooses: ('red', 1)

Red marbles: 0 | Blue marbles: 3 | To move: human

===== Game Over =====
Computer utility: -9
Human utility: 9
  </code></pre>

  <hr />

  <h2>Grading Summary</h2>
  <ul>
    <li>Implements Minimax and Alpha–Beta Pruning</li>
    <li>Includes Depth-Limited Heuristic Search (Extra Credit)</li>
    <li>Follows AIMA Framework</li>
    <li>Interactive, Modular, and Documented</li>
  </ul>

  <p class="center">
    If you found this project useful or educational, consider starring the repository!
  </p>
</body>
</html>
