# Darkweb-Forensics---Investigating-Cyber-criminal-activities
This project was titled as "Vulnerability detection in the dark web links " It focuses on detecting the vulnerabilities in the dark web sites and it will whether it is good to go or not.
!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Batch Processing - Dark Web Analyzer</title>
    <style>
        :root {
            --tor-purple: #7d4698;
            --tor-dark: #1a1a1a;
            --tor-darker: #121212;
            --tor-medium: #2a2a2a;
            --tor-light: #3a3a3a;
            --tor-text: #e0e0e0;
            --tor-accent: #9966cc;
            --tor-highlight: #56347c;
            --high-risk: #ff4d4d;
            --medium-risk: #ffa64d;
            --low-risk: #6bc25d;
        }
        
        body { 
            font-family: 'Segoe UI', Arial, sans-serif; 
            margin: 0; 
            padding: 0; 
            background-color: var(--tor-darker); 
            color: var(--tor-text);
        }
        
        .navbar {
            background-color: var(--tor-dark);
            padding: 15px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.5);
        }
        
        .logo {
            font-size: 22px;
            font-weight: bold;
            color: var(--tor-accent);
        }
        
        .nav-links {
            display: flex;
            gap: 20px;
        }
        
        .nav-links a {
            color: var(--tor-text);
            text-decoration: none;
            padding: 8px 12px;
            border-radius: 4px;
            transition: background-color 0.2s;
        }
        
        .nav-links a:hover {
            background-color: var(--tor-medium);
        }
        
        .nav-links a.active {
            background-color: var(--tor-purple);
            color: white;
        }
        
        .container {
            max-width: 1200px;
            margin: 20px auto;
            padding: 0 20px;
        }
        
        .page-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 30px;
        }
        
        .page-title {
            font-size: 24px;
            font-weight: bold;
        }
        
        .batch-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
        }
        
        .batch-card {
            background-color: var(--tor-dark);
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
            border: 1px solid var(--tor-light);
            display: flex;
            flex-direction: column;
        }
        
        .batch-header {
            margin-bottom: 15px;
            border-bottom: 1px solid var(--tor-light);
            padding-bottom: 10px;
        }
        
        .batch-id {
            font-size: 14px;
            color: #aaa;
            margin-bottom: 5px;
        }
        
        .batch-date {
            font-size: 14px;
            color: var(--tor-accent);
        }
        
        .batch-progress {
            margin: 15px 0;
            height: 10px;
            background-color: var(--tor-medium);
            border-radius: 5px;
            overflow: hidden;
        }
        
        .batch-progress-bar {
            height: 100%;
            background-color: var(--tor-accent);
            border-radius: 5px;
        }
        
        .batch-stats {
            display: flex;
            justify-content: space-between;
            margin-bottom: 15px;
        }
        
        .batch-stat {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        
        .batch-stat-value {
            font-size: 24px;
            font-weight: bold;
        }
        
        .batch-stat-label {
            font-size: 12px;
            color: #aaa;
            text-transform: uppercase;
        }
        
        .batch-footer {
            margin-top: auto;
            display: flex;
            justify-content: space-between;
            padding-top: 15px;
            border-top: 1px solid var(--tor-light);
        }
        
        .btn {
            background-color: var(--tor-medium);
            color: var(--tor-text);
            border: none;
            padding: 8px 12px;
            border-radius: 4px;
            cursor: pointer;
            text-decoration: none;
            font-size: 14px;
            display: inline-block;
        }
        
        .btn:hover {
            background-color: var(--tor-light);
        }
        
        .btn-primary {
            background-color: var(--tor-accent);
            color: white;
        }
        
        .btn-primary:hover {
            background-color: var(--tor-highlight);
        }
        
        .status-badge {
            display: inline-block;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: bold;
            color: white;
        }
        
        .status-pending {
            background-color: var(--tor-accent);
        }
        
        .status-processing {
            background-color: var(--medium-risk);
        }
        
        .status-completed {
            background-color: var(--low-risk);
        }
        
        .status-failed {
            background-color: var(--high-risk);
        }
        
        .new-batch {
            background-color: var(--tor-dark);
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
            margin-bottom: 30px;
            border: 1px solid var(--tor-light);
        }
        
        .new-batch-header {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 20px;
            color: var(--tor-accent);
        }
        
        .new-batch-form {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }
        
        .new-batch-form textarea {
            padding: 12px;
            background-color: var(--tor-medium);
            color: var(--tor-text);
            border: 1px solid var(--tor-light);
            border-radius: 4px;
            height: 150px;
            resize: vertical;
            font-family: inherit;
        }
        
        .no-data {
            text-align: center;
            padding: 40px;
            background-color: var(--tor-dark);
            border-radius: 8px;
            margin-top: 40px;
            color: #888;
        }
        
        .form-actions {
            display: flex;
            justify-content: flex-end;
            gap: 10px;
        }

        /* Dynamic cybersecurity background with cursor effects */
        #particles-js {
            position: fixed;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            z-index: -1;
        }

        .cursor-follower {
            position: fixed;
            width: 200px;
            height: 200px;
            background: radial-gradient(circle, rgba(153, 102, 204, 0.3) 0%, rgba(153, 102, 204, 0) 70%);
            border-radius: 50%;
            pointer-events: none;
            transform: translate(-50%, -50%);
            z-index: -1;
            animation: pulse-cursor 2s infinite;
            mix-blend-mode: screen;
        }

        .data-lines {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -2;
            overflow: hidden;
        }

        .data-line {
            position: absolute;
            height: 1px;
            width: 100%;
            background-image: linear-gradient(to right, 
                transparent, 
                rgba(153, 102, 204, 0.1), 
                rgba(153, 102, 204, 0.2), 
                rgba(153, 102, 204, 0.1), 
                transparent);
            animation-name: data-line-animation;
            animation-timing-function: linear;
            animation-iteration-count: infinite;
            box-shadow: 0 0 5px rgba(153, 102, 204, 0.5);
        }

        @keyframes data-line-animation {
            0% { transform: translateY(-200%); }
            100% { transform: translateY(200vh); }
        }

        .digital-rain {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -3;
            color: rgba(153, 102, 204, 0.1);
            font-family: monospace;
            font-size: 14px;
            overflow: hidden;
            pointer-events: none;
        }

        .digital-rain .rain-column {
            position: absolute;
            top: -20%;
            animation-name: digital-rain-animation;
            animation-timing-function: linear;
            animation-iteration-count: infinite;
            text-align: center;
        }

        @keyframes digital-rain-animation {
            0% { transform: translateY(-100%); }
            100% { transform: translateY(200vh); }
        }

        @keyframes pulse-cursor {
            0% { opacity: 0.2; transform: translate(-50%, -50%) scale(1); }
            50% { opacity: 0.4; transform: translate(-50%, -50%) scale(1.5); }
            100% { opacity: 0.2; transform: translate(-50%, -50%) scale(1); }
        }
    </style>
</head>
<body>
    <!-- Dynamic background elements -->
    <div id="particles-js"></div>
    <div class="cursor-follower"></div>
    <div class="data-lines"></div>
    <div class="digital-rain"></div>

    <div class="navbar">
        <div class="logo">🧅 DARK WEB ANALYZER</div>
        <div class="nav-links">
            <a href="/"><i class="fas fa-home"></i> Home</a>
            <a href="/dashboard"><i class="fas fa-chart-line"></i> Dashboard</a>
            <a href="/history"><i class="fas fa-history"></i> History</a>
            <a href="/batch" class="active"><i class="fas fa-tasks"></i> Batch</a>
            <a href="/vulnerability"><i class="fas fa-shield-alt"></i> Vulnerability</a>
        </div>
    </div>
    
    <div class="container">
        <div class="page-header">
            <div class="page-title">Batch Processing</div>
        </div>
        
        <div class="new-batch">
            <div class="new-batch-header">New Batch Analysis</div>
            <form class="new-batch-form" method="POST" action="/">
                <textarea name="batch_urls" placeholder="Enter one .onion URL per line (e.g., http://example.onion)"></textarea>
                <div class="form-actions">
                    <button type="submit" class="btn btn-primary">Start Batch Analysis</button>
                </div>
            </form>
        </div>
        
        {% if not batch_jobs or batch_jobs|length == 0 %}
            <div class="no-data">
                <h2>No Batch Jobs</h2>
                <p>You haven't created any batch analysis jobs yet.</p>
            </div>
        {% else %}
            <div class="batch-grid">
                {% for batch in batch_jobs %}
                    <div class="batch-card">
                        <div class="batch-header">
                            <div class="batch-id">ID: {{ batch.id[:8] }}...</div>
                            <div class="batch-date">{{ batch.created }}</div>
                            
                            {% if batch.status == "pending" %}
                                <span class="status-badge status-pending">Pending</span>
                            {% elif batch.status == "processing" %}
                                <span class="status-badge status-processing">Processing</span>
                            {% elif batch.status == "completed" %}
                                <span class="status-badge status-completed">Completed</span>
                            {% else %}
                                <span class="status-badge status-failed">Failed</span>
                            {% endif %}
                        </div>
                        
                        <div class="batch-progress">
                            <div class="batch-progress-bar" 
                                 data-processed="{{ batch.processed_urls }}" 
                                 data-total="{{ batch.total_urls }}"
                                 style="width: 0%"></div>
                        </div>
                        
                        <div class="batch-stats">
                            <div class="batch-stat">
                                <div class="batch-stat-value">{{ batch.total_urls }}</div>
                                <div class="batch-stat-label">Total URLs</div>
                            </div>
                            
                            <div class="batch-stat">
                                <div class="batch-stat-value">{{ batch.processed_urls }}</div>
                                <div class="batch-stat-label">Processed</div>
                            </div>
                            
                            <div class="batch-stat">
                                <div class="batch-stat-value percentage-display" 
                                     data-processed="{{ batch.processed_urls }}" 
                                     data-total="{{ batch.total_urls }}">0%</div>
                                <div class="batch-stat-label">Complete</div>
                            </div>
                        </div>
                        
                        <div class="batch-footer">
                            <a href="/batch/{{ batch.id }}" class="btn btn-primary">View Details</a>
                            
                            {% if batch.status != "completed" %}
                                <form method="POST" action="/batch/{{ batch.id }}">
                                    <button type="submit" class="btn">Process Next</button>
                                </form>
                            {% endif %}
                        </div>
                    </div>
                {% endfor %}
            </div>
        {% endif %}
    </div>

