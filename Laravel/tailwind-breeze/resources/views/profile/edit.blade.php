@extends('layouts.app')

@section('content')
<div class="py-12 bg-gray-800 min-h-screen">
    <div class="max-w-7xl mx-auto sm:px-6 lg:px-8 space-y-6">
        <h2 class="font-semibold text-xl text-gray-100 leading-tight mb-6">
            {{ __('Profile') }}
        </h2>
        
        <div class="p-4 sm:p-8 bg-slate-600 shadow sm:rounded-lg">
            <div class="max-w-xl">
                @include('profile.partials.update-profile-information-form')
            </div>
        </div>

        <div class="p-4 sm:p-8 bg-slate-600 shadow sm:rounded-lg">
            <div class="max-w-xl">
                @include('profile.partials.update-password-form')
            </div>
        </div>

        <div class="p-4 sm:p-8 bg-slate-600 shadow sm:rounded-lg">
            <div class="max-w-xl">
                @include('profile.partials.delete-user-form')
            </div>
        </div>
        
        <div class="p-4 sm:p-8 bg-slate-600 shadow sm:rounded-lg">
            <div class="max-w-xl">
                @include('profile.partials.update-avatar-form')
            </div>
        </div>
    </div>
</div>
@endsection
