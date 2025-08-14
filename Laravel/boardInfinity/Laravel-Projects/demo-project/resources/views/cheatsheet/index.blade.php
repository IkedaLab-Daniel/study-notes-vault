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
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            min-height: 100vh;
            color: #e2e8f0;
        }
        
        .container {
            background: #1e293b;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            overflow: hidden;
            border: 1px solid #334155;
        }
        
        .header {
            background: linear-gradient(135deg, #dc2626, #ea580c);
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
            background: #2d3748;
            overflow: hidden;
            box-shadow: 0 2px 10px rgba(0,0,0,0.3);
            border: 1px solid #4a5568;
        }
        
        .section-header {
            background: linear-gradient(135deg, #3b82f6, #1d4ed8);
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
            background: #374151;
            border-radius: 8px;
            padding: 15px;
            border-left: 4px solid #3b82f6;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            border: 1px solid #4b5563;
        }
        
        .command-item:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(0,0,0,0.4);
            background: #4b5563;
        }
        
        .command-item:last-child {
            margin-bottom: 0;
        }
        
        .command {
            font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
            background: #111827;
            color: #34d399;
            padding: 8px 12px;
            border-radius: 5px;
            font-size: 0.9em;
            display: inline-block;
            margin-bottom: 8px;
            word-break: break-all;
            border: 1px solid #374151;
        }
        
        .description {
            color: #cbd5e1;
            line-height: 1.5;
            font-size: 0.95em;
        }
        
        .navigation {
            background: #111827;
            padding: 15px 20px;
            text-align: center;
            border-top: 1px solid #374151;
        }
        
        .nav-link {
            color: #e2e8f0;
            text-decoration: none;
            margin: 0 15px;
            padding: 10px 20px;
            background: #3b82f6;
            border-radius: 5px;
            display: inline-block;
            transition: background-color 0.3s ease;
        }
        
        .nav-link:hover {
            background: #1d4ed8;
            text-decoration: none;
            color: white;
        }
        
        .copy-btn {
            background: #059669;
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
            background: #047857;
        }
        
        .search-box {
            width: 100%;
            padding: 12px;
            border: 2px solid #4b5563;
            border-radius: 8px;
            font-size: 1em;
            margin-bottom: 20px;
            box-sizing: border-box;
            background: #374151;
            color: #e2e8f0;
        }
        
        .search-box:focus {
            outline: none;
            border-color: #3b82f6;
            background: #4b5563;
        }
        
        .search-box::placeholder {
            color: #9ca3af;
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
                event.target.style.background = '#059669';
                setTimeout(() => {
                    event.target.textContent = 'Copy';
                    event.target.style.background = '#059669';
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
                
                // ? Show/hide section based on whether it has visible commands
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