<script>
    // Calculate and set progress bar widths and percentages
    document.addEventListener('DOMContentLoaded', function() {
        // Update progress bars
        var progressBars = document.querySelectorAll('.batch-progress-bar');
        progressBars.forEach(function(bar) {
            var processed = parseInt(bar.getAttribute('data-processed'));
            var total = parseInt(bar.getAttribute('data-total'));
            var percentage = total > 0 ? Math.floor((processed / total) * 100) : 0;
            bar.style.width = percentage + '%';
        });
        
        // Update percentage displays
        var percentageDisplays = document.querySelectorAll('.percentage-display');
        percentageDisplays.forEach(function(display) {
            var processed = parseInt(display.getAttribute('data-processed'));
            var total = parseInt(display.getAttribute('data-total'));
            var percentage = total > 0 ? Math.floor((processed / total) * 100) : 0;
            display.textContent = percentage + '%';
        });

        // Initialize dynamic background
        initDynamicBackground();
    });

    // Initialize dynamic background effects
    function initDynamicBackground() {
        // Load particles.js script if not already loaded
        if (typeof particlesJS === 'undefined') {
            const script = document.createElement('script');
            script.src = 'https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js';
            script.onload = setupParticles;
            document.head.appendChild(script);
        } else {
            setupParticles();
        }
        
        // Initialize cursor follower
        const cursorFollower = document.querySelector('.cursor-follower');
        document.addEventListener('mousemove', (e) => {
            cursorFollower.style.left = e.clientX + 'px';
            cursorFollower.style.top = e.clientY + 'px';
        });
        
        // Create data lines
        const dataLines = document.querySelector('.data-lines');
        for (let i = 0; i < 15; i++) {
            const line = document.createElement('div');
            line.classList.add('data-line');
            line.style.top = Math.random() * 100 + 'vh';
            line.style.animationDuration = (Math.random() * 8 + 5) + 's';
            line.style.opacity = Math.random() * 0.5 + 0.1;
            dataLines.appendChild(line);
        }
        
        // Create digital rain
        const digitalRain = document.querySelector('.digital-rain');
        const characters = '01アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン';
        
        for (let i = 0; i < 30; i++) {
            const column = document.createElement('div');
            column.classList.add('rain-column');
            column.style.left = (Math.random() * 100) + 'vw';
            column.style.animationDuration = (Math.random() * 10 + 10) + 's';
            column.style.opacity = Math.random() * 0.3 + 0.1;
            
            const columnLength = Math.floor(Math.random() * 20 + 10);
            let columnHtml = '';
            
            for (let j = 0; j < columnLength; j++) {
                const charIndex = Math.floor(Math.random() * characters.length);
                columnHtml += characters.charAt(charIndex) + '<br>';
            }
            
            column.innerHTML = columnHtml;
            digitalRain.appendChild(column);
        }
    }
    
    function setupParticles() {
        particlesJS('particles-js', {
            "particles": {
                "number": {
                    "value": 40,
                    "density": {
                        "enable": true,
                        "value_area": 800
                    }
                },
                "color": {
                    "value": "#9966cc"
                },
                "shape": {
                    "type": "circle",
                    "stroke": {
                        "width": 0,
                        "color": "#000000"
                    }
                },
                "opacity": {
                    "value": 0.2,
                    "random": true,
                    "anim": {
                        "enable": true,
                        "speed": 1,
                        "opacity_min": 0.1,
                        "sync": false
                    }
                },
                "size": {
                    "value": 3,
                    "random": true,
                    "anim": {
                        "enable": true,
                        "speed": 2,
                        "size_min": 0.1,
                        "sync": false
                    }
                },
                "line_linked": {
                    "enable": true,
                    "distance": 150,
                    "color": "#7d4698",
                    "opacity": 0.2,
                    "width": 1
                },
                "move": {
                    "enable": true,
                    "speed": 1,
                    "direction": "none",
                    "random": true,
                    "straight": false,
                    "out_mode": "out",
                    "bounce": false,
                    "attract": {
                        "enable": true,
                        "rotateX": 600,
                        "rotateY": 1200
                    }
                }
            },
            "interactivity": {
                "detect_on": "canvas",
                "events": {
                    "onhover": {
                        "enable": true,
                        "mode": "grab"
                    },
                    "onclick": {
                        "enable": true,
                        "mode": "push"
                    },
                    "resize": true
                },
                "modes": {
                    "grab": {
                        "distance": 140,
                        "line_linked": {
                            "opacity": 0.5
                        }
                    },
                    "push": {
                        "particles_nb": 3
                    }
                }
            },
            "retina_detect": true
        });
    }
</script>
</body>
</html> 
<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dark Web Analysis Dashboard</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css">
    <style>
        :root {
            --tor-purple: #7d4698;
            --tor-dark: #1a1a1a;
            --tor-darker: #121212;
            --tor-medium: #2a2a2a;
            --tor-light: #3a3a3a;
            --tor-text: #e0e0e0;
            --tor-accent: #9966cc;
            --tor-highlight: #56347c;
            --high-risk: #ff4d4d;
            --medium-risk: #ffa64d;
            --low-risk: #6bc25d;
            --card-shadow: 0 8px 16px rgba(0,0,0,0.3);
            --card-border: 1px solid rgba(255,255,255,0.05);
            --card-radius: 12px;
            --transition-speed: 0.3s;
        }
        
        [data-theme="light"] {
            --tor-purple: #9356b8;
            --tor-dark: #f5f5f5;
            --tor-darker: #eeeeee;
            --tor-medium: #dddddd;
            --tor-light: #cccccc;
            --tor-text: #333333;
            --tor-accent: #7d4698;
            --tor-highlight: #9966cc;
            --card-shadow: 0 8px 16px rgba(0,0,0,0.1);
            --card-border: 1px solid rgba(0,0,0,0.05);
        }
        
        * {
            box-sizing: border-box;
            transition: background-color var(--transition-speed), color var(--transition-speed);
        }
        
        body { 
            font-family: 'Segoe UI', Arial, sans-serif; 
            margin: 0; 
            padding: 0; 
            background-color: var(--tor-darker); 
            color: var(--tor-text);
        }
        
        .navbar {
            background-color: var(--tor-dark);
            padding: 15px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.5);
            position: sticky;
            top: 0;
            z-index: 100;
        }
        
        .logo {
            font-size: 22px;
            font-weight: bold;
            color: var(--tor-accent);
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .logo i {
            font-size: 24px;
        }
        
        .nav-links {
            display: flex;
            gap: 20px;
        }
        
        .nav-links a {
            color: var(--tor-text);
            text-decoration: none;
            padding: 8px 12px;
            border-radius: 6px;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            gap: 6px;
        }
        
        .nav-links a:hover {
            background-color: var(--tor-medium);
            transform: translateY(-2px);
        }
        
        .nav-links a.active {
            background-color: var(--tor-purple);
            color: white;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        
        .theme-toggle {
            background: none;
            border: none;
            color: var(--tor-text);
            cursor: pointer;
            font-size: 18px;
            padding: 8px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s;
        }
        
        .theme-toggle:hover {
            background-color: var(--tor-medium);
            transform: rotate(30deg);
        }
        
        .container {
            max-width: 1200px;
            margin: 20px auto;
            padding: 0 20px;
            animation: fadeIn 0.5s ease-in-out;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .dashboard-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 30px;
            padding-bottom: 15px;
            border-bottom: 1px solid var(--tor-light);
        }
        
        .dashboard-title {
            font-size: 28px;
            font-weight: bold;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .dashboard-date {
            color: var(--tor-accent);
            font-size: 14px;
            display: flex;
            align-items: center;
            gap: 6px;
        }
        
        .stats-cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        
        .stat-card {
            background-color: var(--tor-dark);
            border-radius: var(--card-radius);
            padding: 25px;
            box-shadow: var(--card-shadow);
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
            border: var(--card-border);
            transition: all 0.3s;
            position: relative;
            overflow: hidden;
        }
        
        .stat-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 20px rgba(0,0,0,0.4);
        }
        
        .stat-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 5px;
            background: linear-gradient(90deg, var(--tor-accent), var(--tor-purple));
        }
        
        .stat-value {
            font-size: 42px;
            font-weight: bold;
            margin: 15px 0;
            background: linear-gradient(90deg, var(--tor-accent), var(--tor-purple));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            position: relative;
        }
        
        .stat-value.counter {
            counter-reset: stat-counter 0;
        }
        
        .stat-label {
            font-size: 14px;
            color: #aaa;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .stat-icon {
            font-size: 28px;
            margin-bottom: 10px;
            color: var(--tor-accent);
            width: 60px;
            height: 60px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 50%;
            background-color: rgba(153, 102, 204, 0.1);
        }
        
        .charts-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        
        @media (max-width: 768px) {
            .charts-grid {
                grid-template-columns: 1fr;
            }
        }
        
        .chart-container {
            background-color: var(--tor-dark);
            border-radius: var(--card-radius);
            padding: 25px;
            box-shadow: var(--card-shadow);
            border: var(--card-border);
            transition: all 0.3s;
        }
        
        .chart-container:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 20px rgba(0,0,0,0.4);
        }
        
        .chart-title {
            font-size: 18px;
            margin-bottom: 15px;
            color: var(--tor-accent);
            font-weight: bold;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .chart-title i {
            font-size: 20px;
        }
        
        .recent-activity {
            background-color: var(--tor-dark);
            border-radius: var(--card-radius);
            padding: 25px;
            box-shadow: var(--card-shadow);
            margin-bottom: 30px;
            border: var(--card-border);
            transition: all 0.3s;
        }
        
        .recent-activity:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 20px rgba(0,0,0,0.4);
        }
        
        .activity-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 1px solid var(--tor-light);
        }
        
        .activity-title {
            font-size: 18px;
            color: var(--tor-accent);
            font-weight: bold;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .view-all {
            color: var(--tor-accent);
            text-decoration: none;
            font-size: 14px;
            display: flex;
            align-items: center;
            gap: 5px;
            transition: all 0.2s;
            padding: 6px 12px;
            border-radius: 4px;
        }
        
        .view-all:hover {
            background-color: var(--tor-medium);
            transform: translateX(5px);
        }
        
        .activity-list {
            list-style-type: none;
            padding: 0;
            margin: 0;
        }
        
        .activity-item {
            padding: 15px;
            border-bottom: 1px solid var(--tor-light);
            display: flex;
            align-items: center;
            transition: all 0.2s;
            border-radius: 6px;
        }
        
        .activity-item:last-child {
            border-bottom: none;
        }
        
        .activity-item:hover {
            background-color: var(--tor-medium);
            transform: translateX(5px);
        }
        
        .activity-site {
            flex-grow: 1;
            margin-left: 10px;
            display: flex;
            align-items: center;
            gap: 10px;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }
        
        .activity-site a {
            max-width: 300px;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }
        
        .activity-time {
            color: #aaa;
            font-size: 14px;
            white-space: nowrap;
        }
        
        .no-data {
            text-align: center;
            padding: 60px 40px;
            background-color: var(--tor-dark);
            border-radius: var(--card-radius);
            margin-top: 40px;
            color: #888;
            box-shadow: var(--card-shadow);
            border: var(--card-border);
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(153, 102, 204, 0.4); }
            70% { box-shadow: 0 0 0 10px rgba(153, 102, 204, 0); }
            100% { box-shadow: 0 0 0 0 rgba(153, 102, 204, 0); }
        }
        
        .no-data h2 {
            color: var(--tor-accent);
            margin-bottom: 10px;
        }
        
        .no-data i {
            font-size: 48px;
            color: var(--tor-accent);
            margin-bottom: 20px;
            opacity: 0.7;
        }
        
        .risk-label {
            display: inline-flex;
            align-items: center;
            padding: 4px 10px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: bold;
            margin-left: 10px;
            gap: 5px;
        }
        
        .risk-high {
            background-color: var(--high-risk);
            color: white;
        }
        
        .risk-medium {
            background-color: var(--medium-risk);
            color: black;
        }
        
        .risk-low {
            background-color: var(--low-risk);
            color: black;
        }
        
        .loading {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: var(--tor-darker);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 9999;
            transition: opacity 0.5s;
        }
        
        .loading.fade-out {
            opacity: 0;
            pointer-events: none;
        }
        
        .loader {
            width: 50px;
            height: 50px;
            border: 5px solid var(--tor-medium);
            border-radius: 50%;
            border-top-color: var(--tor-accent);
            animation: spin 1s linear infinite;
        }
        
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
        
        .loading-text {
            position: absolute;
            bottom: 100px;
            color: var(--tor-accent);
            font-size: 14px;
            letter-spacing: 1px;
        }
        
        .tooltip {
            position: relative;
            display: inline-block;
        }
        
        .tooltip:hover::after {
            content: attr(data-tooltip);
            position: absolute;
            bottom: 100%;
            left: 50%;
            transform: translateX(-50%);
            background-color: rgba(0,0,0,0.8);
            color: white;
            padding: 5px 10px;
            border-radius: 4px;
            font-size: 12px;
            white-space: nowrap;
            z-index: 100;
        }

        /* Dynamic cybersecurity background with cursor effects */
        #particles-js {
            position: fixed;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            z-index: -1;
        }

        .cursor-follower {
            position: fixed;
            width: 200px;
            height: 200px;
            background: radial-gradient(circle, rgba(153, 102, 204, 0.3) 0%, rgba(153, 102, 204, 0) 70%);
            border-radius: 50%;
            pointer-events: none;
            transform: translate(-50%, -50%);
            z-index: -1;
            animation: pulse-cursor 2s infinite;
            mix-blend-mode: screen;
        }

        .data-lines {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -2;
            overflow: hidden;
        }

        .data-line {
            position: absolute;
            height: 1px;
            width: 100%;
            background-image: linear-gradient(to right, 
                transparent, 
                rgba(153, 102, 204, 0.1), 
                rgba(153, 102, 204, 0.2), 
                rgba(153, 102, 204, 0.1), 
                transparent);
            animation-name: data-line-animation;
            animation-timing-function: linear;
            animation-iteration-count: infinite;
            box-shadow: 0 0 5px rgba(153, 102, 204, 0.5);
        }

        @keyframes data-line-animation {
            0% { transform: translateY(-200%); }
            100% { transform: translateY(200vh); }
        }

        .digital-rain {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -3;
            color: rgba(153, 102, 204, 0.1);
            font-family: monospace;
            font-size: 14px;
            overflow: hidden;
            pointer-events: none;
        }

        .digital-rain .rain-column {
            position: absolute;
            top: -20%;
            animation-name: digital-rain-animation;
            animation-timing-function: linear;
            animation-iteration-count: infinite;
            text-align: center;
        }

        @keyframes digital-rain-animation {
            0% { transform: translateY(-100%); }
            100% { transform: translateY(200vh); }
        }

        @keyframes pulse-cursor {
            0% { opacity: 0.2; transform: translate(-50%, -50%) scale(1); }
            50% { opacity: 0.4; transform: translate(-50%, -50%) scale(1.5); }
            100% { opacity: 0.2; transform: translate(-50%, -50%) scale(1); }
        }
    </style>
