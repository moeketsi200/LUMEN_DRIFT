# Fluid-Cave-RunnerLUMEN DRIFT
Decentraland Creator Success — V0 Development Plan
Project type: Arcade precision runner
Platform: Decentraland
Genre: Time trial, obstacle avoidance, collectible racing
Funding target: $1,000 USD, payable upon completion and acceptance of the agreed V0 scope
Project status: Concept and development plan
Working title: Lumen Drift

1. EXECUTIVE SUMMARY
Lumen Drift is a bioluminescent arcade game concept designed for Decentraland. Players control a small, glowing tadpole-like creature that swims automatically through a winding organic tunnel.
Players steer left and right to avoid glowing tendrils, navigate narrow passages, collect luminous nodes and attempt to finish the course in the fastest possible time.
The game combines simple controls, precision movement, increasingly challenging obstacles and an atmospheric visual identity inspired by underwater organisms, cellular structures and bioluminescent deep-sea environments.
The initial development goal is to create a small but complete playable prototype, also known as a vertical slice. This prototype will demonstrate the core gameplay and allow reviewers to enter a Decentraland World, play the game, experience the collision and scoring systems, and restart a run.
The project will prioritise responsive controls, readable hazards, smooth movement, replayability and reliable performance over a large amount of content.
Main objectives
Build a playable prototype using the Decentraland SDK.
Implement automatic forward movement and left/right steering.
Create a short organic tunnel with hazards and collectibles.
Add a timer, score counter, collision system and restart flow.
Establish a distinctive cyan and magenta bioluminescent art direction.
Publish a publicly accessible test scene in a Decentraland World.
Prepare the GitHub repository, Game Design Document and application materials required by Creator Success.

2. GAME CONCEPT
2.1 Game Overview
Name: Lumen Drift
Genre: Arcade precision runner and time trial.
Platform: Decentraland.
Player experience: Single-player core gameplay, with competitive leaderboard potential in a later version.
Visual style: Dark organic environments illuminated by cyan, turquoise, violet and magenta bioluminescence.
Core objective: Travel through a winding tunnel, avoid collisions, collect luminous nodes and complete the course as quickly as possible.
2.2 High Concept
Lumen Drift places the player inside a strange, living tunnel filled with glowing organisms, dangerous tendrils and narrow passages.
The player controls a small luminous creature with an organic trailing tail. The creature moves forward automatically, requiring the player to focus on steering, reading the environment and anticipating hazards.
The experience is designed to be easy to understand but difficult to master. Players should want to retry a run to improve their time, collect more nodes and learn the safest racing line.
2.3 Design Pillars
Simple controls, demanding mastery
Players should understand the controls within seconds. Mastery comes from precision, timing and learning the course.
Flow and momentum
Movement should feel continuous, smooth and responsive rather than stiff or mechanical.
Readable danger
Glowing hazards should contrast clearly against the dark environment. Players should understand why they collided and how to improve.
Replayability
Short runs, collectibles and personal bests should encourage players to try again.
Distinctive atmosphere
The organic tunnel, luminous creature, animated tendrils and glowing particles should create a recognisable visual identity.

3. CORE GAMEPLAY LOOP
The intended gameplay loop is:
The player enters the game and sees a brief control tutorial.
The player starts a run at the tunnel entrance.
The creature automatically moves forward.
The player steers left and right to follow the tunnel.
The player avoids hazards, walls and narrow passages.
The player collects luminous nodes along the route.
A collision ends the run, or the player reaches the finish.
The game displays the elapsed time and collectible score.
The player restarts and attempts to improve the result.
The first course should be short enough to encourage repeated attempts. A target completion time of approximately 30–60 seconds is a proposed design goal, not an official programme requirement.

4. PLAYER CONTROLS
The first prototype will use keyboard controls suitable for desktop browser play.
Left Arrow or A: Steer left.
Right Arrow or D: Steer right.
Enter or Space: Start or restart where appropriate.
Mouse: Interact with interface elements.
The creature moves forward automatically.
Steering should feel responsive, with smooth movement and controlled lateral acceleration where appropriate. The player should be able to make small corrections without losing control.
The control system should avoid excessive sliding, unpredictable momentum or delayed responses that make collisions feel unfair.
Additional control options can be considered after the desktop version works reliably.

