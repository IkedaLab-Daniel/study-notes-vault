<?php

namespace App\Http\Controllers\API;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Models\Course;
use GuzzleHttp\Psr7\Response;
use Illuminate\Http\Response as HttpResponse;

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
        $course = Course::find($id);
        if (!$course){
            return response()->json(['message'=>'Course not found!'], HttpResponse::HTTP_NOT_FOUND);
        }
        return response()->json($course);
    }

    // > Updating data on server, PATCH
    public function update(Request $request, $id){
        $course = Course::find($id);
        if (!$course){
            return response()->json(['message'=>'Course not found'], HttpResponse::HTTP_NOT_FOUND);
        }
        $validateDate = $request->validate([
            'courseName'=>'string|max:255',
            'courseDescription'=>'required|string'
        ]);
        $course->fill($request->all());
        $course->save();
        return response()->json(['message'=>'Course Updated','course'=>$course], HttpResponse::HTTP_OK);
    }

    // > Deleting data from server, DELETE
    public function destroy($id){
        return response()->json();
    }
}