</head>
<body>
    <!-- Dynamic background elements -->
    <div id="particles-js"></div>
    <div class="cursor-follower"></div>
    <div class="data-lines"></div>
    <div class="digital-rain"></div>

    <div class="loading">
        <div class="loader"></div>
        <div class="loading-text">Loading Dashboard...</div>
    </div>

    <div class="navbar">
        <div class="logo"><i class="fas fa-globe-americas"></i> DARK WEB ANALYZER</div>
        <div class="nav-links">
            <a href="/"><i class="fas fa-home"></i> Home</a>
            <a href="/dashboard" class="active"><i class="fas fa-chart-line"></i> Dashboard</a>
            <a href="/history"><i class="fas fa-history"></i> History</a>
            <a href="/batch"><i class="fas fa-tasks"></i> Batch</a>
            <a href="/vulnerability"><i class="fas fa-shield-alt"></i> Vulnerability</a>
        </div>
        <button class="theme-toggle" id="themeToggle"><i class="fas fa-moon"></i></button>
    </div>
    
    <div class="container">
        {% if not stats or stats.total_sites == 0 %}
            <div class="no-data">
                <i class="fas fa-search"></i>
                <h2>No Analysis Data Available</h2>
                <p>Start analyzing .onion sites to see statistics and visualizations here.</p>
                <a href="/" style="color: var(--tor-accent); display: inline-block; margin-top: 15px; padding: 10px 20px; border: 1px solid var(--tor-accent); border-radius: 4px; text-decoration: none;">
                    <i class="fas fa-arrow-right"></i> Return to Home
                </a>
            </div>
        {% else %}
            <div class="dashboard-header">
                <div class="dashboard-title"><i class="fas fa-tachometer-alt"></i> Analysis Dashboard</div>
                <div class="dashboard-date"><i class="far fa-calendar-alt"></i> <span id="currentDate">Loading...</span></div>
            </div>
            
            <div class="stats-cards">
                <div class="stat-card">
                    <div class="stat-icon"><i class="fas fa-globe"></i></div>
                    <div class="stat-value counter" data-target="{{ stats.total_sites }}">0</div>
                    <div class="stat-label">Sites Analyzed</div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-icon"><i class="fas fa-exclamation-triangle"></i></div>
                    <div class="stat-value counter" data-target="{{ stats.risk_levels.high }}">0</div>
                    <div class="stat-label">High Risk Sites</div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-icon"><i class="fas fa-language"></i></div>
                    <div class="stat-value counter" data-target="{{ stats.languages|length }}">0</div>
                    <div class="stat-label">Languages Detected</div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-icon"><i class="fas fa-smile"></i></div>
                    <div class="stat-value">{{ stats.avg_sentiment }}</div>
                    <div class="stat-label">Avg. Sentiment</div>
                </div>
            </div>
            
            {% if charts %}
            <div class="charts-grid">
                <div class="chart-container">
                    <div class="chart-title"><i class="fas fa-shield-alt"></i> Risk Level Distribution</div>
                    <div id="risk-chart" data-chart="{{ charts.risk_chart|safe }}"></div>
                </div>
                
                {% if "language_chart" in charts %}
                <div class="chart-container">
                    <div class="chart-title"><i class="fas fa-language"></i> Top Languages</div>
                    <div id="language-chart" data-chart="{{ charts.language_chart|safe }}"></div>
                </div>
                {% endif %}
                
                {% if "category_chart" in charts %}
                <div class="chart-container">
                    <div class="chart-title"><i class="fas fa-folder"></i> Content Categories</div>
                    <div id="category-chart" data-chart="{{ charts.category_chart|safe }}"></div>
                </div>
                {% endif %}
            </div>
            {% endif %}
            
            <div class="recent-activity">
                <div class="activity-header">
                    <div class="activity-title"><i class="fas fa-signal"></i> Recent Activity</div>
                    <a href="/history" class="view-all">View All <i class="fas fa-arrow-right"></i></a>
                </div>
                
                <ul class="activity-list">
                    {% for analysis in stats.recent_sites[:5] %}
                    <li class="activity-item">
                        <i class="fas fa-globe"></i>
                        <span class="activity-site">
                            <a href="/analysis/{{ analysis.id }}" class="tooltip" data-tooltip="View full analysis" style="color: var(--tor-text); text-decoration: none;">
                                {{ analysis.url }}
                            </a>
                            
                            {% if analysis.risk_level >= 7 %}
                                <span class="risk-label risk-high"><i class="fas fa-exclamation-circle"></i> High Risk</span>
                            {% elif analysis.risk_level >= 4 %}
                                <span class="risk-label risk-medium"><i class="fas fa-exclamation"></i> Medium Risk</span>
                            {% else %}
                                <span class="risk-label risk-low"><i class="fas fa-check-circle"></i> Low Risk</span>
                            {% endif %}
                        </span>
                        <span class="activity-time"><i class="far fa-clock"></i> {{ analysis.timestamp }}</span>
                    </li>
                    {% endfor %}
                </ul>
            </div>
        {% endif %}
    </div>
    
    {% if charts %}
    <script>
        // Set current date
        document.getElementById('currentDate').textContent = new Date().toLocaleDateString('en-US', {
            weekday: 'long', 
            year: 'numeric', 
            month: 'long', 
            day: 'numeric'
        });
        
        // Theme toggle
        const themeToggle = document.getElementById('themeToggle');
        const htmlElement = document.documentElement;
        
        themeToggle.addEventListener('click', function() {
            if (htmlElement.getAttribute('data-theme') === 'dark') {
                htmlElement.setAttribute('data-theme', 'light');
                themeToggle.innerHTML = '<i class="fas fa-sun"></i>';
                localStorage.setItem('theme', 'light');
            } else {
                htmlElement.setAttribute('data-theme', 'dark');
                themeToggle.innerHTML = '<i class="fas fa-moon"></i>';
                localStorage.setItem('theme', 'dark');
            }
        });
        
        // Check for saved theme preference
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme) {
            htmlElement.setAttribute('data-theme', savedTheme);
            themeToggle.innerHTML = savedTheme === 'dark' ? 
                '<i class="fas fa-moon"></i>' : 
                '<i class="fas fa-sun"></i>';
        }
        
        // Counter animation
        const counterElements = document.querySelectorAll('.counter');
        
        function animateCounter(el) {
            const target = parseInt(el.getAttribute('data-target'));
            const duration = 1500;
            const start = 0;
            const increment = target / (duration / 16);
            
            let current = start;
            const timer = setInterval(() => {
                current += increment;
                el.textContent = Math.floor(current);
                
                if (current >= target) {
                    el.textContent = target;
                    clearInterval(timer);
                }
            }, 16);
        }
        
        // Initialize dynamic background effects
        function initDynamicBackground() {
            // Initialize particles.js
            particlesJS('particles-js', {
                "particles": {
                    "number": {
                        "value": 40,
                        "density": {
                            "enable": true,
                            "value_area": 800
                        }
                    },
                    "color": {
                        "value": "#9966cc"
                    },
                    "shape": {
                        "type": "circle",
                        "stroke": {
                            "width": 0,
                            "color": "#000000"
                        }
                    },
                    "opacity": {
                        "value": 0.2,
                        "random": true,
                        "anim": {
                            "enable": true,
                            "speed": 1,
                            "opacity_min": 0.1,
                            "sync": false
                        }
                    },
                    "size": {
                        "value": 3,
                        "random": true,
                        "anim": {
                            "enable": true,
                            "speed": 2,
                            "size_min": 0.1,
                            "sync": false
                        }
                    },
                    "line_linked": {
                        "enable": true,
                        "distance": 150,
                        "color": "#7d4698",
                        "opacity": 0.2,
                        "width": 1
                    },
                    "move": {
                        "enable": true,
                        "speed": 1,
                        "direction": "none",
                        "random": true,
                        "straight": false,
                        "out_mode": "out",
                        "bounce": false,
                        "attract": {
                            "enable": true,
                            "rotateX": 600,
                            "rotateY": 1200
                        }
                    }
                },
                "interactivity": {
                    "detect_on": "canvas",
                    "events": {
                        "onhover": {
                            "enable": true,
                            "mode": "grab"
                        },
                        "onclick": {
                            "enable": true,
                            "mode": "push"
                        },
                        "resize": true
                    },
                    "modes": {
                        "grab": {
                            "distance": 140,
                            "line_linked": {
                                "opacity": 0.5
                            }
                        },
                        "push": {
                            "particles_nb": 3
                        }
                    }
                },
                "retina_detect": true
            });

            // Create cursor follower effect
            const cursorFollower = document.querySelector('.cursor-follower');
            document.addEventListener('mousemove', (e) => {
                cursorFollower.style.left = e.clientX + 'px';
                cursorFollower.style.top = e.clientY + 'px';
            });

            // Create data lines effect
            const dataLines = document.querySelector('.data-lines');
            for (let i = 0; i < 15; i++) {
                const line = document.createElement('div');
                line.classList.add('data-line');
                line.style.top = Math.random() * 100 + 'vh';
                line.style.animationDuration = (Math.random() * 8 + 5) + 's';
                line.style.opacity = Math.random() * 0.5 + 0.1;
                dataLines.appendChild(line);
            }

            // Create digital rain effect
            const digitalRain = document.querySelector('.digital-rain');
            const characters = '01アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン';
            
            for (let i = 0; i < 30; i++) {
                const column = document.createElement('div');
                column.classList.add('rain-column');
                column.style.left = (Math.random() * 100) + 'vw';
                column.style.animationDuration = (Math.random() * 10 + 10) + 's';
                column.style.opacity = Math.random() * 0.3 + 0.1;
                
                const columnLength = Math.floor(Math.random() * 20 + 10);
                let columnHtml = '';
                
                for (let j = 0; j < columnLength; j++) {
                    const charIndex = Math.floor(Math.random() * characters.length);
                    columnHtml += characters.charAt(charIndex) + '<br>';
                }
                
                column.innerHTML = columnHtml;
                digitalRain.appendChild(column);
            }
        }
        
        // Loading screen
        window.addEventListener('load', function() {
            setTimeout(function() {
                const loader = document.querySelector('.loading');
                loader.classList.add('fade-out');
                
                // Start counter animations after loading
                counterElements.forEach(animateCounter);
                
                // Load particles.js script and initialize background
                const script = document.createElement('script');
                script.src = 'https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js';
                script.onload = function() {
                    initDynamicBackground();
                    
                    // Charts
                    const riskChart = JSON.parse(document.getElementById('risk-chart').getAttribute('data-chart'));
                    Plotly.newPlot('risk-chart', riskChart.data, riskChart.layout);
                    
                    if (document.getElementById('language-chart')) {
                        const languageChart = JSON.parse(document.getElementById('language-chart').getAttribute('data-chart'));
                        Plotly.newPlot('language-chart', languageChart.data, languageChart.layout);
                    }
                    
                    if (document.getElementById('category-chart')) {
                        const categoryChart = JSON.parse(document.getElementById('category-chart').getAttribute('data-chart'));
                        Plotly.newPlot('category-chart', categoryChart.data, categoryChart.layout);
                    }
                };
                document.head.appendChild(script);
                
            }, 800);
        });
    </script>
    {% endif %}
