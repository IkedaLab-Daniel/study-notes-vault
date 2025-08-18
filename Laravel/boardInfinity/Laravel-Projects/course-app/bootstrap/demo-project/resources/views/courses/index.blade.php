<!DOCTYPE html>
<html>
<head>
    <title>All Courses</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
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
            margin-bottom: 30px;
        }
        .course-card {
            background-color: #f8f9fa;
            border: 1px solid #dee2e6;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
            transition: box-shadow 0.3s ease;
        }
        .course-card:hover {
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        .course-name {
            color: #007bff;
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .course-description {
            color: #666;
            line-height: 1.6;
            margin-bottom: 15px;
        }
        .course-id {
            color: #999;
            font-size: 14px;
        }
        .course-link {
            color: #007bff;
            text-decoration: none;
            font-weight: bold;
        }
        .course-link:hover {
            text-decoration: underline;
        }
        .back-link {
            display: inline-block;
            margin-top: 20px;
            padding: 10px 20px;
            background-color: #6c757d;
            color: white;
            text-decoration: none;
            border-radius: 5px;
        }
        .back-link:hover {
            background-color: #5a6268;
        }
        .no-courses {
            text-align: center;
            color: #666;
            font-style: italic;
            padding: 40px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>All Courses</h1>
        
        @if($courses && $courses->count() > 0)
            @foreach($courses as $course)
                <div class="course-card">
                    <div class="course-name">
                        <a href="/course/{{ $course->id }}" class="course-link">
                            {{ $course->courseName }}
                        </a>
                    </div>
                    <div class="course-description">{{ $course->courseDescription }}</div>
                    <div class="course-id">Course ID: {{ $course->id }}</div>
                </div>
            @endforeach
            
            <p><strong>Total Courses:</strong> {{ $courses->count() }}</p>
        @else
            <div class="no-courses">
                <h2>No courses available</h2>
                <p>There are currently no courses in the database.</p>
            </div>
        @endif
        
        <a href="{{ url('/') }}" class="back-link">← Back to Home</a>
    </div>
</body>
</html>
