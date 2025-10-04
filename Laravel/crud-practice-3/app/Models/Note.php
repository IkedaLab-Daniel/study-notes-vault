<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Note extends Model
{
    protected $fillable = [
        'title',
        'message',
        'user_id'
    ];

    public function user()
    {
        $this->belongsTo(\App\Models\User::class);
    }

}