</body>
</html> 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Analysis History - Dark Web Analyzer</title>
    <style>
        :root {
            --tor-purple: #7d4698;
            --tor-dark: #1a1a1a;
            --tor-darker: #121212;
            --tor-medium: #2a2a2a;
            --tor-light: #3a3a3a;
            --tor-text: #e0e0e0;
            --tor-accent: #9966cc;
            --tor-highlight: #56347c;
            --high-risk: #ff4d4d;
            --medium-risk: #ffa64d;
            --low-risk: #6bc25d;
        }
        
        body { 
            font-family: 'Segoe UI', Arial, sans-serif; 
            margin: 0; 
            padding: 0; 
            background-color: var(--tor-darker); 
            color: var(--tor-text);
        }
        
        .navbar {
            background-color: var(--tor-dark);
            padding: 15px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.5);
        }
        
        .logo {
            font-size: 22px;
            font-weight: bold;
            color: var(--tor-accent);
        }
        
        .nav-links {
            display: flex;
            gap: 20px;
        }
        
        .nav-links a {
            color: var(--tor-text);
            text-decoration: none;
            padding: 8px 12px;
            border-radius: 4px;
            transition: background-color 0.2s;
        }
        
        .nav-links a:hover {
            background-color: var(--tor-medium);
        }
        
        .nav-links a.active {
            background-color: var(--tor-purple);
            color: white;
        }
        
        .container {
            max-width: 1200px;
            margin: 20px auto;
            padding: 0 20px;
        }
        
        .page-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 30px;
        }
        
        .page-title {
            font-size: 24px;
            font-weight: bold;
        }
        
        .history-table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 30px;
            background-color: var(--tor-dark);
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }
        
        .history-table th, 
        .history-table td {
            padding: 12px 15px;
            text-align: left;
            border-bottom: 1px solid var(--tor-light);
        }
        
        .history-table th {
            background-color: var(--tor-purple);
            color: white;
            font-weight: 500;
        }
        
        .history-table tr:last-child td {
            border-bottom: none;
        }
        
        .history-table tr:hover {
            background-color: var(--tor-medium);
        }
        
        .actions {
            display: flex;
            gap: 8px;
        }
        
        .btn {
            background-color: var(--tor-medium);
            color: var(--tor-text);
            border: none;
            padding: 6px 10px;
            border-radius: 4px;
            cursor: pointer;
            text-decoration: none;
            font-size: 14px;
            display: inline-block;
        }
        
        .btn:hover {
            background-color: var(--tor-light);
        }
        
        .btn-view {
            background-color: var(--tor-accent);
            color: white;
        }
        
        .btn-view:hover {
            background-color: var(--tor-highlight);
        }
        
        .btn-report {
            background-color: var(--tor-medium);
            color: var(--tor-text);
        }
        
        .risk-label {
            display: inline-block;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: bold;
        }
        
        .risk-high {
            background-color: var(--high-risk);
            color: white;
        }
        
        .risk-medium {
            background-color: var(--medium-risk);
            color: black;
        }
        
        .risk-low {
            background-color: var(--low-risk);
            color: black;
        }
        
        .no-data {
            text-align: center;
            padding: 40px;
            background-color: var(--tor-dark);
            border-radius: 8px;
            margin-top: 40px;
            color: #888;
        }
        
        .pagination {
            display: flex;
            justify-content: center;
            gap: 5px;
            margin-top: 20px;
        }
        
        .pagination a,
        .pagination span {
            display: inline-block;
            padding: 8px 12px;
            background-color: var(--tor-medium);
            color: var(--tor-text);
            text-decoration: none;
            border-radius: 4px;
        }
        
        .pagination a:hover {
            background-color: var(--tor-light);
        }
        
        .pagination .active {
            background-color: var(--tor-accent);
            color: white;
        }
        
        .pagination .disabled {
            opacity: 0.5;
            cursor: not-allowed;
        }
        
        .search-box {
            display: flex;
            margin-bottom: 20px;
        }
        
        .search-box input {
            flex-grow: 1;
            padding: 10px;
            border: none;
            border-radius: 4px 0 0 4px;
            background-color: var(--tor-medium);
            color: var(--tor-text);
        }
        
        .search-box button {
            padding: 10px 15px;
            background-color: var(--tor-accent);
            color: white;
            border: none;
            border-radius: 0 4px 4px 0;
            cursor: pointer;
        }
        
        .search-box button:hover {
            background-color: var(--tor-highlight);
        }
        
        .filters {
            display: flex;
            gap: 15px;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }
        
        .filter-group {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .filter-label {
            font-size: 14px;
            color: #aaa;
        }
        
        .filter-select {
            padding: 8px;
            background-color: var(--tor-medium);
            color: var(--tor-text);
            border: none;
            border-radius: 4px;
        }

        /* Dynamic cybersecurity background with cursor effects */
        #particles-js {
            position: fixed;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            z-index: -1;
        }

        .cursor-follower {
            position: fixed;
            width: 200px;
            height: 200px;
            background: radial-gradient(circle, rgba(153, 102, 204, 0.3) 0%, rgba(153, 102, 204, 0) 70%);
            border-radius: 50%;
            pointer-events: none;
            transform: translate(-50%, -50%);
            z-index: -1;
            animation: pulse-cursor 2s infinite;
            mix-blend-mode: screen;
        }

        .data-lines {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -2;
            overflow: hidden;
        }

        .data-line {
            position: absolute;
            height: 1px;
            width: 100%;
            background-image: linear-gradient(to right, 
                transparent, 
                rgba(153, 102, 204, 0.1), 
                rgba(153, 102, 204, 0.2), 
                rgba(153, 102, 204, 0.1), 
                transparent);
            animation-name: data-line-animation;
            animation-timing-function: linear;
            animation-iteration-count: infinite;
            box-shadow: 0 0 5px rgba(153, 102, 204, 0.5);
        }

        @keyframes data-line-animation {
            0% { transform: translateY(-200%); }
            100% { transform: translateY(200vh); }
        }

        .digital-rain {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -3;
            color: rgba(153, 102, 204, 0.1);
            font-family: monospace;
            font-size: 14px;
            overflow: hidden;
            pointer-events: none;
        }

        .digital-rain .rain-column {
            position: absolute;
            top: -20%;
            animation-name: digital-rain-animation;
            animation-timing-function: linear;
            animation-iteration-count: infinite;
            text-align: center;
        }

        @keyframes digital-rain-animation {
            0% { transform: translateY(-100%); }
            100% { transform: translateY(200vh); }
        }

        @keyframes pulse-cursor {
            0% { opacity: 0.2; transform: translate(-50%, -50%) scale(1); }
            50% { opacity: 0.4; transform: translate(-50%, -50%) scale(1.5); }
            100% { opacity: 0.2; transform: translate(-50%, -50%) scale(1); }
        }
    </style>
</head>
<body>
    <!-- Dynamic background elements -->
    <div id="particles-js"></div>
    <div class="cursor-follower"></div>
    <div class="data-lines"></div>
    <div class="digital-rain"></div>

    <div class="navbar">
        <div class="logo">🧅 DARK WEB ANALYZER</div>
        <div class="nav-links">
            <a href="/"><i class="fas fa-home"></i> Home</a>
            <a href="/dashboard"><i class="fas fa-chart-line"></i> Dashboard</a>
            <a href="/history" class="active"><i class="fas fa-history"></i> History</a>
            <a href="/batch"><i class="fas fa-tasks"></i> Batch</a>
            <a href="/vulnerability"><i class="fas fa-shield-alt"></i> Vulnerability</a>
        </div>
    </div>
    
    <div class="container">
        <div class="page-header">
            <div class="page-title">Analysis History</div>
        </div>
        
        <div class="search-box">
            <input type="text" placeholder="Search by URL or content..." id="searchInput">
            <button onclick="filterTable()">Search</button>
        </div>
        
        <div class="filters">
            <div class="filter-group">
                <span class="filter-label">Risk Level:</span>
                <select class="filter-select" id="riskFilter" onchange="filterTable()">
                    <option value="all">All</option>
                    <option value="high">High Risk</option>
                    <option value="medium">Medium Risk</option>
                    <option value="low">Low Risk</option>
                </select>
            </div>
            
            <div class="filter-group">
                <span class="filter-label">Sort By:</span>
                <select class="filter-select" id="sortFilter" onchange="filterTable()">
                    <option value="newest">Newest First</option>
                    <option value="oldest">Oldest First</option>
                    <option value="risk-high">Highest Risk</option>
                    <option value="risk-low">Lowest Risk</option>
                </select>
            </div>
        </div>
        
        {% if not history.analyses or history.analyses|length == 0 %}
            <div class="no-data">
                <h2>No Analysis History</h2>
                <p>You haven't analyzed any sites yet.</p>
                <a href="/" style="color: var(--tor-accent);">Go to Analyzer</a>
            </div>
        {% else %}
            <table class="history-table">
                <thead>
                    <tr>
                        <th>URL</th>
                        <th>Risk Level</th>
                        <th>Category</th>
                        <th>Language</th>
                        <th>Date</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody id="historyTableBody">
                    {% for analysis in history.analyses|sort(attribute='timestamp', reverse=true) %}
                    <tr data-url="{{ analysis.url }}" data-risk="{{ analysis.risk_level if analysis.risk_level is defined else 0 }}" data-time="{{ analysis.timestamp }}">
                        <td>{{ analysis.url }}</td>
                        <td>
                            {% if analysis.risk_level is defined %}
                                {% if analysis.risk_level >= 7 %}
                                    <span class="risk-label risk-high">High ({{ analysis.risk_level }})</span>
                                {% elif analysis.risk_level >= 4 %}
                                    <span class="risk-label risk-medium">Medium ({{ analysis.risk_level }})</span>
                                {% else %}
                                    <span class="risk-label risk-low">Low ({{ analysis.risk_level }})</span>
                                {% endif %}
                            {% else %}
                                <span class="risk-label risk-low">Unknown</span>
                            {% endif %}
                        </td>
                        <td>{{ analysis.category if analysis.category is defined else "Unknown" }}</td>
                        <td>{{ analysis.language if analysis.language is defined else "Unknown" }}</td>
                        <td>{{ analysis.timestamp }}</td>
                        <td class="actions">
                            <a href="/analysis/{{ analysis.id }}" class="btn btn-view">View</a>
                            <a href="/report/{{ analysis.id }}" class="btn btn-report">Report</a>
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
            
            <div class="pagination">
                <!-- Pagination will be added by JavaScript if needed -->
            </div>
        {% endif %}
    </div>

    <script>
        // Simple search and filter functionality
        function filterTable() {
            const searchTerm = document.getElementById('searchInput').value.toLowerCase();
            const riskFilter = document.getElementById('riskFilter').value;
            const sortFilter = document.getElementById('sortFilter').value;
            const tableRows = document.querySelectorAll('#historyTableBody tr');
            
            // Filter rows
            tableRows.forEach(row => {
                const url = row.getAttribute('data-url').toLowerCase();
                const riskLevel = parseInt(row.getAttribute('data-risk'));
                
                let showRow = url.includes(searchTerm);
                
                // Apply risk filter
                if (riskFilter !== 'all') {
                    if (riskFilter === 'high' && riskLevel < 7) showRow = false;
                    if (riskFilter === 'medium' && (riskLevel < 4 || riskLevel >= 7)) showRow = false;
                    if (riskFilter === 'low' && riskLevel >= 4) showRow = false;
                }
                
                row.style.display = showRow ? '' : 'none';
            });
            
            // Sort rows
            const tbody = document.getElementById('historyTableBody');
            const rows = Array.from(tbody.querySelectorAll('tr'));
            
            rows.sort((a, b) => {
                if (sortFilter === 'newest') {
                    return new Date(b.getAttribute('data-time')) - new Date(a.getAttribute('data-time'));
                } else if (sortFilter === 'oldest') {
                    return new Date(a.getAttribute('data-time')) - new Date(b.getAttribute('data-time'));
                } else if (sortFilter === 'risk-high') {
                    return parseInt(b.getAttribute('data-risk')) - parseInt(a.getAttribute('data-risk'));
                } else if (sortFilter === 'risk-low') {
                    return parseInt(a.getAttribute('data-risk')) - parseInt(b.getAttribute('data-risk'));
                }
                return 0;
            });
            
            rows.forEach(row => {
                tbody.appendChild(row);
            });
        }

        // Initialize dynamic background effects
        document.addEventListener('DOMContentLoaded', function() {
            // Load particles.js script
            const script = document.createElement('script');
            script.src = 'https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js';
            script.onload = initDynamicBackground;
            document.head.appendChild(script);
        });

        function initDynamicBackground() {
            // Initialize particles.js
            particlesJS('particles-js', {
                "particles": {
                    "number": {
                        "value": 40,
                        "density": {
                            "enable": true,
                            "value_area": 800
                        }
                    },
                    "color": {
                        "value": "#9966cc"
                    },
                    "shape": {
                        "type": "circle",
                        "stroke": {
                            "width": 0,
                            "color": "#000000"
                        }
                    },
                    "opacity": {
                        "value": 0.2,
                        "random": true,
                        "anim": {
                            "enable": true,
                            "speed": 1,
                            "opacity_min": 0.1,
                            "sync": false
                        }
                    },
                    "size": {
                        "value": 3,
                        "random": true,
                        "anim": {
                            "enable": true,
                            "speed": 2,
                            "size_min": 0.1,
                            "sync": false
                        }
                    },
                    "line_linked": {
                        "enable": true,
                        "distance": 150,
                        "color": "#7d4698",
                        "opacity": 0.2,
                        "width": 1
                    },
                    "move": {
                        "enable": true,
                        "speed": 1,
                        "direction": "none",
                        "random": true,
                        "straight": false,
                        "out_mode": "out",
                        "bounce": false,
                        "attract": {
                            "enable": true,
                            "rotateX": 600,
                            "rotateY": 1200
                        }
                    }
                },
                "interactivity": {
                    "detect_on": "canvas",
                    "events": {
                        "onhover": {
                            "enable": true,
                            "mode": "grab"
                        },
                        "onclick": {
                            "enable": true,
                            "mode": "push"
                        },
                        "resize": true
                    },
                    "modes": {
                        "grab": {
                            "distance": 140,
                            "line_linked": {
                                "opacity": 0.5
                            }
                        },
                        "push": {
                            "particles_nb": 3
                        }
                    }
                },
                "retina_detect": true
            });

            // Create cursor follower effect
            const cursorFollower = document.querySelector('.cursor-follower');
            document.addEventListener('mousemove', (e) => {
                cursorFollower.style.left = e.clientX + 'px';
                cursorFollower.style.top = e.clientY + 'px';
            });

            // Create data lines effect
            const dataLines = document.querySelector('.data-lines');
            for (let i = 0; i < 15; i++) {
                const line = document.createElement('div');
                line.classList.add('data-line');
                line.style.top = Math.random() * 100 + 'vh';
                line.style.animationDuration = (Math.random() * 8 + 5) + 's';
                line.style.opacity = Math.random() * 0.5 + 0.1;
                dataLines.appendChild(line);
            }

            // Create digital rain effect
            const digitalRain = document.querySelector('.digital-rain');
            const characters = '01アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン';
            
            for (let i = 0; i < 30; i++) {
                const column = document.createElement('div');
                column.classList.add('rain-column');
                column.style.left = (Math.random() * 100) + 'vw';
                column.style.animationDuration = (Math.random() * 10 + 10) + 's';
                column.style.opacity = Math.random() * 0.3 + 0.1;
                
                const columnLength = Math.floor(Math.random() * 20 + 10);
                let columnHtml = '';
                
                for (let j = 0; j < columnLength; j++) {
                    const charIndex = Math.floor(Math.random() * characters.length);
                    columnHtml += characters.charAt(charIndex) + '<br>';
                }
                
                column.innerHTML = columnHtml;
                digitalRain.appendChild(column);
            }
        }
    </script>
