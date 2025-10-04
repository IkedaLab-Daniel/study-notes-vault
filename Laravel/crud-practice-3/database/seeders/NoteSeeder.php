<?php

namespace Database\Seeders;

use App\Models\Note;
use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class NoteSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        Note::create([
            'user_id' => 1,
            'title'=> 'sample title',
            'message' => 'I love drinking tea while doing web dev drills'
        ]);
    }
}
