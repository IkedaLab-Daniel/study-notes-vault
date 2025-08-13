<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>{{ config('app.name') }} - User Dashboard</title>
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    
    <!-- Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <!-- CSS -->
    <style>
        :root {
            --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            --success-gradient: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            --dark-gradient: linear-gradient(135deg, #434343 0%, #000000 100%);
            --glass-bg: rgba(255, 255, 255, 0.1);
            --glass-border: rgba(255, 255, 255, 0.2);
            --text-primary: #2d3748;
            --text-secondary: #718096;
            --shadow-soft: 0 10px 25px rgba(0, 0, 0, 0.1);
            --shadow-medium: 0 20px 40px rgba(0, 0, 0, 0.15);
            --shadow-strong: 0 30px 60px rgba(0, 0, 0, 0.2);
            --border-radius: 16px;
            --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: var(--text-primary);
            overflow-x: hidden;
        }

        /* Animated Background */
        .bg-animation {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            overflow: hidden;
        }

        .bg-animation::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: 
                radial-gradient(circle at 20% 50%, rgba(120, 119, 198, 0.3) 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, rgba(255, 119, 198, 0.3) 0%, transparent 50%),
                radial-gradient(circle at 40% 80%, rgba(120, 219, 255, 0.3) 0%, transparent 50%);
            animation: float 20s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translate(-20px, -10px) rotate(0deg); }
            33% { transform: translate(30px, -30px) rotate(120deg); }
            66% { transform: translate(-20px, 20px) rotate(240deg); }
        }

        /* Header */
        .header {
            padding: 2rem 0;
            backdrop-filter: blur(20px);
            background: var(--glass-bg);
            border-bottom: 1px solid var(--glass-border);
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
        }

        .nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.8rem;
            font-weight: 800;
            background: linear-gradient(45deg, #fff, #f0f4f8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .nav-links {
            display: flex;
            gap: 2rem;
            list-style: none;
        }

        .nav-link {
            color: rgba(255, 255, 255, 0.9);
            text-decoration: none;
            font-weight: 500;
            transition: var(--transition);
            position: relative;
        }

        .nav-link::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 0;
            height: 2px;
            background: var(--success-gradient);
            transition: var(--transition);
        }

        .nav-link:hover::after {
            width: 100%;
        }

        .nav-link:hover {
            color: white;
            transform: translateY(-2px);
        }

        /* Main Content */
        .main-content {
            padding: 4rem 0;
        }

        .dashboard-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-bottom: 3rem;
        }

        .card {
            background: var(--glass-bg);
            backdrop-filter: blur(20px);
            border: 1px solid var(--glass-border);
            border-radius: var(--border-radius);
            padding: 2rem;
            box-shadow: var(--shadow-soft);
            transition: var(--transition);
            position: relative;
            overflow: hidden;
        }

        .card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 2px;
            background: var(--primary-gradient);
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: var(--shadow-medium);
        }

        .card-header {
            display: flex;
            align-items: center;
            margin-bottom: 1.5rem;
        }

        .card-icon {
            width: 50px;
            height: 50px;
            border-radius: 12px;
            background: var(--primary-gradient);
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 1rem;
            box-shadow: var(--shadow-soft);
        }

        .card-icon i {
            color: white;
            font-size: 1.2rem;
        }

        .card-title {
            font-size: 1.2rem;
            font-weight: 600;
            color: white;
            margin: 0;
        }

        .card-subtitle {
            color: rgba(255, 255, 255, 0.7);
            font-size: 0.9rem;
            margin-top: 0.25rem;
        }

        .card-content {
            color: rgba(255, 255, 255, 0.9);
            line-height: 1.6;
        }

        /* Stats Cards */
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1.5rem;
            margin-bottom: 3rem;
        }

        .stat-card {
            background: var(--glass-bg);
            backdrop-filter: blur(20px);
            border: 1px solid var(--glass-border);
            border-radius: var(--border-radius);
            padding: 1.5rem;
            text-align: center;
            transition: var(--transition);
            position: relative;
            overflow: hidden;
        }

        .stat-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: var(--success-gradient);
            opacity: 0;
            transition: var(--transition);
        }

        .stat-card:hover::before {
            opacity: 0.1;
        }

        .stat-card:hover {
            transform: scale(1.05);
        }

        .stat-number {
            font-size: 2.5rem;
            font-weight: 800;
            color: white;
            margin-bottom: 0.5rem;
            position: relative;
            z-index: 2;
        }

        .stat-label {
            color: rgba(255, 255, 255, 0.8);
            font-size: 0.9rem;
            font-weight: 500;
            position: relative;
            z-index: 2;
        }

        /* Feature Section */
        .features-section {
            margin-top: 4rem;
        }

        .section-title {
            text-align: center;
            font-size: 2.5rem;
            font-weight: 700;
            color: white;
            margin-bottom: 3rem;
            position: relative;
        }

        .section-title::after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
            width: 80px;
            height: 4px;
            background: var(--success-gradient);
            border-radius: 2px;
        }

        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
        }

        .feature-card {
            background: var(--glass-bg);
            backdrop-filter: blur(20px);
            border: 1px solid var(--glass-border);
            border-radius: var(--border-radius);
            padding: 2rem;
            text-align: center;
            transition: var(--transition);
            position: relative;
            overflow: hidden;
        }

        .feature-card:hover {
            transform: translateY(-10px) scale(1.02);
            box-shadow: var(--shadow-strong);
        }

        .feature-icon {
            width: 80px;
            height: 80px;
            border-radius: 50%;
            background: var(--secondary-gradient);
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 1.5rem;
            box-shadow: var(--shadow-medium);
            transition: var(--transition);
        }

        .feature-card:hover .feature-icon {
            transform: scale(1.1) rotate(5deg);
        }

        .feature-icon i {
            color: white;
            font-size: 2rem;
        }

        .feature-title {
            font-size: 1.3rem;
            font-weight: 600;
            color: white;
            margin-bottom: 1rem;
        }

        .feature-description {
            color: rgba(255, 255, 255, 0.8);
            line-height: 1.6;
        }

        /* CTA Section */
        .cta-section {
            margin-top: 5rem;
            text-align: center;
            padding: 3rem;
            background: var(--glass-bg);
            backdrop-filter: blur(20px);
            border: 1px solid var(--glass-border);
            border-radius: var(--border-radius);
            position: relative;
            overflow: hidden;
        }

        .cta-section::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: var(--primary-gradient);
            opacity: 0.1;
        }

        .cta-title {
            font-size: 2.2rem;
            font-weight: 700;
            color: white;
            margin-bottom: 1rem;
            position: relative;
            z-index: 2;
        }

        .cta-description {
            font-size: 1.1rem;
            color: rgba(255, 255, 255, 0.8);
            margin-bottom: 2rem;
            position: relative;
            z-index: 2;
        }

        .btn {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 1rem 2rem;
            background: var(--success-gradient);
            color: white;
            text-decoration: none;
            border-radius: var(--border-radius);
            font-weight: 600;
            transition: var(--transition);
            border: none;
            cursor: pointer;
            position: relative;
            z-index: 2;
            box-shadow: var(--shadow-soft);
        }

        .btn:hover {
            transform: translateY(-3px);
            box-shadow: var(--shadow-medium);
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .container {
                padding: 0 1rem;
            }
            
            .nav {
                flex-direction: column;
                gap: 1rem;
            }
            
            .nav-links {
                gap: 1rem;
            }
            
            .section-title {
                font-size: 2rem;
            }
            
            .dashboard-grid,
            .stats-grid,
            .features-grid {
                grid-template-columns: 1fr;
            }
        }

        /* Loading Animation */
        .loading {
            display: inline-block;
            width: 20px;
            height: 20px;
            border: 3px solid rgba(255, 255, 255, 0.3);
            border-radius: 50%;
            border-top-color: white;
            animation: spin 1s ease-in-out infinite;
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }

        /* Pulse Animation */
        .pulse {
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
    </style>
</head>
<body>
    <div class="bg-animation"></div>
    
    <!-- Header -->
    <header class="header">
        <div class="container">
            <nav class="nav">
                <div class="logo">
                    <i class="fas fa-rocket"></i> {{ config('app.name', 'LaravelApp') }}
                </div>
                <ul class="nav-links">
                    <li><a href="#" class="nav-link">Dashboard</a></li>
                    <li><a href="#" class="nav-link">Analytics</a></li>
                    <li><a href="#" class="nav-link">Settings</a></li>
                    <li><a href="#" class="nav-link">Profile</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Main Content -->
    <main class="main-content">
        <div class="container">
            <!-- Welcome Section -->
            <section class="welcome-section">
                <div class="card pulse">
                    <div class="card-header">
                        <div class="card-icon">
                            <i class="fas fa-user-circle"></i>
                        </div>
                        <div>
                            <h1 class="card-title">Welcome back, {{ auth()->user()->name ?? 'Developer' }}!</h1>
                            <p class="card-subtitle">{{ now()->format('l, F j, Y') }}</p>
                        </div>
                    </div>
                    <div class="card-content">
                        <p>Ready to build something amazing? Your dashboard is loaded with powerful tools and insights to help you create exceptional user experiences.</p>
                    </div>
                </div>
            </section>

            <!-- Stats Section -->
            <section class="stats-section">
                <div class="stats-grid">
                    <div class="stat-card">
                        <div class="stat-number">{{ rand(1200, 9999) }}</div>
                        <div class="stat-label">Total Users</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">{{ rand(80, 99) }}%</div>
                        <div class="stat-label">Performance</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">{{ rand(50, 500) }}</div>
                        <div class="stat-label">Active Sessions</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">${{ number_format(rand(10000, 99999)) }}</div>
                        <div class="stat-label">Revenue</div>
                    </div>
                </div>
            </section>

            <!-- Dashboard Grid -->
            <section class="dashboard-section">
                <div class="dashboard-grid">
                    <div class="card">
                        <div class="card-header">
                            <div class="card-icon">
                                <i class="fas fa-chart-line"></i>
                            </div>
                            <div>
                                <h3 class="card-title">Analytics Overview</h3>
                                <p class="card-subtitle">Real-time performance metrics</p>
                            </div>
                        </div>
                        <div class="card-content">
                            <p>Monitor your application's performance with advanced analytics. Track user engagement, conversion rates, and system health in real-time.</p>
                            <br>
                            <a href="#" class="btn">
                                <i class="fas fa-external-link-alt"></i>
                                View Details
                            </a>
                        </div>
                    </div>

                    <div class="card">
                        <div class="card-header">
                            <div class="card-icon">
                                <i class="fas fa-shield-alt"></i>
                            </div>
                            <div>
                                <h3 class="card-title">Security Center</h3>
                                <p class="card-subtitle">Protect your application</p>
                            </div>
                        </div>
                        <div class="card-content">
                            <p>Enterprise-grade security features including 2FA, encryption, audit logs, and threat detection to keep your data safe.</p>
                            <br>
                            <a href="#" class="btn">
                                <i class="fas fa-lock"></i>
                                Manage Security
                            </a>
                        </div>
                    </div>

                    <div class="card">
                        <div class="card-header">
                            <div class="card-icon">
                                <i class="fas fa-cogs"></i>
                            </div>
                            <div>
                                <h3 class="card-title">System Configuration</h3>
                                <p class="card-subtitle">Customize your experience</p>
                            </div>
                        </div>
                        <div class="card-content">
                            <p>Fine-tune your application settings, manage integrations, and configure advanced features to match your workflow.</p>
                            <br>
                            <a href="#" class="btn">
                                <i class="fas fa-wrench"></i>
                                Configure
                            </a>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Features Section -->
            <section class="features-section">
                <h2 class="section-title">Powerful Features</h2>
                <div class="features-grid">
                    <div class="feature-card">
                        <div class="feature-icon">
                            <i class="fas fa-lightning-bolt"></i>
                        </div>
                        <h3 class="feature-title">Lightning Fast</h3>
                        <p class="feature-description">
                            Built with modern technologies for maximum performance. Experience blazing fast load times and smooth interactions.
                        </p>
                    </div>
                    
                    <div class="feature-card">
                        <div class="feature-icon">
                            <i class="fas fa-mobile-alt"></i>
                        </div>
                        <h3 class="feature-title">Mobile First</h3>
                        <p class="feature-description">
                            Responsive design that works perfectly on all devices. Your users get a consistent experience everywhere.
                        </p>
                    </div>
                    
                    <div class="feature-card">
                        <div class="feature-icon">
                            <i class="fas fa-database"></i>
                        </div>
                        <h3 class="feature-title">Scalable Architecture</h3>
                        <p class="feature-description">
                            Enterprise-ready infrastructure that grows with your business. Handle millions of users without breaking a sweat.
                        </p>
                    </div>
                </div>
            </section>

            <!-- CTA Section -->
            <section class="cta-section">
                <h2 class="cta-title">Ready to Get Started?</h2>
                <p class="cta-description">
                    Join thousands of developers who trust our platform to build amazing applications.
                </p>
                <a href="#" class="btn">
                    <i class="fas fa-rocket"></i>
                    Launch Your Project
                </a>
            </section>
        </div>
    </main>

    <!-- JavaScript -->
    <script>
        // Smooth scrolling for navigation links
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                
                // Add loading state
                const originalText = this.innerHTML;
                this.innerHTML = '<span class="loading"></span> Loading...';
                
                setTimeout(() => {
                    this.innerHTML = originalText;
                    // You can add actual navigation logic here
                }, 1000);
            });
        });

        // Dynamic stats counter animation
        function animateCounter(element) {
            const target = parseInt(element.textContent.replace(/[^\d]/g, ''));
            const increment = target / 100;
            let current = 0;
            
            const timer = setInterval(() => {
                current += increment;
                if (current >= target) {
                    current = target;
                    clearInterval(timer);
                }
                
                if (element.textContent.includes('%')) {
                    element.textContent = Math.floor(current) + '%';
                } else if (element.textContent.includes('$')) {
                    element.textContent = '$' + Math.floor(current).toLocaleString();
                } else {
                    element.textContent = Math.floor(current).toLocaleString();
                }
            }, 20);
        }

        // Intersection Observer for animations
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                    
                    // Animate counters when stats section is visible
                    if (entry.target.classList.contains('stat-number')) {
                        animateCounter(entry.target);
                    }
                }
            });
        }, observerOptions);

        // Observe elements for animation
        document.querySelectorAll('.card, .stat-card, .feature-card').forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(30px)';
            el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            observer.observe(el);
        });

        // Observe stat numbers for counter animation
        document.querySelectorAll('.stat-number').forEach(el => {
            observer.observe(el);
        });

        // Parallax effect for background
        window.addEventListener('scroll', () => {
            const scrolled = window.pageYOffset;
            const parallax = document.querySelector('.bg-animation');
            const speed = scrolled * 0.5;
            parallax.style.transform = `translateY(${speed}px)`;
        });

        // Button click effects
        document.querySelectorAll('.btn').forEach(btn => {
            btn.addEventListener('click', function(e) {
                e.preventDefault();
                
                // Create ripple effect
                const ripple = document.createElement('span');
                const rect = this.getBoundingClientRect();
                const size = Math.max(rect.width, rect.height);
                const x = e.clientX - rect.left - size / 2;
                const y = e.clientY - rect.top - size / 2;
                
                ripple.style.width = ripple.style.height = size + 'px';
                ripple.style.left = x + 'px';
                ripple.style.top = y + 'px';
                ripple.style.position = 'absolute';
                ripple.style.background = 'rgba(255, 255, 255, 0.3)';
                ripple.style.borderRadius = '50%';
                ripple.style.transform = 'scale(0)';
                ripple.style.animation = 'ripple 0.6s linear';
                ripple.style.pointerEvents = 'none';
                
                this.style.position = 'relative';
                this.style.overflow = 'hidden';
                this.appendChild(ripple);
                
                setTimeout(() => {
                    ripple.remove();
                }, 600);
            });
        });

        // Add ripple animation
        const style = document.createElement('style');
        style.textContent = `
            @keyframes ripple {
                to {
                    transform: scale(4);
                    opacity: 0;
                }
            }
        `;
        document.head.appendChild(style);

        // Console welcome message
        console.log(`
            🚀 Welcome to ${document.title}!
            
            Built with ❤️ using Laravel + Modern CSS/JS
            
            Features:
            ✨ Glassmorphism UI
            🎨 Advanced CSS animations
            📱 Fully responsive design
            ⚡ Optimized performance
            🔒 Security-first approach
            
            Happy coding! 💻
        `);
    </script>
</body>
</html>