</body>
</html> 
!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dark Web Crawler Interface</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css">
    <style>
        :root {
            --tor-purple: #7d4698;
            --tor-dark: #1a1a1a;
            --tor-darker: #121212;
            --tor-medium: #2a2a2a;
            --tor-light: #3a3a3a;
            --tor-text: #e0e0e0;
            --tor-accent: #9966cc;
            --tor-highlight: #56347c;
            --high-risk: #ff2a6d;
            --medium-risk: #ffd000;
            --low-risk: #00ff66;
            --card-shadow: 0 8px 16px rgba(0,0,0,0.3);
            --card-border: 1px solid rgba(255,255,255,0.05);
            --card-radius: 12px;
            --transition-speed: 0.3s;
        }
        
        [data-theme="light"] {
            --tor-purple: #9356b8;
            --tor-dark: #f5f5f5;
            --tor-darker: #eeeeee;
            --tor-medium: #dddddd;
            --tor-light: #cccccc;
            --tor-text: #333333;
            --tor-accent: #7d4698;
            --tor-highlight: #9966cc;
            --card-shadow: 0 8px 16px rgba(0,0,0,0.1);
            --card-border: 1px solid rgba(0,0,0,0.05);
        }
        
        * {
            box-sizing: border-box;
            transition: background-color var(--transition-speed), color var(--transition-speed);
        }
        
        body { 
            font-family: 'Segoe UI', Arial, sans-serif; 
            margin: 0; 
            padding: 0; 
            background-color: var(--tor-darker); 
            color: var(--tor-text);
        }
        
        .navbar {
            background-color: var(--tor-dark);
            padding: 15px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.5);
            position: sticky;
            top: 0;
            z-index: 100;
        }
        
        .logo-nav {
            font-size: 22px;
            font-weight: bold;
            color: var(--tor-accent);
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .logo-nav i {
            font-size: 24px;
        }
        
        .nav-links {
            display: flex;
            gap: 20px;
        }
        
        .nav-links a {
            color: var(--tor-text);
            text-decoration: none;
            padding: 8px 12px;
            border-radius: 6px;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            gap: 6px;
        }
        
        .nav-links a:hover {
            background-color: var(--tor-medium);
            transform: translateY(-2px);
        }
        
        .nav-links a.active {
            background-color: var(--tor-purple);
            color: white;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        
        .theme-toggle {
            background: none;
            border: none;
            color: var(--tor-text);
            cursor: pointer;
            font-size: 18px;
            padding: 8px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s;
        }
        
        .theme-toggle:hover {
            background-color: var(--tor-medium);
            transform: rotate(30deg);
        }
        
        h1, h2, h3 { 
            color: var(--tor-text); 
            text-align: center; 
            margin-bottom: 30px;
            text-shadow: 0 1px 3px rgba(0,0,0,0.5);
        }
        
        .container { 
            max-width: 1200px; 
            margin: 30px auto; 
            animation: fadeIn 0.5s ease-in-out;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .search-card {
            background-color: var(--tor-dark); 
            padding: 30px; 
            border-radius: var(--card-radius); 
            box-shadow: var(--card-shadow);
            border: var(--card-border);
            margin-bottom: 30px;
            transition: all 0.3s;
            position: relative;
            overflow: hidden;
        }
        
        .search-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 20px rgba(0,0,0,0.4);
        }
        
        .logo {
            text-align: center;
            margin-bottom: 30px;
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        
        .logo-inner {
            font-size: 28px;
            font-weight: bold;
            letter-spacing: 1px;
            color: var(--tor-accent);
            display: inline-flex;
            align-items: center;
            gap: 15px;
            padding: 15px 25px;
            border-radius: 50px;
            background-color: rgba(0,0,0,0.2);
            border: 2px solid var(--tor-accent);
            text-shadow: 0 1px 3px rgba(0,0,0,0.5);
            box-shadow: 0 5px 15px rgba(125, 70, 152, 0.3);
        }
        
        .logo-inner i {
            font-size: 32px;
        }
        
        form { 
            display: flex; 
            gap: 10px; 
            margin-bottom: 30px; 
            align-items: center; 
        }
        
        form input[type="text"] { 
            flex-grow: 1; 
            padding: 16px; 
            border: 1px solid var(--tor-light); 
            border-radius: 8px; 
            font-size: 16px; 
            background-color: var(--tor-medium);
            color: var(--tor-text);
            transition: all 0.3s;
            box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        
        form input[type="text"]:focus {
            border-color: var(--tor-accent);
            outline: none;
            box-shadow: 0 0 0 3px rgba(153, 102, 204, 0.3);
        }
        
        form input[type="submit"] { 
            padding: 16px 30px; 
            background-color: var(--tor-purple); 
            color: white; 
            border: none; 
            border-radius: 8px; 
            cursor: pointer; 
            font-size: 16px;
            font-weight: bold;
            transition: all 0.3s;
            display: flex;
            align-items: center;
            gap: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        }
        
        form input[type="submit"]:hover { 
            background-color: var(--tor-accent);
            transform: translateY(-2px);
            box-shadow: 0 6px 10px rgba(0, 0, 0, 0.3);
        }
        
        table { 
            width: 100%; 
            margin-top: 20px; 
            border-collapse: separate;
            border-spacing: 0;
            border-radius: var(--card-radius);
            overflow: hidden;
            box-shadow: var(--card-shadow);
        }
        
        th, td { 
            padding: 15px; 
            text-align: left; 
            word-break: break-word;
        }
        
        th { 
            background-color: var(--tor-purple); 
            color: white;
            font-weight: 500;
            position: sticky;
            top: 70px;
            z-index: 10;
        }
        
        tr:nth-child(even) { background-color: var(--tor-medium); }
        tr:hover { 
            background-color: var(--tor-light); 
            transform: scale(1.01);
            transition: all 0.2s;
        }
        
        td {
            border-bottom: 1px solid var(--tor-light);
        }
        
        tr:last-child td {
            border-bottom: none;
        }
        
        .error { 
            color: var(--high-risk); 
            background-color: rgba(255, 77, 77, 0.1); 
            border-left: 5px solid var(--high-risk); 
            padding: 20px; 
            margin-bottom: 20px; 
            border-radius: 8px;
            display: flex;
            align-items: center;
            gap: 15px;
            animation: shake 0.5s ease-in-out;
        }
        
        @keyframes shake {
            0%, 100% { transform: translateX(0); }
            10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); }
            20%, 40%, 60%, 80% { transform: translateX(5px); }
        }
        
        .error i {
            font-size: 24px;
            color: var(--high-risk);
        }
        
        .no-data { 
            margin-top: 20px; 
            text-align: center; 
            color: var(--tor-text); 
            background-color: var(--tor-medium); 
            padding: 30px; 
            border: var(--card-border);
            border-radius: var(--card-radius);
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 15px;
        }
        
        .no-data i {
            font-size: 32px;
            color: var(--tor-accent);
            opacity: 0.7;
        }
        
        .results-card {
            background-color: var(--tor-dark); 
            border-radius: var(--card-radius); 
            padding: 30px; 
            box-shadow: var(--card-shadow);
            border: var(--card-border);
            margin-top: 30px;
            animation: slideUp 0.5s ease-in-out;
        }
        
        @keyframes slideUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .results-header { 
            font-size: 1.5em; 
            color: var(--tor-text); 
            margin-top: 0;
            margin-bottom: 20px; 
            text-align: left;
            border-bottom: 1px solid var(--tor-light);
            padding-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .results-header i {
            color: var(--tor-accent);
        }
        
        .ip-info { 
            background-color: var(--tor-medium); 
            border-left: 4px solid var(--tor-purple); 
            margin-bottom: 20px; 
            padding: 20px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            gap: 15px;
        }
        
        .ip-info i {
            font-size: 24px;
            color: var(--tor-accent);
        }
        
        .ip-info p { margin: 5px 0; }
        .ip-info strong { color: var(--tor-accent); }
        
        .ai-analysis { 
            background-color: var(--tor-medium); 
            padding: 20px; 
            border-radius: 8px; 
            white-space: pre-line; 
            font-family: 'Consolas', monospace;
            line-height: 1.6;
            overflow: auto;
            max-height: 400px;
            margin-top: 20px;
            position: relative;
            border: 1px solid var(--tor-light);
        }
        
        .ai-analysis::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        
        .ai-analysis::-webkit-scrollbar-track {
            background: var(--tor-dark);
            border-radius: 10px;
        }
        
        .ai-analysis::-webkit-scrollbar-thumb {
            background: var(--tor-accent);
            border-radius: 10px;
        }
        
        .ai-analysis-header { 
            font-weight: bold; 
            color: var(--tor-accent); 
            margin-bottom: 15px;
            font-size: 1.1em;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        #ai-assessment { 
            margin-top: 30px; 
            background-color: var(--tor-dark); 
            padding: 25px; 
            border-radius: var(--card-radius);
            border-left: 5px solid var(--tor-purple);
            margin-bottom: 30px;
            box-shadow: var(--card-shadow);
            transition: all 0.3s;
        }
        
        #ai-assessment:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 20px rgba(0,0,0,0.4);
        }
        
        /* Risk indicators */
        .risk-high {
            background-color: rgba(255, 77, 77, 0.15);
            border-left: 5px solid var(--high-risk) !important;
        }
        
        .risk-medium {
            background-color: rgba(255, 166, 77, 0.15);
            border-left: 5px solid var(--medium-risk) !important;
        }
        
        .risk-low {
            background-color: rgba(255, 166, 77, 0.05);
            border-left: 5px solid var(--low-risk) !important;
        }
        
        /* Risk badge */
        .risk-badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 6px 12px;
            border-radius: 20px;
            font-weight: bold;
            margin-top: 10px;
            font-size: 0.9em;
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }
        
        .badge-high {
            background-color: var(--high-risk);
            color: white;
        }
        
        .badge-medium {
            background-color: var(--medium-risk);
            color: black;
        }
        
        .badge-low {
            background-color: var(--low-risk);
            color: black;
        }
        
        .batch-link {
            margin-top: 20px;
            text-align: center;
        }
        
        .batch-link a {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            color: var(--tor-accent);
            text-decoration: none;
            padding: 10px 15px;
            border: 1px solid var(--tor-accent);
            border-radius: 6px;
            transition: all 0.3s;
        }
        
        .batch-link a:hover {
            background-color: var(--tor-accent);
            color: white;
            transform: translateY(-2px);
        }
        
        .loading {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: var(--tor-darker);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 9999;
            transition: opacity 0.5s;
        }
        
        .loading.fade-out {
            opacity: 0;
            pointer-events: none;
        }
        
        .loader {
            width: 50px;
            height: 50px;
            border: 5px solid var(--tor-medium);
            border-radius: 50%;
            border-top-color: var(--tor-accent);
            animation: spin 1s linear infinite;
        }
        
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
        
        .loading-text {
            position: absolute;
            bottom: 100px;
            color: var(--tor-accent);
            font-size: 14px;
            letter-spacing: 1px;
        }
        
        /* Add cybersecurity themed grid background */
        body::before {
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: 
                radial-gradient(rgba(125, 70, 152, 0.1) 2px, transparent 2px),
                radial-gradient(rgba(125, 70, 152, 0.05) 1px, transparent 1px);
            background-size: 50px 50px, 25px 25px;
            background-position: 0 0, 25px 25px;
            z-index: -1;
            animation: gridShift 60s linear infinite;
        }
        
        @keyframes gridShift {
            0% { background-position: 0 0, 25px 25px; }
            100% { background-position: 100px 100px, 125px 125px; }
        }
        
        /* Add pulsing effect to cards */
        .search-card::after {
            content: "";
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 2px;
            background: linear-gradient(90deg, transparent, var(--tor-accent), transparent);
            animation: scanning 4s linear infinite;
        }
        
        @keyframes scanning {
            0% { left: -100%; }
            100% { left: 100%; }
        }

        /* Dynamic cybersecurity background with cursor effects */
        #particles-js {
            position: fixed;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            z-index: -1;
        }

        .cursor-follower {
            position: fixed;
            width: 200px;
            height: 200px;
            background: radial-gradient(circle, rgba(153, 102, 204, 0.3) 0%, rgba(153, 102, 204, 0) 70%);
            border-radius: 50%;
            pointer-events: none;
            transform: translate(-50%, -50%);
            z-index: -1;
            animation: pulse-cursor 2s infinite;
            mix-blend-mode: screen;
        }

        .data-lines {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -2;
            overflow: hidden;
        }

        .data-line {
            position: absolute;
            height: 1px;
            width: 100%;
            background-image: linear-gradient(to right, 
                transparent, 
                rgba(153, 102, 204, 0.1), 
                rgba(153, 102, 204, 0.2), 
                rgba(153, 102, 204, 0.1), 
                transparent);
            animation-name: data-line-animation;
            animation-timing-function: linear;
            animation-iteration-count: infinite;
            box-shadow: 0 0 5px rgba(153, 102, 204, 0.5);
        }

        @keyframes data-line-animation {
            0% { transform: translateY(-200%); }
            100% { transform: translateY(200vh); }
        }

        .digital-rain {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -3;
            color: rgba(153, 102, 204, 0.1);
            font-family: monospace;
            font-size: 14px;
            overflow: hidden;
            pointer-events: none;
        }

        .digital-rain .rain-column {
            position: absolute;
            top: -20%;
            animation-name: digital-rain-animation;
            animation-timing-function: linear;
            animation-iteration-count: infinite;
            text-align: center;
        }

        @keyframes digital-rain-animation {
            0% { transform: translateY(-100%); }
            100% { transform: translateY(200vh); }
        }

        @keyframes pulse-cursor {
            0% { opacity: 0.2; transform: translate(-50%, -50%) scale(1); }
            50% { opacity: 0.4; transform: translate(-50%, -50%) scale(1.5); }
            100% { opacity: 0.2; transform: translate(-50%, -50%) scale(1); }
        }

        body::before {
            display: none; /* Remove original background */
        }
    </style>
