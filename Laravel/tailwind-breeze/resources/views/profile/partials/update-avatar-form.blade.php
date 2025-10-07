<section>
    <header>
        <h2 class="text-lg font-medium text-gray-900">
            {{ __('Profile Avatar') }}
        </h2>

        <p class="mt-1 text-sm text-gray-600">
            {{ __("Update your account's profile avatar.") }}
        </p>
    </header>

    @if (session('status') === 'avatar-updated')
        <p
            x-data="{ show: true }"
            x-show="show"
            x-transition
            x-init="setTimeout(() => show = false, 2000)"
            class="text-sm text-gray-600"
        >{{ __('Saved.') }}</p>
    @endif

    <div class="mt-6">
        @if (auth()->user()->avatar)
            <img 
                src="{{ asset('storage/' . auth()->user()->avatar) }}" 
                alt="Current Avatar" 
                class="w-24 h-24 rounded-full object-cover"
                onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"
            >
            <div class="w-24 h-24 rounded-full bg-red-200 flex items-center justify-center text-xs p-2" style="display:none;">
                <span class="text-red-600 text-center">Image not found<br>{{ auth()->user()->avatar }}</span>
            </div>
        @else
            <div class="w-24 h-24 rounded-full bg-gray-200 flex items-center justify-center">
                <span class="text-gray-500">No Avatar</span>
            </div>
        @endif
        
        {{-- Debug Info (Remove in production) --}}
        @if(auth()->user()->avatar)
        <div class="mt-2 text-xs text-gray-500">
            <p><strong>Avatar Path:</strong> {{ auth()->user()->avatar }}</p>
            <p><strong>Full URL:</strong> {{ asset('storage/' . auth()->user()->avatar) }}</p>
            <p><strong>File Exists:</strong> {{ file_exists(public_path('storage/' . auth()->user()->avatar)) ? 'Yes' : 'No' }}</p>
        </div>
        @endif
    </div>

    <form 
        method="post" 
        action="{{ route('profile.avatar') }}" 
        class="mt-6 space-y-6"
        enctype="multipart/form-data"
    >
        @csrf

        <div>
            <x-input-label for="avatar" :value="__('New Avatar')" />
            <x-text-input 
                id="avatar" 
                name="avatar" 
                type="file" 
                class="mt-1 block w-full" 
            />
            <x-input-error class="mt-2" :messages="$errors->get('avatar')" />
        </div>

        <div class="flex items-center gap-4">
            <x-primary-button>{{ __('Save') }}</x-primary-button>
        </div>
    </form>
</section>