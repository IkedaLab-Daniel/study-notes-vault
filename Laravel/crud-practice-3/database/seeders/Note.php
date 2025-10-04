<?php

namespace Database\Seeders;

use App\Models\Note as ModelsNote;
use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class Note extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        ModelsNote::create([
            'user_id' => 1,
            'title' => 'sample note',
            'message' => 'I like drinking tea while doing web development drills'
        ]);
    }
}