</head>
<body>
    <!-- Dynamic background elements -->
    <div id="particles-js"></div>
    <div class="cursor-follower"></div>
    <div class="data-lines"></div>
    <div class="digital-rain"></div>

    <div class="loading">
        <div class="loader"></div>
        <div class="loading-text">Loading Dark Web Analyzer...</div>
    </div>

    <div class="navbar">
        <div class="logo-nav"><i class="fas fa-globe-americas"></i> DARK WEB ANALYZER</div>
        <div class="nav-links">
            <a href="/" class="active"><i class="fas fa-home"></i> Home</a>
            <a href="/dashboard"><i class="fas fa-chart-line"></i> Dashboard</a>
            <a href="/history"><i class="fas fa-history"></i> History</a>
            <a href="/batch"><i class="fas fa-tasks"></i> Batch</a>
            <a href="/vulnerability"><i class="fas fa-shield-alt"></i> Vulnerability</a>
        </div>
        <button class="theme-toggle" id="themeToggle"><i class="fas fa-moon"></i></button>
    </div>
    
    <div class="container">
        <div class="search-card">
            <div class="logo">
                <div class="logo-inner"><i class="fas fa-search"></i> DARK WEB ANALYZER</div>
            </div>
            
            <form method="POST" id="analyzeForm">
                <input type="text" name="onion_url" placeholder="Enter .onion URL (e.g., http://example.onion)" required>
                <input type="submit" value="Analyze URL"><i class="fas fa-arrow-right"></i>
            </form>

            <div class="batch-link">
                <a href="/batch"><i class="fas fa-layer-group"></i> Need to analyze multiple URLs? Use Batch Processing</a>
            </div>

            {% if tor_ip_address %}
                <div class="ip-info">
                    <i class="fas fa-globe"></i>
                    <div>
                        <p><strong>Apparent IP via Tor Session:</strong> {{ tor_ip_address }}</p>
                        <p><small>If this IP is different from your actual public IP, it indicates the script is likely using Tor. If it shows an error or your actual IP, the script is not correctly routing through Tor for the IP check.</small></p>
                    </div>
                </div>
            {% endif %}

            {% if error_message %}
                <div class="error">
                    <i class="fas fa-exclamation-triangle"></i>
                    <div>
                        <p><strong>Analysis Failed:</strong> {{ error_message }}</p>
                    </div>
                </div>
            {% endif %}
        </div>

        {% if data and data|length > 0 %}
            <div class="results-card">
                <h2 class="results-header"><i class="fas fa-file-alt"></i> Analysis Results</h2>
                
                {% for result in data %}
                    {% if result.success %}
                        {% if result.ai_analysis %}
                            <div id="ai-assessment" class="{% if 'RISK_LEVEL: 7' in result.ai_analysis or 'RISK_LEVEL: 8' in result.ai_analysis or 'RISK_LEVEL: 9' in result.ai_analysis or 'RISK_LEVEL: 10' in result.ai_analysis %}risk-high{% elif 'RISK_LEVEL: 4' in result.ai_analysis or 'RISK_LEVEL: 5' in result.ai_analysis or 'RISK_LEVEL: 6' in result.ai_analysis %}risk-medium{% else %}risk-low{% endif %}">
                                <div class="ai-analysis-header">
                                    <i class="fas fa-robot"></i> AI Analysis for {{ result.url }}
                                </div>
                                <div class="ai-analysis">{{ result.ai_analysis }}</div>
                                
                                {% if 'RISK_LEVEL: 7' in result.ai_analysis or 'RISK_LEVEL: 8' in result.ai_analysis or 'RISK_LEVEL: 9' in result.ai_analysis or 'RISK_LEVEL: 10' in result.ai_analysis %}
                                    <div class="risk-badge badge-high"><i class="fas fa-exclamation-triangle"></i> High Risk Content Detected</div>
                                {% elif 'RISK_LEVEL: 4' in result.ai_analysis or 'RISK_LEVEL: 5' in result.ai_analysis or 'RISK_LEVEL: 6' in result.ai_analysis %}
                                    <div class="risk-badge badge-medium"><i class="fas fa-exclamation"></i> Medium Risk Content Detected</div>
                                {% else %}
                                    <div class="risk-badge badge-low"><i class="fas fa-check-circle"></i> Low Risk Content</div>
                                {% endif %}
                            </div>
                        {% endif %}
                        
                        <table>
                            <tr>
                                <th>Property</th>
                                <th>Value</th>
                            </tr>
                            <tr>
                                <td>URL</td>
                                <td>{{ result.url }}</td>
                            </tr>
                            <tr>
                                <td>Language</td>
                                <td>{{ result.language }}</td>
                            </tr>
                            <tr>
                                <td>Sentiment</td>
                                <td>{{ result.sentiment }}</td>
                            </tr>
                            <tr>
                                <td>Suspicious Keywords</td>
                                <td>
                                    {% if result.suspicious_keywords and result.suspicious_keywords|length > 0 %}
                                        {% for keyword in result.suspicious_keywords %}
                                            <span style="display: inline-block; background-color: rgba(255,77,77,0.2); padding: 3px 8px; margin: 2px; border-radius: 4px;">{{ keyword }}</span>
                                        {% endfor %}
                                    {% else %}
                                        None detected
                                    {% endif %}
                                </td>
                            </tr>
                            <tr>
                                <td>Text Snippet</td>
                                <td>{{ result.raw_text_snippet }}</td>
                            </tr>
                        </table>
                    {% else %}
                        <div class="error">
                            <i class="fas fa-exclamation-triangle"></i>
                            <div>
                                <p><strong>Analysis Failed for {{ result.url }}:</strong> {{ result.error }}</p>
                            </div>
                        </div>
                    {% endif %}
                {% endfor %}
            </div>
        {% elif not error_message %}
            <div class="no-data">
                <i class="fas fa-info-circle"></i>
                <p>Enter a .onion URL to analyze its content and evaluate potential risks.</p>
            </div>
        {% endif %}
    </div>
    
    <script>
        // Loading screen
        window.addEventListener('load', function() {
            setTimeout(function() {
                const loader = document.querySelector('.loading');
                loader.classList.add('fade-out');
            }, 800);
            
            // Initialize dynamic background
            initDynamicBackground();
        });
        
        // Loading animation during form submission
        document.getElementById('analyzeForm').addEventListener('submit', function() {
            const loader = document.querySelector('.loading');
            loader.classList.remove('fade-out');
            document.querySelector('.loading-text').textContent = "Analyzing .onion site...";
        });
        
        // Theme toggle
        const themeToggle = document.getElementById('themeToggle');
        const htmlElement = document.documentElement;
        
        themeToggle.addEventListener('click', function() {
            if (htmlElement.getAttribute('data-theme') === 'dark') {
                htmlElement.setAttribute('data-theme', 'light');
                themeToggle.innerHTML = '<i class="fas fa-sun"></i>';
                localStorage.setItem('theme', 'light');
            } else {
                htmlElement.setAttribute('data-theme', 'dark');
                themeToggle.innerHTML = '<i class="fas fa-moon"></i>';
                localStorage.setItem('theme', 'dark');
            }
        });
        
        // Check for saved theme preference
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme) {
            htmlElement.setAttribute('data-theme', savedTheme);
            themeToggle.innerHTML = savedTheme === 'dark' ? 
                '<i class="fas fa-moon"></i>' : 
                '<i class="fas fa-sun"></i>';
        }
        
        // Initialize dynamic background effects
        function initDynamicBackground() {
            // Load particles.js if not already loaded
            if (typeof particlesJS === 'undefined') {
                const script = document.createElement('script');
                script.src = 'https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js';
                script.onload = setupParticles;
                document.head.appendChild(script);
            } else {
                setupParticles();
            }
            
            // Initialize cursor follower
            const cursorFollower = document.querySelector('.cursor-follower');
            document.addEventListener('mousemove', (e) => {
                cursorFollower.style.left = e.clientX + 'px';
                cursorFollower.style.top = e.clientY + 'px';
            });
            
            // Create data lines
            const dataLines = document.querySelector('.data-lines');
            for (let i = 0; i < 15; i++) {
                const line = document.createElement('div');
                line.classList.add('data-line');
                line.style.top = Math.random() * 100 + 'vh';
                line.style.animationDuration = (Math.random() * 8 + 5) + 's';
                line.style.opacity = Math.random() * 0.5 + 0.1;
                dataLines.appendChild(line);
            }
            
            // Create digital rain
            const digitalRain = document.querySelector('.digital-rain');
            const characters = '01アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン';
            
            for (let i = 0; i < 30; i++) {
                const column = document.createElement('div');
                column.classList.add('rain-column');
                column.style.left = (Math.random() * 100) + 'vw';
                column.style.animationDuration = (Math.random() * 10 + 10) + 's';
                column.style.opacity = Math.random() * 0.3 + 0.1;
                
                const columnLength = Math.floor(Math.random() * 20 + 10);
                let columnHtml = '';
                
                for (let j = 0; j < columnLength; j++) {
                    const charIndex = Math.floor(Math.random() * characters.length);
                    columnHtml += characters.charAt(charIndex) + '<br>';
                }
                
                column.innerHTML = columnHtml;
                digitalRain.appendChild(column);
            }
        }
        
        function setupParticles() {
            particlesJS('particles-js', {
                "particles": {
                    "number": {
                        "value": 40,
                        "density": {
                            "enable": true,
                            "value_area": 800
                        }
                    },
                    "color": {
                        "value": "#9966cc"
                    },
                    "shape": {
                        "type": "circle",
                        "stroke": {
                            "width": 0,
                            "color": "#000000"
                        }
                    },
                    "opacity": {
                        "value": 0.2,
                        "random": true,
                        "anim": {
                            "enable": true,
                            "speed": 1,
                            "opacity_min": 0.1,
                            "sync": false
                        }
                    },
                    "size": {
                        "value": 3,
                        "random": true,
                        "anim": {
                            "enable": true,
                            "speed": 2,
                            "size_min": 0.1,
                            "sync": false
                        }
                    },
                    "line_linked": {
                        "enable": true,
                        "distance": 150,
                        "color": "#7d4698",
                        "opacity": 0.2,
                        "width": 1
                    },
                    "move": {
                        "enable": true,
                        "speed": 1,
                        "direction": "none",
                        "random": true,
                        "straight": false,
                        "out_mode": "out",
                        "bounce": false,
                        "attract": {
                            "enable": true,
                            "rotateX": 600,
                            "rotateY": 1200
                        }
                    }
                },
                "interactivity": {
                    "detect_on": "canvas",
                    "events": {
                        "onhover": {
                            "enable": true,
                            "mode": "grab"
                        },
                        "onclick": {
                            "enable": true,
                            "mode": "push"
                        },
                        "resize": true
                    },
                    "modes": {
                        "grab": {
                            "distance": 140,
                            "line_linked": {
                                "opacity": 0.5
                            }
                        },
                        "push": {
                            "particles_nb": 3
                        }
                    }
                },
                "retina_detect": true
            });
        }
    </script>
