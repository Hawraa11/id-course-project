from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn

# Create a new document
doc = Document()

# Set up styles
style = doc.styles['Normal']
font = style.font
font.name = 'Calibri'
font.size = Pt(11)

# Title
title = doc.add_heading('Autonomous Drone AI: A Complete Handbook from Beginner to Expert', 0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

# Add the main content
content = """
The Real Value: Software for Autonomy, Resilience, and Precision

The real value is in the software that provides autonomy, resilience, and precision.

The Replicator Initiative
The Pentagon's "Replicator" initiative is focused on fielding large numbers of low-cost, autonomous systems at speed and scale, specifically highlighting the need for attritable, software-enabled options over traditional high-cost hardware. This signals a clear demand for your software capabilities.

SPARC AI's Overwatch Platform
SPARC AI has created a "software-only platform meant to equip any drone, regardless of cost or manufacturer, with GPS-denied navigation and precision targeting capability". Their platform has moved beyond the concept phase; they have secured operational field testing in Ukraine and licensing agreements in the UAE and India. This is a direct proof of concept for your business model.

Shield AI's Hivemind SDK
Shield AI, a major player in defense AI, offers its Hivemind software development kit (SDK). Their partnership with the Republic of Singapore Air Force allows Singapore to "independently design, test, and deploy mission autonomy" using their software, without requiring Shield AI to supply the hardware. This partnership explicitly focuses on building "true sovereign autonomy"—the ability to develop and field its own AI pilots—which is a software capability. This partnership validates that militaries see immense value in a software-first approach that they can integrate into their own platforms.

The Technical Solutions Already Exist (As Software)

The key technical challenges you identified—operating without GPS and making autonomous decisions—are being actively solved at the software level.

GPS-Denied Navigation
This is one of the most critical software problems to solve.

1. Sensor Fusion: The solution is in software that fuses data from different onboard sensors (IMU, camera, LiDAR). This allows the drone to maintain a stable position and navigate through "dead-reckoning" when GPS is unavailable. The FusionCore package, for example, is an open-source sensor fusion package written in C++ that fuses IMU, wheel odometry, and Visual SLAM data for GPS-denied operation.

2. Visual-Inertial SLAM: Systems like GhostPilot demonstrate that you can create a complete visual-inertial SLAM system for GPS-denied drone operation without needing expensive custom hardware.

3. Autonomous Decision-Making: This is where your ML models will shine. Research shows that learning-based approaches are outperforming traditional, pre-programmed control systems.

4. Deep Reinforcement Learning (DRL): A proposed "Combat-Ready UAV Intelligence System" uses DRL algorithms to enable "fully autonomous drone engagement in combat scenarios, threat analysis, and navigation". This hybrid architecture handles both continuous flight control and discrete mission choices like strike timing and evasion.

5. Vision-Based Tracking: Another research paper presents a solution using a combination of deep learning and reinforcement learning to enable a "chaser UAV" to actively and efficiently track a flying target, which is core to your self-defense use case. This is a software solution for a hardware problem.

Your success will depend on mastering the software integration layer.

1. You Will Need an SDK: To be hardware-agnostic, your software must provide an SDK that abstracts away the complexities of low-level flight control. This allows you to write high-level commands (e.g., "track target") without worrying about the specifics of each drone's motors and firmware. Shield AI's success is built on providing an effective SDK. Projects like AeroGen are also pioneering this approach, using an SDK to help AI generate correct drone control programs.

2. Hardware and Software Are Inseparable Partners: While you are not building the hardware, you are intimately dependent on it. Your software's performance is directly tied to the sensors (cameras, LiDAR, IMU) and the onboard computer (like the NVIDIA Jetson series) that runs your models. The partnership between hardware and software is what creates the final product.

3. Real-World Validation is Non-Negotiable: As the report on SPARC AI emphasizes, a key differentiator is moving from a concept to "actual deployment". You will need to be ready to test and refine your software in rigorous simulation and, ultimately, in field tests to prove its effectiveness in contested electronic warfare environments.

Security Challenges: The Software Attack Surface

The shift from vulnerable wireless systems to fiber-optic control demonstrates the extreme lengths being taken to evade detection, and it perfectly highlights why true autonomy is the next strategic imperative.

While using software-based AI for navigation and action offers a way out of this trap, it introduces a new set of security challenges. The systems you mentioned—sensor fusion, SLAM, and DRL—are powerful, but they have specific limitations and are vulnerable to sophisticated attacks.

The True Price of "No GPS": The Software Attack Surface

The core irony is this: In the quest to eliminate the attack vector of GPS jamming, we create a new, more subtle attack surface focused on the drone's perception and decision-making. The drone can no longer be tricked by a false GPS signal, but it can be tricked into "seeing" or "believing" a false environment.

The Attack Vectors on Your Tech Stack

Visual SLAM (vSLAM) and Sensor Fusion: "Phantom Paths" and Forced Errors
The "Phantom Path Attack" is a direct example of this. By projecting an adversarial video onto a surface in the drone's environment, attackers can inject false visual features that vSLAM algorithms like ORB-SLAM3 lock onto. This doesn't just cause a crash; it creates a "phantom path," deliberately steering the drone off course. Research shows this attack can cause localization errors of up to 252 meters and altitude deviations of 70 meters, often leading to a crash.

Black-Box Adversarial Attacks are particularly dangerous because the attacker doesn't even need to know the drone's specific internal software. By adding imperceptible perturbations to the images fed into a CNN-based SLAM system, researchers have shown that tracking can fail in up to 76% of frames.

Sensor Spoofing Cascades can also exploit the fusion process. Spoofing the position of just one drone in a swarm by 5 meters can cause other drones that rely on that fused data to crash into obstacles, with an attack success rate of 76.67%.

Deep Reinforcement Learning (DRL): "Confusing the Brain"
Strategic Time Attacks exploit the fact that not every decision a DRL agent makes is equally critical. A new attack method targets these "critical decision states" by analyzing multiple factors like policy stability and environmental risk. This attack achieves three times the reward reduction compared to a random-time attack, showing it can more effectively cripple a drone's navigation capabilities while using fewer resources.

GPS Spoofing in Disguise: Even with a DRL system, an attacker can try to manipulate the inputs to the learning algorithm. GPS spoofing attacks, even those that must bypass an Extended Kalman Filter (EKF) sensor fusion check, have been shown to still effectively disrupt DRL-based autonomous navigation systems.

Summary of Limitations and How to Build Resilience

To answer your core question, these technologies are not invincible. Their limitations and potential for attack come from an over-reliance on a single, manipulatable data source.

The first line of defense is sensor redundancy and multi-modal fusion. Relying on a single camera makes vSLAM attacks trivial. By fusing data from IMUs, LiDAR, radar, and event cameras, you create a system that is much harder to fool. A sensor fusion attack succeeds only if it can simultaneously deceive all the sensors the drone relies on.

In short, an autonomous system's intelligence is only as reliable as the integrity of its sensory inputs. This is the central battleground for the future of drone warfare.

"""

# Add the introduction section
for paragraph in content.split('\n\n'):
    if paragraph.strip():
        if paragraph.startswith('The Replicator Initiative') or paragraph.startswith('SPARC AI') or paragraph.startswith('Shield AI') or paragraph.startswith('GPS-Denied Navigation') or paragraph.startswith('The Attack Vectors') or paragraph.startswith('Visual SLAM') or paragraph.startswith('Deep Reinforcement Learning') or paragraph.startswith('Summary of Limitations'):
            doc.add_heading(paragraph.split('\n')[0], 2)
            if '\n' in paragraph:
                doc.add_paragraph(paragraph.split('\n', 1)[1])
        else:
            doc.add_paragraph(paragraph)

# PART 1: FIELD OVERVIEW
doc.add_page_break()
doc.add_heading('PART 1: FIELD OVERVIEW', 1)

doc.add_heading('1.1 What This Field Is', 2)
doc.add_paragraph("""
This field sits at the intersection of artificial intelligence, robotics, and defense technology. You are building the "brain" for a flying machine that can:

- Perceive its environment using cameras and sensors
- Navigate without external signals (GPS, fiber optics, radio beacons)
- Make decisions autonomously in dynamic, hostile environments
- Act on those decisions—evading, tracking, engaging—without human intervention

The core technical challenge is building a software-only intelligence layer that transforms any drone hardware into a fully autonomous combat-capable system, immune to electronic warfare countermeasures like GPS jamming and signal spoofing.

Definition: This is the engineering of embodied AI for contested environments—a system where perception models, reinforcement learning policies, and control algorithms run on resource-constrained edge hardware to enable real-time autonomous operation.
""")

doc.add_heading('1.2 Why It Matters', 2)
doc.add_paragraph("""
The strategic importance is monumental:

- Electronic Warfare Reality: GPS jamming has become standard in modern conflicts. Drones without GPS-denied capabilities are effectively "blind" in contested airspace.
- Warfare Democratization: As Jesse Hamel of Victus AI puts it, "Everyone can have their own air force." Low-cost drones with sophisticated AI are shifting global power dynamics.
- Economic Impact: The drone industry is projected to contribute ~£42 billion to the UK economy alone by 2030, with defense and autonomy being the fastest-growing segments.
- Strategic Independence: Nations seek "sovereign autonomy"—the ability to develop and deploy AI pilots without dependency on foreign hardware or GPS infrastructure.

The macro trend: 2025-2035 has been called the "Decade of Robotics" in defense and commercial applications.
""")

doc.add_heading('1.3 Current State of the Industry', 2)

# Add table
table = doc.add_table(rows=6, cols=3)
table.style = 'Table Grid'
table.rows[0].cells[0].text = 'Domain'
table.rows[0].cells[1].text = 'State'
table.rows[0].cells[2].text = 'Key Players'
table.rows[1].cells[0].text = 'GPS-Denied Navigation'
table.rows[1].cells[1].text = 'Emerging, with proven software-only solutions'
table.rows[1].cells[2].text = 'Victus AI, SPARC AI, Shield AI'
table.rows[2].cells[0].text = 'Perception (Detection/Tracking)'
table.rows[2].cells[1].text = 'Mature; YOLO-based real-time detection is standard'
table.rows[2].cells[2].text = 'Academic research, defense contractors'
table.rows[3].cells[0].text = 'Autonomous Decision-Making'
table.rows[3].cells[1].text = 'Rapidly advancing; DRL outperforming classical control'
table.rows[3].cells[2].text = 'IIT Hyderabad, MIT, defense labs'
table.rows[4].cells[0].text = 'Edge AI Deployment'
table.rows[4].cells[1].text = 'Maturing; Jetson platform is industry standard'
table.rows[4].cells[2].text = 'NVIDIA, Google Coral'
table.rows[5].cells[0].text = 'Swarm Coordination'
table.rows[5].cells[1].text = 'Early-stage; federated learning approaches emerging'
table.rows[5].cells[2].text = 'IEEE research, DARPA programs'

doc.add_paragraph("""
Real-world validation: SPARC AI's Overwatch platform has moved from concept to operational field testing in Ukraine, with licensing agreements in the UAE and India. Shield AI's Hivemind SDK now powers autonomous systems across aerial, surface, and subsurface domains.
""")

doc.add_heading('1.4 Future Trends (5-10 Years)', 2)
doc.add_paragraph("""
1. Event Cameras & Neuromorphic Sensing: Event-based vision will replace traditional frame-based cameras for drone detection, virtually eliminating motion blur and enabling extreme low-light performance.

2. Federated Learning for Swarms: Multi-agent systems will learn collaboratively while preserving privacy, enabling coordinated actions without constant communication.

3. On-Device Training: Rather than just inference, drones will fine-tune their models in-flight using federated approaches.

4. AI-Powered Integration: The month-long process of integrating AI with new drone hardware will be reduced to hours using generative AI for "translator" code.

5. Regulatory Evolution: BVLOS (Beyond Visual Line of Sight) regulations will mature, requiring more robust autonomous navigation systems.
""")

doc.add_heading('1.5 Common Misconceptions', 2)

# Add misconceptions table
table2 = doc.add_table(rows=6, cols=2)
table2.style = 'Table Grid'
table2.rows[0].cells[0].text = 'Myth'
table2.rows[0].cells[1].text = 'Reality'
table2.rows[1].cells[0].text = '"You need custom hardware for autonomy"'
table2.rows[1].cells[1].text = 'Software-only solutions exist and are proving effective'
table2.rows[2].cells[0].text = '"GPS denial is impossible to solve"'
table2.rows[2].cells[1].text = 'Sensor fusion + VIO + SLAM provide reliable navigation without GPS'
table2.rows[3].cells[0].text = '"Autonomous drones replace human pilots"'
table2.rows[3].cells[1].text = 'They augment humans, shifting roles from piloting to fleet supervision'
table2.rows[4].cells[0].text = '"Simulation is enough for training"'
table2.rows[4].cells[1].text = 'Simulation provides foundational training; real-world validation is non-negotiable'
table2.rows[5].cells[0].text = '"Edge AI isn\'t powerful enough for complex models"'
table2.rows[5].cells[1].text = 'Jetson Orin achieves up to 67 TOPS; model compression enables complex models on edge'

# PART 2: LEARNING ROADMAP
doc.add_page_break()
doc.add_heading('PART 2: LEARNING ROADMAP', 1)

doc.add_heading('2.1 Beginner → Intermediate → Advanced → Expert', 2)

doc.add_heading('🟢 BEGINNER (0-6 Months)', 3)
doc.add_paragraph("""
Goal: Build foundational skills in programming, mathematics, and basic ML.

Skills Required:
- Python programming (intermediate level)
- Linear algebra, calculus, probability/statistics
- Basic Linux command line
- Version control with Git
- Basic understanding of neural networks

Prerequisites:
- High school mathematics
- Basic computer literacy
- Willingness to learn through projects

Milestones:
- Complete Python for Data Science course
- Implement linear regression from scratch
- Build and train a CNN on MNIST
- Understand backpropagation and gradient descent

Recommended Time Allocation:
- Daily: 2-3 hours
- Weekly: 15-20 hours
- Total: ~500 hours
""")

doc.add_heading('🟡 INTERMEDIATE (6-18 Months)', 3)
doc.add_paragraph("""
Goal: Master deep learning fundamentals, computer vision, and reinforcement learning.

Skills Required:
- Deep learning architectures (CNNs, RNNs, Transformers)
- Computer vision (object detection, segmentation, tracking)
- Reinforcement learning fundamentals (Q-learning, Policy Gradients)
- PyTorch or TensorFlow proficiency
- Basic robotics concepts (kinematics, control)

Prerequisites:
- Beginner level completion
- Strong programming fundamentals

Milestones:
- Implement YOLO or similar object detector
- Train a PPO agent in a simulated environment (e.g., Gym)
- Build a vision-based navigation system in AirSim
- Deploy a model on NVIDIA Jetson

Recommended Time Allocation:
- Daily: 3-4 hours
- Weekly: 20-25 hours
- Total: ~1,000 hours
""")

doc.add_heading('🟠 ADVANCED (18-36 Months)', 3)
doc.add_paragraph("""
Goal: Specialize in autonomous drone systems and push state-of-the-art.

Skills Required:
- Advanced RL (PPO, SAC, TD3, multi-agent RL)
- Sensor fusion (Kalman filters, factor graphs)
- Edge AI optimization (quantization, pruning, distillation)
- ROS2 and robotics middleware
- Formal verification and safety-critical systems

Prerequisites:
- Intermediate level completion
- Research-level understanding of DL/RL

Milestones:
- Publish a paper at a relevant conference (ICRA, IROS, NeurIPS)
- Build a complete autonomous drone system from sensor to actuator
- Implement federated learning for drone swarms
- Optimize a model to run at 30+ FPS on Jetson

Recommended Time Allocation:
- Daily: 4-5 hours
- Weekly: 25-30 hours
- Total: ~1,500-2,000 hours
""")

doc.add_heading('🔴 EXPERT (3-5+ Years)', 3)
doc.add_paragraph("""
Goal: Lead research or development teams, define architectural decisions, contribute to standards.

Skills Required:
- All advanced skills plus:
- System architecture design
- Project leadership
- Cross-domain expertise (electronics, aerospace, communications)
- Research methodology
- Technology strategy

Prerequisites:
- Advanced level completion
- Demonstrated expertise (publications, shipped products)

Milestones:
- Lead a successful autonomy project
- Contribute to open-source autonomous drone frameworks
- Advise on national defense AI strategy
- Mentor others in the field
""")

doc.add_heading('2.2 Knowledge Map: Concepts & Dependencies', 2)
doc.add_paragraph("""
Critical Path (Must-Learn in Order):
1. Python + Linear Algebra
2. Calculus + Basic Statistics
3. Machine Learning Fundamentals
4. Deep Learning (CNNs)
5. PyTorch/TensorFlow
6. Computer Vision Basics
7. Reinforcement Learning (Q-learning → Policy Gradients → PPO)
8. ROS2 & Robot Control
9. Sensor Fusion
10. Edge AI Optimization
11. Autonomous Drone Systems

The knowledge hierarchy flows from foundational mathematics through programming, to machine learning, then splits into computer vision and reinforcement learning branches, which converge in robotics and control, then edge AI deployment, and finally autonomous drone systems.
""")

# PART 3: LEARNING RESOURCES
doc.add_page_break()
doc.add_heading('PART 3: LEARNING RESOURCES', 1)

doc.add_heading('3.1 Best Books', 2)
table3 = doc.add_table(rows=8, cols=4)
table3.style = 'Table Grid'
table3.rows[0].cells[0].text = 'Topic'
table3.rows[0].cells[1].text = 'Book'
table3.rows[0].cells[2].text = 'Author'
table3.rows[0].cells[3].text = 'Why'
table3.rows[1].cells[0].text = 'ML Fundamentals'
table3.rows[1].cells[1].text = 'Pattern Recognition and Machine Learning'
table3.rows[1].cells[2].text = 'Bishop'
table3.rows[1].cells[3].text = 'Comprehensive mathematical foundation'
table3.rows[2].cells[0].text = 'Deep Learning'
table3.rows[2].cells[1].text = 'Deep Learning'
table3.rows[2].cells[2].text = 'Goodfellow, Bengio, Courville'
table3.rows[2].cells[3].text = 'The "Bible" of DL'
table3.rows[3].cells[0].text = 'Computer Vision'
table3.rows[3].cells[1].text = 'Computer Vision: Algorithms and Applications'
table3.rows[3].cells[2].text = 'Szeliski'
table3.rows[3].cells[3].text = 'Practical, comprehensive'
table3.rows[4].cells[0].text = 'Reinforcement Learning'
table3.rows[4].cells[1].text = 'Reinforcement Learning: An Introduction'
table3.rows[4].cells[2].text = 'Sutton & Barto'
table3.rows[4].cells[3].text = 'The definitive RL text'
table3.rows[5].cells[0].text = 'Robotics'
table3.rows[5].cells[1].text = 'Probabilistic Robotics'
table3.rows[5].cells[2].text = 'Thrun, Burgard, Fox'
table3.rows[5].cells[3].text = 'SLAM, localization, Kalman filters'
table3.rows[6].cells[0].text = 'Optimal Control'
table3.rows[6].cells[1].text = 'Optimal Control and Estimation'
table3.rows[6].cells[2].text = 'Stengel'
table3.rows[6].cells[3].text = 'Control theory for autonomous systems'
table3.rows[7].cells[0].text = 'UAV Autonomy'
table3.rows[7].cells[1].text = 'Unmanned Aircraft Systems'
table3.rows[7].cells[2].text = 'Valavanis & Vachtsevanos'
table3.rows[7].cells[3].text = 'Domain-specific systems'

doc.add_heading('3.2 Best Courses', 2)
table4 = doc.add_table(rows=11, cols=4)
table4.style = 'Table Grid'
table4.rows[0].cells[0].text = 'Course'
table4.rows[0].cells[1].text = 'Platform'
table4.rows[0].cells[2].text = 'Focus'
table4.rows[0].cells[3].text = 'Estimated Time'
table4.rows[1].cells[0].text = 'CS231n: CNNs for Visual Recognition'
table4.rows[1].cells[1].text = 'Stanford'
table4.rows[1].cells[2].text = 'Computer Vision'
table4.rows[1].cells[3].text = '3 months'
table4.rows[2].cells[0].text = 'CS224n: NLP with Deep Learning'
table4.rows[2].cells[1].text = 'Stanford'
table4.rows[2].cells[2].text = 'NLP'
table4.rows[2].cells[3].text = '3 months'
table4.rows[3].cells[0].text = 'CS285: Deep Reinforcement Learning'
table4.rows[3].cells[1].text = 'UC Berkeley'
table4.rows[3].cells[2].text = 'RL'
table4.rows[3].cells[3].text = '3 months'
table4.rows[4].cells[0].text = 'Deep Learning Specialization'
table4.rows[4].cells[1].text = 'Coursera (DeepLearning.AI)'
table4.rows[4].cells[2].text = 'DL Fundamentals'
table4.rows[4].cells[3].text = '3 months'
table4.rows[5].cells[0].text = 'Reinforcement Learning Specialization'
table4.rows[5].cells[1].text = 'Coursera (UAlberta)'
table4.rows[5].cells[2].text = 'RL'
table4.rows[5].cells[3].text = '2 months'
table4.rows[6].cells[0].text = 'Robotics: Perception'
table4.rows[6].cells[1].text = 'Coursera (UPenn)'
table4.rows[6].cells[2].text = 'Computer Vision for Robotics'
table4.rows[6].cells[3].text = '4 weeks'
table4.rows[7].cells[0].text = 'Robotics: Estimation and Learning'
table4.rows[7].cells[1].text = 'Coursera (UPenn)'
table4.rows[7].cells[2].text = 'State estimation, SLAM'
table4.rows[7].cells[3].text = '4 weeks'
table4.rows[8].cells[0].text = 'Control of Mobile Robots'
table4.rows[8].cells[1].text = 'Coursera (Georgia Tech)'
table4.rows[8].cells[2].text = 'Control theory'
table4.rows[8].cells[3].text = '4 weeks'
table4.rows[9].cells[0].text = 'Aerial Robotics'
table4.rows[9].cells[1].text = 'Coursera (UPenn)'
table4.rows[9].cells[2].text = 'Drones specifically'
table4.rows[9].cells[3].text = '4 weeks'
table4.rows[10].cells[0].text = 'ROS2 for Beginners'
table4.rows[10].cells[1].text = 'The Construct'
table4.rows[10].cells[2].text = 'ROS2'
table4.rows[10].cells[3].text = '2 weeks'

doc.add_heading('3.3 University Lectures (Free)', 2)
table5 = doc.add_table(rows=5, cols=3)
table5.style = 'Table Grid'
table5.rows[0].cells[0].text = 'Institution'
table5.rows[0].cells[1].text = 'Course'
table5.rows[0].cells[2].text = 'Focus'
table5.rows[1].cells[0].text = 'MIT'
table5.rows[1].cells[1].text = '6.S191: Intro to Deep Learning'
table5.rows[1].cells[2].text = 'DL Fundamentals'
table5.rows[2].cells[0].text = 'Stanford'
table5.rows[2].cells[1].text = 'CS231n (see above)'
table5.rows[2].cells[2].text = 'CV'
table5.rows[3].cells[0].text = 'UC Berkeley'
table5.rows[3].cells[1].text = 'CS188: Intro to AI'
table5.rows[3].cells[2].text = 'AI Fundamentals'
table5.rows[4].cells[0].text = 'ETH Zurich'
table5.rows[4].cells[1].text = 'Autonomous Mobile Robots'
table5.rows[4].cells[2].text = 'Robotics'

doc.add_heading('3.4 YouTube Channels', 2)
table6 = doc.add_table(rows=8, cols=3)
table6.style = 'Table Grid'
table6.rows[0].cells[0].text = 'Channel'
table6.rows[0].cells[1].text = 'Focus'
table6.rows[0].cells[2].text = 'Level'
table6.rows[1].cells[0].text = 'Two Minute Papers'
table6.rows[1].cells[1].text = 'AI research summaries'
table6.rows[1].cells[2].text = 'All'
table6.rows[2].cells[0].text = 'Yannic Kilcher'
table6.rows[2].cells[1].text = 'Deep learning paper explanations'
table6.rows[2].cells[2].text = 'Advanced'
table6.rows[3].cells[0].text = 'Sentdex'
table6.rows[3].cells[1].text = 'Practical ML/DL coding'
table6.rows[3].cells[2].text = 'Intermediate'
table6.rows[4].cells[0].text = 'Siraj Raval'
table6.rows[4].cells[1].text = 'ML/DL project tutorials'
table6.rows[4].cells[2].text = 'Beginner'
table6.rows[5].cells[0].text = 'The Construct'
table6.rows[5].cells[1].text = 'ROS tutorials'
table6.rows[5].cells[2].text = 'All'
table6.rows[6].cells[0].text = 'OpenCV'
table6.rows[6].cells[1].text = 'Computer vision tutorials'
table6.rows[6].cells[2].text = 'Intermediate'
table6.rows[7].cells[0].text = 'NVIDIA Developer'
table6.rows[7].cells[1].text = 'Edge AI & Jetson'
table6.rows[7].cells[2].text = 'Intermediate/Advanced'

doc.add_heading('3.5 Research Papers (Essential Reading)', 2)
doc.add_paragraph("""
Foundational Papers:
- AlexNet - "ImageNet Classification with Deep CNNs" (2012) - Starting point for modern CV
- YOLO - "You Only Look Once" (2015/2016) - Real-time object detection
- DQN - "Playing Atari with Deep RL" (2013) - Deep RL breakthrough
- PPO - "Proximal Policy Optimization" (2017) - State-of-the-art RL algorithm
- Federated Learning - "Communication-Efficient Learning of Deep Networks" (2017)

UAV Autonomy Papers:
- FDRL for GPS-Denied Navigation (IEEE 2025) - Federated DRL framework integrating YOLOv8 and PPO
- Deep-PPO for MAV Navigation (arXiv 2025) - End-to-end training with 91% training time reduction
- Event-Based Drone Detection (ICCVW 2025) - Neuromorphic vision for drone detection

Where to Find Papers:
- Google Scholar (set alerts for key topics)
- IEEE Xplore
- arXiv (cs.AI, cs.RO, cs.CV)
- Papers with Code (implementation + paper)
""")

doc.add_heading('3.6 Documentation & Frameworks', 2)
table7 = doc.add_table(rows=9, cols=2)
table7.style = 'Table Grid'
table7.rows[0].cells[0].text = 'Resource'
table7.rows[0].cells[1].text = 'Purpose'
table7.rows[1].cells[0].text = 'PyTorch Docs'
table7.rows[1].cells[1].text = 'Primary DL framework'
table7.rows[2].cells[0].text = 'TensorFlow Lite'
table7.rows[2].cells[1].text = 'Edge deployment'
table7.rows[3].cells[0].text = 'ROS2 Documentation'
table7.rows[3].cells[1].text = 'Robotics middleware'
table7.rows[4].cells[0].text = 'PX4/ArduPilot Docs'
table7.rows[4].cells[1].text = 'Flight controllers'
table7.rows[5].cells[0].text = 'NVIDIA Jetson Docs'
table7.rows[5].cells[1].text = 'Edge hardware'
table7.rows[6].cells[0].text = 'OpenCV Docs'
table7.rows[6].cells[1].text = 'Computer vision library'
table7.rows[7].cells[0].text = 'AirSim Documentation'
table7.rows[7].cells[1].text = 'Drone simulation'
table7.rows[8].cells[0].text = 'MAVSDK'
table7.rows[8].cells[1].text = 'Drone control API'

doc.add_heading('3.7 Communities', 2)
table8 = doc.add_table(rows=7, cols=3)
table8.style = 'Table Grid'
table8.rows[0].cells[0].text = 'Platform'
table8.rows[0].cells[1].text = 'Community'
table8.rows[0].cells[2].text = 'Focus'
table8.rows[1].cells[0].text = 'Reddit'
table8.rows[1].cells[1].text = 'r/MachineLearning, r/computervision, r/robotics'
table8.rows[1].cells[2].text = 'Discussion, news'
table8.rows[2].cells[0].text = 'Discord'
table8.rows[2].cells[1].text = 'Various open-source drone/AI Discord servers'
table8.rows[2].cells[2].text = 'Real-time help'
table8.rows[3].cells[0].text = 'Stack Overflow'
table8.rows[3].cells[1].text = '#pytorch, #tensorflow, #ros'
table8.rows[3].cells[2].text = 'Technical Q&A'
table8.rows[4].cells[0].text = 'GitHub'
table8.rows[4].cells[1].text = 'Open-source drone autonomy projects'
table8.rows[4].cells[2].text = 'Code collaboration'
table8.rows[5].cells[0].text = 'LinkedIn'
table8.rows[5].cells[1].text = 'Defense AI groups'
table8.rows[5].cells[2].text = 'Professional networking'
table8.rows[6].cells[0].text = 'IEEE'
table8.rows[6].cells[1].text = 'Robotics & Automation Society'
table8.rows[6].cells[2].text = 'Academic/professional'

doc.add_heading('3.8 Newsletters', 2)
table9 = doc.add_table(rows=5, cols=2)
table9.style = 'Table Grid'
table9.rows[0].cells[0].text = 'Newsletter'
table9.rows[0].cells[1].text = 'Focus'
table9.rows[1].cells[0].text = 'The Batch (DeepLearning.AI)'
table9.rows[1].cells[1].text = 'Weekly AI news'
table9.rows[2].cells[0].text = 'Import AI'
table9.rows[2].cells[1].text = 'AI research and policy'
table9.rows[3].cells[0].text = 'AI Alignment Newsletter'
table9.rows[3].cells[1].text = 'Safety/alignment'
table9.rows[4].cells[0].text = 'Robotics Weekly'
table9.rows[4].cells[1].text = 'Robotics news'

doc.add_heading('3.9 Podcasts', 2)
table10 = doc.add_table(rows=5, cols=3)
table10.style = 'Table Grid'
table10.rows[0].cells[0].text = 'Podcast'
table10.rows[0].cells[1].text = 'Focus'
table10.rows[0].cells[2].text = 'Hosts'
table10.rows[1].cells[0].text = 'Lex Fridman Podcast'
table10.rows[1].cells[1].text = 'AI, robotics, defense'
table10.rows[1].cells[2].text = 'Lex Fridman'
table10.rows[2].cells[0].text = 'Financial Freedom (episode with Jesse Hamel)'
table10.rows[2].cells[1].text = 'Drone autonomy startups'
table10.rows[2].cells[2].text = 'Jesse Hamel'
table10.rows[3].cells[0].text = 'Robot Brains Podcast'
table10.rows[3].cells[1].text = 'Robotics research'
table10.rows[3].cells[2].text = 'Pieter Abbeel'
table10.rows[4].cells[0].text = 'The AI Podcast'
table10.rows[4].cells[1].text = 'NVIDIA\'s AI podcast'
table10.rows[4].cells[2].text = 'Various'

# PART 4: TOOLS AND TECHNOLOGIES
doc.add_page_break()
doc.add_heading('PART 4: TOOLS AND TECHNOLOGIES', 1)

doc.add_heading('4.1 Core Tools Matrix', 2)
table11 = doc.add_table(rows=12, cols=6)
table11.style = 'Table Grid'
table11.rows[0].cells[0].text = 'Tool'
table11.rows[0].cells[1].text = 'Purpose'
table11.rows[0].cells[2].text = 'Alternatives'
table11.rows[0].cells[3].text = 'Pros'
table11.rows[0].cells[4].text = 'Cons'
table11.rows[0].cells[5].text = 'When to Choose'
table11.rows[1].cells[0].text = 'PyTorch'
table11.rows[1].cells[1].text = 'DL Framework'
table11.rows[1].cells[2].text = 'TensorFlow'
table11.rows[1].cells[3].text = 'Dynamic graphs, Pythonic, research-friendly'
table11.rows[1].cells[4].text = 'Mobile deployment less mature'
table11.rows[1].cells[5].text = 'Research, prototyping, custom architectures'
table11.rows[2].cells[0].text = 'TensorFlow'
table11.rows[2].cells[1].text = 'DL Framework'
table11.rows[2].cells[2].text = 'PyTorch'
table11.rows[2].cells[3].text = 'Production-ready, TF Lite'
table11.rows[2].cells[4].text = 'Static graphs (TF1), steeper learning'
table11.rows[2].cells[5].text = 'Production deployment, industry environments'
table11.rows[3].cells[0].text = 'YOLOv8/v11'
table11.rows[3].cells[1].text = 'Object Detection'
table11.rows[3].cells[2].text = 'Faster R-CNN, DETR'
table11.rows[3].cells[3].text = 'Fastest real-time detection, good accuracy'
table11.rows[3].cells[4].text = 'Less accurate than two-stage on small objects'
table11.rows[3].cells[5].text = 'Any real-time drone perception'
table11.rows[4].cells[0].text = 'YOLOv8n (nano)'
table11.rows[4].cells[1].text = 'Lightweight Detection'
table11.rows[4].cells[2].text = 'MobileNet-SSD'
table11.rows[4].cells[3].text = 'Optimized for edge: 40 TOPS minimal'
table11.rows[4].cells[4].text = 'Lower accuracy than larger variants'
table11.rows[4].cells[5].text = 'Jetson Nano, Coral, resource-constrained'
table11.rows[5].cells[0].text = 'PPO'
table11.rows[5].cells[1].text = 'RL Algorithm'
table11.rows[5].cells[2].text = 'SAC, TD3, DQN'
table11.rows[5].cells[3].text = 'Stable, sample-efficient'
table11.rows[5].cells[4].text = 'Hyperparameter sensitive'
table11.rows[5].cells[5].text = 'Continuous control, navigation, decision-making'
table11.rows[6].cells[0].text = 'ROS2'
table11.rows[6].cells[1].text = 'Robotics Middleware'
table11.rows[6].cells[2].text = 'None (industry standard)'
table11.rows[6].cells[3].text = 'Ecosystem, integration with simulation'
table11.rows[6].cells[4].text = 'Learning curve'
table11.rows[6].cells[5].text = 'Any drone software architecture'
table11.rows[7].cells[0].text = 'MAVSDK/MAVROS'
table11.rows[7].cells[1].text = 'Drone Control API'
table11.rows[7].cells[2].text = 'PX4 offboard API'
table11.rows[7].cells[3].text = 'High-level commands, cross-platform'
table11.rows[7].cells[4].text = 'Limited low-level access'
table11.rows[7].cells[5].text = 'Talking to PX4/ArduPilot flight controllers'
table11.rows[8].cells[0].text = 'AirSim'
table11.rows[8].cells[1].text = 'Simulation'
table11.rows[8].cells[2].text = 'Gazebo, CopterSim'
table11.rows[8].cells[3].text = 'Realistic physics, UE4 graphics'
table11.rows[8].cells[4].text = 'Heavy resource usage'
table11.rows[8].cells[5].text = 'Perception and navigation simulation'
table11.rows[9].cells[0].text = 'Gazebo'
table11.rows[9].cells[1].text = 'Simulation'
table11.rows[9].cells[2].text = 'AirSim'
table11.rows[9].cells[3].text = 'ROS integration, lighter'
table11.rows[9].cells[4].text = 'Less realistic graphics'
table11.rows[9].cells[5].text = 'System-level testing, CI/CD'
table11.rows[10].cells[0].text = 'Jetson Orin Nano'
table11.rows[10].cells[1].text = 'Edge AI Hardware'
table11.rows[10].cells[2].text = 'Google Coral, Intel Movidius'
table11.rows[10].cells[3].text = 'Up to 40-67 TOPS, 7-15W, 30x improvement'
table11.rows[10].cells[4].text = 'Cost ($100-2K), availability'
table11.rows[10].cells[5].text = 'Production deployment, real-time inference'
table11.rows[11].cells[0].text = 'TensorRT'
table11.rows[11].cells[1].text = 'Model Optimization'
table11.rows[11].cells[2].text = 'ONNX Runtime, OpenVINO'
table11.rows[11].cells[3].text = '2-4x faster inference, 4x smaller models'
table11.rows[11].cells[4].text = 'NVIDIA-only'
table11.rows[11].cells[5].text = 'Jetson inference optimization'

doc.add_heading('4.2 Tool Selection Guide', 2)
doc.add_paragraph("""
- BEGINNER → Start with PyTorch + OpenCV + AirSim
- INTERMEDIATE → Add ROS2, MAVSDK, Jetson, YOLO
- ADVANCED → Master TensorRT, quantization, PPO/SAC, federated learning
- EXPERT → Build custom architectures, hardware-aware NAS, formal verification
""")

# PART 5: CAREER PATHS
doc.add_page_break()
doc.add_heading('PART 5: CAREER PATHS', 1)

doc.add_heading('5.1 Roles, Responsibilities & Salaries', 2)
table12 = doc.add_table(rows=10, cols=4)
table12.style = 'Table Grid'
table12.rows[0].cells[0].text = 'Role'
table12.rows[0].cells[1].text = 'Responsibilities'
table12.rows[0].cells[2].text = 'Key Skills'
table12.rows[0].cells[3].text = 'UK Salary'
table12.rows[1].cells[0].text = 'AI Drone Developer'
table12.rows[1].cells[1].text = 'Design/implement AI algorithms for autonomy'
table12.rows[1].cells[2].text = 'PyTorch, CV, ML'
table12.rows[1].cells[3].text = '£50-80K'
table12.rows[2].cells[0].text = 'UAV Data Scientist'
table12.rows[2].cells[1].text = 'Process aerial data, build ML models'
table12.rows[2].cells[2].text = 'Python, geospatial, ML'
table12.rows[2].cells[3].text = '£55K+'
table12.rows[3].cells[0].text = 'Autonomous Systems Engineer'
table12.rows[3].cells[1].text = 'Integrate AI, robotics, control'
table12.rows[3].cells[2].text = 'Robotics, ROS, ML'
table12.rows[3].cells[3].text = '£60-85K'
table12.rows[4].cells[0].text = 'ML Engineer (UAV)'
table12.rows[4].cells[1].text = 'Develop models for perception/decision'
table12.rows[4].cells[2].text = 'DL, RL, optimization'
table12.rows[4].cells[3].text = '£78K+'
table12.rows[5].cells[0].text = 'UAV Avionics Engineer'
table12.rows[5].cells[1].text = 'Hardware/software integration'
table12.rows[5].cells[2].text = 'Embedded systems, controls'
table12.rows[5].cells[3].text = '£50-75K'
table12.rows[6].cells[0].text = 'AI Autonomy Engineer'
table12.rows[6].cells[1].text = 'End-to-end autonomy systems'
table12.rows[6].cells[2].text = 'All of the above'
table12.rows[6].cells[3].text = '£70-90K'
table12.rows[7].cells[0].text = 'Drone Systems Designer'
table12.rows[7].cells[1].text = 'System architecture, integration'
table12.rows[7].cells[2].text = 'Systems engineering'
table12.rows[7].cells[3].text = '£60-80K'
table12.rows[8].cells[0].text = 'UAS Operations Manager'
table12.rows[8].cells[1].text = 'Drone fleet oversight'
table12.rows[8].cells[2].text = 'Ops, safety, regulations'
table12.rows[8].cells[3].text = '£50-80K'
table12.rows[9].cells[0].text = 'SWARM Specialist'
table12.rows[9].cells[1].text = 'Multi-agent coordination'
table12.rows[9].cells[2].text = 'Distributed RL, communication'
table12.rows[9].cells[3].text = '£70-85K'

doc.add_heading('5.2 Personality-Type Fit', 2)
table13 = doc.add_table(rows=5, cols=2)
table13.style = 'Table Grid'
table13.rows[0].cells[0].text = 'Role'
table13.rows[0].cells[1].text = 'Best Personality'
table13.rows[1].cells[0].text = 'Researcher'
table13.rows[1].cells[1].text = 'Curious, detail-oriented, patient, enjoys theoretical challenges'
table13.rows[2].cells[0].text = 'Engineer (Product)'
table13.rows[2].cells[1].text = 'Practical, delivery-focused, enjoys building things that work'
table13.rows[3].cells[0].text = 'Entrepreneur'
table13.rows[3].cells[1].text = 'Risk-tolerant, visionary, strategic, understands markets'
table13.rows[4].cells[0].text = 'Consultant'
table13.rows[4].cells[1].text = 'Communicative, broad knowledge, enjoys problem-solving for others'

doc.add_heading('5.3 Career Progression Path', 2)
doc.add_paragraph("""
BEGINNER
  ↓
Junior AI Engineer (1-2 years)
  ↓
AI Engineer / ML Engineer (2-5 years)
  ↓
Senior AI Engineer / Lead (5-8 years)
  ↓
Principal Engineer / Manager (8-12 years)
  ↓
Director / CTO / VP (12+ years)
  OR
Researcher → Senior Researcher → Research Scientist → Principal Scientist
""")

# PART 6: SPECIALIZATION DECISIONS
doc.add_page_break()
doc.add_heading('PART 6: SPECIALIZATION DECISIONS', 1)

doc.add_heading('6.1 Deep Dive: Navigation (RL) vs. Perception (CV)', 2)

doc.add_heading('Perception (CV)', 3)
doc.add_paragraph("""
What You Build: Models that see and understand the environment—detect drones, classify friend/foe, track targets.

Technical Depth:
- CNNs (YOLO, EfficientNet, DETR)
- Tracking (SORT, DeepSORT)
- Multi-modal fusion (RGB + Thermal + Depth)

When to Choose: You enjoy visual data, image processing, and want to see immediate results.
""")

doc.add_heading('Navigation (RL)', 3)
doc.add_paragraph("""
What You Build: The decision-making engine—how the drone moves, where it goes, when it engages.

Technical Depth:
- MDPs, Bellman equations
- Policy Gradients, PPO, SAC
- Reward engineering
- Sim-to-real transfer

When to Choose: You enjoy decision theory, control, and the challenge of dynamic environments.

Recommendation: Learn both. The strongest autonomous drone engineers understand the complete pipeline.
""")

# PART 7: DECISION FRAMEWORK
doc.add_page_break()
doc.add_heading('PART 7: DECISION FRAMEWORK', 1)

doc.add_heading('7.1 Career Decision Matrix', 2)
table14 = doc.add_table(rows=8, cols=3)
table14.style = 'Table Grid'
table14.rows[0].cells[0].text = 'Your Situation'
table14.rows[0].cells[1].text = 'Recommended Path'
table14.rows[0].cells[2].text = 'Why'
table14.rows[1].cells[0].text = 'Student (Undergrad)'
table14.rows[1].cells[1].text = 'Academic or Industry (internships)'
table14.rows[1].cells[2].text = 'Build foundation, explore options'
table14.rows[2].cells[0].text = 'Master\'s Student'
table14.rows[2].cells[1].text = 'Industry (specialized) or PhD'
table14.rows[2].cells[2].text = 'Leverage advanced degree'
table14.rows[3].cells[0].text = 'PhD Candidate'
table14.rows[3].cells[1].text = 'Academic Research or R&D Lab'
table14.rows[3].cells[2].text = 'Deep expertise needed for these roles'
table14.rows[4].cells[0].text = 'Career Changer (tech background)'
table14.rows[4].cells[1].text = 'Bootcamp + Self-study → Industry'
table14.rows[4].cells[2].text = 'Leverage existing coding skills'
table14.rows[5].cells[0].text = 'Career Changer (non-tech)'
table14.rows[5].cells[1].text = 'Certifications + Projects → Entry-level'
table14.rows[5].cells[2].text = 'Start from foundational concepts'
table14.rows[6].cells[0].text = 'Entrepreneurial'
table14.rows[6].cells[1].text = 'Startup (founder or early employee)'
table14.rows[6].cells[2].text = 'Need risk tolerance, drive'
table14.rows[7].cells[0].text = 'Risk-averse/Seeking Stability'
table14.rows[7].cells[1].text = 'Government/Defense or Large Corp'
table14.rows[7].cells[2].text = 'Stability, benefits'

doc.add_heading('7.2 Technical Depth Decision Tree', 2)
doc.add_paragraph("""
What do you enjoy?
├─ Visual Data & Images → Perception Specialist
├─ Decisions/Control → Navigation Specialist
└─ Building/Systems → Integration Specialist
     ↓
Autonomous Systems Expert (All Three)
""")

# PART 8: PROJECTS
doc.add_page_break()
doc.add_heading('PART 8: PROJECTS', 1)

doc.add_heading('8.1 Beginner Projects (0-6 months)', 2)
table15 = doc.add_table(rows=6, cols=3)
table15.style = 'Table Grid'
table15.rows[0].cells[0].text = 'Project'
table15.rows[0].cells[1].text = 'Skills Learned'
table15.rows[0].cells[2].text = 'Time'
table15.rows[1].cells[0].text = 'MNIST Classifier'
table15.rows[1].cells[1].text = 'Basic CNN, PyTorch/TF'
table15.rows[1].cells[2].text = '1-2 weeks'
table15.rows[2].cells[0].text = 'Object Detection in Images'
table15.rows[2].cells[1].text = 'YOLO inference, OpenCV'
table15.rows[2].cells[2].text = '2-4 weeks'
table15.rows[3].cells[0].text = 'Simulated Drone Hover'
table15.rows[3].cells[1].text = 'PID control, simulation'
table15.rows[3].cells[2].text = '1-2 weeks'
table15.rows[4].cells[0].text = 'Image Classification (CIFAR-10)'
table15.rows[4].cells[1].text = 'Training, overfitting, data augmentation'
table15.rows[4].cells[2].text = '2-4 weeks'
table15.rows[5].cells[0].text = 'Flight Path Visualization'
table15.rows[5].cells[1].text = 'Data handling, plotting, basic analysis'
table15.rows[5].cells[2].text = '1-2 weeks'

doc.add_heading('8.2 Intermediate Projects (6-18 months)', 2)
table16 = doc.add_table(rows=6, cols=3)
table16.style = 'Table Grid'
table16.rows[0].cells[0].text = 'Project'
table16.rows[0].cells[1].text = 'Skills Learned'
table16.rows[0].cells[2].text = 'Time'
table16.rows[1].cells[0].text = 'Drone Object Detection (Real-time)'
table16.rows[1].cells[1].text = 'YOLO + OpenCV, performance optimization'
table16.rows[1].cells[2].text = '1-2 months'
table16.rows[2].cells[0].text = 'Vision-Based Obstacle Avoidance'
table16.rows[2].cells[1].text = 'Perception → Action pipeline'
table16.rows[2].cells[2].text = '2-3 months'
table16.rows[3].cells[0].text = 'Deep RL in AirSim (Basic)'
table16.rows[3].cells[1].text = 'PPO with continuous action space'
table16.rows[3].cells[2].text = '2-3 months'
table16.rows[4].cells[0].text = 'Sensor Fusion (IMU + Camera)'
table16.rows[4].cells[1].text = 'Kalman filters, coordinate transforms'
table16.rows[4].cells[2].text = '1-2 months'
table16.rows[5].cells[0].text = 'ROS2 + Drone Simulation'
table16.rows[5].cells[1].text = 'ROS2 nodes, MAVSDK, Gazebo'
table16.rows[5].cells[2].text = '1-2 months'

doc.add_heading('8.3 Advanced Projects (18-36 months)', 2)
table17 = doc.add_table(rows=6, cols=3)
table17.style = 'Table Grid'
table17.rows[0].cells[0].text = 'Project'
table17.rows[0].cells[1].text = 'Skills Learned'
table17.rows[0].cells[2].text = 'Time'
table17.rows[1].cells[0].text = 'Full GPS-Denied Navigation'
table17.rows[1].cells[1].text = 'VIO, SLAM, RL policy, sensor fusion'
table17.rows[1].cells[2].text = '3-6 months'
table17.rows[2].cells[0].text = 'Multi-Agent Swarm Coordination'
table17.rows[2].cells[1].text = 'Federated learning, communication protocols'
table17.rows[2].cells[2].text = '6-12 months'
table17.rows[3].cells[0].text = 'Event Camera-Based Detection'
table17.rows[3].cells[1].text = 'Neuromorphic vision, spiking NNs'
table17.rows[3].cells[2].text = '4-8 months'
table17.rows[4].cells[0].text = 'End-to-End Autonomous Combat'
table17.rows[4].cells[1].text = 'Perception + decision + control + failsafe'
table17.rows[4].cells[2].text = '6-12 months'
table17.rows[5].cells[0].text = 'Model Optimization for Edge'
table17.rows[5].cells[1].text = 'Quantization, pruning, TensorRT, ONNX'
table17.rows[5].cells[2].text = '2-4 months'

doc.add_heading('8.4 Portfolio-Worthy Projects', 2)
doc.add_paragraph("""
1. GPS-Denied Autonomous Drone: A complete system that navigates a drone through an obstacle course without GPS, using only onboard sensors. Show:
- Architecture diagram
- Training results
- Real-world (or high-fidelity simulation) video
- Performance metrics (success rate, latency, computational cost)

2. Defensive Target Tracking System: A drone that detects, tracks, and autonomously follows a target while avoiding obstacles. Demonstrate:
- Detection accuracy (mAP, F1)
- Tracking robustness (MOTA, IDF1)
- Decision-making (engagement vs. evasion)

3. Federated Swarm Coordination: Multiple drones learning collaboratively. Show:
- Communication protocol
- Learning curve with/without federated learning
- Emergent swarm behaviors
""")

doc.add_heading('8.5 Research Projects', 2)
table18 = doc.add_table(rows=4, cols=3)
table18.style = 'Table Grid'
table18.rows[0].cells[0].text = 'Topic'
table18.rows[0].cells[1].text = 'Description'
table18.rows[0].cells[2].text = 'Reference'
table18.rows[1].cells[0].text = 'FDRL for GPS-Denied Navigation'
table18.rows[1].cells[1].text = 'Federated deep RL with YOLOv8 and PPO'
table18.rows[1].cells[2].text = 'IEEE 2025'
table18.rows[2].cells[0].text = 'Deep-PPO for MAVs'
table18.rows[2].cells[1].text = 'End-to-end training with 91% training time reduction'
table18.rows[2].cells[2].text = 'arXiv 2025'
table18.rows[3].cells[0].text = 'Event Camera Detection'
table18.rows[3].cells[1].text = 'Spiking neural networks for low-latency drone detection'
table18.rows[3].cells[2].text = 'ICCVW 2025'

# PART 9: COMMON MISTAKES
doc.add_page_break()
doc.add_heading('PART 9: COMMON MISTAKES', 1)

doc.add_heading('9.1 Beginner Mistakes', 2)
table19 = doc.add_table(rows=7, cols=3)
table19.style = 'Table Grid'
table19.rows[0].cells[0].text = 'Mistake'
table19.rows[0].cells[1].text = 'Why It\'s Wrong'
table19.rows[0].cells[2].text = 'How to Avoid'
table19.rows[1].cells[0].text = 'Jumping to advanced topics too soon'
table19.rows[1].cells[1].text = 'Lack fundamentals → confusion'
table19.rows[1].cells[2].text = 'Follow a structured curriculum'
table19.rows[2].cells[0].text = 'Only reading, not coding'
table19.rows[2].cells[1].text = 'Passive learning doesn\'t build skills'
table19.rows[2].cells[2].text = 'Code every day, even if small'
table19.rows[3].cells[0].text = 'Ignoring mathematics'
table19.rows[3].cells[1].text = 'DL/RL is applied math'
table19.rows[3].cells[2].text = 'Review linear algebra and calculus early'
table19.rows[4].cells[0].text = 'Not using version control'
table19.rows[4].cells[1].text = 'Hard to track changes, collaborate'
table19.rows[4].cells[2].text = 'Use Git from day one'
table19.rows[5].cells[0].text = 'Skipping simulation'
table19.rows[5].cells[1].text = 'Real hardware is expensive and slow'
table19.rows[5].cells[2].text = 'Start with AirSim/Gazebo'
table19.rows[6].cells[0].text = 'Over-relying on cloud compute'
table19.rows[6].cells[1].text = 'Real drone uses edge devices'
table19.rows[6].cells[2].text = 'Practice on local machines, optimize'

doc.add_heading('9.2 Intermediate Mistakes', 2)
table20 = doc.add_table(rows=6, cols=3)
table20.style = 'Table Grid'
table20.rows[0].cells[0].text = 'Mistake'
table20.rows[0].cells[1].text = 'Why It\'s Wrong'
table20.rows[0].cells[2].text = 'How to Avoid'
table20.rows[1].cells[0].text = 'Tuning hyperparameters randomly'
table20.rows[1].cells[1].text = 'Wastes time, poor results'
table20.rows[1].cells[2].text = 'Use systematic methods (Bayesian optimization)'
table20.rows[2].cells[0].text = 'Ignoring sim-to-real gap'
table20.rows[2].cells[1].text = 'Simulation ≠ reality'
table20.rows[2].cells[2].text = 'Test on real data early'
table20.rows[3].cells[0].text = 'Overfitting to benchmarks'
table20.rows[3].cells[1].text = 'Models don\'t generalize'
table20.rows[3].cells[2].text = 'Cross-validate, test on varied data'
table20.rows[4].cells[0].text = 'Poor reward design in RL'
table20.rows[4].cells[1].text = 'Agent learns wrong behavior'
table20.rows[4].cells[2].text = 'Iterate, visualize rewards, use curriculum learning'
table20.rows[5].cells[0].text = 'Not optimizing for edge'
table20.rows[5].cells[1].text = 'Models won\'t run in real-time'
table20.rows[5].cells[2].text = 'Start with small models, profile early'

doc.add_heading('9.3 Advanced Mistakes', 2)
table21 = doc.add_table(rows=6, cols=3)
table21.style = 'Table Grid'
table21.rows[0].cells[0].text = 'Mistake'
table21.rows[0].cells[1].text = 'Why It\'s Wrong'
table21.rows[0].cells[2].text = 'How to Avoid'
table21.rows[1].cells[0].text = 'Designing in isolation'
table21.rows[1].cells[1].text = 'Real drones need integration'
table21.rows[1].cells[2].text = 'Work with hardware engineers'
table21.rows[2].cells[0].text = 'Not considering safety'
table21.rows[2].cells[1].text = 'Defense systems must be trustworthy'
table21.rows[2].cells[2].text = 'Build fail-safes, formal verification'
table21.rows[3].cells[0].text = 'Ignoring data quality'
table21.rows[3].cells[1].text = 'Garbage in, garbage out'
table21.rows[3].cells[2].text = 'Build robust data pipelines'
table21.rows[4].cells[0].text = 'Over-engineering'
table21.rows[4].cells[1].text = 'Complexity without benefit'
table21.rows[4].cells[2].text = 'Start simple, add complexity when needed'
table21.rows[5].cells[0].text = 'Neglecting documentation'
table21.rows[5].cells[1].text = 'Hard to maintain, share'
table21.rows[5].cells[2].text = 'Document as you code'

# PART 10: STUDY PLAN
doc.add_page_break()
doc.add_heading('PART 10: STUDY PLAN', 1)

doc.add_heading('10.1 Daily Plan', 2)
table22 = doc.add_table(rows=6, cols=2)
table22.style = 'Table Grid'
table22.rows[0].cells[0].text = 'Time'
table22.rows[0].cells[1].text = 'Activity'
table22.rows[1].cells[0].text = 'Morning'
table22.rows[1].cells[1].text = 'Theory (read a book chapter or paper) - 1 hour'
table22.rows[2].cells[0].text = 'Mid-morning'
table22.rows[2].cells[1].text = 'Code (implement what you read) - 1.5 hours'
table22.rows[3].cells[0].text = 'Afternoon'
table22.rows[3].cells[1].text = 'Projects (work on your current project) - 2 hours'
table22.rows[4].cells[0].text = 'Evening'
table22.rows[4].cells[1].text = 'Review (write notes, reflect) - 30 mins'
table22.rows[5].cells[0].text = 'Total'
table22.rows[5].cells[1].text = '5 hours'

doc.add_heading('10.2 Weekly Plan', 2)
table23 = doc.add_table(rows=8, cols=3)
table23.style = 'Table Grid'
table23.rows[0].cells[0].text = 'Day'
table23.rows[0].cells[1].text = 'Focus'
table23.rows[0].cells[2].text = 'Activities'
table23.rows[1].cells[0].text = 'Monday'
table23.rows[1].cells[1].text = 'Theory'
table23.rows[1].cells[2].text = 'Read/book chapter, take notes'
table23.rows[2].cells[0].text = 'Tuesday'
table23.rows[2].cells[1].text = 'Coding'
table23.rows[2].cells[2].text = 'Implement algorithm from Monday\'s reading'
table23.rows[3].cells[0].text = 'Wednesday'
table23.rows[3].cells[1].text = 'Project'
table23.rows[3].cells[2].text = 'Work on portfolio project'
table23.rows[4].cells[0].text = 'Thursday'
table23.rows[4].cells[1].text = 'Papers'
table23.rows[4].cells[2].text = 'Read 1 research paper, summarize'
table23.rows[5].cells[0].text = 'Friday'
table23.rows[5].cells[1].text = 'Project/Revision'
table23.rows[5].cells[2].text = 'Continue project, revise week\'s learning'
table23.rows[6].cells[0].text = 'Saturday'
table23.rows[6].cells[1].text = 'Deep Work'
table23.rows[6].cells[2].text = '6-hour deep dive into a challenging topic'
table23.rows[7].cells[0].text = 'Sunday'
table23.rows[7].cells[1].text = 'Rest/Review'
table23.rows[7].cells[2].text = 'Light review, plan next week'

doc.add_heading('10.3 Monthly Milestones', 2)
table24 = doc.add_table(rows=13, cols=2)
table24.style = 'Table Grid'
table24.rows[0].cells[0].text = 'Month'
table24.rows[0].cells[1].text = 'Milestone'
table24.rows[1].cells[0].text = '1'
table24.rows[1].cells[1].text = 'Python proficiency; basic math review completed'
table24.rows[2].cells[0].text = '2'
table24.rows[2].cells[1].text = 'Linear regression; logistic regression implemented'
table24.rows[3].cells[0].text = '3'
table24.rows[3].cells[1].text = 'Neural network from scratch; basic CNN built'
table24.rows[4].cells[0].text = '4'
table24.rows[4].cells[1].text = 'Completed Deep Learning Specialization (or equivalent)'
table24.rows[5].cells[0].text = '5'
table24.rows[5].cells[1].text = 'Object detection in images (YOLO) implemented'
table24.rows[6].cells[0].text = '6'
table24.rows[6].cells[1].text = 'First project completed (e.g., image classifier)'
table24.rows[7].cells[0].text = '7'
table24.rows[7].cells[1].text = 'Reinforcement Learning fundamentals understood'
table24.rows[8].cells[0].text = '8'
table24.rows[8].cells[1].text = 'PPO implemented in a simple environment'
table24.rows[9].cells[0].text = '9'
table24.rows[9].cells[1].text = 'First ROS2 package created'
table24.rows[10].cells[0].text = '10'
table24.rows[10].cells[1].text = 'AirSim drone simulation running'
table24.rows[11].cells[0].text = '11'
table24.rows[11].cells[1].text = 'Sensor fusion (Kalman filter) implemented'
table24.rows[12].cells[0].text = '12'
table24.rows[12].cells[1].text = 'End-to-end autonomous drone project started'

doc.add_heading('10.4 One-Year Roadmap', 2)
doc.add_paragraph("""
Q1 (Months 1-3): FOUNDATION
- Python, Linear Algebra, Calculus, Probability
- Basic ML (Regression, Classification, Clustering)
- Deep Learning (NNs, CNNs, Backpropagation)

Q2 (Months 4-6): DEEPENING
- Computer Vision (YOLO, Tracking, OpenCV)
- Reinforcement Learning (MDPs, Q-learning, Policy Gradients)
- First Portfolio Project (Object Detection System)

Q3 (Months 7-9): SPECIALIZATION
- Advanced RL (PPO, SAC, Multi-Agent)
- Robotics (ROS2, Sensor Fusion, Control)
- Simulation (AirSim, Gazebo)

Q4 (Months 10-12): APPLICATION
- Edge AI (Jetson, Quantization, TensorRT)
- Complete Autonomous Drone Project
- Portfolio refinement, job applications
""")

doc.add_heading('10.5 Two-Year Roadmap', 2)
table25 = doc.add_table(rows=4, cols=3)
table25.style = 'Table Grid'
table25.rows[0].cells[0].text = 'Period'
table25.rows[0].cells[1].text = 'Focus'
table25.rows[0].cells[2].text = 'Deliverable'
table25.rows[1].cells[0].text = 'Year 1'
table25.rows[1].cells[1].text = 'All above (months 1-12)'
table25.rows[1].cells[2].text = 'Autonomous drone project'
table25.rows[2].cells[0].text = 'Year 1-1.5'
table25.rows[2].cells[1].text = 'Advanced topics'
table25.rows[2].cells[2].text = 'Research paper or open-source contribution'
table25.rows[3].cells[0].text = 'Year 1.5-2'
table25.rows[3].cells[1].text = 'Specialization/Deep expertise'
table25.rows[3].cells[2].text = 'Domain-specific expertise (e.g., swarm, event cameras, etc.)'

# PART 11: SKILLS MATRIX
doc.add_page_break()
doc.add_heading('PART 11: SKILLS MATRIX', 1)

doc.add_heading('11.1 Core Skills (Must-Have)', 2)
table26 = doc.add_table(rows=11, cols=3)
table26.style = 'Table Grid'
table26.rows[0].cells[0].text = 'Skill'
table26.rows[0].cells[1].text = 'Level'
table26.rows[0].cells[2].text = 'Why'
table26.rows[1].cells[0].text = 'Python'
table26.rows[1].cells[1].text = 'Expert'
table26.rows[1].cells[2].text = 'Primary language for ML/DL'
table26.rows[2].cells[0].text = 'PyTorch or TensorFlow'
table26.rows[2].cells[1].text = 'Advanced'
table26.rows[2].cells[2].text = 'Deep learning framework'
table26.rows[3].cells[0].text = 'Computer Vision'
table26.rows[3].cells[1].text = 'Intermediate-Advanced'
table26.rows[3].cells[2].text = 'Perception core'
table26.rows[4].cells[0].text = 'Reinforcement Learning'
table26.rows[4].cells[1].text = 'Intermediate'
table26.rows[4].cells[2].text = 'Decision-making core'
table26.rows[5].cells[0].text = 'ROS2'
table26.rows[5].cells[1].text = 'Intermediate'
table26.rows[5].cells[2].text = 'Robotics middleware'
table26.rows[6].cells[0].text = 'Sensor Fusion'
table26.rows[6].cells[1].text = 'Intermediate'
table26.rows[6].cells[2].text = 'GPS-denied navigation'
table26.rows[7].cells[0].text = 'Edge Optimization'
table26.rows[7].cells[1].text = 'Intermediate'
table26.rows[7].cells[2].text = 'Real-time deployment'
table26.rows[8].cells[0].text = 'Linux'
table26.rows[8].cells[1].text = 'Intermediate'
table26.rows[8].cells[2].text = 'Development environment'
table26.rows[9].cells[0].text = 'Git'
table26.rows[9].cells[1].text = 'Intermediate'
table26.rows[9].cells[2].text = 'Version control'
table26.rows[10].cells[0].text = 'Mathematics'
table26.rows[10].cells[1].text = 'Intermediate-Advanced'
table26.rows[10].cells[2].text = 'Foundational for all'

doc.add_heading('11.2 Optional Skills (Valuable)', 2)
table27 = doc.add_table(rows=6, cols=3)
table27.style = 'Table Grid'
table27.rows[0].cells[0].text = 'Skill'
table27.rows[0].cells[1].text = 'Level'
table27.rows[0].cells[2].text = 'When Needed'
table27.rows[1].cells[0].text = 'C++'
table27.rows[1].cells[1].text = 'Intermediate'
table27.rows[1].cells[2].text = 'Performance-critical code, ROS'
table27.rows[2].cells[0].text = 'CUDA'
table27.rows[2].cells[1].text = 'Intermediate'
table27.rows[2].cells[2].text = 'GPU optimization'
table27.rows[3].cells[0].text = 'Docker'
table27.rows[3].cells[1].text = 'Intermediate'
table27.rows[3].cells[2].text = 'Deployment, reproducibility'
table27.rows[4].cells[0].text = 'MLOps'
table27.rows[4].cells[1].text = 'Intermediate'
table27.rows[4].cells[2].text = 'Production ML'
table27.rows[5].cells[0].text = 'Formal Verification'
table27.rows[5].cells[1].text = 'Advanced'
table27.rows[5].cells[2].text = 'Safety-critical systems'

doc.add_heading('11.3 Nice-to-Have Skills', 2)
table28 = doc.add_table(rows=6, cols=2)
table28.style = 'Table Grid'
table28.rows[0].cells[0].text = 'Skill'
table28.rows[0].cells[1].text = 'Why'
table28.rows[1].cells[0].text = 'Aerospace Engineering Basics'
table28.rows[1].cells[1].text = 'Understand drone dynamics'
table28.rows[2].cells[0].text = 'Electrical Engineering'
table28.rows[2].cells[1].text = 'Hardware integration'
table28.rows[3].cells[0].text = 'UX/UI Design'
table28.rows[3].cells[1].text = 'GCS interfaces'
table28.rows[4].cells[0].text = 'Communications Engineering'
table28.rows[4].cells[1].text = 'Swarm coordination'
table28.rows[5].cells[0].text = 'Cybersecurity'
table28.rows[5].cells[1].text = 'Secure systems'

doc.add_heading('11.4 Future Skills (Emerging)', 2)
table29 = doc.add_table(rows=5, cols=2)
table29.style = 'Table Grid'
table29.rows[0].cells[0].text = 'Skill'
table29.rows[0].cells[1].text = 'Why'
table29.rows[1].cells[0].text = 'Spiking Neural Networks'
table29.rows[1].cells[1].text = 'Event cameras, ultra-low-power AI'
table29.rows[2].cells[0].text = 'Federated Learning'
table29.rows[2].cells[1].text = 'Swarm coordination, privacy'
table29.rows[3].cells[0].text = 'Neuromorphic Computing'
table29.rows[3].cells[1].text = 'Event-driven AI'
table29.rows[4].cells[0].text = 'Quantum Sensing'
table29.rows[4].cells[1].text = 'Future GPS-denied navigation'

# PART 12: INDUSTRY INSIGHTS
doc.add_page_break()
doc.add_heading('PART 12: INDUSTRY INSIGHTS', 1)

doc.add_heading('12.1 Current Hiring Trends', 2)
doc.add_paragraph("""
- Massive demand for AI autonomy engineers with drone experience
- Defense sector is leading employer; commercial sector growing
- Software-first companies are disrupting traditional defense
- Crossover skills (AI + robotics + aerospace) are premium
""")

doc.add_heading('12.2 Most Valuable Skills (2025-2026)', 2)
table30 = doc.add_table(rows=9, cols=3)
table30.style = 'Table Grid'
table30.rows[0].cells[0].text = 'Rank'
table30.rows[0].cells[1].text = 'Skill'
table30.rows[0].cells[2].text = 'Demand Level'
table30.rows[1].cells[0].text = '1'
table30.rows[1].cells[1].text = 'Autonomous Navigation (GPS-denied)'
table30.rows[1].cells[2].text = '⭐⭐⭐⭐⭐'
table30.rows[2].cells[0].text = '2'
table30.rows[2].cells[1].text = 'Reinforcement Learning (PPO, Multi-agent)'
table30.rows[2].cells[2].text = '⭐⭐⭐⭐⭐'
table30.rows[3].cells[0].text = '3'
table30.rows[3].cells[1].text = 'Edge AI Optimization (TensorRT, Quantization)'
table30.rows[3].cells[2].text = '⭐⭐⭐⭐⭐'
table30.rows[4].cells[0].text = '4'
table30.rows[4].cells[1].text = 'Computer Vision (Object Detection, Tracking)'
table30.rows[4].cells[2].text = '⭐⭐⭐⭐⭐'
table30.rows[5].cells[0].text = '5'
table30.rows[5].cells[1].text = 'Sensor Fusion (Kalman, SLAM)'
table30.rows[5].cells[2].text = '⭐⭐⭐⭐'
table30.rows[6].cells[0].text = '6'
table30.rows[6].cells[1].text = 'ROS2'
table30.rows[6].cells[2].text = '⭐⭐⭐⭐'
table30.rows[7].cells[0].text = '7'
table30.rows[7].cells[1].text = 'Federated Learning'
table30.rows[7].cells[2].text = '⭐⭐⭐ (rising)'
table30.rows[8].cells[0].text = '8'
table30.rows[8].cells[1].text = 'Event-based Vision'
table30.rows[8].cells[2].text = '⭐⭐⭐ (niche, rising)'

doc.add_heading('12.3 Emerging Technologies', 2)
doc.add_paragraph("""
- Event Cameras: 120+ dB dynamic range, microsecond temporal resolution, no motion blur
- Federated DRL: Privacy-preserving, collaborative learning for swarms
- Quantization-Aware Training: Enabling complex models on edge
- AI-Powered Integration: Reducing integration time from months to hours
""")

doc.add_heading('12.4 Future Opportunities', 2)
doc.add_paragraph("""
- Urban Air Mobility (UAM): Autonomous package delivery, air taxis
- Disaster Response: Search and rescue in GPS-denied areas
- Precision Agriculture: Autonomous crop monitoring
- Infrastructure Inspection: Power lines, pipelines, bridges
- Defense: Swarm tactics, ISR, autonomous strike
""")

# PART 13: COMPARISON WITH RELATED FIELDS
doc.add_page_break()
doc.add_heading('PART 13: COMPARISON WITH RELATED FIELDS', 1)

table31 = doc.add_table(rows=7, cols=3)
table31.style = 'Table Grid'
table31.rows[0].cells[0].text = 'Field'
table31.rows[0].cells[1].text = 'Focus'
table31.rows[0].cells[2].text = 'When to Choose This Instead'
table31.rows[1].cells[0].text = 'General ML Engineer'
table31.rows[1].cells[1].text = 'Broad ML applications'
table31.rows[1].cells[2].text = 'You want to work on non-robotics AI'
table31.rows[2].cells[0].text = 'Computer Vision Engineer'
table31.rows[2].cells[1].text = 'Image/video analysis'
table31.rows[2].cells[2].text = 'You don\'t care about control/robotics'
table31.rows[3].cells[0].text = 'Robotics Engineer'
table31.rows[3].cells[1].text = 'Control, kinematics, hardware'
table31.rows[3].cells[2].text = 'You prefer hardware to AI'
table31.rows[4].cells[0].text = 'Embedded Systems Engineer'
table31.rows[4].cells[1].text = 'Low-level firmware, electronics'
table31.rows[4].cells[2].text = 'You want to work on chip/board design'
table31.rows[5].cells[0].text = 'Data Scientist'
table31.rows[5].cells[1].text = 'Analytics, business intelligence'
table31.rows[5].cells[2].text = 'You want to work with data, not drones'
table31.rows[6].cells[0].text = 'Game AI Developer'
table31.rows[6].cells[1].text = 'AI for games'
table31.rows[6].cells[2].text = 'You want to work in entertainment'

doc.add_paragraph("""
Recommendation: If you're passionate about AI and want to see it physically change the world, autonomous drone AI is the perfect intersection.
""")

# PART 14: RECOMMENDATIONS BY BACKGROUND
doc.add_page_break()
doc.add_heading('PART 14: RECOMMENDATIONS BY BACKGROUND', 1)

doc.add_heading('14.1 Students (Undergrad)', 2)
doc.add_paragraph("""
Path: Academic foundations → Internships → Industry/Research

Recommendations:
- Major in Computer Science, Electrical Engineering, or Robotics
- Take courses in ML, CV, RL, and Robotics
- Join robotics/AI clubs
- Apply for internships at defense tech companies (Shield AI, Anduril, Palantir)
- Build a strong GitHub portfolio
""")

doc.add_heading('14.2 Master\'s Students', 2)
doc.add_paragraph("""
Path: Specialization → Thesis/Project → Industry/PhD

Recommendations:
- Choose a thesis on a drone autonomy topic
- Publish at least one paper
- Network at conferences
- Apply for defense research labs (MIT Lincoln, DARPA, etc.)
- Consider industry internships
""")

doc.add_heading('14.3 PhD Candidates', 2)
doc.add_paragraph("""
Path: Deep Research → Postdoc/Industry Research

Recommendations:
- Publish at top conferences (NeurIPS, ICRA, IROS, CVPR)
- Collaborate with industry partners
- Build a strong research network
- Consider defense research labs or faculty positions
""")

doc.add_heading('14.4 Career Changers (Tech)', 2)
doc.add_paragraph("""
Path: Self-study → Projects → Industry

Recommendations:
- Leverage existing coding skills
- Take structured online courses
- Build a portfolio of drone projects
- Contribute to open-source drone projects
- Network via LinkedIn
""")

doc.add_heading('14.5 Career Changers (Non-Tech)', 2)
doc.add_paragraph("""
Path: Foundational Skills → Certifications → Entry-level

Recommendations:
- Start with Python and basic math
- Complete certifications (TensorFlow Developer Certificate, etc.)
- Build small projects first
- Consider a Master's in CS/Data Science
- Apply to entry-level ML Engineer roles
""")

doc.add_heading('14.6 Entrepreneurs', 2)
doc.add_paragraph("""
Path: Solve a real problem → Build MVP → Fundraise → Scale

Recommendations:
- Identify a genuine market need (e.g., GPS-denied navigation)
- Build a software-only solution to reduce hardware dependencies
- Apply to defense tech accelerators
- Network with VCs and military stakeholders
""")

# PART 15: FRAMEWORKS & METHODOLOGIES
doc.add_page_break()
doc.add_heading('PART 15: FRAMEWORKS & METHODOLOGIES', 1)

doc.add_heading('15.1 Important Frameworks', 2)
table32 = doc.add_table(rows=8, cols=3)
table32.style = 'Table Grid'
table32.rows[0].cells[0].text = 'Framework'
table32.rows[0].cells[1].text = 'Purpose'
table32.rows[0].cells[2].text = 'Why It Matters'
table32.rows[1].cells[0].text = 'ROS2'
table32.rows[1].cells[1].text = 'Robotics middleware'
table32.rows[1].cells[2].text = 'Industry standard for drone software'
table32.rows[2].cells[0].text = 'PyTorch'
table32.rows[2].cells[1].text = 'Deep learning'
table32.rows[2].cells[2].text = 'Research and industry standard'
table32.rows[3].cells[0].text = 'TensorRT'
table32.rows[3].cells[1].text = 'Model optimization'
table32.rows[3].cells[2].text = 'Essential for edge deployment'
table32.rows[4].cells[0].text = 'AirSim/Gazebo'
table32.rows[4].cells[1].text = 'Simulation'
table32.rows[4].cells[2].text = 'Safe, fast testing'
table32.rows[5].cells[0].text = 'PX4/ArduPilot'
table32.rows[5].cells[1].text = 'Flight controller'
table32.rows[5].cells[2].text = 'Open-source autopilots'
table32.rows[6].cells[0].text = 'MAVSDK'
table32.rows[6].cells[1].text = 'Drone control API'
table32.rows[6].cells[2].text = 'High-level control abstraction'
table32.rows[7].cells[0].text = 'ONNX'
table32.rows[7].cells[1].text = 'Model interchange'
table32.rows[7].cells[2].text = 'Cross-framework compatibility'

doc.add_heading('15.2 Architecture Patterns', 2)
doc.add_paragraph("""
Pipeline Architecture (Perception → Decision → Control)
[Camera/Sensors] → [Perception Model] → [Decision Engine] → [Control Commands] → [Drone]
Use: When you want modular, maintainable systems.

End-to-End Architecture
[Sensors] → [Deep Neural Network] → [Motor Commands]
Use: When tasks are well-defined and you have enough data.

Multi-Agent Architecture (Swarms)
[Drone 1] ←→ [Communication Layer] ←→ [Drone 2]
     ↓                                        ↓
  [Local Policy]                           [Local Policy]
Use: Coordinated drone fleets.
""")

doc.add_heading('15.3 Best Practices', 2)
doc.add_paragraph("""
1. Simulation-First Development: Validate in simulation before hardware
2. Edge-First Design: Optimize for edge from the beginning
3. Sensor Fusion > Single Sensor: Never rely on just one data source
4. Failsafe-First: Build failsafe mechanisms before complex behaviors
5. Model Compression Early: Quantize and prune before deployment
6. Real-World Validation: Sim2real gaps are real; test early and often
7. Version Control Everything: Code, data, and models
""")

# PART 16: INTERVIEW PREPARATION
doc.add_page_break()
doc.add_heading('PART 16: INTERVIEW PREPARATION', 1)

doc.add_heading('16.1 Common Interview Questions', 2)

doc.add_heading('Technical Questions', 3)
doc.add_paragraph("""
ML Fundamentals:
- Explain the bias-variance tradeoff
- What is backpropagation? Explain it step by step
- How do you handle overfitting?
- What's the difference between L1 and L2 regularization?

Computer Vision:
- How does YOLO work? Explain the architecture
- What is object tracking? Explain SORT/DeepSORT
- How do you handle small object detection?

Reinforcement Learning:
- Explain the difference between on-policy and off-policy RL
- How does PPO work?
- What is the exploration-exploitation tradeoff?

Robotics:
- What is sensor fusion? How does a Kalman filter work?
- How do you localize a drone without GPS?
- Explain ROS2 architecture

Edge AI:
- How do you deploy a model to an edge device?
- What is quantization? How does it affect model performance?
- What are the constraints of running AI on a drone?
""")

doc.add_heading('Behavioral Questions', 3)
doc.add_paragraph("""
- Describe a project you built from scratch
- How do you handle failure?
- How do you work in a team?
- What's your approach to learning new technologies?
""")

doc.add_heading('16.2 Technical Interviews', 2)
doc.add_paragraph("""
What to Expect:
1. Coding Interview: Implement algorithms in Python (2-3 problems)
2. ML Design Interview: Design a system (e.g., object detection pipeline)
3. ML Knowledge Interview: Theory questions
4. Portfolio Walkthrough: Deep dive into one of your projects
5. Behavioral: Fit and collaboration
""")

doc.add_heading('Companies Hiring', 3)
table33 = doc.add_table(rows=9, cols=3)
table33.style = 'Table Grid'
table33.rows[0].cells[0].text = 'Company'
table33.rows[0].cells[1].text = 'Sector'
table33.rows[0].cells[2].text = 'Notable'
table33.rows[1].cells[0].text = 'Shield AI'
table33.rows[1].cells[1].text = 'Defense Tech'
table33.rows[1].cells[2].text = 'Hivemind SDK'
table33.rows[2].cells[0].text = 'SPARC AI'
table33.rows[2].cells[1].text = 'Defense Tech'
table33.rows[2].cells[2].text = 'Overwatch platform'
table33.rows[3].cells[0].text = 'Victus AI'
table33.rows[3].cells[1].text = 'Defense Tech'
table33.rows[3].cells[2].text = 'Software-only autonomy'
table33.rows[4].cells[0].text = 'Anduril'
table33.rows[4].cells[1].text = 'Defense Tech'
table33.rows[4].cells[2].text = 'Lattice platform'
table33.rows[5].cells[0].text = 'Palantir'
table33.rows[5].cells[1].text = 'Defense Tech'
table33.rows[5].cells[2].text = 'Gotham platform'
table33.rows[6].cells[0].text = 'NVIDIA'
table33.rows[6].cells[1].text = 'Hardware/Software'
table33.rows[6].cells[2].text = 'Jetson platform'
table33.rows[7].cells[0].text = 'Amazon'
table33.rows[7].cells[1].text = 'Delivery'
table33.rows[7].cells[2].text = 'Prime Air'
table33.rows[8].cells[0].text = 'DJI'
table33.rows[8].cells[1].text = 'Hardware'
table33.rows[8].cells[2].text = 'Commercial drones'

doc.add_heading('16.3 Portfolio Expectations', 2)
doc.add_paragraph("""
A strong portfolio should show:
- One or more complete projects
- Code quality (clean, documented)
- Architecture diagrams
- Performance results (metrics, graphs)
- Real-world or simulation videos
- GitHub repository
""")

doc.add_heading('16.4 Resume Advice', 2)
doc.add_paragraph("""
Keywords to include:
- "Autonomous Systems"
- "GPS-denied Navigation"
- "Reinforcement Learning"
- "Computer Vision"
- "Edge AI / Edge Deployment"
- "ROS2"
- "Sensor Fusion"
- "YOLO"
- "PPO"
- "NVIDIA Jetson"

Structure:
1. Summary (2-3 sentences)
2. Skills (bulleted list)
3. Experience (relevant projects/jobs)
4. Education
5. Projects (with links)
""")

doc.add_heading('16.5 Hiring Process', 2)
doc.add_paragraph("""
Application → Technical Screen → On-site Interviews → Offer
     ↓              ↓                  ↓              ↓
  (1-2 weeks)   (1 week)          (1-2 weeks)    (negotiation)
""")

# PART 17: CERTIFICATIONS
doc.add_page_break()
doc.add_heading('PART 17: CERTIFICATIONS', 1)

doc.add_heading('17.1 Certifications That Matter', 2)
table34 = doc.add_table(rows=5, cols=4)
table34.style = 'Table Grid'
table34.rows[0].cells[0].text = 'Certification'
table34.rows[0].cells[1].text = 'Focus'
table34.rows[0].cells[2].text = 'Effort'
table34.rows[0].cells[3].text = 'ROI'
table34.rows[1].cells[0].text = 'TensorFlow Developer Certificate'
table34.rows[1].cells[1].text = 'TensorFlow proficiency'
table34.rows[1].cells[2].text = 'Medium'
table34.rows[1].cells[3].text = 'High (industry recognition)'
table34.rows[2].cells[0].text = 'NVIDIA Jetson AI Specialist'
table34.rows[2].cells[1].text = 'Edge AI, Jetson'
table34.rows[2].cells[2].text = 'Medium'
table34.rows[2].cells[3].text = 'High (relevant to drone deployment)'
table34.rows[3].cells[0].text = 'DGCA Remote Pilot Certificate'
table34.rows[3].cells[1].text = 'Drone piloting (India)'
table34.rows[3].cells[2].text = 'Low-Medium'
table34.rows[3].cells[3].text = 'Required for drone operations'
table34.rows[4].cells[0].text = 'AWS/Azure ML Certifications'
table34.rows[4].cells[1].text = 'Cloud ML'
table34.rows[4].cells[2].text = 'Medium'
table34.rows[4].cells[3].text = 'Low (drones use edge, not cloud)'

doc.add_heading('17.2 Certifications That Don\'t Matter', 2)
doc.add_paragraph("""
- General data science bootcamps (unless from top providers)
- Generic "AI" certificates without hands-on projects
- University certificates (non-degree)
""")

doc.add_heading('17.3 Recommended Order', 2)
doc.add_paragraph("""
1. TensorFlow Developer Certificate (or PyTorch equivalent)
2. NVIDIA Jetson AI Specialist (if pursuing edge deployment)
3. ROS2 Basics (The Construct)
4. Drone-Specific Certifications (if needed for your role)
""")

# PART 18: FINAL MASTER PLAN
doc.add_page_break()
doc.add_heading('PART 18: FINAL MASTER PLAN', 1)

doc.add_heading('The Optimal Path (Based on Your Goals)', 2)
doc.add_paragraph("""
Your Goal: Build the ML/DL software layer for self-defensive drones that operate without GPS or fiber optics.

Why This Path Works: You've chosen a high-growth, high-impact field with clear technical challenges. The software-only approach means you don't need to build hardware, making this a pure software engineering and AI challenge.
""")

doc.add_heading('Phase 1: Foundation (Months 1-4)', 3)
table35 = doc.add_table(rows=6, cols=3)
table35.style = 'Table Grid'
table35.rows[0].cells[0].text = 'Week'
table35.rows[0].cells[1].text = 'Focus'
table35.rows[0].cells[2].text = 'Activities'
table35.rows[1].cells[0].text = '1-2'
table35.rows[1].cells[1].text = 'Python Mastery'
table35.rows[1].cells[2].text = 'Code daily; build small projects'
table35.rows[2].cells[0].text = '3-4'
table35.rows[2].cells[1].text = 'Linear Algebra & Calculus'
table35.rows[2].cells[2].text = 'Review (3Blue1Brown, Khan Academy)'
table35.rows[3].cells[0].text = '5-8'
table35.rows[3].cells[1].text = 'ML Fundamentals'
table35.rows[3].cells[2].text = 'Coursera Deep Learning Specialization'
table35.rows[4].cells[0].text = '9-12'
table35.rows[4].cells[1].text = 'Deep Learning Deep Dive'
table35.rows[4].cells[2].text = 'Deep Learning book (Goodfellow)'
table35.rows[5].cells[0].text = '13-16'
table35.rows[5].cells[1].text = 'PyTorch Proficiency'
table35.rows[5].cells[2].text = 'Official tutorials, build a small neural network'

doc.add_paragraph("""
Milestone: Code a CNN from scratch in PyTorch.
""")

doc.add_heading('Phase 2: Computer Vision (Months 5-8)', 3)
table36 = doc.add_table(rows=5, cols=3)
table36.style = 'Table Grid'
table36.rows[0].cells[0].text = 'Week'
table36.rows[0].cells[1].text = 'Focus'
table36.rows[0].cells[2].text = 'Activities'
table36.rows[1].cells[0].text = '17-20'
table36.rows[1].cells[1].text = 'CV Fundamentals'
table36.rows[1].cells[2].text = 'CS231n lectures, OpenCV tutorials'
table36.rows[2].cells[0].text = '21-24'
table36.rows[2].cells[1].text = 'Object Detection'
table36.rows[2].cells[2].text = 'Implement YOLO training/inference'
table36.rows[3].cells[0].text = '25-28'
table36.rows[3].cells[1].text = 'Tracking'
table36.rows[3].cells[2].text = 'SORT/DeepSORT implementation'
table36.rows[4].cells[0].text = '29-32'
table36.rows[4].cells[1].text = 'Multi-modal Vision'
table36.rows[4].cells[2].text = 'RGB + Depth + Thermal fusion'

doc.add_paragraph("""
Milestone: Real-time object detection pipeline on video.
""")

doc.add_heading('Phase 3: Reinforcement Learning (Months 9-12)', 3)
table37 = doc.add_table(rows=5, cols=3)
table37.style = 'Table Grid'
table37.rows[0].cells[0].text = 'Week'
table37.rows[0].cells[1].text = 'Focus'
table37.rows[0].cells[2].text = 'Activities'
table37.rows[1].cells[0].text = '33-36'
table37.rows[1].cells[1].text = 'RL Fundamentals'
table37.rows[1].cells[2].text = 'Sutton & Barto Chapters 1-6'
table37.rows[2].cells[0].text = '37-40'
table37.rows[2].cells[1].text = 'Policy Gradients'
table37.rows[2].cells[2].text = 'Implement REINFORCE, PPO'
table37.rows[3].cells[0].text = '41-44'
table37.rows[3].cells[1].text = 'Advanced RL'
table37.rows[3].cells[2].text = 'SAC, TD3, Multi-agent RL'
table37.rows[4].cells[0].text = '45-48'
table37.rows[4].cells[1].text = 'Navigation RL'
table37.rows[4].cells[2].text = 'DRL in AirSim/Gazebo'

doc.add_paragraph("""
Milestone: PPO agent navigating a drone in simulation.
""")

doc.add_heading('Phase 4: Robotics & Integration (Months 13-16)', 3)
table38 = doc.add_table(rows=5, cols=3)
table38.style = 'Table Grid'
table38.rows[0].cells[0].text = 'Week'
table38.rows[0].cells[1].text = 'Focus'
table38.rows[0].cells[2].text = 'Activities'
table38.rows[1].cells[0].text = '49-52'
table38.rows[1].cells[1].text = 'ROS2'
table38.rows[1].cells[2].text = 'The Construct ROS2 courses'
table38.rows[2].cells[0].text = '53-56'
table38.rows[2].cells[1].text = 'Sensor Fusion'
table38.rows[2].cells[2].text = 'Kalman filters, VIO, SLAM'
table38.rows[3].cells[0].text = '57-60'
table38.rows[3].cells[1].text = 'Drone Control'
table38.rows[3].cells[2].text = 'PX4/ArduPilot, MAVSDK'
table38.rows[4].cells[0].text = '61-64'
table38.rows[4].cells[1].text = 'Simulation'
table38.rows[4].cells[2].text = 'AirSim + ROS2 integration'

doc.add_paragraph("""
Milestone: Simulated drone navigating without GPS.
""")

doc.add_heading('Phase 5: Edge AI & Deployment (Months 17-20)', 3)
table39 = doc.add_table(rows=5, cols=3)
table39.style = 'Table Grid'
table39.rows[0].cells[0].text = 'Week'
table39.rows[0].cells[1].text = 'Focus'
table39.rows[0].cells[2].text = 'Activities'
table39.rows[1].cells[0].text = '65-68'
table39.rows[1].cells[1].text = 'Edge Hardware'
table39.rows[1].cells[2].text = 'NVIDIA Jetson setup, benchmarking'
table39.rows[2].cells[0].text = '69-72'
table39.rows[2].cells[1].text = 'Model Compression'
table39.rows[2].cells[2].text = 'Quantization, pruning, TensorRT'
table39.rows[3].cells[0].text = '73-76'
table39.rows[3].cells[1].text = 'Knowledge Distillation'
table39.rows[3].cells[2].text = 'Teacher-student training'
table39.rows[4].cells[0].text = '77-80'
table39.rows[4].cells[1].text = 'Deployment Pipeline'
table39.rows[4].cells[2].text = 'OTA updates, monitoring'

doc.add_paragraph("""
Milestone: Model running at 30+ FPS on Jetson.
""")

doc.add_heading('Phase 6: End-to-End System (Months 21-24)', 3)
table40 = doc.add_table(rows=5, cols=3)
table40.style = 'Table Grid'
table40.rows[0].cells[0].text = 'Week'
table40.rows[0].cells[1].text = 'Focus'
table40.rows[0].cells[2].text = 'Activities'
table40.rows[1].cells[0].text = '81-84'
table40.rows[1].cells[1].text = 'System Integration'
table40.rows[1].cells[2].text = 'Perception + Navigation + Control'
table40.rows[2].cells[0].text = '85-88'
table40.rows[2].cells[1].text = 'Autonomous Missions'
table40.rows[2].cells[2].text = 'Complex scenarios in simulation'
table40.rows[3].cells[0].text = '89-92'
table40.rows[3].cells[1].text = 'Failsafe Systems'
table40.rows[3].cells[2].text = 'Graceful degradation, safety'
table40.rows[4].cells[0].text = '93-96'
table40.rows[4].cells[1].text = 'Portfolio Completion'
table40.rows[4].cells[2].text = 'Documentation, GitHub, video'

doc.add_paragraph("""
Milestone: Complete autonomous self-defense drone system (software).
""")

doc.add_heading('Phase 7: Specialization & Career (Months 25-36)', 3)
table41 = doc.add_table(rows=5, cols=3)
table41.style = 'Table Grid'
table41.rows[0].cells[0].text = 'Month'
table41.rows[0].cells[1].text = 'Focus'
table41.rows[0].cells[2].text = 'Activities'
table41.rows[1].cells[0].text = '25-27'
table41.rows[1].cells[1].text = 'Deepen Expertise'
table41.rows[1].cells[2].text = 'Choose specialization (swarm, event cameras, etc.)'
table41.rows[2].cells[0].text = '28-30'
table41.rows[2].cells[1].text = 'Research/Publication'
table41.rows[2].cells[2].text = 'Contribute to research, publish a paper'
table41.rows[3].cells[0].text = '31-33'
table41.rows[3].cells[1].text = 'Networking'
table41.rows[3].cells[2].text = 'LinkedIn, conferences, GitHub open-source'
table41.rows[4].cells[0].text = '34-36'
table41.rows[4].cells[1].text = 'Job/Startup'
table41.rows[4].cells[2].text = 'Apply for roles, build your startup'

doc.add_heading('Why This Order?', 2)
doc.add_paragraph("""
1. Foundations first ensures you understand the tools and math
2. Computer Vision is the easiest entry point with immediate visual results
3. RL builds on CV for decision-making
4. Robotics ties everything to the real world
5. Edge AI makes it deployable
6. Integration is the culmination
7. Specialization makes you unique and valuable
""")

doc.add_heading('Final Expert Advice', 2)
doc.add_paragraph("""
"The gap between simulation and reality is where most projects fail. Get to real hardware—even if it's a cheap drone—as early as possible. Perfect is the enemy of deployed."

"Focus on one complete system, not ten half-finished projects. Build, test, deploy, iterate."

"The software-only approach is the future. Companies like Shield AI, Victus AI, and SPARC AI are proving that the brain matters more than the body."

"In five years, autonomous drone software will be as standard as operating systems are for computers today. You're in the right place, at the right time."
""")

doc.add_heading('Quick Reference: The 3-Year Roadmap at a Glance', 2)
doc.add_paragraph("""
MONTH 0                  12                    24                    36
     │                      │                     │                     │
     ▼                      ▼                     ▼                     ▼
  ┌──────┐              ┌──────┐             ┌──────┐             ┌──────┐
  │Base  │──────────────│  CV  │─────────────│  RL  │─────────────│Spec. │
  │Python│              │YOLO  │             │ PPO  │             │Team  │
  │Math  │              │OpenCV│             │AirSim│             │Lead  │
  └──────┘              └──────┘             └──────┘             └──────┘
     │                      │                     │                     │
     ▼                      ▼                     ▼                     ▼
  ┌──────┐              ┌──────┐             ┌──────┐             ┌──────┐
  │PyTorch│─────────────│Sensor│─────────────│Edge  │─────────────│Project│
  │NNs   │              │Fusion│             │Jetson│             │Deploy │
  └──────┘              └──────┘             └──────┘             └──────┘

MILESTONES:
Q1: CNN from scratch
Q2: YOLO deployment
Q3: RL in simulation
Q4: ROS2 + AirSim integration
Q5: Jetson deployment
Q6: Complete autonomous system
Q7-12: Specialization, job search, or startup launch
""")

# Save the document
doc.save('Autonomous_Drone_AI_Handbook.docx')
print("Word document created successfully!")