5. PLAYER CHARACTER AND TAIL PHYSICS
5.1 Character Design
The player controls a small tadpole-like creature with:
A luminous head.
A visible eye.
An elongated organic tail.
A soft cyan or turquoise glow.
Smooth swimming animation.
A clear silhouette against the dark environment.
The character should be visually appealing but lightweight enough to perform well in a browser-based game.
5.2 Tail Animation
The tail should follow the head with a natural undulating motion.
A practical first implementation is to record a short history of the head's previous positions. Different sections of the tail follow earlier positions in that history.
This creates a trailing effect without requiring complicated fluid simulation.
The tail can also use a subtle sine-wave animation to create a swimming sensation.
5.3 Collision Behaviour
The creature's collision boundary should be predictable and smaller than its full visual silhouette where necessary.
This prevents players from feeling that they collided with an obstacle despite appearing to have enough clearance.
The head should be the primary collision reference in the first prototype.

6. ENVIRONMENT AND LEVEL DESIGN
6.1 Organic Tunnel
The course will be constructed from a sequence of curved or angled tunnel sections.
The environment should include:
Winding passages.
Narrow constrictions.
Wider chambers.
Dark outer walls.
Cyan and magenta tendril patches.
Central obstacles that divide the route.
Dotted guide lines in selected sections.
Luminous collectible nodes.
A clearly defined start and finish.
The first version will contain one complete course.
6.2 Visual Direction
The art direction should create the impression of travelling through a living biological structure.
Recommended visual elements include:
Deep navy or almost-black backgrounds.
Cyan and turquoise light.
Magenta and violet hazard illumination.
Soft emissive materials.
Floating particles.
Organic curves and rounded surfaces.
Subtle pulses of light.
Selective use of fog or atmospheric effects, if supported and performant.
The environment must remain readable. Decorative elements should not obscure hazards or make safe routes difficult to identify.
6.3 Level Progression
The initial course should introduce challenges gradually.
Opening section: A wide passage that teaches steering.
Middle section: Gentle curves and isolated hazards.
Precision section: Narrow passages and tendril patches.
Route-choice section: A central obstacle that divides the tunnel into two possible paths.
Final section: A short, more demanding sequence leading to the finish.
The level should feel complete without requiring multiple separate stages.

7. HAZARDS AND COLLISION SYSTEM
7.1 Hazard Types
Glowing tendrils
Spiky, brush-like growths along the tunnel edges. These are the main recurring hazard.
Narrow passages
Constricted sections that require careful steering.
Central obstacles
Large organic formations that force players to choose a route.
Tunnel boundaries
The outer walls define the safe playable area.
7.2 Collision Rules
In the initial prototype, contact with a hazard or tunnel boundary will end the current run.
The game will then display a results or failure screen and offer an immediate retry.
A penalty-based system can be considered later, but the first implementation should use simple, consistent rules.
7.3 Collision Feedback
When a collision occurs:
Stop or transition the player out of active movement.
Display a brief impact effect if feasible.
Record the elapsed time and collected nodes.
Show the results screen.
Allow the player to restart.
The system should be consistent and easy to test.

8. COLLECTIBLES AND SCORING
8.1 Luminous Nodes
Small glowing nodes will appear along the route.
Collectibles should be visually distinct from hazards and should encourage players to make meaningful steering decisions.
Some nodes can be placed along the safest route, while others can be placed in slightly riskier positions.
8.2 Scoring
The first version will use a straightforward score counter.
Each collected node increases the score by a defined amount.
The interface will display the current score during the run and the final collectible count on the results screen.
8.3 Potential Future Mechanics
If the core gameplay works well, later versions could introduce:
Temporary speed boosts.
Special collectibles.
Alternative routes with different rewards.
Checkpoints.
More difficult course variants.
These are optional future features and are not necessary for the initial V0 prototype.