</body>
</html> 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DarkWeb Crawler - Vulnerability Assessment</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        :root {
            --cyber-dark: #0a0e17;
            --cyber-darker: #050709;
            --cyber-accent: #00b4d8;
            --cyber-accent-hover: #0096c7;
            --cyber-text: #e0e0e0;
            --cyber-green: #00ff66;
            --cyber-yellow: #ffd000;
            --cyber-red: #ff2a6d;
            --risk-high: rgba(255, 42, 109, 0.1);
            --risk-medium: rgba(255, 208, 0, 0.1);
            --risk-low: rgba(0, 255, 102, 0.1);
        }
        
        body {
            background-color: var(--cyber-dark);
            color: var(--cyber-text);
            font-family: 'Courier New', monospace;
            position: relative;
            overflow-x: hidden;
        }
        
        body::before {
            display: none; /* Remove original background */
        }
        
        .navbar {
            background-color: var(--cyber-darker);
            border-bottom: 1px solid var(--cyber-accent);
        }
        
        .navbar-brand, .nav-link {
            color: var(--cyber-accent) !important;
            text-shadow: 0 0 5px rgba(0, 180, 216, 0.5);
            transition: all 0.3s ease;
        }
        
        .nav-link:hover, .navbar-brand:hover {
            color: var(--cyber-text) !important;
            text-shadow: 0 0 10px var(--cyber-accent);
        }
        
        .content-section {
            background-color: rgba(10, 14, 23, 0.7);
            border: 1px solid var(--cyber-accent);
            border-radius: 5px;
            padding: 20px;
            margin-bottom: 30px;
            box-shadow: 0 0 15px rgba(0, 180, 216, 0.2);
            position: relative;
            overflow: hidden;
        }
        
        .content-section::after {
            content: "";
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 2px;
            background: linear-gradient(90deg, transparent, var(--cyber-accent), transparent);
            animation: scanning 3s linear infinite;
        }
        
        @keyframes scanning {
            0% { left: -100%; }
            100% { left: 100%; }
        }
        
        .section-title {
            color: var(--cyber-accent);
            font-weight: bold;
            text-transform: uppercase;
            display: inline-block;
            position: relative;
            margin-bottom: 20px;
        }
        
        .section-title::before, .section-title::after {
            content: "//";
            color: var(--cyber-accent);
            margin: 0 8px;
            opacity: 0.7;
        }
        
        .btn-cyber {
            background-color: var(--cyber-accent);
            color: var(--cyber-darker);
            border: none;
            font-weight: bold;
            text-transform: uppercase;
            position: relative;
            overflow: hidden;
            z-index: 1;
            transition: all 0.3s ease;
        }
        
        .btn-cyber:hover {
            background-color: var(--cyber-accent-hover);
            box-shadow: 0 0 10px var(--cyber-accent);
            color: white;
        }
        
        .btn-cyber::before {
            content: "";
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
            transition: all 0.3s ease;
            z-index: -1;
        }
        
        .btn-cyber:hover::before {
            left: 100%;
            transition: all 0.3s ease;
        }
        
        .risk-indicator {
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            line-height: 50px;
            margin: 0 auto;
            transition: all 0.3s ease;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
            position: relative;
            overflow: hidden;
        }
        
        .risk-high {
            background-color: var(--cyber-red);
            color: white;
        }
        
        .risk-high::after {
            content: "";
            position: absolute;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            background: radial-gradient(circle, rgba(255, 42, 109, 0.7) 0%, rgba(255, 42, 109, 0) 70%);
            animation: pulse 1.5s ease-out infinite;
        }
        
        .risk-medium {
            background-color: var(--cyber-yellow);
            color: var(--cyber-darker);
        }
        
        .risk-medium::after {
            content: "";
            position: absolute;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            background: radial-gradient(circle, rgba(255, 208, 0, 0.7) 0%, rgba(255, 208, 0, 0) 70%);
            animation: pulse 2s ease-out infinite;
        }
        
        .risk-low {
            background-color: var(--cyber-green);
            color: var(--cyber-darker);
        }
        
        .risk-low::after {
            content: "";
            position: absolute;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            background: radial-gradient(circle, rgba(0, 255, 102, 0.7) 0%, rgba(0, 255, 102, 0) 70%);
            animation: pulse 3s ease-out infinite;
        }
        
        @keyframes pulse {
            0% { opacity: 0.7; transform: scale(1); }
            100% { opacity: 0; transform: scale(2.5); }
        }
        
        .card {
            background-color: rgba(5, 7, 9, 0.7);
            border: 1px solid var(--cyber-accent);
            margin-bottom: 15px;
            transition: all 0.3s ease;
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0, 180, 216, 0.2);
        }
        
        .card-header {
            background-color: rgba(0, 180, 216, 0.1);
            border-bottom: 1px solid var(--cyber-accent);
            color: var(--cyber-accent);
            font-weight: bold;
        }
        
        .risk-card-high {
            border-color: var(--cyber-red);
            background: var(--risk-high);
        }
        
        .risk-card-high .card-header {
            background-color: rgba(255, 42, 109, 0.2);
            border-bottom: 1px solid var(--cyber-red);
            color: var(--cyber-red);
        }
        
        .risk-card-medium {
            border-color: var(--cyber-yellow);
            background: var(--risk-medium);
        }
        
        .risk-card-medium .card-header {
            background-color: rgba(255, 208, 0, 0.2);
            border-bottom: 1px solid var(--cyber-yellow);
            color: var(--cyber-yellow);
        }
        
        .risk-card-low {
            border-color: var(--cyber-green);
            background: var(--risk-low);
        }
        
        .risk-card-low .card-header {
            background-color: rgba(0, 255, 102, 0.2);
            border-bottom: 1px solid var(--cyber-green);
            color: var(--cyber-green);
        }
        
        .typing-effect {
            border-right: 2px solid var(--cyber-accent);
            white-space: nowrap;
            overflow: hidden;
            width: 0;
            animation: typing 3.5s steps(40, end) forwards, blink-caret 0.75s step-end infinite;
        }
        
        @keyframes typing {
            from { width: 0 }
            to { width: 100% }
        }
        
        @keyframes blink-caret {
            from, to { border-color: transparent }
            50% { border-color: var(--cyber-accent) }
        }
        
        .spinner {
            width: 40px;
            height: 40px;
            margin: 0 auto;
            border: 4px solid rgba(0, 180, 216, 0.2);
            border-top: 4px solid var(--cyber-accent);
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        /* Dynamic background with cursor effects */
        #particles-js {
            position: fixed;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            z-index: -1;
        }

        .cursor-follower {
            position: fixed;
            width: 200px;
            height: 200px;
            background: radial-gradient(circle, rgba(0,180,216,0.3) 0%, rgba(0,180,216,0) 70%);
            border-radius: 50%;
            pointer-events: none;
            transform: translate(-50%, -50%);
            z-index: -1;
            animation: pulse-cursor 2s infinite;
            mix-blend-mode: screen;
        }

        .data-lines {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -2;
            overflow: hidden;
        }

        .data-line {
            position: absolute;
            height: 1px;
            width: 100%;
            background-image: linear-gradient(to right, 
                transparent, 
                rgba(0, 180, 216, 0.1), 
                rgba(0, 180, 216, 0.2), 
                rgba(0, 180, 216, 0.1), 
                transparent);
            animation-name: data-line-animation;
            animation-timing-function: linear;
            animation-iteration-count: infinite;
            box-shadow: 0 0 5px rgba(0, 180, 216, 0.5);
        }

        @keyframes data-line-animation {
            0% { transform: translateY(-200%); }
            100% { transform: translateY(200vh); }
        }

        .digital-rain {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -3;
            color: rgba(0, 180, 216, 0.1);
            font-family: monospace;
            font-size: 14px;
            overflow: hidden;
            pointer-events: none;
        }

        .digital-rain .rain-column {
            position: absolute;
            top: -20%;
            animation-name: digital-rain-animation;
            animation-timing-function: linear;
            animation-iteration-count: infinite;
            text-align: center;
        }

        @keyframes digital-rain-animation {
            0% { transform: translateY(-100%); }
            100% { transform: translateY(200vh); }
        }

        @keyframes pulse-cursor {
            0% { opacity: 0.2; transform: translate(-50%, -50%) scale(1); }
            50% { opacity: 0.4; transform: translate(-50%, -50%) scale(1.5); }
            100% { opacity: 0.2; transform: translate(-50%, -50%) scale(1); }
        }
    </style>
