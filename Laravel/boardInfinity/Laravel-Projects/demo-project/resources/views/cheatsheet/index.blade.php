<!DOCTYPE html>
<html>
<head>
    <title>Laravel Commands Cheatsheet</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: #333;
        }
        
        .container {
            background: white;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            overflow: hidden;
        }
        
        .header {
            background: linear-gradient(135deg, #ff6b6b, #ffa726);
            color: white;
            text-align: center;
            padding: 40px 20px;
        }
        
        .header h1 {
            margin: 0;
            font-size: 2.5em;
            font-weight: bold;
        }
        
        .header p {
            margin: 10px 0 0 0;
            font-size: 1.2em;
            opacity: 0.9;
        }
        
        .content {
            padding: 30px;
        }
        
        .section {
            margin-bottom: 40px;
            border-radius: 10px;
            background: #f8f9fa;
            overflow: hidden;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .section-header {
            background: linear-gradient(135deg, #4facfe, #00f2fe);
            color: white;
            padding: 15px 20px;
            font-size: 1.3em;
            font-weight: bold;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .section-content {
            padding: 20px;
        }
        
        .command-item {
            margin-bottom: 15px;
            background: white;
            border-radius: 8px;
            padding: 15px;
            border-left: 4px solid #4facfe;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        
        .command-item:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        
        .command-item:last-child {
            margin-bottom: 0;
        }
        
        .command {
            font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
            background: #2d3748;
            color: #68d391;
            padding: 8px 12px;
            border-radius: 5px;
            font-size: 0.9em;
            display: inline-block;
            margin-bottom: 8px;
            word-break: break-all;
        }
        
        .description {
            color: #666;
            line-height: 1.5;
            font-size: 0.95em;
        }
        
        .navigation {
            background: #343a40;
            padding: 15px 20px;
            text-align: center;
        }
        
        .nav-link {
            color: white;
            text-decoration: none;
            margin: 0 15px;
            padding: 10px 20px;
            background: #007bff;
            border-radius: 5px;
            display: inline-block;
            transition: background-color 0.3s ease;
        }
        
        .nav-link:hover {
            background: #0056b3;
            text-decoration: none;
        }
        
        .copy-btn {
            background: #28a745;
            color: white;
            border: none;
            padding: 4px 8px;
            border-radius: 3px;
            cursor: pointer;
            font-size: 0.8em;
            margin-left: 10px;
            transition: background-color 0.2s ease;
        }
        
        .copy-btn:hover {
            background: #218838;
        }
        
        .search-box {
            width: 100%;
            padding: 12px;
            border: 2px solid #e9ecef;
            border-radius: 8px;
            font-size: 1em;
            margin-bottom: 20px;
            box-sizing: border-box;
        }
        
        .search-box:focus {
            outline: none;
            border-color: #4facfe;
        }
        
        @media (max-width: 768px) {
            body {
                padding: 10px;
            }
            
            .header h1 {
                font-size: 2em;
            }
            
            .content {
                padding: 20px;
            }
            
            .command {
                font-size: 0.8em;
                word-break: break-all;
            }
            
            .nav-link {
                display: block;
                margin: 5px 0;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 Laravel Commands Cheatsheet</h1>
            <p>Your complete guide to Laravel Artisan commands</p>
        </div>
        
        <div class="content">
            <input type="text" class="search-box" id="searchBox" placeholder="🔍 Search commands..." onkeyup="searchCommands()">
            
            @foreach($commandSections as $sectionName => $section)
                <div class="section" data-section="{{ $sectionName }}">
                    <div class="section-header">
                        <span>{{ $section['icon'] }}</span>
                        <span>{{ $sectionName }}</span>
                    </div>
                    <div class="section-content">
                        @foreach($section['commands'] as $commandItem)
                            <div class="command-item" data-command="{{ $commandItem['command'] }}" data-description="{{ $commandItem['description'] }}">
                                <div class="command">
                                    {{ $commandItem['command'] }}
                                    <button class="copy-btn" onclick="copyCommand(`{{ $commandItem['command'] }}`)">Copy</button>
                                </div>
                                <div class="description">{{ $commandItem['description'] }}</div>
                            </div>
                        @endforeach
                    </div>
                </div>
            @endforeach
        </div>
        
        <div class="navigation">
            <a href="{{ url('/') }}" class="nav-link">🏠 Home</a>
            <a href="{{ url('/course') }}" class="nav-link">📚 Courses</a>
            <a href="{{ url('/user/1') }}" class="nav-link">👤 User Profile</a>
        </div>
    </div>

    <script>
        // Copy command to clipboard
        function copyCommand(command) {
            navigator.clipboard.writeText(command).then(function() {
                // Show success feedback
                event.target.textContent = 'Copied!';
                event.target.style.background = '#28a745';
                setTimeout(() => {
                    event.target.textContent = 'Copy';
                    event.target.style.background = '#28a745';
                }, 2000);
            }).catch(function(err) {
                console.error('Could not copy text: ', err);
                // Fallback for older browsers
                const textArea = document.createElement("textarea");
                textArea.value = command;
                document.body.appendChild(textArea);
                textArea.focus();
                textArea.select();
                try {
                    document.execCommand('copy');
                    event.target.textContent = 'Copied!';
                    setTimeout(() => {
                        event.target.textContent = 'Copy';
                    }, 2000);
                } catch (err) {
                    console.error('Fallback: Could not copy text: ', err);
                }
                document.body.removeChild(textArea);
            });
        }

        // Search functionality
        function searchCommands() {
            const searchTerm = document.getElementById('searchBox').value.toLowerCase();
            const sections = document.querySelectorAll('.section');
            
            sections.forEach(section => {
                const commandItems = section.querySelectorAll('.command-item');
                let hasVisibleCommands = false;
                
                commandItems.forEach(item => {
                    const command = item.getAttribute('data-command').toLowerCase();
                    const description = item.getAttribute('data-description').toLowerCase();
                    
                    if (command.includes(searchTerm) || description.includes(searchTerm)) {
                        item.style.display = 'block';
                        hasVisibleCommands = true;
                    } else {
                        item.style.display = 'none';
                    }
                });
                
                // Show/hide section based on whether it has visible commands
                if (hasVisibleCommands || searchTerm === '') {
                    section.style.display = 'block';
                } else {
                    section.style.display = 'none';
                }
            });
        }
    </script>
</body>
</html>
