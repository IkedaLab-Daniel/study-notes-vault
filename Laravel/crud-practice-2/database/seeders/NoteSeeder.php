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
            'message' => 'this is a sample note aksjdklajs lorem ao;jksdo jasjdkalskjas kldjkjaskldj. akjslndjnasj dhrq3jnjknas dasjhdjnqwj jdnas djanbdkqwbnbdhk qwbekhndbqw kqd kjqwdb qwkbd b wqbd jqwbdbhqwgdg hqbwdhbqbwhdqbwe mnbqwbdqhbhkegduq ukqwbdkhbqksbd kuqwb wkjhdbkqbwdb. kuqwbdkbqwkdbhjqwd kqbd kqwjbdkqwkd k qwbdkhqbkhbsdna ansbdnmqw qwn,mbenqwbdas nqwjkebhqjwbbe qjksdbasbdnab bbqwneb mqwebmq wqwbemhqwbembqwmnbemnqw asn,bdsbnabnbdnmasbdnmabqwuhe bnqkwbejnqbwnas hhjqwljehjqkwbdas n,qnwbe',
            'status' => 'pending',
            'user_id' => 1
        ]);
    }
}