9. USER INTERFACE
The prototype will include the following screens and interface elements.
9.1 Start Screen
The start screen will display:
Game title.
A short description.
Basic controls.
A Start button.
9.2 In-Game HUD
During a run, the interface will display:
Elapsed time.
Collectible count.
Optional progress indicator, if feasible.
The HUD should remain minimal and should not obstruct the tunnel.
9.3 Results Screen
At the end of a run, the interface will display:
Final time.
Collectible score.
Whether the player finished or collided.
A Retry button.
Personal-best tracking is a useful optional enhancement, but the core V0 can be completed without a persistent leaderboard.

10. AUDIO AND VISUAL FEEDBACK
Audio and visual effects should reinforce the feeling of speed and the biological environment.
Potential effects include:
Soft ambient underwater sound.
A subtle movement sound.
A distinct collection sound.
A collision effect.
Pulsing light around collectibles.
Animated hazard tendrils.
Small particles around the player.
Subtle visual feedback when steering.
These effects should be added after the basic gameplay works.
All external assets must have suitable permissions or licences for the intended use.

11. V0 VERTICAL SLICE
The V0 prototype will demonstrate one complete, playable experience.
11.1 Required Proposed Deliverables
A playable scene deployed in a public Decentraland World.
A controllable glowing creature.
Automatic forward movement.
Responsive left/right steering.
A short winding tunnel.
Tunnel boundaries and hazards.
Working collision detection.
A restart flow.
Collectible nodes and a score counter.
An elapsed-time display.
A results screen.
Basic visual effects establishing the bioluminescent art direction.
A GitHub repository containing the scene code.
A completed Game Design Document.
A README explaining setup and access to the test scene.
11.2 Acceptance Goals
The prototype should allow a reviewer to:
Enter the Decentraland World.
Understand the controls.
Start a run.
Steer through the tunnel.
Encounter hazards.
Collect luminous nodes.
Finish or experience a collision.
See the final time and score.
Restart the game.
The experience should be sufficiently stable and documented for playtesting.
These are proposed project goals. The final scope and acceptance criteria must be agreed with Creator Success if the project is selected.

12. TECHNICAL IMPLEMENTATION
12.1 Technology
The planned implementation will use the Decentraland SDK and TypeScript, with supported 3D scene and UI features.
Before development, the current SDK version, project template, collision APIs and supported rendering capabilities should be verified.
The scene should be designed to perform reliably in a browser-based environment.
12.2 Main Systems
Movement system
Controls automatic forward movement and lateral steering.
Player system
Manages the character's position, orientation and animation.
Tail animation system
Maintains a history of the player's previous positions to create trailing movement.
Collision system
Detects contact with hazards and tunnel boundaries.
Collectible system
Detects collected nodes, updates the score and deactivates collected objects.
Course system
Builds or manages the tunnel sections and their placement.
Game manager
Manages the game states: start, playing, crashed, finished and results.
Interface system
Displays controls, timer, score and results.
12.3 Proposed Repository Structure
lumen-drift/
README.md
design/
gdd.md
src/
index.ts
game/
GameManager.ts
PlayerController.ts
TailAnimator.ts
CollisionSystem.ts
CollectibleSystem.ts
CourseManager.ts
entities/
Player.ts
Hazard.ts
Collectible.ts
ui/
StartScreen.ts
GameHUD.ts
ResultsScreen.ts
levels/
Level01.ts
assets/
models/
textures/
audio/
materials/
This is a proposed structure. It may be adjusted to match the official Decentraland project template and the requirements of the chosen SDK version.

