<?php

namespace App\Http\Controllers\API;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Models\Course;

class CourseAPIController extends Controller
{
    // ? GET, PUT, POST & DELETE (fetching, updateing, adding, deleting)

    // > adding, POST
    public function store(Request $request){
        $validatedData = $request->validate([
            'courseName' => 'required|string|max:255',
            'courseDescription' => 'required|string'
        ]);
        
        $course = new Course();
        $course->courseName = $validatedData['courseName'];
        $course->courseDescription = $validatedData['courseDescription'];
        $course->save();

        return response()->json(['message'=> 'Course created successfully', 'course' => $course], 201);
    }

    // > Fetching all data from server, GET
    public function index(){
        $courses = Course::all();
        return response()->json($courses);
    }

    // > Fetching single record from server, GET
    public function show($id){
        return response()->json();
    }

    // > Updating data on server, PATCH
    public function update(Request $request, $id){

    }

    // > Deleting data from server, DELETE
    public function destroy($id){
        return response()->json();
    }
}
