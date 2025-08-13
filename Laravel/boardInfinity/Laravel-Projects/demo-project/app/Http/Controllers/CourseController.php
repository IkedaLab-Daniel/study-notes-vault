<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Course;

class CourseController extends Controller
{
    /**
     * Display all courses
     */
    public function index()
    {
        $courses = Course::all();
        return view('courses.index', ['courses' => $courses]);
    }

    /**
     * Find and display a specific course by ID
     */
    public function findCourse($id)
    {
        $course = Course::find($id);
        return view('courses.show', ['course' => $course]);
    }
}