13. SIX-WEEK DEVELOPMENT ROADMAP
The following schedule is a planning estimate. Actual timing will depend on development experience, technical challenges, asset creation and feedback.
Week 1 — Foundation and Application Preparation
Tasks:
Verify the current Creator Success requirements.
Create or prepare a GitHub account.
Create the Lumen Drift repository.
Prepare the GDD and README.
Play the Featured games in Decentraland.
Record genuine observations for the application.
Install and test the Decentraland development environment.
Create a basic scene.
Milestone: The project is documented and the development environment works.
Week 2 — Core Movement
Tasks:
Build a basic tunnel.
Implement automatic forward movement.
Implement left/right steering.
Set up the camera.
Create the first version of the creature.
Add tunnel boundaries.
Implement collision detection.
Add a basic restart flow.
Milestone: The player can move, collide and restart.
Week 3 — Complete Gameplay Loop
Tasks:
Add hazards.
Add collectible nodes.
Add the score counter.
Implement the timer.
Create the start screen.
Create the results screen.
Add a complete short course.
Implement finish and collision states.
Milestone: The full gameplay loop works from start to finish.
Week 4 — Visual Polish
Tasks:
Improve the tunnel's organic appearance.
Add cyan and magenta lighting.
Add creature glow and tail animation.
Improve hazard visibility.
Add collectible effects.
Add subtle speed feedback.
Add audio if feasible.
Milestone: The game has a distinctive and coherent visual identity.
Week 5 — Deployment and Playtesting
Tasks:
Deploy the scene to a Decentraland World.
Confirm public access.
Test the controls and collision system.
Test the timer and score.
Test restarting repeatedly.
Ask other people to play.
Identify confusing sections.
Fix bugs and performance problems.
Milestone: The prototype can be played independently by a reviewer.
Week 6 — Submission Readiness
Tasks:
Finalise the GDD.
Complete the README.
Confirm the repository contains the actual test-scene code.
Add the requested reviewer IDs.
Capture genuine screenshots or video.
Confirm that the public scene works.
Complete the application with accurate information.
Verify all declarations before submission.
Milestone: A documented project and publicly playable prototype are ready for review.
The programme's actual deadlines and eligibility conditions must be checked separately.

14. PROJECT PRIORITIES
Must Have
Automatic forward movement.
Left/right steering.
A recognisable glowing creature.
A short winding tunnel.
Hazards and collision detection.
Collectibles and score.
Timer.
Start screen and results screen.
Restart functionality.
Public Decentraland test scene.
GitHub repository.
GDD and README.
Optional if Time Permits
Highly detailed creature modelling.
Complex procedural tunnel generation.
Multiple levels.
Online matchmaking.
Multiplayer races.
Persistent global leaderboard.
Elaborate particle systems.
Full soundtrack.
Mobile-specific controls.
The priority is to deliver a complete and enjoyable core experience before expanding the scope.

15. BUDGET AND FUNDING PLAN
The application describes a $1,000 USD V0 payment made after the agreed scope is completed and accepted as ready for playtesting.
The payment is not guaranteed by submitting the application.
An illustrative allocation of the eventual payment could be:
Category
Proposed allocation
Development and testing
$550
Art and assets
$200
Quality assurance and deployment
$150
Contingency
$100
Total
$1,000

This is a personal planning estimate, not an official Decentraland budget or a requirement to spend the full amount.
If the project is built independently using free tools and self-created assets, actual expenses may be lower.
The applicant remains responsible for the project repository and for maintaining any third-party permissions required for the work.
If selected, additional contractual and KYC requirements may apply, including a Master Services Agreement and Purchase Order.

16. CREATOR SUCCESS APPLICATION PLAN
Section 1 — About You
Prepare the following information:
Name.
Email address.
Discord ID used to join the Decentraland Discord.
Studio or team name; use "Individual" if applying alone.
Decentraland account ID or wallet address.
Use your actual information. Do not share passwords or private wallet keys.
Section 2 — Feedback on Featured Games
This section should be based on games actually played in Decentraland.
Question 2.1: Which Featured games did you play? Which was the most engaging, and why?
Record the games you played and explain which one held your attention most strongly.
Consider:
How quickly the game taught you its controls.
Whether the objective was clear.
How engaging the movement and feedback felt.
What motivated you to continue.
What made the experience memorable.
Question 2.2: Which Featured games did you return to and why?
Explain which games you revisited and what encouraged you to return.
Consider progression, challenge, competition, rewards, social interaction and the desire to improve.
Question 2.3: What are your top five learnings?
Potential topics to evaluate after playing include:
Clear onboarding helps players understand the game.
Responsive controls make gameplay feel fair.
Immediate feedback makes actions satisfying.
Short sessions can encourage replayability.
Visible progression or measurable improvement can motivate repeat visits.
Use these only if they genuinely reflect your observations. Replace them with your own findings where appropriate.
Section 3 — Your Project
Question 3.1: Project name
Lumen Drift (working title).
Question 3.2: GitHub repository URL
Create the repository and add the following reviewer IDs as requested by the form:
pravusjif
popuz
baybackner
nearnshaw
Verify the correct GitHub usernames and grant the access requested by the programme. Do not invent a repository URL.
Question 3.3: Your Decentraland World
Deploy the test scene and enter the actual World name in the application.
Do not claim a scene is live before it is accessible.
Section 4 — Final Confirmations
Application steps
Confirm that:
The GDD is saved at design/gdd.md.
The repository contains the submitted test-scene code.
The test scene is live and publicly accessible in a Decentraland World.
Applicant declarations
Read each declaration carefully before agreeing.
The applicant must be at least 18 years old, have legal capacity to apply, own or have permission to use all submitted materials, understand the payment terms, understand possible additional contractual and KYC requirements, and provide accurate information.
Communications
Confirm that Decentraland may contact you about the application and participation in Creator Success.
The separate option for future programme emails and platform news is optional.
How did you hear about the opportunity?
Provide the truthful source through which you discovered the programme.

