<!DOCTYPE html>
<html>
<head>
    <title>{{fake()->name()}}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            border-bottom: 2px solid #007bff;
            padding-bottom: 10px;
        }
        .user-info {
            margin: 20px 0;
            font-size: 16px;
            line-height: 1.6;
        }
        .back-link {
            display: inline-block;
            margin-top: 20px;
            padding: 10px 20px;
            background-color: #007bff;
            color: white;
            text-decoration: none;
            border-radius: 5px;
        }
        .back-link:hover {
            background-color: #0056b3;
        }
        .error {
            text-align: center;
            color: #dc3545;
            font-size: 18px;
        }
    </style>
</head>
<body>
    <div class="container">
        @if($user)
            <h1>User Profile</h1>
            <div class="user-info">
                <p><strong>Name:</strong> {{ $user->name }}</p>
                <p><strong>Fake Name:</strong> {{ fake()->name() }}</p>
                <p><strong>Email:</strong> {{ $user->email }}</p>
                <p><strong>User ID:</strong> {{ $user->id }}</p>
                <p><strong>Member since:</strong> {{ $user->created_at->format('F d, Y') }}</p>
            </div>
        @else
            <div class="error">
                <h1>User Not Found</h1>
                <p>Sorry, the user you're looking for doesn't exist.</p>
            </div>
        @endif
        
        <a href="{{ url('/') }}" class="back-link">← Back to Home</a>
    </div>

</body>
</html>
