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
            'title' => 'Sample note',
            'message' => 'this is a sample note',
            'status' => 'pending',
            'user_id' => 1
        ]);
    }
}
