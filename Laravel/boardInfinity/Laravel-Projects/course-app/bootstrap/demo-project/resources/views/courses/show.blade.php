<!DOCTYPE html>
<html>
<head>
    <title>Course Details</title>
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
        .course-info {
            margin: 20px 0;
            font-size: 16px;
            line-height: 1.6;
        }
        .course-name {
            font-size: 24px;
            font-weight: bold;
            color: #007bff;
            margin-bottom: 15px;
        }
        .course-description {
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 5px;
            border-left: 4px solid #007bff;
            margin: 20px 0;
        }
        .back-link {
            display: inline-block;
            margin-top: 20px;
            margin-right: 10px;
            padding: 10px 20px;
            background-color: #007bff;
            color: white;
            text-decoration: none;
            border-radius: 5px;
        }
        .back-link:hover {
            background-color: #0056b3;
        }
        .courses-link {
            display: inline-block;
            margin-top: 20px;
            padding: 10px 20px;
            background-color: #6c757d;
            color: white;
            text-decoration: none;
            border-radius: 5px;
        }
        .courses-link:hover {
            background-color: #5a6268;
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
        @if($course)
            <h1>Course Details</h1>
            <div class="course-name">{{ $course->courseName }}</div>
            <div class="course-info">
                <p><strong>Course ID:</strong> {{ $course->id }}</p>
            </div>
            <div class="course-description">
                <strong>Description:</strong><br>
                {{ $course->courseDescription }}
            </div>
        @else
            <div class="error">
                <h1>Course Not Found</h1>
                <p>Sorry, the course you're looking for doesn't exist.</p>
            </div>
        @endif
        
        <a href="{{ url('/') }}" class="back-link">← Back to Home</a>
        <a href="{{ url('/course') }}" class="courses-link">View All Courses</a>
    </div>
</body>
</html>
