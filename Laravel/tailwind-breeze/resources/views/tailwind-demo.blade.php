@extends('layouts.app')

@section('content')
<div class="max-w-4xl mx-auto p-8">
    <h1 class="text-3xl font-bold text-center mb-6 text-indigo-600">
        ■ Tailwind CSS Demo Page
    </h1>

    <!-- Example Card -->
    <div class="bg-white shadow-lg rounded-2xl p-6 mb-6">
        <h2 class="text-xl font-semibold mb-2">Card Component</h2>
        <p class="text-gray-600">
            This is a simple Tailwind CSS card with padding, rounded corners, and a shadow.
        </p>
    </div>

    <!-- Example Button -->
    <div class="mb-6">
        <button class="px-6 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg shadow">
            Tailwind Button
        </button>
    </div>

    <!-- Example Alert -->
    <div class="p-4 mb-6 text-sm text-green-800 rounded-lg bg-green-100 border border-green-300" role="alert">
        ■ This is a success alert — styled with Tailwind!
    </div>

    <!-- Example Table -->
    <div class="overflow-x-auto shadow-md rounded-lg">
        <table class="min-w-full border border-gray-200">
            <thead class="bg-gray-100">
                <tr>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Email</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Role</th>
                </tr>
            </thead>
            <tbody>
                <tr class="bg-white border-b">
                    <td class="px-6 py-4">John Doe</td>
                    <td class="px-6 py-4">john@example.com</td>
                    <td class="px-6 py-4">Admin</td>
                </tr>
                <tr class="bg-gray-50 border-b">
                    <td class="px-6 py-4">Jane Smith</td>
                    <td class="px-6 py-4">jane@example.com</td>
                    <td class="px-6 py-4">User</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
@endsection