</head>
<body>
    <!-- Dynamic background elements -->
    <div id="particles-js"></div>
    <div class="cursor-follower"></div>
    <div class="data-lines"></div>
    <div class="digital-rain"></div>
    
    <nav class="navbar navbar-expand-lg navbar-dark mb-4">
        <div class="container">
            <a class="navbar-brand" href="/"><i class="fas fa-spider me-2"></i>DarkWeb Crawler</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="/"><i class="fas fa-home me-1"></i> Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/dashboard"><i class="fas fa-chart-line me-1"></i> Dashboard</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/history"><i class="fas fa-history me-1"></i> History</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/batch"><i class="fas fa-tasks me-1"></i> Batch</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link active" href="/vulnerability"><i class="fas fa-shield-alt me-1"></i> Vulnerability</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <div class="container">
        <div class="content-section mb-4">
            <h2 class="section-title typing-effect">Vulnerability Assessment</h2>
            <p>Analyze .onion sites for security risks and vulnerabilities using AI-powered assessment.</p>
            
            <form id="vulnerability-form" class="mb-4">
                <div class="input-group">
                    <span class="input-group-text bg-dark text-light border-secondary"><i class="fas fa-link"></i></span>
                    <input type="text" id="url-input" class="form-control bg-dark text-light border-secondary" placeholder="Enter .onion URL to analyze">
                    <button type="submit" class="btn btn-cyber">
                        <i class="fas fa-search-plus me-1"></i> Analyze now
                    </button>
                </div>
            </form>
        </div>

        <div class="row">
            <div class="col-md-4">
                <div class="content-section">
                    <h4 class="section-title">Risk Summary</h4>
                    <div id="risk-overview" class="text-center">
                        <p>Enter a URL to analyze vulnerability risks</p>
                        <div class="risk-indicator">?</div>
                    </div>
                </div>
            </div>
            <div class="col-md-8">
                <div class="content-section">
                    <h4 class="section-title">Vulnerability Details</h4>
                    <div id="vulnerability-details">
                        <p class="text-center">No vulnerability analysis available yet.</p>
                    </div>
                </div>
            </div>
        </div>

        <div class="content-section">
            <h4 class="section-title">Recent Vulnerability Assessments</h4>
            <div id="recent-assessments" class="row">
                {% if recent_assessments %}
                    {% for assessment in recent_assessments %}
                    <div class="col-md-6 mb-3">
                        <div class="card {% if assessment.risk_level >= 7 %}risk-card-high{% elif assessment.risk_level >= 4 %}risk-card-medium{% else %}risk-card-low{% endif %}">
                            <div class="card-header">
                                <i class="fas {% if assessment.risk_level >= 7 %}fa-exclamation-triangle{% elif assessment.risk_level >= 4 %}fa-exclamation-circle{% else %}fa-check-circle{% endif %} me-2"></i>
                                {{ assessment.url }}
                            </div>
                            <div class="card-body">
                                <h5 class="card-title">{{ assessment.category }}</h5>
                                <div class="d-flex justify-content-between align-items-center">
                                    <div class="risk-indicator {% if assessment.risk_level >= 7 %}risk-high{% elif assessment.risk_level >= 4 %}risk-medium{% else %}risk-low{% endif %}">
                                        {{ assessment.risk_level }}
                                    </div>
                                    <a href="/analysis/{{ assessment.id }}" class="btn btn-sm btn-cyber">
                                        <i class="fas fa-eye me-1"></i> View
                                    </a>
                                </div>
                            </div>
                            <div class="card-footer text-muted">
                                <small>{{ assessment.timestamp }}</small>
                            </div>
                        </div>
                    </div>
                    {% endfor %}
                {% else %}
                    <p class="text-center">No recent assessments found.</p>
                {% endif %}
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const vulnerabilityForm = document.getElementById('vulnerability-form');
            const riskOverview = document.getElementById('risk-overview');
            const vulnerabilityDetails = document.getElementById('vulnerability-details');
            
            // Initialize dynamic background elements
            initDynamicBackground();
            
            vulnerabilityForm.addEventListener('submit', function(e) {
                e.preventDefault();
                
                const url = document.getElementById('url-input').value;
                if (!url) return;
                
                // Show loading spinner
                riskOverview.innerHTML = '<div class="spinner my-4"></div><p>Analyzing site security...</p>';
                vulnerabilityDetails.innerHTML = '<div class="spinner my-4"></div><p>Gathering vulnerability data...</p>';
                
                // Call the API to analyze the URL
                fetch('/api/process', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ url: url }),
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        updateRiskDisplay(data);
                        setTimeout(() => {
                            location.reload(); // Refresh to show updated recent assessments
                        }, 3000);
                    } else {
                        showError(data.error);
                    }
                })
                .catch(error => {
                    showError("Failed to analyze URL: " + error);
                });
            });
            
            function updateRiskDisplay(data) {
                // Extract risk level from AI analysis
                let riskLevel = 0;
                let riskClass = "risk-low";
                let riskCategory = "Unknown";
                
                const riskMatch = data.ai_analysis.match(/RISK_LEVEL:\s*(\d+)/);
                if (riskMatch) {
                    riskLevel = parseInt(riskMatch[1]);
                    if (riskLevel >= 7) {
                        riskClass = "risk-high";
                    } else if (riskLevel >= 4) {
                        riskClass = "risk-medium";
                    }
                }
                
                const categoryMatch = data.ai_analysis.match(/CONTENT_TYPE:\s*([^\n]+)/);
                if (categoryMatch) {
                    riskCategory = categoryMatch[1].trim();
                }
                
                // Update risk overview
                riskOverview.innerHTML = `
                    <h5>${riskCategory}</h5>
                    <div class="risk-indicator ${riskClass}">${riskLevel}</div>
                    <p class="mt-3">
                        <span class="badge ${riskLevel >= 7 ? 'bg-danger' : riskLevel >= 4 ? 'bg-warning text-dark' : 'bg-success'}">
                            ${riskLevel >= 7 ? 'High Risk' : riskLevel >= 4 ? 'Medium Risk' : 'Low Risk'}
                        </span>
                    </p>
                `;
                
                // Update vulnerability details
                let sections = data.ai_analysis.split(/\d+\.\s+/);
                if (sections.length > 1) {
                    sections = sections.slice(1); // Remove the first empty element
                    
                    let detailsHtml = '';
                    
                    // Process CONCERNS section
                    const concernsSection = sections.find(s => s.startsWith('CONCERNS'));
                    if (concernsSection) {
                        const concernsList = concernsSection.replace('CONCERNS:', '').trim().split('\n')
                            .filter(item => item.trim().length > 0)
                            .map(item => `<li>${item.trim()}</li>`)
                            .join('');
                            
                        if (concernsList) {
                            detailsHtml += `
                                <div class="mb-4">
                                    <h5><i class="fas fa-exclamation-triangle me-2"></i>Security Concerns</h5>
                                    <ul>${concernsList}</ul>
                                </div>
                            `;
                        }
                    }
                    
                    // Process VULNERABILITIES section
                    const vulnSection = sections.find(s => s.startsWith('VULNERABILITIES'));
                    if (vulnSection) {
                        const vulnList = vulnSection.replace('VULNERABILITIES:', '').trim().split('\n')
                            .filter(item => item.trim().length > 0)
                            .map(item => `<li>${item.trim()}</li>`)
                            .join('');
                            
                        if (vulnList) {
                            detailsHtml += `
                                <div class="mb-4">
                                    <h5><i class="fas fa-bug me-2"></i>Technical Vulnerabilities</h5>
                                    <ul class="text-danger">${vulnList}</ul>
                                </div>
                            `;
                        }
                    }
                    
                    // Process POTENTIAL_FUTURE_RISKS section
                    const futureSection = sections.find(s => s.startsWith('POTENTIAL_FUTURE_RISKS'));
                    if (futureSection) {
                        const futureList = futureSection.replace('POTENTIAL_FUTURE_RISKS:', '').trim().split('\n')
                            .filter(item => item.trim().length > 0)
                            .map(item => `<li>${item.trim()}</li>`)
                            .join('');
                            
                        if (futureList) {
                            detailsHtml += `
                                <div class="mb-4">
                                    <h5><i class="fas fa-binoculars me-2"></i>Potential Future Risks</h5>
                                    <ul class="text-warning">${futureList}</ul>
                                </div>
                            `;
                        }
                    }
                    
                    // Process SUMMARY section
                    const summarySection = sections.find(s => s.startsWith('SUMMARY'));
                    if (summarySection) {
                        const summary = summarySection.replace('SUMMARY:', '').trim();
                        detailsHtml += `
                            <div class="mb-4">
                                <h5><i class="fas fa-info-circle me-2"></i>Summary</h5>
                                <p>${summary}</p>
                            </div>
                        `;
                    }
                    
                    // Add text snippet
                    detailsHtml += `
                        <div>
                            <h5><i class="fas fa-file-alt me-2"></i>Content Sample</h5>
                            <div class="bg-dark p-3 rounded" style="max-height: 200px; overflow-y: auto;">
                                <pre class="text-light mb-0" style="white-space: pre-wrap;">${data.raw_text_snippet}</pre>
                            </div>
                        </div>
                    `;
                    
                    vulnerabilityDetails.innerHTML = detailsHtml;
                } else {
                    vulnerabilityDetails.innerHTML = `<p>${data.ai_analysis}</p>`;
                }
            }
            
            function showError(errorMessage) {
                riskOverview.innerHTML = `
                    <div class="alert alert-danger">
                        <i class="fas fa-exclamation-triangle me-2"></i>${errorMessage}
                    </div>
                `;
                vulnerabilityDetails.innerHTML = `
                    <div class="alert alert-danger">
                        <i class="fas fa-exclamation-triangle me-2"></i>Failed to analyze vulnerabilities.
                    </div>
                `;
            }

            // Initialize dynamic background effects
            function initDynamicBackground() {
                // Initialize particles.js
                particlesJS('particles-js', {
                    "particles": {
                        "number": {
                            "value": 40,
                            "density": {
                                "enable": true,
                                "value_area": 800
                            }
                        },
                        "color": {
                            "value": "#00b4d8"
                        },
                        "shape": {
                            "type": "circle",
                            "stroke": {
                                "width": 0,
                                "color": "#000000"
                            }
                        },
                        "opacity": {
                            "value": 0.2,
                            "random": true,
                            "anim": {
                                "enable": true,
                                "speed": 1,
                                "opacity_min": 0.1,
                                "sync": false
                            }
                        },
                        "size": {
                            "value": 3,
                            "random": true,
                            "anim": {
                                "enable": true,
                                "speed": 2,
                                "size_min": 0.1,
                                "sync": false
                            }
                        },
                        "line_linked": {
                            "enable": true,
                            "distance": 150,
                            "color": "#00b4d8",
                            "opacity": 0.2,
                            "width": 1
                        },
                        "move": {
                            "enable": true,
                            "speed": 1,
                            "direction": "none",
                            "random": true,
                            "straight": false,
                            "out_mode": "out",
                            "bounce": false,
                            "attract": {
                                "enable": true,
                                "rotateX": 600,
                                "rotateY": 1200
                            }
                        }
                    },
                    "interactivity": {
                        "detect_on": "canvas",
                        "events": {
                            "onhover": {
                                "enable": true,
                                "mode": "grab"
                            },
                            "onclick": {
                                "enable": true,
                                "mode": "push"
                            },
                            "resize": true
                        },
                        "modes": {
                            "grab": {
                                "distance": 140,
                                "line_linked": {
                                    "opacity": 0.5
                                }
                            },
                            "push": {
                                "particles_nb": 3
                            }
                        }
                    },
                    "retina_detect": true
                });

                // Create cursor follower effect
                const cursorFollower = document.querySelector('.cursor-follower');
                document.addEventListener('mousemove', (e) => {
                    cursorFollower.style.left = e.clientX + 'px';
                    cursorFollower.style.top = e.clientY + 'px';
                });

                // Create data lines effect
                const dataLines = document.querySelector('.data-lines');
                for (let i = 0; i < 15; i++) {
                    const line = document.createElement('div');
                    line.classList.add('data-line');
                    line.style.top = Math.random() * 100 + 'vh';
                    line.style.animationDuration = (Math.random() * 8 + 5) + 's';
                    line.style.opacity = Math.random() * 0.5 + 0.1;
                    dataLines.appendChild(line);
                }

                // Create digital rain effect
                const digitalRain = document.querySelector('.digital-rain');
                const characters = '01アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン';
                
                for (let i = 0; i < 30; i++) {
                    const column = document.createElement('div');
                    column.classList.add('rain-column');
                    column.style.left = (Math.random() * 100) + 'vw';
                    column.style.animationDuration = (Math.random() * 10 + 10) + 's';
                    column.style.opacity = Math.random() * 0.3 + 0.1;
                    
                    const columnLength = Math.floor(Math.random() * 20 + 10);
                    let columnHtml = '';
                    
                    for (let j = 0; j < columnLength; j++) {
                        const charIndex = Math.floor(Math.random() * characters.length);
                        columnHtml += characters.charAt(charIndex) + '<br>';
                    }
                    
                    column.innerHTML = columnHtml;
                    digitalRain.appendChild(column);
                }
            }
        });
    </script>
</body>
</html> 