17. TESTING AND QUALITY ASSURANCE
Before submission, test the following.
Gameplay
The creature moves forward automatically.
Steering responds reliably.
The creature stays within the intended movement area.
Hazards trigger collisions consistently.
Collectibles increase the score once each.
The timer starts and stops correctly.
Finishing and crashing both produce valid results.
Restarting resets the run correctly.
Usability
Players understand the controls.
The start button works.
The timer and score are readable.
Hazards are visually distinct.
The player can identify the next route.
The retry flow is clear.
Deployment
The scene is publicly accessible.
The published scene matches the repository version.
The project starts without critical errors.
Assets load correctly.
Performance is acceptable.
A new visitor can play without help from the developer.

18. RISKS AND MITIGATION
Risk: Scope becomes too large.
Mitigation: Build one course and one complete gameplay loop before adding extra content.
Risk: The game looks attractive but is not fun.
Mitigation: Test movement and collisions early, before investing heavily in artwork.
Risk: Collisions feel unfair.
Mitigation: Use predictable collision boundaries and repeatedly test narrow passages.
Risk: The scene works locally but fails when published.
Mitigation: Test the actual public Decentraland World from a clean session.
Risk: Application feedback is generic or inaccurate.
Mitigation: Play the Featured games and write from genuine experience.
Risk: Third-party assets create licensing issues.
Mitigation: Use original work or assets whose licences permit the intended use, and keep records of their source and permissions.
Risk: Funding is assumed before approval.
Mitigation: Treat the $1,000 as conditional payment for an accepted V0 scope, not upfront funding or guaranteed income.

19. SUCCESS CRITERIA
The project will be considered ready for review when:
A player can enter the World and start the game.
The creature can be controlled reliably.
The tunnel contains a complete playable route.
Hazards and collisions work consistently.
Collectibles and score work.
The timer and results screen work.
The player can restart the game.
The visual presentation establishes the intended art direction.
The public test scene is stable enough for playtesting.
The repository and GDD accurately document the submitted project.
The final acceptance criteria will be the criteria agreed with Creator Success if the application is accepted.

20. IMMEDIATE ACTION CHECKLIST
Complete these tasks in order:
Confirm the official application requirements and deadline.
Prepare the GitHub account and repository.
Save this document as design/gdd.md.
Prepare a README.
Play the Featured games and record your feedback.
Set up the Decentraland SDK environment.
Build the first basic tunnel and movement system.
Add collisions and restarting.
Add collectibles, score and timer.
Build the complete short course.
Add the creature's appearance and tail animation.
Deploy the test scene to a public Decentraland World.
Test the published experience.
Add the requested repository reviewer IDs.
Complete the application truthfully and submit when all required steps are complete.

FINAL VISION
Lumen Drift aims to turn a simple movement mechanic into a distinctive arcade experience inside Decentraland.
The long-term vision is a world of organic tunnels, luminous creatures, dangerous currents, collectible organisms and increasingly demanding routes. Players could eventually compete for the fastest completion times, discover alternate paths and master different courses.
The first milestone is deliberately smaller: one memorable creature, one beautiful tunnel and one satisfying gameplay loop.
Build the core. Make it playable. Make it public. Document it properly. Then expand.

